import requests
from bs4 import BeautifulSoup
import re
import requests.exceptions as rs
import json
import time

#获取电影排行页面
def getting_page(url):
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.368N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'}
	try:
		response = requests.get(url,headers = headers)
	except (rs.HTTPError,rs.InvalidURL,rs.ConnectTimeout):
		print("链接出错或连接超时！")
	return response.text
	
movieslist = []
#获取页面信息
def getting_pageinfo(url,offset = 0):
	html = getting_page(url)
	soup = BeautifulSoup(html,'lxml')
	orgin = soup.find('dl').find_all('dd')
	for each in orgin:
		movie = {
			'sort' : each.i.string.strip(),
			'title' : each.find('a')['title'].strip(),
			'acters' : each.find_all('p')[1].text.strip(),
			'releasetime' : each.findAll('p')[2].text.strip(),
			'score' : each.findAll('p')[3].text.strip(),
			'url' : 'maoyan.com'+each.find('a')['href'].strip(),
			'image' : each.find('a').findAll('img')[1]['data-src'].strip()
		}
		movieslist.append(movie)
	if (offset < 100):
		time.sleep(0.5)
		offset += 10
		url = 'http://maoyan.com/board/4?offset='+str(offset)
		getting_pageinfo(url,offset)
	else:
		print(movieslist)

#写入文件
def write_movies(content):
	with open('result.txt','a',encoding='utf-8') as f:
		f.write(json.dumps(content,ensure_ascii = False)+'\n')

def main():
	url = 'http://maoyan.com/board/4'
	getting_pageinfo(url)
	for each in movieslist:
		write_movies(each)

if __name__ == '__main__':
	main()
