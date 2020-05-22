def factorial(n):
	if (n==1):
		fact=1
		return fact
	else:
		fact=n*factorial(n-1)
		return fact
num=int(input("Enter number to find strong or not: "))
n1=num
sum=0
while(num!=0):
	n=num % 10
	if (n == 0):
		sum = 1
	else:
		sum = sum + factorial(n)
	num=num//10
if (sum==n1):
	print("The given number",n1,"is a strong number")
else:
	print("The given number",n1,"is not a strong number")
