# String: data type that holds text

# prints out "Doggies Doggies Doggies "
"Doggies " * 3

# practice
def double_word(word):
    return((word*2) + str(len(word)*2))

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0

# Print characters from a string
name = "Jaylen"
print(name[1]) # Would print 'a' because Python counts from 0 and up
print(name[5]) # Would print 'n'

# Print negative index
text = "Vamos chuntis"
print(text[-1]) # Would print 's' because Python starts counting backwards from -1 since 0 would be the starting letter, 'V' in this case
print(text[-3]) # Would print 't'

# Want to give it a go yourself? Be my guest! Modify the first_and_last function so that it returns True if the first letter of the string is the same as the last letter of the string, False if they’re different. Remember that you can access characters using message[0] or message[-1].
# Be careful how you handle the empty string, which should return True since nothing is equal to nothing.
def first_and_last(message):
    if len(message) <= 1 or message[0] == message[-1]:
        return True
    if message[0] != message[-1]:
        return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))

# Slice: The portion of a string that can contain more than one character; also sometimes called a substring
color = "Orange"
color[1:4] # Would be 'ran'

fruit = 'Pineapple'
print(fruit[:4]) # Would take the first 4 characters of the string, 'Pine'
print(fruit[4:]) # Would take everything past index 4, 'apple'

# Strings in Python are immutable, can't be modified
message = "A kong string with a silly typo" # can't replace the 'k' with an 'l' because it is immutable
# Have to create a new string instead
new_message = message[0:2] + "l" + message[3:] # message[0:2] = 'A ' and message[3:] = 'ong string with silly typo'
print(new_message)

# Using a method to get the INDEX of a string
pets = "Cats & Dogs"
print(pets.index("&")) # Looks for "&", which is located at index 5, and prints out the index number
print(pets.index("s")) # Just prints out 3 because it looks for the first instance of what you're looking for, and stops there
print(pets.index("Dog")) # Prints out 7 because "D" in "Dog" is at index 7, and stops there

# Method: a function associated with a specific class

# To check if a specific "word" is in a string, we can use: in
"Dragons" in pets # Would return false because there is no "Dragons" in pets
"Cats" in pets # Would return true
# print(pets.index("x")) would err due to the char not being in pets string, that's why we would use "x" in pets instead

# function to replace old domain email addresses and update with the new domain
def replace_domain(email, old_domain, new_domain): # defined the replace_domain function with 3 arguments, email to be checked, old domain, and new domain
                                                   # Having these parameters in a function instead of directly in the code, makes it REUSABLE
    if "@" + old_domain in email:                   # This checks to see if "@" and the old domain are in the email address to be checked
        index = email.index("@" + old_domain)       # If old_domain found, we use index to find where the old_domain including @, starts
        new_email = email[:index] + "@" + new_domain # Using the index, we create a new email. email[:index] = is writing the email UP TO INDEX, + "@" +, new_domain = is writing the new domain at the end of the mail
        return new_email # Finally, we return the new_email with the new domain written on it
    return email # If the original email did not contain the old_domain, we return the original email


# String transformations
# .upper()
# .lower()

"Mountains".upper() # "MOUNTAINS"
"Mountains".lower() # "mountains"
" Mountains ".strip() #Removes whitespace "Mountains"
# .lstrip() would remove the left whitespace, while .rstrip() would remove the right whitespace

# when handling user input, transformations could be helpful
user_input = "Yes"
if user_input.lower() == "yes":
    print("User said 'Yes'")

answer = " Yes "
if answer.strip() == "Yes": 
    print("User said 'Yes'")

# .count() counts how many times the speficied character appears in the string
"The number of times e occurs in this string is 4".count("e") # Should print 4

# .endswith() searches to see if the string ends with the substring provided
"Forest".endswith("rest") #True!

# .isnumeric() checks to see if string is numeric
"12345".isnumeric() # True

# .join() concatenates strings together
" ".join(["This", "is", "the", "beef"]) # 'This is the beef'

# .split() splits the string into smaller strings
"This is another example".split() # ['This', 'is', 'another', 'example']

# Turning long names into acronyms
def initials(phrase):
    words = phrase.split() # This would split the string into substrings
    result = ""
    for word in words:
        result += word[0].upper() # Grabs the first index of every word, turns it cap, adds to Result
    return result

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS

# .format method
name = "Richie"
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name, number)) # .format() takes the variables, and inserts them into the {} placeholders, and deals with data types as well
print("Your lucky number is {number}, {name}.".format(name=name, number=len(name)*3)) # Having the placeholders labeled, means you have to link them to the variables in the .format() method

# using a formatting expression
price = 7.5
with_tax = price * 1.09
print(price,with_tax)
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price,with_tax)) 
# Expression starts with a : to separate it from the field name that we saw before "7.5",
# after we write ".2f", which signals that we're gonna have a float number and that it its gonna have
# 2 digits after the decimal dot, so no matter the function, it'll always print two decimals

def to_celsius(x):
    return (x-32)*5/9

for x in range(0,101,10):
    print(x, to_celsius(x))
for x in range(0,101,10):
    print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))
# '>' to align text to the right
# '>3' align to the right for a total of 3 spaces "__0", "_10", "100"
# '>6.2' align to the right 6 spaces and two decimal places

# Quiz
# 1
def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = ""
	# Traverse through each letter of the input string
	for letter in input_string:
		# Add any non-blank letters to the 
		# end of one string, and to the front
		# of the other string. 
		new_string = new_string + letter.replace(" ","")
		reverse_string  = letter.replace(" ","") + reverse_string
	# Compare the strings
	if new_string == reverse_string:
		return True
	return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True

weather = "Rainfall"
print(weather[:4])

list2 = ['cat', 'bat', 'mat', 'cat', 
         'get', 'cat', 'sat', 'pet']
  
# Will print index of 'cat' in sublist
# having index from 2 to 6
print(list2.index('cat', 2, 6 ))

def replace_ending(sentence, old, new):
	# Check if the old string is at the end of the sentence 
	if sentence.endswith(old) == True:
		# Using i as the slicing index, combine the part
		# of the sentence up to the matched string at the 
		# end with the new string
		i = len(old) # counts the how long the "old" is | "cats" = 4 characters
		new_sentence = sentence[:-i] + new # sentence BACKWARDS from -i | backwards 4 if "cats"
		return new_sentence

	# Return the original sentence if there is no match 
	return sentence
	
print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"

