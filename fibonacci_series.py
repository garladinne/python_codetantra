n=int(input("Enter the maximum limit to generate the fibonacci series: "))
i=0
j=1
print("The fibonacci series is")
print(i)
if (n==0):
	pass
else:
	print(j)
s=0
while(s<n):
	if(n==0):
		break
	
	s=i+j
	if (s>n):
		break
	print(s)
	i=j
	j=s
