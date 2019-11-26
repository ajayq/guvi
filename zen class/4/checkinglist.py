a=[]
a=input().split()
b=[]
b=input().split()
count=0
	for i in a:
		for j in b:
			if int(i)==int(j):
		 		count+=1
if count==len(a):
	print("same")
else:
	print("different")
