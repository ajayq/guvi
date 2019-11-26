n=12345
count=0
while(n>0):
	a=n%10
	if a!=0:
		count=count+1
	n//10	
print(count)