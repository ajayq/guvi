string=input("enter the string")
character=input("enter the letter:")
count=0
position=[]
for i in range(0,len(string)):
 if string[i]==character:
  count+=1
  position.append(i+1)
print("the number of times " ,character," occured in string is",count)
print("occured position:",position)