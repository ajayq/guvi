# program to count alphabets,char,digits

string = input("Enter a string: ")
length = len(string)
uppercount = 0
smallcount = 0
numbercount = 0
specialcount = 0
for i in range(0,length):
 temp = ord(string[i])
 if(temp>48 and temp<58):
  numbercount +=1
 elif(temp>64 and temp<91):
  uppercount += 1
 elif(temp>96 and temp<123):
  smallcount += 1
 else:
  specialcount += 1
print("The number of digits are: ",numbercount)
print("The number of upper case alphabets are: ",uppercount)
print("The number of lower case alphabets are: ",smallcount)
print("The number of special characters are: ",specialcount)