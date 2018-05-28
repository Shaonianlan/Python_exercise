import random
import easygui as g

g.msgbox('欢迎进入界面小游戏')
secret=random.randint(1,10)
msg='猜一下现在这个随机的数字（1~10）:'
title='数字小游戏'
guess=g.integerbox(msg,title,lowerbound=1,upperbound=10)

while True:
	if guess==secret:
		g.msgbox('猜对了')
		break
	else:
		if guess>secret:
			g.msgbox('大了')
		else:
			g.msgbox('小了')
		guess=g.integerbox(msg,title,lowerbound=1,upperbound=10)
		
g.msgbox('游戏结束')
					