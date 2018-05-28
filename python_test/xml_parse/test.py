from xml.sax.handler import ContentHandler
from xml.sax import parse

class HeadlineHandler(ContentHandler):
	in_handline = False

	def __init__(self,headlines):
		ContentHandler.__init__(self)
		self.headlines = headlines
		self.data = []

	def startElement(self,name,attrs):
		if name == 'h1':
			self.in_handline = True

	def characters(self,string):
		if self.in_handline:
			self.data.append(string)

	def endElement(self,name):
		if name == 'h1':
			text = ''.join(self.data)
			self.data = []
			self.in_handline = False
			self.headlines.append(text)

headlines = []
parse('website.xml',HeadlineHandler(headlines))
print("the following<h1>:")
for h in headlines:
	print(h)	
