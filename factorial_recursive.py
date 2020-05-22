def factorial(n):
	if (n==1):
		fact=1
		return fact
	else:
		fact=n*factorial(n-1)
		return fact
n=int(input("Enter a number to find its factorial: "))
if (n>0):
	fact=factorial(n)
	print("The factorial of",n,"is:",fact)
else:
	print("Enter a positive value to find its factorial")