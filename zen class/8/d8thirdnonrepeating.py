list=[]
list=input().split()
print(list)
duplicate=[]
nonrepeat=[]
for i in range(0,len(list)):
 for j in range(i+1,len(list)):
  if list[i]==list[j]:
   duplicate.append(list[i])
for i in range(0,len(list)):
 if list[i] not in duplicate:
  nonrepeat.append(list[i])
print(nonrepeat)
if len(nonrepeat)==0:
 print("none")
if len(nonrepeat)<3:
 print("the last non repeating element is :",nonrepeat[len(nonrepeat)-1])
print(nonrepeat[2])	