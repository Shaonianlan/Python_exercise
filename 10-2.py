def Dec2Bin(n):
	result=''
	if n==0:
		return result
	else:
		result=Dec2Bin(n//2)
		return result+str(n%2)	
print(Dec2Bin(62))
