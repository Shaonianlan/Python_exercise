import requests
import re
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError,ConnectionError,Timeout

#获取图书馆页面
def getting_page(url):
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.368N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'}
	try:
		response=requests.get(url,headers=headers,timeout=5)
	except (HTTPError,ConnectionError,Timeout):
		print('网页不存在或链接超时！')
	return response.text
#操作
def getting_info(url):
	html = getting_page(url)
	soup = BeautifulSoup(html,'html.parser')
	#new_bookkinds = soup.find('div',{'id':'0_childrenBox'})
	print(soup)


def main():
	url = 'http://opac.library.shmtu.edu.cn:8080/opac/newpub/tree/cls'
	getting_info(url)

if __name__ == '__main__':
	main()	