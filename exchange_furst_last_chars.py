st=input("Enter a string: ")
l=len(st)
if (l==1):
	print(st)
elif (l==0):
	print("Null string")
else:
	first=st[0]
	last=st[-1]
	middle=st
	qq=st[-1:] + st[1:-1] + st[:1]
	print("The string after exchanging first and last characters:",qq)
