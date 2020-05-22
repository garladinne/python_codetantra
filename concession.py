gen=input("Please enter M(male) or F(female): ")
age=int(input("Please enter Age: "))
if (gen=='M' and age>=65) or (gen=='F' and age>=60):
	print("Eligible for Concession")
else:
	print("Not Eligible for Concession")