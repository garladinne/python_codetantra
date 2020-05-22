str="12,24,36"
T1=str
print(str)
print(T1)
print("1"+"2")
#T1=["12","24","36"]
T3=[]
b=""
T3 = [[int(column) for column in row] for row in T1]
T3 = [list(map(int, x)) for x in T1]
for i in range(len(T3)):
    print(i)
print("Length of T1 is ",len(T1))
for i in range(0,len(T1)):
    #T3.append([])
    b=""
    for j in range(0,len(T1[i])):
        #print(T1[i][j],i,j)
        if (T1[i][j]!=","):
            b=b+(T1[i][j])
            print("b is in if block",b)
        else:
            print("b is in else block",b)
            T3.append(b)
            break
    #T3[i].append(b)

print(T3)
