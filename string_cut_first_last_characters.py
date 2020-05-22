st=input("Enter a string: ")
l=len(st)
#if(l<3):
#	print("The string is:",st)
#else:
#	print("The first & last two characters of the string:",st[0]+st[1]+st[-2]+st[-1])
print("String after removing first and last characters:",st[1:(l-1):1])
