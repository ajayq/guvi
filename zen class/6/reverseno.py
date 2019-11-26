num=int(input())
temp=num
reverse=0
while(temp>0):
	a=temp%10
    reverse=reverse*10+a
    temp=temp//10
 print("reversed number:"reverse)