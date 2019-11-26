n=int(input())
l,r=input().split()
l=int(l)
r=int(r)
count=0
for i in range(l,r):
	if i==n:
		count=count+1
		print("yes")
		break
if count==0:
	print("no")	