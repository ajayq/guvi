n=[]
b=[]
n=input().split()
print(n)
for i in n:
	order=ord(i)+1
	b.append(chr(order))
print(b)
