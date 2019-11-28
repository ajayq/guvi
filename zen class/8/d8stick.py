def stick(list,joiner):
 string=''
 for  i in range(0,len(list)):
  if isinstance(list[i],int):
   a=str(list[i])
   print("acasd",a)
   string=string+a+joiner
  else:
   string=string+list[i]+joiner
   
 return string

 
list=[1,2,3,3,2,23,2,2,3,23,123,24,234,234,234]
list2=[]
list2=input().split()
print(stick(list,"%"))
print(stick(list2,"*")) 
