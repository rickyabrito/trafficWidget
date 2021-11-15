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
	if len(first_name) > 0 or len(last_name) > 0:
		string = ("Name: ", first_name, "", last_name)
	else:
		string = ""
	
	return string 

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string



def fractional_part(numerator, denominator):
	if denominator > 0:
		return((numerator % denominator)/denominator)
	else:
	# Operate with numerator and denominator to 
# keep just the fractional part of the quotient
		return("0")

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0

# one of the issues was that i had print((numerator......)), so it spat out the answer and then "none" right after it for every input
# also, the only number that couldn't be 0 was the denominator
# so i just had to write a condition for that