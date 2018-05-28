

'''
def Fabnaqi(n):
	if (n<1):
		print("输入的数字不能小于1！")
	elif (n==1):
		return 1;
	elif (n==2):
		return 1;
	else:
		return Fabnaqi(n-1)+Fabnaqi(n-2)
print(Fabnaqi(int(input("请输入大于1的整数"))))	
'''
'''
def Fabnaqi1(n):
	n1=1
	n2=1
	n3=1

	if(n<1):
		print("输入的数字不能小于1！")
		return -1
	while  n>2:
		n3=	n1+n2
		n1=n2
		n2=n3
		n-=1
	return n3
input1=	int(input("请输入大于1的整数:"))
result=Fabnaqi1(input1)
if(result != -1):
	print("%d 斐波那契数列 %d " % (input1,result))
'''

'''
def HanNuoTa(m,x,y,z):
	if(m==1):
		print(x,"-->",z,"1在被调用",m)
	else:
		HanNuoTa(m-1,x,z,y)
		"将前n-1个盘子从x移动到y上"	
		print(x,"-->",z,m)
		"将最底下的盘子从x移动\
		到z上"
		HanNuoTa(m-1,y,x,z)
		"将y上的n-1个盘子移动到z上"
n=int(input("输入汉诺塔的层数："))
HanNuoTa(n,"x","y","z")
'''
'''
brand=['上海']
print("%s 是个好地方" % brand[0])
dict1={1:"one",2:"two",3:"threee",2:"sdja k"}
for each in dict1:
	print
print(dict1[2])
dict1[1]="ONE"
print(dict1[1])
dict1[6]="SIX"
print(dict1[6])

num1=[1,2,3,4,5,4,3,2,1]
temp=[]
for i in num1:
	if i not in temp:
		temp.append(i)
print(temp)

print(list(set(num1)))
'''
'''
f=open("C:/Users/10096/Desktop/学习进程.txt")
#print(f.read())
for each_line in f:
	print(each_line)
'''
'''
f=open('E:/123.txt','w')
f.write('Python 文件写入练习')
f.close()

f=open('E:/123.txt','a')
f.write('学习中。。。')
f.close()
'''	
'''
def fun1(x):
	def fun2(y):
		return x*y
	return fun2
i=fun1(2)(4)	
print(i)
'''
'''
def save_file(i,you,count):
	file_name_i='E:/i_'+str(count)+'.txt'
	file_name_you='E:/you'+str(count)+'.txt'

	i_file=open(file_name_i,'w')
	you_file=open(file_name_you,'w')

	i_file.writelines(i)
	you_file.writelines(you)

	i_file.close()
	you_file.close()
 	

def split_file():
	f=open('E:/test.txt')

	i=[]
	you=[]
	count=1

	for eachline in f:
		if eachline[:6] != '======':
			#进行分割
			(role,line_sopken)=eachline.split(':',1)
			if role == '我':
				i.append(line_sopken)
			if role == '你'	:
				you.append(line_sopken)
		else:
			#文件的分别保存
			save_file(i,you,count)

			i=[]
			you=[]
			count+=1

	save_file(i,you,count)	

	f.close()	
split_file()	
'''
'''
import pickle
my_list=[123,3.14,'Python',[1,'s']]
pickle_file=open('my_list','wb')
pickle.dump(my_list,pickle_file)
pickle_file.close()
pickle_file=open('my_list','rb')
my_list2=pickle.load(pickle_file)
print(my_list2)
pickle_file.close()
'''
'''
try:
	f=open('Python.txt')
	print(f.read())
	f.close()
except OSError as reason:
	print('文件出错\n错误的原因是：'+str(reason))	
'''
'''
def showMaxFactor(num):
	count=num//2
	while count>1:
		if(num%count==0):
			print('%d最大的约数是%d' % (num,count))
			break
		count-=1
	else:
		print('%d是素数' % num)
num=int(input('请输入一个数：'))
showMaxFactor(num)				
'''
'''
def showMaxFactor2(num):
	temp=num-1
	while temp>1:
		i=num%temp
		if(i==0):
			print('%d是合数，最大约数是：%d' % (num,temp))
			break
		else:	
			temp-=1
	else:
		print('%d是素数。' % num)
num=int(input('请输入一个数：'))
showMaxFactor2(num)			

for i in range (1,)
'''
'''
def showMaxFactor2(num):
	temp=num-1
	for i in range(temp,2,-1):
		if(num%i==0):
			print('%d是合数，最大约数是：%d' % (num,i))
			break	
	else:
		print('%d是素数。' % num)
num=int(input('请输入一个数：'))
showMaxFactor2(num)
'''
'''
import easygui as g
import sys

while 1:
        g.msgbox("嗨，欢迎进入第一个界面小游戏^_^")

        msg ="请问你希望在鱼C工作室学习到什么知识呢？"
        title = "小游戏互动"
        choices = ["谈恋爱", "编程", "OOXX", "琴棋书画"]
        
        choice = g.choicebox(msg, title, choices)

        # note that we convert choice to string, in case
        # the user cancelled the choice, and we got None.
        g.msgbox("你的选择是: " + str(choice), "结果")

        msg = "你希望重新开始小游戏吗？"
        title = "请选择"
        
        if g.ccbox(msg, title):     # show a Continue/Cancel dialog
                pass  # user chose Continue
        else:
                sys.exit(0)     # user chose Cancel
'''
'''
class Dog:
	def setName(self,name):
		self.name=name
	def	showname(self):
		print('I am %s ' % self.name)
a=Dog()
b=Dog()
a.setName('泰迪')
b.setName('金毛')
a.showname()
b.showname()
''' 
'''
class Cat(object):
	"""docstring for Cat"""
	def __init__(self, name='折耳'):
		super().__init__()
		self.name=name
	__gg=1
	cc=2	
	def show(self,noise='喵喵喵'):
		print('I am %s , %s' % (self.name,noise))
	def showprivate(self):
			return self.__gg	

class SmallCat(Cat):
	pass
sc=SmallCat()		
print(sc._Cat__gg)		
'''
'''
class Cat:
	def __init__(self,x):
		self.num=x
class Dog:
	def __init__(self,y):
		self.num=y				
class Home:
	def __init__(self,x,y):
		self.cat=Cat(x)
		self.dog=Dog(y)
	def print_num(self):
		print('家里有%d只猫，%d只狗'%(self.cat.num,self.dog.num))		
h=Home(1,1)		
h.print_num()	
'''
'''
class Capstr:
	def __init__(self,value):
		self.name=value
		print('构造方法调用中。。。。')
	def __del__(self):
		print('析构方法调用中。。。')	
cps=Capstr('XCM')
print(3+3.14)
print(help(int))
'''
'''
sum=0
for i in range(99,0,-2):
	if i%2!=0:
		sum+=i
	else:
		continue	
print(sum)
'''
'''
for i in range(100):
	temp=i*7
	if (temp-5)%6==0 and (temp-4)%5==0 and (temp-2)%3==0 and (temp-1)%2==0:
		print('总共有%d阶楼梯' % temp)
		break
	else:
		continue	
#2x+1=3y+2=5m+4=6n+5=7z
'''
'''
def findpassword(n):
	for each in n:
		if each.islower():
			temp1=index(each)
			count1=0
			while temp>=0:
				if n[temp].isupper():
					count1+=1
					temp1-=1
				else:
					temp1-=1	
			if count1==3:
				temp2
				while 
		else:
			continue			
'''
'''
class Person():
	name='me'
	def show_name(self):
		print(self.name)
p=Person()
p.show_name()		
'''
'''
class A:
	def fun(self):
		print("A")
class B(A):
	def	fun(self):
		super().fun()
		print("B")
class C(B):
	def fun(self):
		super().fun()	
c=C()
c.fun()	
'''		
'''	
class Count_variable:
	count=0
	def __init__(self):
		Count_variable.count+=1
	def __del__(self):
		Count_variable.count-=1

a=Count_variable()
b=Count_variable()
print(Count_variable.count)
'''
'''
class FileObject:
	#给文件对象进行包装从而确认在删除时文件流关闭
	def __init__(self,filename=''):
		#读写模式打开一个文件
		self.new_file=open(filename,'r+')
	def __del__(self):
		self.new_file.close()
		del self.new_file	
'''
'''
class test:
	count=0
	def __getattr__(self,name):
		return '属性不存在'
		
one=test()
print(one.count)
one.count=2
print(one.count)
'''
#python中class的__dict__包含了类的属性  
'''
class A():  
    def __init__(self):  
        self.x=1   #定义一个实例属性  
    y = 2          #定义一个类属性  
  
a = A()  
print (a.__dict__) 

print(dir(A))
#print (a.x) #这里会提示不包含x属性的错误，因为已被清空  

#A.__dict__ = {} #清空类的所有属性，x不受影响  
#print (a.x)  
#print (a.y) #提示错误 
'''
'''
class one:
	def __init__(self,*value):
		self.value=value
	def __len__(self):
		return 1
str1=[11,245.56,48,5]
print(len(str1))
'''
'''
import urllib.request
import re
from bs4 import BeautifulSoup


url = "http://baike.baidu.com/view/284853.htm"
response = urllib.request.urlopen(url)
html = response.read()
soup = BeautifulSoup(html, "html.parser") # 使用 Python 默认的解析器

for each in soup.find_all(href=re.compile("view")):
	print(each['href'])
	#print(each.text, "->", ''.join(["http://baike.baidu.com", each["href"]]))


'''
'''
for each in soup.find_all(href=re.compile("view")):
	print(each.text, "->", ''.join(["http://baike.baidu.com", each["href"]]))
	# 上边用 join() 不用 + 直接拼接，是因为 join() 被证明执行效率要高很多
'''
'''
import urllib.request
import urllib.parse
import re 
from bs4 import BeautifulSoup

def main():
	keyword = input("请输入关键词：")
	keyword = urllib.parse.urlencode({"word":keyword})
	response = urllib.request.urlopen("http://baike.baidu.com/search/word?%s" % keyword)
	html = response.read()
	soup = BeautifulSoup(html, "html.parser")

	for each in soup.find_all(href=re.compile("view")):
		content = ''.join([each.text])
		url2 = ''.join(["http://baike.baidu.com", each["href"]])
		response2 = urllib.request.urlopen(url2)
		html2 = response2.read()
		soup2 = BeautifulSoup(html2, "html.parser")
		if soup2.h2:
			content = ''.join([content, soup2.h2.text])
		content = ''.join([content, " -> ", url2])
		print(content)

if __name__ == "__main__":
	main()
'''
'''
import urllib.request
import urllib.parse
import re 
from bs4 import BeautifulSoup

def test_url(soup):
	esult = soup.find(text=re.compile("百度百科尚未收录词条"))
	if result:
		print(result[0:-1]) # 百度这个碧池在最后加了个“符号，给它去掉
		return False
	else:
		return True

def summary(soup):
	word = soup.h1.text
	# 如果存在副标题，一起打印
	if soup.h2:
		word += soup.h2.text
	# 打印标题
	print(word)
	# 打印简介
	if soup.find(class_="lemma-summary"):
		print(soup.find(class_="lemma-summary").text)   

def get_urls(soup):
	for each in soup.find_all(href=re.compile("view")):
		content = ''.join([each.text])
		url2 = ''.join(["http://baike.baidu.com", each["href"]])
		response2 = urllib.request.urlopen(url2)
		html2 = response2.read()
		soup2 = BeautifulSoup(html2, "html.parser")
		if soup2.h2:
			content = ''.join([content, soup2.h2.text])
		content = ''.join([content, " -> ", url2])
		yield content
        

def main():
	word = input("请输入关键词：")
	keyword = urllib.parse.urlencode({"word":word})
	response = urllib.request.urlopen("http://baike.baidu.com/search/word?%s" % keyword)
	html = response.read()
	soup = BeautifulSoup(html, "html.parser")

	if test_url(soup):
		summary(soup)

		print("下边打印相关链接：")
		each = get_urls(soup)
		while True:
			try:
				for i in range(10):
					print(next(each))
			except StopIteration:
					break

			command = input("输入任意字符将继续打印，q退出程序：")
			if command == 'q':
				break
			else:
				continue
    
if __name__ == "__main__":
	main()
'''
'''
import urllib.request as request

url='http://tieba.baidu.com/p/5267352154'
req=request.Request(url)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36')
response=request.urlopen(req)
html=response.read()
with open('tieba_1.html','wb') as f:
	f.write(html)
'''
'''
import get_url as gu
html=gu.get_url('http://www.baidu.com').decode('utf-8')
print(html)
'''
'''
import urllib.request as request
from bs4 import BeautifulSoup
import pandas

new_fiction=[]
res=request.urlopen('http://r.qidian.com/yuepiao?style=1')
response=res.read().decode('utf-8')
#print(response)#中间打印看看，好习惯
soup=BeautifulSoup(response,'html.parser')
#print(soup)

for news in soup.select('.rank-view-list li'):#定位    
	#print(news.select('a')[1].text,news.select('a')[2].text,news.select('a')[3].text,news.select('p')[1].text,news.select('p')[2].text,news.select('a')[0]['href'])
	new_fiction.append({'title':news.select('a')[1].text,'name':news.select('a')[2].text,'style':news.select('a')[3].text,'describe':news.select('p')[1].text,'lastest':news.select('p')[2].text,'url':news.select('a')[0]['href']})
newsdf=pandas.DataFrame(new_fiction)
newsdf.to_excel('qidian_rank.xlsx')
'''
'''
def hannuota(n,x,y,z):
	if n==1:
		print(x,' -->', z)
	else:
		hannuota(n-1,x,z,y) # 把上面的n-1个从x移动到y
		print(x,' -->', z)  #把最后一个从x移动到z
		hannuota(n-1,y,x,z)	 #把y上的n-1个移动到z
hannuota(5,'x','y','z')		
'''
'''
import urllib.request
import re
from bs4 import BeautifulSoup

ip_list=[]

def get_daili_ip():
	url='http://www.xicidaili.com/nn'
	req=urllib.request.Request(url)
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36')
	response=urllib.request.urlopen(req)
	html=response.read().decode('utf-8')
	soup=BeautifulSoup(html,'html.parser')
	ips=soup.findAll('tr')

	for x in range(1,len(ips)):  
		ip = ips[x]  
		tds = ip.findAll("td")
		ip_temp = tds[1].text+":"+tds[2].text+' '+'存活时间'+tds[8].text
		ip_list.append(ip_temp)
	return 	 ip_list


if __name__=='__main__':
	get_daili_ip()
	print(ip_list)
'''
'''
import urllib.request
import urllib.parse


data={}
data['word']='Java'

value_url=urllib.parse.urlencode(data)
url='http://www.baidu.com/s?'
full_url=url+value_url
print(full_url)
response=urllib.request.urlopen(full_url)
html=response.read().decode('utf-8')
print(html)
'''
'''
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry 入队
queue.append("Graham")          # Graham 入队
queue.pop()                # 队首元素出队
#输出: 'Eric'
queue.popleft()                 # 队首元素出队
#输出: 'John'
print(queue)                         # 队列中剩下的元素
#输出: deque(['Michael', 'Terry', 'Graham'])
'''
'''
import re
import urllib.request
import urllib
 
from collections import deque
 
queue = deque()
visited = set()
 
url = 'http://news.dbanotes.net'  # 入口页面, 可以换成别的
 
queue.append(url)
cnt = 0
 
while queue:
  url = queue.popleft()  # 队首元素出队
  visited |= {url}  # 标记为已访问
 
  print('已经抓取: ' + str(cnt) + '   正在抓取 <---  ' + url)
  cnt += 1
  urlop = urllib.request.urlopen(url)
  if 'html' not in urlop.getheader('Content-Type'):
    continue
 
  # 避免程序异常中止, 用try..catch处理异常
  try:
    data = urlop.read().decode('utf-8')
  except:
    continue
 
  # 正则表达式提取页面中所有队列, 并判断是否已经访问过, 然后加入待爬队列
  linkre = re.compile('href="(.+?)"')
  for x in linkre.findall(data):
    if 'http' in x and x not in visited:
      queue.append(x)
      print('加入队列 --->  ' + x)
'''
'''
import urllib.request

url='http://www.baidu.com'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
#req=urllib.request.Request(url)
#req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36')
response=urllib.request.urlopen(url)
'''
'''
import urllib.request
import http.cookiejar
 
# head: dict of header
def makeMyOpener(head = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
}):
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    print(cj)
    print(opener)
    return opener
 
oper = makeMyOpener()
uop = oper.open('http://www.baidu.com/', timeout = 1000)
data = uop.read()
#print(data.decode())
'''
# coding: utf8

# @Author: 郭 璞
# @File: MyZhiHuLogin.py                                                                 
# @Time: 2017/4/8                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 我的模拟登录知乎
'''
import requests
from bs4 import BeautifulSoup
import os, time
import re
# import http.cookiejar as cookielib

# 构造 Request headers
agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.368N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'
headers = {
    "Host": "www.zhihu.com",
    "Referer": "https://www.zhihu.com/",
    'User-Agent': agent
}

######### 构造用于网络请求的session
session = requests.Session()
# session.cookies = cookielib.LWPCookieJar(filename='zhihucookie')
# try:
#     session.cookies.load(ignore_discard=True)
# except:
#     print('cookie 文件未能加载')

############ 获取xsrf_token
homeurl = 'https://www.zhihu.com'
homeresponse = session.get(url=homeurl, headers=headers)
homesoup = BeautifulSoup(homeresponse.text, 'html.parser')
xsrfinput = homesoup.find('input', {'name': '_xsrf'})
xsrf_token = xsrfinput['value']
print("获取到的xsrf_token为： ", xsrf_token)

########## 获取验证码文件
randomtime = str(int(time.time() * 1000))
captchaurl = 'https://www.zhihu.com/captcha.gif?r='+\
             randomtime+"&type=login"
captcharesponse = session.get(url=captchaurl, headers=headers)
with open('checkcode.gif', 'wb') as f:
    f.write(captcharesponse.content)
    f.close()
# os.startfile('checkcode.gif')
captcha = input('请输入验证码：')
print(captcha)

########### 开始登陆
headers['X-Xsrftoken'] = xsrf_token
headers['X-Requested-With'] = 'XMLHttpRequest'
loginurl = 'https://www.zhihu.com/login/phone_num'
postdata = {
    '_xsrf': xsrf_token,
    'phone_num': '13817204085',
    'password': '5jiu2DNF'
}
loginresponse = session.post(url=loginurl, headers=headers, data=postdata)
print('服务器端返回响应码：', loginresponse.status_code)
print(loginresponse.json())
# 验证码问题输入导致失败: 猜测这个问题是由于session中对于验证码的请求过期导致
if loginresponse.json()['r']==1:
    # 重新输入验证码，再次运行代码则正常。也就是说可以再第一次不输入验证码，或者输入一个错误的验证码，只有第二次才是有效的
    randomtime = str(int(time.time() * 1000))
    captchaurl = 'https://www.zhihu.com/captcha.gif?r=' + \
                 randomtime + "&type=login"
    captcharesponse = session.get(url=captchaurl, headers=headers)
    with open('checkcode.gif', 'wb') as f:
        f.write(captcharesponse.content)
        f.close()
    os.startfile('checkcode.gif')
    captcha = input('请输入验证码：')
    print(captcha)

    postdata['captcha'] = captcha
    loginresponse = session.post(url=loginurl, headers=headers, data=postdata)
    print('服务器端返回响应码：', loginresponse.status_code)
    print(loginresponse.json())




##########################保存登陆后的cookie信息
# session.cookies.save()
############################判断是否登录成功
profileurl = 'https://www.zhihu.com/settings/profile'
profileresponse = session.get(url=profileurl, headers=headers)
print('profile页面响应码：', profileresponse.status_code)
profilesoup = BeautifulSoup(profileresponse.text, 'html.parser')
div = profilesoup.find('div', {'id': 'rename-section'})
print(div)
'''
'''
#get_urltitle
import urllib.request
from bs4 import BeautifulSoup
from urllib.error import HTTPError

def gettitle(url):
	try:
		response=urllib.request.urlopen(url)
	except HTTPError as e:
		return None

	try:
		soup=BeautifulSoup(response.read(),'html.parser')
		title=soup.h1	 	
	except AttributeError as e:
		return None
	return title

title=gettitle('http://www.baidu.com')
if title==None:
	print('Title could not be found!')
else:
	print(title)		
'''
'''
import	scrapy
import urllib.request
from bs4 import BeautifulSoup
import re
import datetime
import random

url='http://www.baidu.com'
response=urllib.request.urlopen(url)
soup=BeautifulSoup(response,'html.parser')

#for each in soup.findAll('a',{'href':re.compile('http.+')}):
#	print(each['href'])
pages={1,2,5,3,5,'s'}
pages.add(('s','f'))
print(pages)
'''
'''import re
from bs4 import BeautifulSoup
import os
import requests

#获取页面信息
def get_url(url):
	headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.368N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'}
	response=requests.get(url,headers=headers)
	return response.content

def get_mzpicture(url):
	html=get_url(url).decode('utf-8')
	soup=BeautifulSoup(html,'html.parser')

	#获取初始图片url
	orgin_purl=soup.findAll('img',{'src':re.compile('.+sinaimg.+')})
	picture_url=[]

	#记录图片的url
	for each in orgin_purl:
		temp='http:'+each['src']
		print(temp)
		picture_url.append(temp)

	#保存图片
	for each in picture_url:
		filename=each.split('/')[-1]
		try:
			with open(filename,'wb') as f:
				img=get_url(each)
				f.write(img)
		except Exception as reason:
			print('文件出错的原因是：'+str(reason))	
			continue	

	#获取下一页的url
	page_url=soup.findAll('a',{'href':re.compile(r'http://jandan.net/ooxx/page-\d+#comments')})[2]['href']
	get_mzpicture(page_url)
	return None
def main_downloadmzp(url,folder='catch_mzp'):
	os.mkdir(folder)
	os.chdir(folder)

	get_mzpicture(url)


if __name__=='__main__':
	url='http://jandan.net/ooxx/'
	main_downloadmzp(url)
'''
'''
from bs4 import BeautifulSoup  
import requests  
import re
  
  
url = 'http://www.zhihu.com'  
login_url ='https://www.zhihu.com/login/phone_num'
captcha_url = 'http://www.zhihu.com/captcha.gif'  
headers={
    "Host": "www.zhihu.com",
    "Referer": "https://www.zhihu.com/",
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.368N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36' 
}  
login_data={
           'phone_num': '13817204085',#替换为账号  
           'password':'5jiu2DNF',#替换为密码  
           'remember_me':'true',  
           'Referer': 'http://www.zhihu.com/'  
           }  
def add_xsrf(url,headers):  
    #向login_data里面添加_xsrf值，首先获取未登录状态的响应报文，利用soup解析出_xsrf值 
    soup=BeautifulSoup(requests.get(url).text,'html.parser')  
    xsrf=soup.find('input',{'name':re.compile(r'_xsrf')})['value']  
    login_data['_xsrf'] = xsrf.encode('utf-8') 
  
def add_captcha():  
      
    captcha =session.get(captcha_url,stream=True)  
    with open('captcha.gif','wb') as f:  
        for line in captcha.iter_content(10):  
            f.write(line)  
    captcha_str = input('请输入验证码:')   
    login_data['captcha'] = captcha_str  
  
if __name__=='__main__':  
	
    #session = requests.Session()  
    #add_xsrf(login_url,headers)  
    #add_captcha()  
    #responds=session.post(login_url, headers=headers, data=login_data)  
    #with open('zhihu.txt','wt',encoding="utf8",errors='ignore')as f:  
    #  print(session.get(url).text,file=f)
	
	response=requests.get(login_url)
	soup=BeautifulSoup(response.text,'html.parser')
	print(soup)
'''
'''
import urllib
import http.cookiejar as cookielib

cookie=cookielib.CookieJar()
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)

response=opener.open('http://www.baidu.com')

for item in cookie:
	print('Name:'+item.name)
	print('Value:'+item.value)
'''
'''
import requests
import http.cookiejar as cookielib

s=requests.session()
#response=requests.get('http://www.baidu.com')
response2=requests.get('http://fanyi.baidu.com/?aldtype=16047#auto/zh')
print ({c.name: c.value for c in response2.cookies})
'''
'''
import requests

url = 'http://www.baidu.com'
r = requests.get(url)
print(r.cookies)
'''
'''
import pymysql

conn=pymysql.connect(host="127.0.0.1",user='root',password='5jiu2DNF',db='scraping')

cur=conn.cursor()
cur.execute('select * from pages where id=3')
print(cur.fetchone())
cur.close()
conn.close()
'''
'''
import requests
from bs4 import BeautifulSoup
import re

url='http://www.qidian.com'
headers={
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}
response=requests.get(url,headers=headers,)
soup=BeautifulSoup(response.content,'html.parser')
paihang_href=soup.find('a',{'href':re.compile(".+")},text="排行")['href']
paihang_href='http:'+paihang_href
response=requests.get(paihang_href,headers=headers)
soup=BeautifulSoup(response.content,'html.parser')
type_paihang=soup.findAll('h3',{'class':'wrap-title lang'})
print(type_paihang)
'''
#for each_type in type_paihang:
#	print(each_type.text)

'''
import requests
from bs4 import BeautifulSoup
import re

url='https://www.taobao.com/'
headers={
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}
response=requests.get(url,headers=headers)
soup=BeautifulSoup(response.text,'html.parser')
#print(soup.)
jiadian_href=soup.find('a',{'href':re.compile('https.+')},text='家电')['href']

jiadians_urladdress=[]
'''
'''
import requests
params={'firstname':"XC",'lastname':'M'}
response=requests.post('http://pythonscraping.com/files/processing.php',data=params)
print(response.text)
'''
'''
import requests

params={'username':'XCM','password':'password'}
r=requests.post('http://pythonscraping.com/pages/cookies/welcome.php',data=params)
print('cookie is set to:')
print(r.cookies.get_dict())
print('---------------------')
print('Going to profile page....')
r=requests.get('http://pythonscraping.com/pages/cookies/profile.php',cookies=r.cookies)
print(r.text)
'''
'''
str1='I am a boy,you are a girl,gjh gj hjk.'
str2=str1.split(',')
length=0
for i in range(len(str2)):
	length+=len(str2[i].split(' '))
print(length)	
'''
'''
list1=[123,545,6,4,56]
list2=list1.copy()
list1.append(8585)
print(list1)
print(list2)
print(list1[:])
'''
'''
str1='SHnagahi i上ove u abcdefghijklmnopqrstuvwxyz'
m=str1.index('abc')
print(str1[17:])
str2=str1[0:17]+'cha'+str1[18:]
print(str2)
'''
'''
class Cat(object):
	"""docstring for Cat"""
	def __init__(self, name='折耳'):
		super().__init__()
		self.name=name
	__gg=1
	cc=2	
	def show(self,noise='喵喵喵'):
		print('I am %s , %s' % (self.name,noise))
	def showprivate(self):
			return self.__gg	

class SmallCat(Cat):
	pass
sc=SmallCat()	
cat1=Cat()	
cat1.show()
print(cat1._Cat__gg)
print(1/2)
'''
#!/usr/bin/env python
'''
sum=0  
num=[]  
for i in range(1,5):  
    for j in range(1,5):  
        for k in range(1,5):  
            if i!=j and j!=k and i!=k:  
                str1=""  
                str1+=str(i)  
                str1+=str(j)  
                str1+=str(k)  
                print(str1,end=',')  
                sum+=1  
print(sum) 
'''
'''
str1='5656jska'
list1=[1,5,2,'ss']
print(str1*3)
print(list1*2)
print(1//2)
print('')

a='aaaa'
b='aaaa'
print(a is b)
a=[1,2,'s']
b=[1,2,'s']
print(a == b)
'''
'''
a=0
b=1
if ( a > 0 ) and ( b / a > 2 ):
    print( "yes")
else :
    print ("no")

def my_print(args):
    print (args)

def move(n, a, b, c):
    if n==1:
    	my_print ((a, '-->', c)) 
    else :
    	(move(n-1,a,c,b) or move(1,a,b,c) or move(n-1,b,a,c))

move (3, 'a', 'b', 'c')    
'''
'''
denum = int(input("输入十进制数:"))
binnum = []
# 二进制数
while denum > 0:
    binnum.append(denum % 2) # 栈压入
    denum //= 2
while len(binnum)>0:
    print(binnum.pop(),end='')
    '''
'''
i=[1,2,3,4,5]
m=len(i)//2
for n in range(0,m):
	print (n)
class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
'''
'''
import pymysql

# 打开数据库连接
db = pymysql.connect("localhost","xcm","5jiu2DNF","scraping" )
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
# 使用 execute()  方法执行 SQL 查询 
cursor.execute("SELECT VERSION()")
 
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
 
print ("Database version : %s " % data)
 
# 关闭数据库连接
db.close()		
'''
#!/usr/bin/python3
'''
import _thread
import time

# 为线程定义一个函数
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

# 创建两个线程
try:
   _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   _thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
   print ("Error: 无法启动线程")

while 1:
   pass
'''
'''
import threading
import time

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("开始线程：" + self.name)
        print_time(self.name, self.counter, 5)
        print ("退出线程：" + self.name)

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print ("退出主线程")   
'''
'''
def hammingDistance( x, y):
	list1 = []
	list2 = []
	count = 0
	while (x > 0):
		list1.append(x % 2)
		x = x // 2

	while(y > 0):
		list2.append(y % 2)
		y = y // 2
	if list1[-1] == 0:
		list1.pop()
	if list2[-1] == 0:
		list2.pop()
	m = len(list1)
	n = len(list2)
	max = m if m > n else n
	cha=abs(m - n)
	if m > n:
		for i in range(cha):
			list2.append(0)
	else:
		for i in range(cha):
			list1.append(0)	
	print(list1,list2)			
	for i in range(max):
		if (list1[i] != list2[i]):
			count += 1
	print(count)
hammingDistance(1,4)
'''
'''
def test1(nums1,nums2):
	for i in nums2:
		nums1.append(i)
	#nums1=nums1.sort()
	print(nums1)
	print(nums2)	

test1([1,215,6,5],[6,59,3,4])	
'''
'''
#多线程 _thread
import _thread
from time import sleep,ctime

def loop0():
	print("start loop 0 at:",ctime())
	sleep(4)
	print("loop 0 done at:",ctime())

def  loop1():
	print("start loop 1 at:",ctime())
	sleep(2)
	print("loop 1         end at:",ctime())	

def main():
	print("sarting at:",ctime())
	_thread.start_new_thread(loop0,())
	_thread.start_new_thread(loop1,())
	sleep(6)
	print("all done at:",ctime())

if __name__ == '__main__':
	s = "sss"
	c = "ccc"
	print(s+c,3,"s",3)
'''
'''
#多线程 threading
import threading
from time import sleep, ctime

loops = [4,2]

def loop(nloop, nsec):
	print("start loop ", nloop, "at:", ctime())
	sleep(nsec)
	print("loop", nloop, "done at:", ctime())

def main():
	print("starting at:", ctime())
	threads = []
	l = len(loops)
	for i in range(l):
		t = threading.Thread(target = loop, args = (i, loops[i]))
		threads.append(t)
	for i in range(l):
		threads[i].start()

	for i in range(l):
		threads[i].join()

	print("all done at:", ctime())

if __name__ == '__main__':
	main()		
'''
#threading 传入可调用类的实例
'''
import threading
from time import sleep, ctime

loops = [4,2]

class ThreadFunc(object):
	"""docstring for ThreadFunc"""
	def __init__(self, func, args, name = ""):
		self.name = name
		self.func = func
		self.args = args

	def __call__(self):
		self.func(*self.args)

def loop(nloop, nsec):
	print("start loop", nloop, "at:",ctime())
	sleep(nsec)
	print("loop", nloop, "done at:", ctime())

def main():
	print("starting at:", ctime())
	threads = []
	nloops = range(len(loops))

	for i in nloops:
		t = threading.Thread(target = ThreadFunc(loop, (i, loops[i]), loop.__name__))	
		threads.append(t)

	for i in nloops:
		threads[i].start()

	for i in nloops:
		threads[i].join()

	print("all done at:", ctime())	

if __name__ == '__main__':
	main()	

'''
'''
import pymysql
import selenium
db = pymysql.connect("localhost","xcm","5jiu2DNF","ecweb",charset="utf8")
cursor = db.cursor()
result = cursor.execute("select * from orders")
data =cursor.fetchmany(15)
for i in data:
	print(str(i))
db.close()
print(help(selenium))
'''
'''
import re
 
content = 'Hello 1234567 World_This is a Regex Demo'
result = re.search('^Hello\s(\d+)(\sWorld)', content)
print(result)
print(result.group())
print(result.group(2))
print(result.span())
'''
'''
mygenerator = [x*x for x in range(3)]
for i in mygenerator:
	print(i)
print(123156465)
for i in mygenerator:
	print(i)
print(range(5))	
'''

'''
import requests
from pyquery import PyQuery as pq
 
url = 'https://www.zhihu.com/explore'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
html = requests.get(url, headers=headers).text
doc = pq(html)
items = doc('.explore-tab .feed-item').items()
for item in items:
    question = item.find('h2').text()
    author = item.find('.author-link-line').text()
    answer = pq(item.find('.content').html()).text()
    file = open('explore.txt', 'a', encoding='utf-8')
    file.write('\n'.join([question, author, answer]))
    file.write('\n' + '=' * 50 + '\n')
    file.close()
    '''
'''
from urllib.parse import urlencode
import requests
from pyquery import PyQuery as pq

base_url = 'https://m.weibo.cn/api/container/getIndex?'
 
headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/2830678474',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
 
def get_page(page):
    params = {
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1076032830678474',
        'page': page
    }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)
 
def parse_page(json):
    if json:
        items = json.get('data').get('cards')
        for item in items:
            item = item.get('mblog')
            weibo = {}
            weibo['id'] = item.get('id')
            weibo['text'] = pq(item.get('text')).text()
            weibo['attitudes'] = item.get('attitudes_count')
            weibo['comments'] = item.get('comments_count')
            weibo['reposts'] = item.get('reposts_count')
            yield weibo
if __name__ == '__main__':
    for page in range(1, 11):
        json = get_page(page)
        results = parse_page(json)
        for result in results:     
            print(result)    
'''
'''
import requests
from urllib.parse import urlencode
 
def get_page(offset):
    params = {
	        'offset': offset,
	        'format': 'json',
	        'keyword': '街拍',
	        'autoload': 'true',
	        'count': '20',
	        'cur_tab': '1',
	    }
    url = 'http://www.toutiao.com/search_content/?' + urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None
def get_images(json):
    if json.get('data'):
        for item in json.get('data'):
            title = item.get('title')
            images = item.get('image_detail')
            if(title is not None and images is not None):
                for image in images:
                    yield {
                        'image': image.get('url'),
                        'title': title
                    } 
            else:
                pass
import os
from hashlib import md5
 
def save_image(item):
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        response = requests.get(item.get('image'))
        if response.status_code == 200:
            file_path = '{0}/{1}.{2}'.format(item.get('title'), md5(response.content).hexdigest(), 'jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to Save Image')
from multiprocessing.pool import Pool
 
def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        save_image(item)
 
 
GROUP_START = 1
GROUP_END = 20
 
if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()
'''
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
 
browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
    input = browser.find_element_by_id('kw')
    input.send_keys('Python')
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
finally:
    browser.close()
'''
'''
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("http://opac.library.shmtu.edu.cn:8080/opac/newpub/tree/cls")

wait = WebDriverWait(browser, 10)
submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.folder')))
print(browser)
'''
'''
class  Rectangle():
	def __init__(self):
		self.width = 0
		self.height = 0
	def set_size(self,size):
		self.width, self.height = size
	def get_size(self):
		return self.width,self.height
	size = property(get_size,set_size)
r = Rectangle()
r.size = 10,15
print(r.size)		
'''
'''
import os
import sys
import re

def lines(file):
	for line in file:
		yield line
	yield '\n'	

def blocks(file):
	block = []
	for line in lines(file):
		if line.strip():
			block.append(line)
		elif block:	
			yield ''.join(block).strip()
			block = []	

def main():
	print('<html><head><title>test</title><body>')

	title = True

	for block in blocks(sys.stdin):
		block = re.sub(r'\*(.+?)\*',r'<em>\1</em>',block)
		if title:
			print('<h1>')
			print(block)
			print('</h1>')
			title = False
		else:
			print('<p>')
			print(block)
			print('</p>')
	print('</body></html>')		

if __name__ == '__main__':
	main()	

'''
"""class test(object):
	def __init__(self):
		self.data = "sss"
	def test1(self):
		print(self.data)	
t = test()
t.test1()
		"""
#webserver

s = None
if s == None:
	print(1)
else:
	print(2)