import requests
from bs4 import BeautifulSoup
import re 
import datetime 
import random
import pymysql

conn=pymysql.connect(host='127.0.0.1',user='root',password='5jiu2DNF',
	db='scraping')
cur=conn.cursor()
cur.execute('use scraping')

random.seed(datetime.datetime.now())

def store(title,content):
	cur.execute('insert into pages(title,content) values(\'%s\',\'%s\')',(title,content))
	cur.connection.commit()

def getLinks(articleurl):
	url='http://en.wikipedia.org'+articleurl
	html=requests.get(url)
	soup=BeautifulSoup(html.text,'html.parser')
	title=soup.find('h1').text
	content=soup.find('div',{'id':'mw-content-text'}).find('p').text
	store(title,content)
	target_urls=soup.find('div',{'id':'bodyContent'}).findAll('a',{'href':re.compile('^(/wiki/)((?!:).)*$')})
	return 	target_urls

links=getLinks('/wiki/Kevin_Bacon')
try:
	while len(links)>0:
		newArticle=links[random.randint(0,len(links)-1).attrs['href']]
		print(newArticle)
		links=getLinks(newArticle)

except:
	print('出错了')
	pass

finally:
	cur.close()
	conn.close()
