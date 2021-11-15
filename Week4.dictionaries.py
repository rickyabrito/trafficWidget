# Dictionaries: the data inside dictionaries take the form of pairs of keys and values
# Like in a real world example; the word in the dictionary would be THE KEY, and the definition of the word would be THE VALUE
# Use {} brackets

x = {}
print(type(x))

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
print(file_counts)

print(file_counts["txt"])
print("jpg" in file_counts)

file_counts["cfg"] = 8
print(file_counts)

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
for extension in file_counts: # Iterating through the dictionary
    print(extension)

for ext, amount in file_counts.items(): # Passing a TUPLE through the for loop (ext, amount)
    print("There are {} files with the .{} extension".format(amount, ext)) # Setting the output of the loop to go into the sentence, and formatting

print(file_counts.keys()) # Prints just the keys in the dict
print(file_counts.values()) # Prints just the values in the dict

def count_letter(text):
    result = {} # initialize an empty dictionary
    for letter in text: # loop through the text
        if letter not in result: #rules for what to do with the letters/value
            result[letter] = 0 # the word in [] becomes the whatever you chose to loop through the original argument, letter in text for this one
        result[letter] += 1    # and the value, becomes the number of times the letter is in the text
    return result

# Lists vs Dictionaries
# if you've got a list of info you'd like to collect and use in your script, then the list is probably the right approach
# BUT if you have a HOSTNAME along with the IP ADDRESSES, then you'd do a dict #

ip_addresses = ["192.168.1.1", "127.0.0.1", "8.8.8.8"]

host_addresses = {"Router": "192.168.1.1", "localhost":"127.0.0.1", "google":"8.8.8.8"}

print(ip_addresses)

# You want to use dictionaries when you plan on searching for a specific element

# in LISTS you can store any data types
# in DICTS you can store any data types in the values, but only the KEYS are restricted to specific type

wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for item in wardrobe:
	for color in wardrobe[item]:
		print("{} {}".format(color,item))

# Set
# Used when you want to store a bunch of elements and be certain that they're only present once

def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for group in group_dictionary:
		# Now go through the users in the group
		for users in group_dictionary[group]:
			user_groups[users] = user_groups.get(users,[]) + [group] # first half, uses 'users' as the key | second, uses .get(users,[blank for?]) + [group] to have the groups the user is linked with
			# Now add the group to the the list of
            # groups for this user, creating the entry
            # in the dictionary if necessary

	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"], "public":  ["admin", "userB"], "administrator": ["admin"] }))