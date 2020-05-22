
str1=input("Enter First String: ")
str2=input("Enter Second String: ")
if len(str1)<=1 or len(str2)<=1:
	print("Concatenation of two Strings excepting first characters is NULL string")
else:
	print("Concatenation of two Strings excepting first chars:",str1[1:]+str2[1:])
