import random

#边界范围
legal_x=[0,10]
legal_y=[0,10]

#乌龟
class Turtle:
	def __init__(self):
		#初始化乌龟的体力和位置
		self.power=100
		self.x=random.randint(legal_x[0],legal_x[1])
		self.y=random.randint(legal_y[0],legal_y[1])

	def turtle_moving(self):
		#移动
		moved_x=self.x+random.randint(-2,2)
		moved_y=self.y+random.randint(-2,2)
		#检查x方向移动后是否还在界内
		if moved_x<legal_x[0]:
			self.x=legal_x[0]-(moved_x-legal_x[0])
		elif moved_x>legal_x[1]:
			self.x=legal_x[1]-(moved_x-legal_x[1])
		else:
			self.x=moved_x
		#判断y方向移动后是否还在界内
		if moved_y<legal_y[0]:
			self.y=legal_y[0]-(moved_y-legal_y[0])
		elif moved_y>legal_y[1]:
			self.y=legal_y[1]-(moved_y-legal_y[1])	
		else:
			self.y=moved_y
		#体力消耗	
		self.power-=1
		return (self.x,self.y)

	def turtle_eating(self):
		self.power+=20
		if self.power>100:
			self.power=100

#鱼
class Fish:
	def __init__(self):
		#初始化鱼的位置
		self.x=random.randint(legal_x[0],legal_x[1])
		self.y=random.randint(legal_y[0],legal_y[1])

	def fish_moving(self):
		#移动
		moved_x=self.x+random.randint(-1,1)
		moved_y=self.y+random.randint(-1,1)	
		#检查移动后x是否在界内
		if moved_x<legal_x[0]:
			self.x=legal_x[0]-(moved_x-legal_x[0])
		elif moved_x>legal_x[1]:
			self.x=legal_x[1]-(moved_x-legal_x[1])
		else:
			self.x=moved_x
		#检查移动后y是否在界内
		if moved_y<legal_y[0]:
			self.y=legal_y[0]-(moved_y-legal_y[0])	
		elif moved_y>legal_y[1]:
			self.y=legal_y[1]-(moved_y-legal_y[1])
		else:
			self.y=moved_y	
		return (self.x,self.y)	

turtle=Turtle()
fish=[]
for i in range(10):
	new_fish=Fish()
	fish.append(new_fish)

while True:
	if len(fish)==0:
		print('鱼被吃完了！')
		break
	if turtle.power==0:
		print('乌龟体力耗尽，游戏结束!')
		break

	pos=turtle.turtle_moving()
	#在迭代器中删除列表元素是非常危险的，经常会出现意想不到的问题，迭代器是直接引用列表的数据进行引用
	#把列表拷贝给迭代器，然后对原列表进行删除
	for each_fish in fish[:]:
		if each_fish.fish_moving()==pos:
			turtle.turtle_eating()
			fish.remove(each_fish)
			print('吃掉了一条鱼！')
