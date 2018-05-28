for i in range(100):
	temp=i*7
	if (temp-5)%6==0 and (temp-4)%5==0 and (temp-2)%3==0 and (temp-1)%2==0:
		print('总共有%d阶楼梯' % temp)
		break
	else:
		continue	
#2x+1=3y+2=5m+4=6n+5=7z