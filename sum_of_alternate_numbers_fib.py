n=int(input("Please enter a number: "))
i=0
j=1
myList=[0,1]
print(i)
print(j)
sum=0
while((i+j)<n):
	next=i+j
	myList.append(next)
	print(next)
	i=j
	j=next
#print(myList)
k=0
#print(len(myList))
while k<len(myList):
	sum=sum+int(myList[k])
	k+=2
print("Sum = %d" % sum)
