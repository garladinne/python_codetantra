# Deductions
Ded_std = 150000
# Request Inputs
Ded_80c = int(input("Enter Amount to be deducted under 80c: "))
Ded_80cc = int(input("Enter Amount to be deducted under 80cc: "))
Ded_hra = int(input("Enter Amount to be deducted under HRA: "))
Ded_med = int(input("Enter Amount to be deducted under Medical: "))
Gross_Income = int(input("Enter Gross Income: "))
Ded_tot = (Ded_std + Ded_80c + Ded_80cc + Ded_hra + Ded_med)
Tax_Income = Gross_Income - Ded_tot
if (Tax_Income > 0):
	if (Gross_Income <= 500000):
		Income_Tax = (Tax_Income * .1)
	if (Gross_Income <= 1000000) and (Gross_Income > 500000):
		Income_Tax = 25000 + ((Gross_Income - 500000)*.2)
	if (Gross_Income > 1000000):
		Income_Tax = 75000 + ((Gross_Income - 1000000) *.3)
	print("Gross Income is" , Gross_Income)
	print("Total Deductions =" , Ded_tot)
	print("Income Tax =" , Income_Tax)
#else :
#	print("Hurray..No Income Tax")
# complete the missing code
#print ("Gross Income is" , Gross_Income)
#print ("Total Deductions =" , Ded_tot)
#print ("Income Tax =" , Income_Tax)
else :
	print ("Hurray..No Income Tax")
