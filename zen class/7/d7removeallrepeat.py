string=input("enter the string:")
list=string.split()
for i in range(0,len(string)):
 print(i,"//////////")
 for j in range(i+1,len(string)):
  print("************",j)
  if list[i]==list[j]:
   print(list[i])