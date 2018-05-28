class SolidList(object):
	"""docstring for SolidList"""
	def __init__(self, *args):
		super(SolidList, self).__init__()
		self.value=[x for x in args]
		self.count={}.frokeys(range(len(self.values)),0)
	def __len__(self):
			return len(self.values)
		
	def __getitem__(self,key):
			self.count[key]+=1
			return self.values[key]	
			