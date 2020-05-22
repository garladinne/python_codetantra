n=int(input("Enter a number: "))
sum=0
i=1
while(i<=n):
	sum = sum + i
	i += 1
if (n<0):
	i=n
	while(i<0):
		sum=sum+i
		i += 1
print("The sum is %d" % sum)
