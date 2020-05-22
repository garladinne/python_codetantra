S=input("Enter String: ")
open_bracket=closed_bracket=0
n = len(S) 
for i in range(n): 
	if S[i] == '(':
		open_bracket += 1
	elif S[i] == ')':
		closed_bracket+=1
if (open_bracket>closed_bracket):
	diff=open_bracket-closed_bracket
elif (open_bracket<closed_bracket):
	diff=closed_bracket-open_bracket
else:
	diff=0
if(diff == 0):
   print("%s is a valid expression and depth is: %d" % (S,open_bracket))
else:
   print("%s is not a valid expression and there are %d errors" % (S,diff))