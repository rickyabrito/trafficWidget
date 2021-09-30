# valid user name needs at least 3 CHARACTERS
# branching:
# executing code by having it check conditions first and modifying the output/execution depending on those conditions

def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    else:
        print("Congrats on the name cuh")

hint_username("rickyabrito")

# got it ^

def is_even(number):
    if number % 2 == 0:
        return print("True!")
    return print("False!")

x = 6
y = 3
maths = x % y
is_even(maths)

# also got it ^

def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    elif len(username) > 15:
        print("Invalid username. Must be at most 15 characters long")
    else:
        print("Congrats on the name cuh")

hint_username("rickyabrito1234567890")

x = 6000//4096
z = 4097//4096
y = 1//4096
a = 4096//4096

print(y, a, z, x)

b = 4096%6000
c = 4096%4097
d = 4096%1
e = 4096%4096

print(d, e, c, b)

print("big" > "small")

print(11 % 5)

#Quiz question 6

def format_name(first_name, last_name):
	if len(first_name) > 0:
		string.("Name: ", first_name)
	elif len(last_name) > 0:
		string = Name: last_name
	elif len(first_name) == 0 and len(last_name) == 0:
		string = 
	
	return string 

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string