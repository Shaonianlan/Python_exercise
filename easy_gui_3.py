import easygui as g
import os

target=['.c','.cpp','.py','.cc','.java','.pas','.asm','.txt','.css','.jsp']
file_list={}
source_list={}

def search_file(start_dir):
	os.chdir(start_dir)

	for each_file in os.listdir(os.curdir):
		ext=os.path.splitext(each_file)[1]
		if ext in target:
			lines=calc_code(each_file) #记录行数
			#用抛出异常地方法，如果字典中不存在，抛出Keyerror，添加字典键
			#统计文件数
			try:
				file_list[ext]+=1
			except KeyError:
				file_list[ext]=1
			#统计源代码行数
			try:
				source_list[ext]+=lines
			except KeyError:
				source_list[ext]=lines
		elif os.path.isdir(each_file):
			search_file(each_file) #递归调用
			os.chdir(os.pardir) #必须要返回上一层目录

def calc_code(file_name):
	lines=0
	with open(file_name,'rb') as f:
		print('正在分析文件：%s ...' % file_name)

		for each_line in f:
			lines+=1
	return lines			
'''
		except UnicodeDecodeError:
			print(file_name)
			pass #不可避免会遇到格式不兼容的文件 忽略掉

	return lines
'''		

def show_result(start_dir):
	lines=0
	total=0
	text=''

	for i in source_list:
		lines=source_list[i]
		total+=lines
		text+='【%s】源文件%d个，源代码%d行\n' % (i,file_list[i],lines)
	title='统计结果'
	msg='目前共累计编写了%d行代码，完成进度：%.2f %% \n 离10万行代码还差%d行。'%(total,\
		total/1000,100000-total)
	g.textbox(msg,title,text)

g.msgbox('                           请打开你存放所有代码的文件夹','统计代码')
path=g.diropenbox('请选择你的代码库：')

search_file(path)
show_result(path)	
