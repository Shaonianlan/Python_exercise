from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery as pq
import pymysql

#获取商品
def get_products(browser):
	"""
	提取商品数据
	"""
	html = browser.page_source
	doc = pq(html)
	items = doc('#mainsrp-itemlist .items .item').items()
	for item in items:
		product = {
			'image': item.find('.pic .img').attr('data-src'),
			'price': item.find('.price').text(),
			'deal': item.find('.deal-cnt').text(),
			'title': item.find('.title').text(),
			'shop': item.find('.shop').text(),
			'location': item.find('.location').text()
		}
		print(product)
		save_to_mysql(product)

#获取商品页面
def index_page(page):
	SERVICE_ARGS = ['--load-images=false', '--disk-cache=true']
	browser = webdriver.PhantomJS(service_args=SERVICE_ARGS)
	wait = WebDriverWait(browser, 10)
	KEYWORD = 'iPad'

	print("正在爬取",page,"页")
	try:
		url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
		browser.get(url)
		if page > 1:
			input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
			submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit')))
			input.clear()
			input.send_keys(page)
			submit.click()
		wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))
		wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
		get_products(browser)
	except TimeoutException:
		index_page(page)

#保存到mysql
def save_to_mysql(product):
	db = pymysql.connect("localhost","xcm","5jiu2DNF","scraping",charset="utf8")
	cursor = db.cursor()
	sql = cursor.execute("insert into taobao_goods values ")
	"""
	保存至Mysql
	:param result: 结果
	"""
	try:
		if cursor.execute(sql):
		    print('存储到Mysql成功')
		db.commit()   
	except Exception:
		print('存储到Mysql失败')
		db.rollback()
	db.close()		

#执行
def main():
	MAX_PAGE = 2
	"""
	遍历每一页
	"""
	for i in range(1, MAX_PAGE + 1):
		index_page(i)
if __name__ == '__main__':
	main()		