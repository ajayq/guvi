string=input("enter the string")
list=[]
character=input("enter the letter:")
for i in range(0,len(string)):
 list.append(string[i])
for i in list:
 if(i==character):
  list.remove(i)
  break
 
print("deleted first occurence","".join(list))