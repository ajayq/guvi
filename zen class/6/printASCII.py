#printing all ASCII VALUES
specialcharacters=[]
cl=[]
smallletters=[]
condition=[]
numbers=[]
for i in range(33,48):
 specialcharacters.append(chr(i))
for i in range(48,58):
 numbers.append(chr(i))
for i in range(58,65):
 condition.append(chr(i))
for i in range(65,91):
 cl.append(chr(i))
for i  in range(97,123):
 smallletters.append(chr(i))
print("specialcharacters:",specialcharacters)
print("captialletters:",cl)
print("smallletters:",smallletters)
print("condition:",condition)
print("numbers",numbers)