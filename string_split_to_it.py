string=input("Enter three comma separated numbers: ")
m = 0
for i in string.split(','):
	if(m<int(i)):
		m=int(i)
print("Biggest number is",m)
