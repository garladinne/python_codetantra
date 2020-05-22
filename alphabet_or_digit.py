print("Enter '0' for exit.")

# take th input from the user
ch=input("Enter any character: ")
if ch == '0':
	exit()
elif (ord(ch)>=48 and ord(ch)<=57):
	print("Given character %s is a digit" % ch)
elif (ord(ch)>=65 and ord(ch)<=92) or (ord(ch)>=97 and ord(ch)<=122):
	print("Given character %s is an alphabet" % ch)
else:
	print("%s is not an alphabet nor a digit" % ch)
