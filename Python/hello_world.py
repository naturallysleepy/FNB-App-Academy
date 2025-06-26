print("Hello World! (This is a coding rite of passage)")

# This is a comment, they help explain the code
# Comments are ignored by the Python interpreter, but they keep it readable, remember to use them frequently! 
# Seriously, use them a lot. 

# Python Basics

# Strings:

#Strings are sequences of characters, they can be enclosed in single (') or double quotes (")
message = "Hello, World!"  # This is a string variable

print(message)  # This prints the message in the console

# This is a multi-line string, it can be enclosed in triple quotes
message = """  This is a multi-line string!

You can use it to write longer messages, and format them.

You can also use it to write comments that span multiple lines, but this is not a comment.

You can make one using triple quotes.

""" # By the way, = is the assignment operator, message was reassigned to a new value, == is the equality operator, which will be covered later

# String operations:
print(message) # This prints the message in the console

# Print the message without leading and trailing whitespace
print(message.strip())

# Print the message in lowercase
print(message.lower())

# Print the message in uppercase
print(message.upper())

# Print the message with the first letter of each word capitalized
print(message.title())

str1 = "Hello"
str2 = "World"

# Concatenate two strings
print(str1 + " " + str2)

# Repeat a string multiple times
print(str1 * 3 + "!")

# String formatting using f-strings
name = "Alice"

# Add name to string
print(f"Hello, {name}! Welcome to Python.")

# ints and floats:

int_num = 42  # Integer
float_num = 3.14  # Float

# Arithmetic operations:
print(int_num + float_num)  # Addition
print(int_num - float_num)  # Subtraction
print(int_num * float_num)  # Multiplication
print(int_num / float_num)  # Division
print(int_num // 2)  # Floor division
print(int_num % 5)  # Modulus
print(int_num ** 2)  # Exponentiation

int_num += 1  # Increment the integer by 1
print(int_num)  # Now int_num is 43

"int_num++"  # This is not valid in Python, use int += 1 instead

# Booleans and conditionals:
# Booleans represent truth values: True or False
bool1 = True  
bool2 = False  

# Conditional statements
if bool1:
    print("bool1 is True!")
elif bool2:
    print("bool2 is True!")
else:
    print("Both are False!")

# Conditional statements with comparison operators
int_num = 0

if int_num > 0:
    print("int is positive")
elif int_num < 0:
    print("int is negative")
else:
    print("int is zero")
    
# Lists, tuples, and sets

# Lists are ordered collections that can contain duplicate elements, lists are mutable
my_list = [1, 2, 3, 4, 5] # Lists are made with square brackets []

# Add an element to the end of the list
my_list.append(3)  
print(my_list)

# Remove an element from the list
my_list.remove(3)
  
print(my_list) # Only the first instance is removed

# Insert an element at a specific index
my_list.insert(2, 10)  # Insert 10 at index 2
print(my_list)

# Sort the list in descending order
my_list.sort(reverse=True)
print(my_list)

# Access elements in the list by index
my_list[0] = 10  # Elements are always zero-indexed
my_list[-1] = 20  # Last element of the list has index -1
print(my_list)

# Tuples are ordered collections that can contain duplicate elements, tuples are immutable
my_tuple = ("apple", "banana", "cherry", "apple") # Tuples are made with parentheses ()
new_tuple = my_tuple + ("orange",)  # Concatenate tuples
print(new_tuple)

# Tuples can be repeated
rep_tuple = my_tuple * 2  # Repeat the tuple
print(rep_tuple)

# Access elements in the tuple by index
print(new_tuple[3]) # Access the fourth element of the tuple

# Sets are unordered collections that do not allow duplicate elements, sets are mutable
my_set = {1, 2, 3, 4, 5} # Sets are made with curly braces/brackets {}

# Add an element to the set
my_set.add(6)
print(my_set)

# Sets automatically remove duplicates, so adding an existing element has no effect
my_set.add(3)
print(my_set)  # 3 is not added again

# Remove an element from the set
my_set.remove(2)
print(my_set)

new_set = {6, 7, 8}
# Union of two sets
union_set = my_set.union(new_set)
print(union_set)

# Intersection of two sets
inter_set = my_set.intersection(new_set) # This will find common elements in both sets 
print(inter_set)

# Difference of two sets
diff_set = my_set.difference(new_set) # This will find elements in my_set that are not in new_set
print(diff_set)

# Dictionaries:

# Dictionaries are collections of key-value pairs, they are mutable and unordered
my_dict = {'apple': 1, 'banana': 2, 'cherry': 3}  # Dictionaries are made with curly braces/brackets {}
print(my_dict["apple"])  # Access value by key

# Add a new key-value pair to the dictionary
my_dict["orange"] = 4
print(my_dict)

# Remove a key-value pair from the dictionary
del my_dict["banana"] 
print(my_dict)

# Modify an existing key-value pair
my_dict["cherry"] = 5

# Print all keys in the dictionary
print(my_dict.keys())

# Print all values in the dictionary
print(my_dict.values())


# Loops

# for loops are used to iterate over a sequence (like a list, tuple, or string)

for i in range(5):
    # Print each number in the range
    print(i)
    
# Identical for any variable name
for k in range(5):
    # Print each number in the range
    print(k)
    
# Can iterate over lists, sets, tuples, or dictionaries
for fruit in my_dict:
    # Print each key in the dictionary
    print(fruit)

# while loops are used to repeat a block of code as long as a condition is true
count = 0
while count < 5:
    print(count)
    count += 1  # Increment the count by 1
    # This will print numbers from 0 to 4, but not 5
# Note that this is the same as the for loop above, but it uses a while loop instead, for loops are generally preferred for iterating over a sequence

# do-while loops are not supported in Python :(
    
# break, continue and pass statements:
# break statement is used to exit a loop prematurely
for element in new_tuple:
    if element == "orange": 
        print("Found orange!") 
        break  # If the element is "orange", break the loop
    print(f"This is not orange, this is {element}")
    
# continue statement is used to skip the current iteration and continue with the next one
for item in my_list:
    if item > 7:
        print(item)
        continue  # If the item is bigger than 7, skip this iteration
    item = 0
    print(item)
    
for item in my_set:
    if item > 3 and item < 6:
        pass  # This does nothing, but it is a valid statement, it is used as a placeholder
    item += 1
    print(item)

# Functions:

#Functions are reusable blocks of code that perform a specific task, they can take parameters and return values
def greet(name):
    """This function greets the person with the given name."""
    print(f"Hello, {name}!")

greet("Alice")  # Call the function with the argument "Alice"

def triangle_area(base, height):
    """This function calculates the area of a triangle given its base and height."""
    return 0.5 * base * height  

# Oh by the way, you can also use input() to get user input, but it returns a string, so you need to convert it to the appropriate type 
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

area = triangle_area(base, height)  # Call the function with the user input and print the result
print(f"The area is: {area}")  

print("This is the end of the Python basics tutorial. Congratulations on completing it!")