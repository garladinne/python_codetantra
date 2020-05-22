num=int(input("Enter a number: "))
n=num
count=0
while(num!=0):
	digit=num%10
	count+=1
	num=num//10
num=n
#print("Number of digits",count)
sum=0
while (num !=0):
	digit=num % 10
	
	sum=sum+digit ** count
	
	num=num//10

print("The sum of the powers of the digits = %d" % sum)
if (sum==n):
	print("The given number %d is an armstrong number" % n)
else:
	print("The given number %d is not an armstrong number" % n)
