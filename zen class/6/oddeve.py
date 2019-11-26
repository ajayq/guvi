oddno=[]
evenno=[]
n=int(input())
evensum=0
oddsum=0
i=0
while(i<=n):
 if(i%2==0):
  evenno.append(i)
 else:
  oddno.append(i)
 i=i+1
print("oddnumbers:",oddno)
print("evennumber:",evenno)
for i in oddno:
 oddsum=oddsum+i
for i in evenno:
 evensum=evensum+i
print("oddnumber sum",oddsum)
print("evennumber sum",evensum)