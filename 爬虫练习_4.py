import urllib.request 
import urllib.error 

if __name__ == '__main__':
	url='http://knadk hnajiksnhkojd .com/'
	req=urllib.request.Request(url)
	try:
		response=urllib.request.urlopen(req)
		html=response.read().decode('utf-8')
		print(html)
	except urllib.error.URLError as e:
		print(e)	
