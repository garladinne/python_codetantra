def computeGCD(x, y): 
    if x > y: 
        small = y 
    else: 
        small = x 
    for i in range(1, small+1): 
        if((x % i == 0) and (y % i == 0)): 
        	gcd = i     
    return gcd 
a=int(input("Please enter an integer: "))
b=int(input("Please enter another integer: "))
a1=a
b1=b
if(a<0):
	a1=-a
if (b<0):
	b1=-b
if(a==0 or b==0):
	print("Numbers must be non zero")
else:
	gcd=computeGCD(a1,b1)
print("The GCD of %d and %d is %d" % (a,b,gcd))
