def filesave(filename):
	f=open(filename,'w')
	print('请输入内容【单独输入\':w\'保存退出】：')

	while True:
		write_some=input()
		if write_some != ':w':
			f.write('%s\n' % write_some)
		else:
			break
	f.close()
filename=input('请输入文件名：')
filesave(filename)			