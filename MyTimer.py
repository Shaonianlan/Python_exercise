import time

class MyTimer(object):
	def __init__(self):
		self.prompt='未开始计时'
		self.unit=['年','月','日','时','分','秒']
		self.lasted=[]
		self.begin=0
		self.end=0
		pass
	def __str__(self):
		return self.prompt	

	__repr__=__str__	`

	def __add__(self,other):
		prompt='总共运行了'
		result=[]
		for index in range(6):
			result.append(self.lasted[index]+other.lasted[index])
			if result[index]:
				prompt+=(str(result[index])+self.unit[index])
		return prompt		

	#开始计时
	def start(self):
		self.begin=time.localtime()
		self.prompt='请先调用stop() 停止计时'
		print('计时开始')

	#停止计时
	def stop(self):
		if not self.begin:
			print('请先调用start() 开始计时')
		else:	
			self.end=time.localtime()
			print('停止计时')
			self.eachtime()
		pass

	#计算运行时间
	def eachtime(self):
		self.lasted=[]
		self.prompt='运行了'
		for index in range(6):
			self.lasted.append(self.end[index]-self.begin[index])
			self.prompt+=(str(self.lasted[index])+self.unit[index])	
		self.begin=0
		self.end=0		
t1=MyTimer()
t1.start()
t1.stop()
print(t1)
t2=MyTimer()
t2.start()
t2.stop()
print(t1+t2)
