num=int(input("Enter number to find prime or not: "))
n=num
p=0
for i in range (2,num):
	if (num % i == 0):
		p=1
if (p==1):
	print("The given number",n,"is not a prime number")
else:
	print("The given number",n,"is a prime number")