from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt
import psycopg2

class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()
	self.conn=psycopg2.connect(database="tcount",user="postgres",password="",host="localhost",port="5432")
	self.cur=self.conn.cursor()

    def process(self, tup):
        newword = tup.values[0]
        self.counts[newword] += 1
        self.emit([newword, self.counts[newword]])
        #self.log('%s: %d' % (newword, self.counts[newword]))
      
	self.cur.execute("SELECT word,count FROM wordtable WHERE word=%s",(newword,))
	check_word = self.cur.fetchall()
	self.conn.commit()

	if len(check_word)==0:
		self.cur.execute ("INSERT into wordtable (word,count) VALUES (%s,%s);",(newword,self.counts[newword]))
		self.conn.commit()
	else:
		self.cur.execute ("UPDATE wordtable SET count=%s WHERE word=%s",(self.counts[newword],newword))
