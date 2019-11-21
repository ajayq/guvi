n=int(input("enter the number of subjects"))
marks=[]
total=0

for j in range(1,n+1):
	marks.append(int(input("enter the marks%d:"%j)))
for i in range(n):
	total=total+marks[i]
average=total/n	
for i in range(n):
	print(marks[i])
print(total)
print(average)
