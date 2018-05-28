import os

def print_pos(key_dict):
	keys=key_dict.keys()
	keys=sorted(keys)
	for each_key in keys:
		print('关键字出现在第%s行，第%s个位置。' %(each_key,str(key_dict[each_key]))) 

def pos_in_file(line,key):
	pos=[]
	begin=line.find(key)
	while begin!=-1:
		pos.append(begin+1)
		begin=line.find(key,begin+1)
	return pos

def search_in_file(file_name,key):
	f=open(file_name)
	count=0
	key_dict={}

	for each_line in f:
		count+=1
		if key in each_line:
			pos=pos_in_file(each_line,key)
			key_dict[count]=pos
	f.close()
	return key_dict

def search_files(key,detail):
	all_files=os.walk(os.getcwd())
	txt_files=[]

	for i in all_files:
		for each_file in i[2]:
			if os.path.splitext(each_file)[1]=='.txt':
				each_file=os.path.join(i[0],each_file)
				txt_files.append(each_file)	
	for each_txt_file in txt_files:
		key_dict=search_in_file(each_txt_file,key)
		if key_dict:
			print('==============================================')
		print('在文件%s中找到关键字\"%s\"' % (each_txt_file,key))
		if detail in ['YES','Yes','yes']:
			print_pos(key_dict)	

key=input('请将该脚本放在待查找的文件夹中，请输入关键字：')
detail=input('是否需要打印关键字\"%s\"在文件中的位置（YES/NO）：'%key)
search_files(key,detail)			