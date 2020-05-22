num=int(input("Enter the number: "))
n=num
sum=0
while(num!=0):
	digit=num % 10
	sum = sum + digit
	num=num//10
print("The sum of digits of",n,"is",sum)