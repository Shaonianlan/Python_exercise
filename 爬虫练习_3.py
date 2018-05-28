import urllib.request
import os
import get_url as gu


def get_page(url):
	html=gu.get_url(url).decode('utf-8')

	a=html.find('current-comment-page')+23
	b=html.find(']',a)

	return html[a:b]

def find_image(url):
	html=gu.get_url(url).decode('utf-8')
	img_addrs=[]

	a=html.find('img src=')

	while a!=-1:
		b=html.find('.jpg',a,a+255)

		if b!=-1:
			htmln='http:'+str(html[a+9:b+4])
			img_addrs.append(htmln)
		else:
			b=a+9	
		a=html.find('img src=',b)

	return img_addrs

def save_image(folder,img_addrs):
	for each in img_addrs:
		filename=each.split('/')[-1]
		with open(filename,'wb') as f:
			try:
				img=gu.get_url(each)
				f.write(img)
			except:
				pass	


def download__mm(folder='ooxx',pages=10):
	os.mkdir(folder)
	os.chdir(folder)


	url='http://jandan.net/ooxx/'
	page_num=int(get_page(url))

	for i in range(page_num):
		page_num-=i
		page_url=url+'page-'+str(page_num)+'#comments'
		img_addrs=find_image(page_url)
		save_image(folder,img_addrs)
		print(img_addrs)

if __name__=='__main__':
	download__mm()	
			