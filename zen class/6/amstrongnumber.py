n=int(input())
power=len(str(n))
temp=0
while(n>0):
	digit=n%10
	temp+=digit**power
	temp=n//10
if temp==n:
	print("amstrongnumber")
else:
	print("no")
