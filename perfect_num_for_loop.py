num=int(input("please enter an integer: "))
list1=[1]
sum=1
for i in range(2,num):
	if (num % i == 0):
		list1.append(i)
		sum+=i
print("Factors of the given number %d are: %s" % (num, list1))
if (sum == num):
	print("%d is a perfect number" % num)
else:
	print("%d is not a perfect number" % num)
