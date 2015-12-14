1. Install Parsestream as per instructions
2. Create project EX2Tweetwordcount
3.Run Dan's file: setup_ucb_complete_plus_postgres.sh
4. Create Postgres table:

psql -U postgres
cur = conn.cursor()
CREATE TABLE tcount
       (word TEXT PRIMARY KEY     NOT NULL,
       count INT NOT NULL);


5. Go into /../EX2Tweetwordcount
6. sparse run  
7. Exit after a while (^c)
#run the serving scripts
7. python FinalResults.py word
8. python histogram.py k1 k2

Note that I've merged all of EX2Tweetwordcount into the branch  - but the important scripts are:
1. EX2Tweetwordcount/src/spouts/tweets.py
2. EX2Tweetwordcount/src/bolts/wordcount.py
3. EX2Tweetwordcount/src/bolts/parse.py
4. EX2Tweetwordcount/topologies/EX2Tweetwordcount.clj
