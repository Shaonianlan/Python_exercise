#coding:utf-8

import urllib.request as request
import sys,operator
from bs4 import BeautifulSoup

def getURL(url):
	req=request.Request(url)
	response=request.urlopen(req)
	html=response.read().decode('utf-8')
	return html

def main():
	i=0
	while i<67:--
		url='http://www.fmprc.gov.cn/web/fyrbt_673021/jzhsl_673025/'
		homeurl=url
		if i==0:
			url+='default.shtml'
		else:
			url+='default_'+str(i)+'.shtml'
		print(url)	
		html=getURL(url)
		soup=BeautifulSoup(html,'html.parser')
		data=soup.select('body div div div ul li a')
		for html_tag in data:
			if '主持例行记者会' in html_tag.string:
				title=html_tag.string
				fileURL=homeurl+html_tag['href'][2:]
				file_the_page=getURL(fileURL)
				file_soup=BeautifulSoup(file_the_page,'html.parser')
				datal=file_soup.find('div',id='News_Body_Txt_A')
				file_name='result'+title+'.txt'
				print(file_name)
				with open(file_name,'w',encoding='utf-8') as f:
					for file_page in datal:
						if file_page.string==None:
							temp_data=file_page.find_all('b')
							result=''
							for temp_file in temp_data:
								try:
									result+=temp_file.span.string
								except (TypeError,AttributeError):
									continue
							if result!='':
								print(result,file=f)
						elif file_page.string !='\n':
							print(file_page.string ,file=f)
					print(title+'Done!')
		i+=1

if __name__ == '__main__':
		main()								

