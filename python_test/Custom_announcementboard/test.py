#!/user/bin/env python
#addmessage.py

import pymysql

conn=pymysql.connect(host="127.0.0.1",user='root',password='5jiu2DNF',db='baz')
cur=conn.cursor()

reply_to = input("Reply to:")
subject = input("Subject:")
sender = input("Sender:")
text = input("Text:")

if reply_to:
	query = '''
			insert into test(reply_to,sender,subject,text) values({},{},{},{})
			'''.format(reply_to,sender,subject,text)
else:
	query = '''
			insert into test(sender,subject,text) values("{}","{}","{}")
			'''.format(sender,subject,text)			

cur.execute(query)
conn.commit()
