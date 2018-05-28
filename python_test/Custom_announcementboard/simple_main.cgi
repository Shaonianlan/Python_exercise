#!‪E:\Python\python.exe

print('Content-type: text/html\n')

import pymysql
import cgitb;cgitb.enable()

conn=pymysql.connect(host="127.0.0.1",user='root',password='5jiu2DNF',db='baz')
curs=conn.cursor(pymysql.cursors.DictCursor)


print('''
	<html>
		<head>
			<title>The FooBar Bulletin Board</title>
		</head>
		<body>
			<h1>The Foo Bulletin Board</h1>
		</body>
	</html>
	''')

query = 'select * from test'
curs.execute(query)
rows = curs.fetchall()
print(rows)

toplevel = []
children = {}

for row in rows:
	parent_id = row['reply_to']
	if parent_id is None:
		toplevel.append(row)
	else:
		children.setdefault(parent_id,row)

def format(row):
	print(row['subject'])
	try:
		kids = children[row['id']]
	except KeyError:
		pass
	else:
		print('<blockquote>')
		for kid in kids:
			format(kid)
		print('</blockquote>')	

print('<p>')

for row in toplevel:
	format(row)

print('''
		</p>
	</body>
	</html>
	''')	