import requests
from bs4 import BeautifulSoup
import os, time
import re
import http.cookiejar as cookielib

# 构造 Request headers
agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.368N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'
headers = {
    "Host": "www.zhihu.com",
    "Referer": "https://www.zhihu.com/",
    'User-Agent': agent
}

#构造用于网络请求的session
session = requests.Session()
'''
session.cookies = cookielib.LWPCookieJar(filename='zhihucookie')
try:
    session.cookies.load(ignore_discard=True)
except:
    print('cookie 文件未能加载')
'''

#获取xsrf_token
homeurl = 'https://www.zhihu.com'
homeresponse = session.get(url=homeurl, headers=headers)
#print('cookie is set to:')
#print(homeresponse.cookies.get_dict()['_xsrf'])
#print(homeresponse.text)
homesoup = BeautifulSoup(homeresponse.text, 'html.parser')
print(homesoup)

'''
xsrfinput = homesoup.find('input', {'name':re.compile(r'_xsrf')})
#print(xsrfinput)
xsrf_token = xsrfinput['value']
print("获取到的xsrf_token为： ", xsrf_token)


#开始登陆
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
    # 获取验证码文件
    randomtime = str(int(time.time() * 1000))
    captchaurl = 'https://www.zhihu.com/captcha.gif?r=' + \
                 randomtime + "&type=login"
    captcharesponse = session.get(url=captchaurl, headers=headers)
    with open('checkcode.gif', 'wb') as f:
        f.write(captcharesponse.content)
        f.close()
    os.startfile('checkcode.gif')

    #发送登陆信息
    captcha = input('请输入验证码：')
    postdata['captcha'] = captcha
    loginresponse = session.post(url=loginurl, headers=headers, data=postdata)
    print('服务器端返回响应码：', loginresponse.status_code)
    print(loginresponse.json())


#保存登陆后的cookie信息
#session.cookies.save()
#登录成功
profileurl = 'https://www.zhihu.com/settings/profile'
profileresponse = session.get(url=profileurl, headers=headers)
print('profile页面响应码：', profileresponse.status_code)
profilesoup = BeautifulSoup(profileresponse.text, 'html.parser')
div = profilesoup.find('span', {'class': 'name'})
print('用户名为：%s' % div.text)

main_url='https://www.zhihu.com'
main_response=session.get(url=main_url,headers=headers)
main_soup=BeautifulSoup(main_response.text,'html.parser')
new_questions=main_soup.findAll('a',{'target':'_blank','data-za-detail-view-element_name':'Title'})

for each_news in new_questions:
    print(each_news.text)

keyword_question_url_list=[]    
keyword=input('请输入关键字：')

for each_news in new_questions:
    if keyword in each_news.text:
        keyword_question_url='https://www.zhihu.com'+str(each_news['href'])
        keyword_question_url_list.append(keyword_question_url)
        break

questions=[]
for each in keyword_question_url_list:
    print(each)
    response=requests.get(url=each,headers=headers)
    soup=BeautifulSoup(response.text,'html.parser')
    questions=soup.findAll('span',{'class':'RichText CopyrightRichText-richText'}) 
    #print(questions)

for each in questions:
    print(each)           
'''