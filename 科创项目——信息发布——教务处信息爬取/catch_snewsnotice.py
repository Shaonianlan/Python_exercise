import requests
import re
from  bs4 import BeautifulSoup
from requests.exceptions import HTTPError,ConnectionError,Timeout

#获取教务处页面
def getting_mainpage(url):
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) \
	AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.368N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'}
	try:
		response=requests.get(url,headers=headers,timeout=5)
	except (HTTPError,ConnectionError,Timeout):
		print('网页不存在或链接超时！')
	return response.text
#获取教务新闻
def getting_news(url):
	#创建最近新闻url字典
	dict_news = {} 
	html = getting_mainpage(url)
	soup = BeautifulSoup(html,'html.parser')
	#获取教务新闻
	orgin_newsurls = soup.find('div',{'class':'top_center'}).findAll('a',{'href':re.compile(r'News.aspx')})
	titles = []
	urls = []
	for title in orgin_newsurls:
		#print(title['title'])
		titles.append(title['title'])
	for each in orgin_newsurls:
		news_url = url+each['href']
		#print(news_url)
		urls.append(news_url)
	#dict_news = dict(zip(title,urls))
	return dict(zip(titles,urls))

#获取教务公告
def getting_notice(url):
	#创建最近公告url字典
	dict_notice = {} 
	html = getting_mainpage(url)
	soup = BeautifulSoup(html,'html.parser')
	#获取教务公告
	orgin_noticeurls = soup.find('div',{'class':'top_center_list_2'}).findAll('a',{'href':re.compile(r'News.aspx')})
	titles = []
	urls = []
	for title in orgin_noticeurls:
		titles.append(title['title'])
	for each in orgin_noticeurls:
		notice_url = url+each['href']
		urls.append(notice_url)
	return dict(zip(titles,urls))

def main():
	dict_news = {} #最近新闻url字典
	dict_notice = {} #最近公告url字典
	url = 'http://jwc.shmtu.edu.cn/'
	dict_news = getting_news(url)
	dict_notice = getting_notice(url)
	print("新闻：")
	for each in dict_news:
		print(each+" :\n"+dict_news[each])
	print("\n")
	print("通知：")	
	for each in dict_notice:
		print(each+" :\n"+dict_notice[each])	


if __name__ == '__main__':
	main()
	
