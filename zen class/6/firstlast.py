n=int(input())
temp=n
lastdigit=n%10
while(n>=10):
 firstdigit=n//10
 n=n//10
 
print("lastdigit:",lastdigit)
print("firstdigit:",firstdigit)
print("sum of last&first",lastdigit+firstdigit)