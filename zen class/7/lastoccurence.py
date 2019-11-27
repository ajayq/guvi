string=input("enter the string")
character=input("enter the letter:")
count=0
for i in range(0,len(string)):
 if string[i]==character:
   count+=1
   print(i)