str=input()
j=len(str)-1
count=0
for i  in range(0,len(str)):
	if str[i]==str[j]:
		count=count+1
	j=j-1
if len(str)==count:
	print("pallindrome")
else:
	print("no")