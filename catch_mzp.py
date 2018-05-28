from requests.exceptions import HTTPError,ConnectionError,Timeout
from bs4 import BeautifulSoup
import re
import requests
import os
import os.path
import shutil

#获取页面
def get_url(url):
	headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.368N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'}
	try:
		response=requests.get(url,headers=headers,timeout=5)
	except (HTTPError,ConnectionError,Timeout):
		print('网页不存在或链接超时！')	
	return response.content

#分析页面
def get_mzpicture(url,max_page):
	html=get_url(url).decode('utf-8')
	soup=BeautifulSoup(html,'html.parser')

	#获取初始图片url
	orgin_purl=soup.findAll('img',{'src':re.compile('.+sinaimg.+')})
	print(orgin_purl)
	picture_url=[]

	#记录图片的url
	for each in orgin_purl:
		temp='http:'+each['src']
		picture_url.append(temp)
		print(picture_url)

	#保存图片
	for each in picture_url:
		filename=each.split('/')[-1]
		try:
			with open(filename,'wb') as f:
				img=get_url(each)
				f.write(img)
				print('正在下载：',each)
				f.close()
		except Exception as reason:
			print('文件出错的原因是：'+str(reason))	
			continue	

	#获取下一页的url
	try:
		soup=soup.findAll('a',{'href':re.compile(r'//jandan.net/ooxx/page-\d+#comments')})
		page_url='http:'+soup[2]['href']
		print(page_url)
		#页面url规律数字
		num=int(soup[2].text)
		global	first_num
		
		#判断是否达到指定的最大页数
		if first_num-num<max_page:
			print('P%s 本页有%d张图片。\n'% (num+1,len(picture_url)))
			get_mzpicture(page_url,max_page)
		else:
			print('P%s 本页有%d张图片。'% (num+1,len(picture_url)))
			print('图片已全部下载')	
	except:
		print('下一页面不存在！')


def main_downloadmzp(url,pages,folder='catch_mzp'):
	if os.path.exists(folder):
		shutil.rmtree(folder)
		os.mkdir(folder)
		os.chdir(folder)
	else:
		os.mkdir(folder)
		os.chdir(folder)

	get_mzpicture(url,max_page)

first_num=0
if __name__=='__main__':
	url='http://jandan.net/ooxx/'

	#获取现在jandan网妹子图总共有多少页
	html=get_url(url).decode('utf-8')
	soup=BeautifulSoup(html,'html.parser')
	soup=soup.findAll('a',{'href':re.compile(r'//jandan.net/ooxx/page-\d+#comments')})
	first_num=int(soup[2].text)+1
	
	#想要获取的妹子图页数
	max_page=int(input('请输入需要下载的页数(最大不可超过%s): '% first_num))

	main_downloadmzp(url,max_page)
