string=input("enter the string")
list=[]
character=input("enter the letter:")
for i in range(0,len(string)):
 list.append(string[i])
list=list[::-1]
for i in list:
 if(i==character):
  list.remove(i)
  break
print("deleted lastoccurence occurence","".join(list[::-1]))