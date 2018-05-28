print('|---欢迎进入通讯录程序---|')
print('|---1:查询联系人资料  ---|')
print('|---2:添加新的联系人  ---|')
print('|---3:删除已有联系人  ---|')
print('|---4:退出通讯录成勋  ---|')

tongxunlu={}
while True:
	n=input('请输入要进行的操作的标号：')
	while not n.isdigit():
		n=input('请输入正确的操作的标号：')
	else:	
		#查询
		funcpoint=int(n)
		if funcpoint==1:
			temp1=input('请输入要查询的联系人姓名：')
			if tongxunlu.get(temp1.strip())==None:
				print('联系人不存在！')
			else:
				print(temp1.strip()+':'+tongxunlu[temp1.strip()])	
			continue
		#添加	
		elif funcpoint==2:
			temp1=input('请输入要新添加联系人姓名：')
			if tongxunlu.get(temp1.strip())==None:
				temp2=input('请输入新联系人的电话：')
				tongxunlu.setdefault(temp1,temp2)
				print('添加成功！')
			else:
				print('联系人已存在！')
				print(temp1.strip()+':'+tongxunlu[temp1.strip()])
			continue	
		#删除
		elif funcpoint==3:
			temp1=input('请输入要删除的联系人姓名：')
			if tongxunlu.get(temp1.strip())==None:
				print('联系人不存在！')
			else:
				tongxunlu.pop(temp1)
				print('%s 已删除' % temp1)
			continue
		#退出
		elif funcpoint==4:
			break	
		else:
			print('请输入1-4的序号!')	

