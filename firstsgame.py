import random
answer=random.randint(1,10)
num=input("请输入1-10的整数：")
if num.isdigit():
	n=int(num)
	count=1
	if n==answer:
		print("True!")
	else:	
		while count<=3 :
			n=int(num)
			print(n)
			count=count+1
			if(n>answer):
				print("大了!")
				if(count!=4):
					num=input("请重新输入1-10的整数:")
			else: 
				if(n<answer):
					print("小了!")
					if(count!=4):
						num=input("请重新输入1-10的整数:")
				else:
					print("true!");			
	print("End!")
else:
	print("请输入正确的数字")	
