# Multiplication table
x = int(input("Enter the number for which you want the multiplication table: "))
y = int(input("Enter the number of rows in the multiplication table: "))
print("Muliplication table for", x)

# Fill in the missing code below to print a multiplication table for x upto y rows.
# If y is more than 20, print the relevant message as per instructions and limit the number of rows to 20
for i in range(1, y+1 ):
	if (i>=21):
		print("Number of rows in this multiplication table is limited to 20")
		break
	print("%d * %d = %d" % (x,i,x*i))
	

#else:

