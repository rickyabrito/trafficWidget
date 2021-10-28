# Lists
x = ["Now", "we", "are", "cooking!"]
print(type(x))
print(len(x)) # How many indices are in x

print("are" in x)

# Modding lists
fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.append("Kiwi")
print(fruits)

fruits.insert(0, "Orange")
print(fruits)

fruits.remove("Melon") # Removes the first instance of in the list
print(fruits)

print(fruits.pop(3)) # Returns the element that was removed
print(fruits)

fruits[2] = "Strawberry" # moddifies the indicated index
print(fruits)

def skip_elements(elements):
	# Initialize variables
	new_list = []
	i = 0

	# Iterate through the list
	for index,element in enumerate(elements):
		# Does this element belong in the resulting list?
		if index%2==0:
			# Add this element to the resulting list
			new_list.append(elements[index])
		# Increment i
	

	return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []

# Tuples: sequences of elements of any type, that are immutable
fullname = ('Grace', 'M', 'Hopper')

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

result = convert_seconds(5000)
print(type(result)) # class 'tuple'

# iterating over lists and tuples
animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals:
    chars += len(animals)
print("Total characters: {}, Average length: {}".format(chars, chars/len(animals)))

winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners): # Index becomes the first value in the Tuple, and person becomes the second value 
    print("{} - {}".format(index + 1, person))

def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}".format(name, email))
    return result

print(full_emails([("alex@example.com", "Alex Diego"),
("shay@example.com", "Shay Brandt")]))

# List comprehensions
multiples = []
for x in range (1, 11):
    multiples.append(x*7)

print(multiples) # [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]

multiples = [ x * 7 for x in range(1, 11)] # Same result

languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
lengths = [len(language) for language in languages]
print(lengths)

z = [x for x in range(0,101) if x % 3 == 0] # find numbers divisible by 3 up to 100
print(z)