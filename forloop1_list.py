#Program to illustrate simple for loop
numbers = [1, 10, 20, 30, 40, 50]
sum = 0
#  Find sum of all the numbers using for loop 

for i in range(0,len(numbers)):
	sum=sum+numbers[i]
print ("The sum of numbers is", sum ) # print sum here


colors = ['red', 'orange', 'green', 'yellow', 'white', 'violet']
for j in (colors):
	print(j)
# Similarly ierate over the given colors and print the colors
