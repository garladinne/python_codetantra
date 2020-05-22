import math
num = float(input("Please enter Float Number: "))
#print(num-int(num))
if (num - int(num) >=.5):
	print (num, "is roundedup to:", math.ceil(num))
else:
	print(num, "is truncated to:", math.trunc(num))
