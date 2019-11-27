# write   a program to find how many vowels and consonants in a string
string=input()
countvowel=0
countcon=0
# (a e i o u)-vowels and remaining consonants
for i in range(0,len(string)):
 if string[i]=='a' or string[i]=='e' or string[i]=='i' or string[i]=='o' or string[i]=='u' or string[i]=='A' or string[i]=='E' or string[i]=='I' or string[i]=='O' or string[i]=='U':
  countvowel=countvowel+1
 else:
  countcon=countcon+1
print("number of vowels",countvowel)
print("numbers of consonants",countcon)