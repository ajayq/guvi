name1=input("enter your name")
maths1=int(input())
science1=int(input())
social1=int(input())
total1=maths1+science1+social1
print("total:",total1)
average1=total1/3

print("average:",float(average1))
name2=input("enter your name")
maths2=int(input())
science2=int(input())
social2=int(input())
total2=maths2+science2+social2
print("total:",total2)
average2=total2/3
print("average:",float(average2))
name3=input("enter your name")
maths3=int(input())
science3=int(input())
social3=int(input())
total3=maths3+science3+social3
print("total:",total3)
average3=total3/3
print("average:",float(average3))
if average1>60:
	if average1<=100 and average1>90:
		print(name1,"is selected for IIT")
	elif average1<=90 and average1>80:
		print(name1,"is selected for MCC")
	elif average1<=80 and average1>70:
		print(name1,"is selected for loyola")
else:
	print(name1,"is rejected ")
if average2>60:
	if average2<=100 and average2>90:
		print(name2,"is selected for IIT")
	elif average2<=90 and average2>80:
		print(name2,"is selected for MCC")
	elif average2<=80 and average2>70:
		print(name2,"is selected for loyola")
else:
	print(name2,"is rejected ")
if average1>60:
	if average3<=100 and average3>90:
		print(name3,"is selected for IIT")
	elif average3<=90 and average1>80:
		print(name3,"is selected for MCC")
	elif average3<=80 and average1>70:
		print(name3,"is selected for loyola")
else:
	print(name3,"is rejected ")
r=input()