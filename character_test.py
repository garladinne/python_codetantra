ch=input("Enter a character: ")
if ((ord(ch)>=65 and ord(ch)<=92) or (ord(ch)>=97 and ord(ch)<=122)):
	if (ch in ['a','A','e','E','i','I',"o","O",'u',"U" ]):
		print("The given character %s is a letter and a vowel" % ch)
	else:
		print("The given character %s is a letter and a consonant" % ch)
else:
	print("The given character %s is not a letter" % ch)
