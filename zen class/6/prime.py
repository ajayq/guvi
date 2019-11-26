n=int(input())
for i in range(2, n+ 1):
       for j in range(3, n+1):
           if (i % j) == 0:
               break
           else:
               print(i)