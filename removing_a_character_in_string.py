new_str=""
test_str=input("Enter string: ")
j=int(input("Enter integer value(index): "))
if j<0 or j>len(test_str):
    print("Index should be positive and less than the length of the string")
else:
    for i in range(0, len(test_str)):
        if i != j:
            new_str = new_str + test_str[i]
    print("String after removing",test_str[j],":",new_str)
