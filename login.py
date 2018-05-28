user_data={}

def old_user():
	prompt='请输入用户名：'
	panduan=True
	while panduan:
		name=input(prompt)
		if name not in user_data:
			if name=='esc' or name=='ESC':
				break
			else:	
				prompt='用户名不存在，请重新输入：'
				continue
		else:
			panduan=False
	else:		
		password=input('请输入密码：')
		pwd=user_data.get(name)
		if password==pwd:
			print('欢迎进入***系统！')
		else:
			print('密码错误！')		


def new_user():
	prompt='请输入注册的用户名：'
	while True:
		name=input(prompt)
		if name in user_data:
			prompt='用户名已存在，请重新输入：'
			continue
		else:
			if name=='esc' or name=='ESC':
				break
			else:	
				password1=input('请输入密码：')
				password2=input('确认密码：')
				if password1==password2:
					user_data.setdefault(name,password1)
					print('注册成功！')
					break
				else:
					print('请确保两次输入的密码相同！')	
					continue


def showmenu():
	prompt='''
	|---新建用户：N/n---|
	|---登陆账户：E/e---|
	|---退出程序：Q/q---|
	|---请输入指令代码---
	'''
	while True:
		chosen=False
		while not chosen:
			choice=input(prompt)
			if choice not in 'NnEeQq':
				print('输入的指令代码错误，请重新输入：')
			else:
				chosen=	True
		if choice=='q' or choice=='Q':
			break
		elif choice=='N' or choice=='n':
			print('|---输入esc/ESC返回---|')
			new_user()
		elif choice=='E' or choice=='e':
			print('|---输入esc/ESC返回---|')
			old_user()			
showmenu()			