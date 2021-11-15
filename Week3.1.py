# while loops

x = 0
while x < 5:
    print("Not there yet, x=" + str(x))
    x = x + 1
print("x=" + str(x))


def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")
    
attempts(5)

# initializing variables matter!

def count_down(start_number):
  current = start_number  # initialized the variable to getasdfasdfas the code to work, or else we get a nameerror
  while (current > 0):
    print(current)
    current -= 1
  print("Zero!")

count_down(3)

# infinite loops and how to break them!

name_list = ['Charly', 'Robbie', 'Jocelyn', 'Ricky', 'Richie', 'Santi']
for name in name_list:
  print(name)
  if name == 'Richie':
    break
print('Found him! ^^^')

#QUIZ.3
def is_power_of_two(n):
  # Check if the number can be divided by two without a remainder
  while n % 2 == 0 and n != 0:
    n = n / 2
  # If after dividing by two the number is 1, it's a power of two
  if n == 1:
    return True
  return False
  

print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False

# QUIZ.4
def sum_divisors(n):
    return sum([i for i in range(1, n)
               if n % i == 0])
  # Return the sum of all divisors of n, not including n
    return sum

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114

# for loops: iterates over a sequence of values

for x in range(5):
  print(x)

def square(n):
    return n*n

def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += (n**2)
    return sum

print(sum_squares(10)) # Should be 285

product = 1
for n in range(1,10):
  product = product * n

print(product)

# For example, the factorial of four (4!) is equal to 1*2*3*4=24.

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result = result * i
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120

# coding dominoes combination


#basketball teams 

teams = ['Dragons', 'Wolves', 'Pands', 'Unicorns']

for home_team in teams:
  for away_team in teams:
    if home_team != away_team:
      print(home_team + " vs " + away_team)

# recursion

def factorial(n): # function
  if n < 2: # conditional defining BASE CASE
    return 1
  result =  n * factorial(n-1) # function calling itself | RECURSIVE CASE
  print("Returning " + str(result) + " for factorial of " + str(n))
  return result

print(factorial(3))

