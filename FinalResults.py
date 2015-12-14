#finalResults.py




import psycopg2
import sys

#FinalResults.py = sys.argv[0]
if len(sys.argv)>1:
	keyword=sys.argv[1]
else:
	keyword=""
conn = psycopg2.connect(database="tcount", user="postgres", password="", host="localhost", port="5432")

 

cur = conn.cursor()

if len(keyword)>0:
	cur.execute("SELECT word,count from wordtable WHERE word=%s",(keyword,))
	records = cur.fetchall()
	for rec in records:
   		print "word = ", rec[0]
   		print "count = ", rec[1], "\n"
	conn.commit()
else:
	cur.execute("SELECT word,count FROM wordtable ORDER BY word ASC")
	records = cur.fetchall()
	for rec in records:
        	print "word = ", rec[0]
        	print "count = ", rec[1], "\n"
        conn.commit()

conn.close()
