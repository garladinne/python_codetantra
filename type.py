# Type Conversion Example
a = '0111110'
b=int(a,2)
#print(b)
c=float(b)
d=complex(b)
print("Value after converting to int =",b,"and data type of value =",type(b))
print("Value after converting to float =",c,"and data type of value =",type(c))
print("Value after converting to complex =",d,"and data type of value =",type(d))
