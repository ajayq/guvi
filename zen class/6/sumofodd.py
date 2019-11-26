oddno=[]
n=int(input())
oddsum=0
i=0
while(i<=n):
 if(i%2!=0):
  oddno.append(i)
 i=i+1
print("oddnumbers:",oddno)
for i in oddno:
 oddsum=oddsum+i
print("oddnumber sum",oddsum)