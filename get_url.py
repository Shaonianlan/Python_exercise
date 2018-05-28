# coding:utf-8

import requests


def get_url(url):
	headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.368N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'}
	response=requests.get(url,headers=headers)
	#session=requests.Session()
	#response=session.get(url,headers=headers)
	print(response.cookies)
	return response.text

if __name__ == '__main__':
	html=get_url('http://www.baidu.com')	
	#html=html.decode('utf')
	#print(html)