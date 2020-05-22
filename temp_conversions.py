sr=input("Please enter temperature with unit: ")
unit=sr[-1]
f=float(sr[:-1])
if (unit=='f' or unit=='F'):
	c=(5/9)*(f-32)
	c=round(c,2)
	print(sr[:-1],"F","=",c,"C")
elif (unit=='c' or unit=='C'):
	f=(9*f+32*5)/5
	f=round(f,2)
	print(sr[:-1],"C","=",f,"F")
else:
	print("Unrecognized unit:",sr[-1])
	