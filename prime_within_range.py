start=int(input("Enter lower limit: "))
end=int(input("Enter upper limit: "))
flag=0
print("Prime numbers between %d and %d are:" % (start, end))
for i in range(start,end):
        flag=0
       
        for j in range(2,i):
                if (i % j == 0):
                        flag=1
                        break
        if (flag==0):
                print(i)
		
		
		
		
		
