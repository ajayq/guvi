class stack:
	def __init__(self):
		self.list=[]
	def push(self,a):
		self.list.append(a)
	def pop(self):
	        return self.list.pop()
s1=stack()
s1.push(5)
s1.push(7)
a=s1.pop()

print(s1.list)
