n=int(input("Please enter a number: "))
print("Odd and Even numbers")
for i in range(0,n):
	if(i % 2 == 0):
		print("{0} is an even number".format(i))
	else:
		print("{0} is an odd number".format(i))
