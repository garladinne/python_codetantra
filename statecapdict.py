st2cap = dict()
state = input("Enter the state or 'end' to quit: ")
while(state!="end"):
	capital=input("Enter the capital: ")
	d1={state:capital}
	st2cap.update(d1)
	state=input("Enter the state: ")
# write your logic using while loop

# take inputs capital anad state from the user and store it in a dictionary till the user enters state as end

print(sorted(st2cap.items()))
