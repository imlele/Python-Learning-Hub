# Thank you for coming! Here are notes for first lesson:

# Terminal:
# Win + "cmd" -> open terminal
# cd <path>   -> change directory in terminal, to <path>

# PRINTING:

print("Hello world")

# VARIABLE ASSIGNMENT

# Python is dynamically typed, so we don't specify
# the variable type (unlike Java or C/C++)

x = 5
y = 2.5
z = True
name = "Bob"
name2 = 'Alice'
# In python, single and double quotes don't matter
# Use whichever one you prefer
# Try to stick to one or another, avoid using both in same program

# Asking user for input
name = input("Enter name: ")

# Checking type of value
print(type(name)) # <class 'str'>
print(type(x))    # <class 'int'>
print(type(z))    # <class 'bool'>

# TYPE CONVERSION:
age_string = "20"
print(age_string)
# '20'

age_number = int(age_string)
print(age_number)
# 20

# MATH OPERATIONS
a = 3
b = 5
print(a + b) # 8
print(a - b) # -2
print(a * b) #15
print(10 + a * b) # Multiplication before addition!
# first a * b, then + 10 = 25

# will print float
print(10 / 5) # 2.0

# will print integer
print(10 // 5) # 2

print("10" - 2) # ERROR! can't subtract int from string!

# LOGIC
age = 20
print(age > 15) # True
print(age >= 20) # True
print(age > 20) # False
print(age > 35) # False
print(age < 100) # True
print(age == 20) # True

# CONDITIONS
# note: indentations are 4 spaces, NOT "TAB"
# Python uses indentations instead of curly brackets
# to track blocks of code
age = 20
if age >= 18:
    print("you are at least 18!")
elif age >= 16:
    print("You are not 18 yet")
    print("But you can now drive!")
else:
    print("You are too young to drive")
print("this will be printed at the end regardless of age")

# LISTS

lst = [1,2,4, 7, 9, 11, 14]

# Lists are zero-indexed (the first element in list is element number 0)
print(lst[0]) # 1
print(lst[2]) # 4
print(lst[99]) # ERROR!

# Sublists:

# lst[a:b], from a, up to (not including) b
print(lst[0:4]) # [1, 2, 4, 7]
print(lst[:4]) # if you leave it empty, it will start at the beginning
print(lst[2:5]) # [4, 7, 9]


print(lst[3:]) # [7, 9, 11, 14]
print(type(lst)) # <class 'list'>

lst[2] = 100
print(lst) # [1, 2, 100, 7, 9, 11, 14]

lst[1:3] = [100, 101]
print(lst) # [1, 100, 101, 7, 9, 11, 14] 

lst.append(-123)
print(lst) # [1, 100, 101, 7, 9, 11, 14, -123] 

# removes and returns element number 2 (101)
lst.pop(2) # 101

print(lst) # [1, 100, 7, 9, 11, 14, -123]

# You can have a list of different types if you want
lst2 = [1, 2.5, "test", True]

# SETS

# similar to list, but no order and no duplicaties
a = {5, 1, 1, 3}
print(a) # {1, 3, 5}
print(type(a)) # <class 'set'>

print(list(a)) # [1, 3, 5]

print(a[0]) # ERROR!

print(1 in a) # True
print(2 in a) # False

# You can also check if an element is in a list the same way
# But lists become slow when they are very large
# Sets do many things MUCH faster, even with >1000000 elements

print(len(a)) # 3

a = {1,2,3}
b = {3,4}
print(a.union(b)) # {1,2,3,4}
print(a.intersection(b)) # {3}

# DICTIONARY

# Analogous of Hashmap or dict in other languages
ages = {
    "Bob": 20,
    "Alice": 25,
    "Jim": 30
}

print(ages["Bob"]) # 20
print(type(ages)) # <class 'dict'>

# TUPLES

# Similar to lists but immutable!
# Often used for grouping multiple values together

jim = ("Jim", 25)
alice = ("Alice", 30)

print(jim[0]) # "jim"
print(jim[1]) # 25

jim[0] = "Bob" # ERROR!

# FOR LOOP

# in Python, a for loop is a "for-each" loop.
# it repeats code, for every element in a collection

lst = [1,3,5]
for n in lst:
    print(n)
# 1
# 3
# 5

# RANGE

# range is a special function which takes numbers a, b
# and returns a list (kind of) from [a, a+1, a+2, ... ..b-1]

for i in range(2, 10):
    print(i)

# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9


