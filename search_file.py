import os
#查找目标目录下所有的视屏文件，并把文件路径保存到新建文本中
def search_file(start_dir,target=['.mp4','.avi','.rmvb','.mp3']):
	os.chdir(start_dir)

	for each_file in os.listdir(os.curdir):
		ext=os.path.splitext(each_file)[1]
		if ext in target:
			vedio_list.append(os.getcwd()+os.sep+each_file+os.linesep)
		elif os.path.isdir(each_file):#判断each_file是否是一个目录
			search_file(each_file,target) #递归调用
			os.chdir(os.pardir) #返回上一层目录

vedio_list=[]
program_dir=os.getcwd()
start_dir=input('请输入待查找的初始目录：')
search_file(start_dir)

f=open(program_dir+os.sep+'vediolist.txt','w')	
f.writelines(vedio_list)
f.close()
