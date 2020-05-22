while(1):
	ch=input("Enter a vowel, or 9 to quit: ")
	if ((ord(ch)>=65 and ord(ch)<=92) or (ord(ch)>=97 and ord(ch)<=122)):
		#if (ch=='a' or 'A' or 'e' or 'E' or 'i' or 'I' or 'u' or 'U'):
		if (ch in ['a','A','e','E','i','I',"o","O",'u',"U" ]):
			print("That is a vowel")
		else:
			print("That is not a vowel")
	elif (ch=='9'):
		break
	else:
		print("Wrong input")