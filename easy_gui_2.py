import easygui as g
msg='请填写一下联系方式'
title='账号中心'
fieldNames=['*用户名','*真实姓名','*手机号码','QQ','*E-mail']
fieldValues=[]
fieldValues=g.multenterbox(msg,title,fieldNames)

while True:
	if fieldValues==None:
		break
	errmsg=''
	for i in range(len(fieldNames)):
		option=fieldNames[i].strip()
		if fieldValues[i].strip()=="" and option[0] == "*":
			errmsg+=('【%s】为必填项。\n\n' % fieldNames[i])
	if errmsg=='':
		break
	fieldValues=g.multenterbox(errmsg,title,fieldNames,fieldValues)

print('用户的资料如下：%s ' % str(fieldValues))				