def countword(*param):
	length=len(param)
	for i in range(length):
		zimu=0
		kongge=0
		shuzi=0
		qitazifu=0
		for each in param[i]:
			if each.isalpha():
				zimu+=1
			elif each.isspace():
				kongge+=1
			elif each.isdigit():
				shuzi+=1
			else:
				qitazifu+=1
		print('第 %d 个字符有 %d 个字母，%d个数字，%d 个空格，%d 个其他字符'\
		 % (i+1,zimu,shuzi,kongge,qitazifu))
countword('sda fsadwa 5264s5a1d54_)(+_(O','shdij&^&*HG(')