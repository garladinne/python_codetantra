#Program to print value of pi 1 to 25 decimals
import math
pi = math.pi
dec=int(input("Please enter the no. of decimal places: "))
for i in range(1,dec+1):
	print("{:.{}f}".format(pi,i))