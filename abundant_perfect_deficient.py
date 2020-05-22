num=int(input("Enter an integer: "))
factors=[1]
sum=1
for i in range(2,num):
	if (num%i==0):
		factors.append(i)
		sum+=i
print("The factors of",num,"are:",factors)
#sum=0
#for i in factors:
#	sumt=sum+factors(i)
print("The sum of the factors is:",sum)
if(sum==num):
	print("The given number",num,"is a perfect number")
elif (sum>num):
	print("The given number",num,"is an abundant number")
else:
	print("The given number",num,"is a deficient number")