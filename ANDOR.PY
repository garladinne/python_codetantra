x=int(input("Enter an integer value: "))
y=int(input("Enter an integer value: "))
x1=x
y1=y
x=x&y
#print(x1,"&",y,":",x)
print("{0} & {1}: {2}".format(x1,y,x))
x=x1
y=y1
x=x|y
print("{0} | {1}: {2}".format(x1,y,x))
