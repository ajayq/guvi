nstring=input("enter the string")
character=input("enter the letter:")
count=0
position=[]
for i in range(0,len(string)):
 if string[i]==character:
   string2=string.replace(string[i],"")
print("deleted string",string2)