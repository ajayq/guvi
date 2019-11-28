def isnewupper(val):
 count=0
 for i in range(0,len(val)):
  for j in range(65,91):
   if val[i]==chr(j):
    count=count+1
 if count==len(val):
  return True
   
 