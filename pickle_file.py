import pickle

def save_file(I,You,count):
	file_name_i='i_'+str(count)+'.txt'
	file_name_you='you_'+str(count)+'.txt'

	i_file=open(file_name_i,'wb') #以二进制写入
	you_file=open(file_name_you,'wb')

	pickle.dump(i,i_file)
	pickle.dump(you,you_file)

	i_file.close()
	you_file.close()

def split_file(file_name):
	count=1
	i=[]
	you=[]

	f=open(file_name)

	for each_line in f:
		if each_line[:6]='=======':
			(role,line_spoken)=each_line.split(':',1)
			if role=='我':
				i.append(line_spoken)
			elif role =='你':
				you.append(line_spoken)

			i=[]
			you=[]	
			count+=1

	save_file(i,you,count)
	f.close()

split_file(filename)			
