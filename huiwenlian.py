def huilian(n):
	length=len(n)
	for index in range(length-1):
		flag=0
		if n[index]==n[length-index-1]:
			flag=1
			continue
		else:
			flag=0	
			break
	if flag:
		print('%s 是回文联。' % n)
	else:
		print('%s 不是回文联' % n)			
				

#递归法
def  huilian2(n,start,end):
	if start<end:
		if n[start]==n[end]:
			return huilian2(n,start+1,end-1)
		else:
			return 0
	else:
		return 1	
n=input('请输入一段文字，判断是否是回文联：')
result=huilian2(n,0,len(n)-1)	
if result:
	print('%s \n是回文联' % n)
else:
	print('%s \n不是回文联' % n)				