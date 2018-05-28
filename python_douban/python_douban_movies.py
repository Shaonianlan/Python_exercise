#utf-8

import requests
from bs4 import BeautifulSoup

#上海正在热映的电影
url='https://movie.douban.com/cinema/nowplaying/shanghai/'
headers={'User-Agnet':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
response=requests.get(url,headers=headers)
main_soup=BeautifulSoup(response.text,'html.parser')
newmoviews_urls=main_soup.find('div',{'id':'nowplaying'}).findAll('li',{'class':'stitle'})

#创建字典 用于存储电影名和url
new_movies={}
for each_url in newmoviews_urls:
	new_movies[each_url.a['title']]=each_url.a['href']
print(new_movies.keys())
temp=input('请输入你想要了解的电影名字：')
temp_url=new_movies[temp]
print(temp_url)

response=requests.get(temp_url,headers=headers)
soup=BeautifulSoup(response.text,'html.parser')
jianjie=soup.find('span',{'property':'v:summary'})
print(jianjie.text.strip())