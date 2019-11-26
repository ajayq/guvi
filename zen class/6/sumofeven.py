evenno=[]
n=int(input())
evensum=0
i=0
while(i<=n):
 if(i%2==0):
  evenno.append(i)
 i=i+1
print("evennumber:",evenno)
for i in evenno:
 evensum=evensum+i
print("evennumber sum:",evensum)