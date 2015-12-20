#histogram.py

import psycopg2
import sys
conn = psycopg2.connect(database="tcount", user="postgres", password="", host="localhost", port="5432")


k1=sys.argv[1]
k2=sys.argv[2]
cur = conn.cursor()
#k1=3
#k2=10


cur.execute("SELECT word,count from wordtable WHERE count>=%s AND count<=%s;",(k1,k2))
records = cur.fetchall()
for rec in records:
   	print "word = ", rec[0]
   	print "count = ", rec[1], "\n"
conn.commit()

conn.close()
