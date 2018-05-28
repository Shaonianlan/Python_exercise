class CountList(list):
	def __init__(self,*params):
		super().__init__(params)
		self.count=[]
		for i in params:
			self.count.append(0)

	def __len__(self):
		return len(self.count)

	def __getitem__(self):
		self.count[key]+=1
		return super().__getitem__(key,value)			