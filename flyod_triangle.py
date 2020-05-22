n = int(input("Enter the value of n: "))
rowIndex = 1
value = 1
while(rowIndex <= n):
	colIndex = 1
	while(colIndex <= rowIndex):
		print("%d " % value, end = '')
		value = value + 1
		colIndex = colIndex + 1
	rowIndex = rowIndex + 1
	print()
