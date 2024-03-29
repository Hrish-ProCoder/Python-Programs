# CREATION of TUPLE

# Different types of tuples

# Empty tuple
my_tuple = ()
print(my_tuple)

# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

my_tuple = 3, 4.6, "lion"
print(my_tuple)

# Represent Tuple
a, b, c = my_tuple

print(a)       
print(b)       
print(c)       

my_tuple = ("hello")
print(type(my_tuple))  # <class 'str'>

# Creating a tuple having one element
my_tuple = ("hello",)
print(type(my_tuple))  # <class 'tuple'>

# Parentheses is optional
my_tuple = "hello",
print(type(my_tuple))  # <class 'tuple'>




#ACCESSING TUPLES

1. Indexing

# Accessing tuple elements using indexing
my_tuple = ('p','e','r','m','i','t')

print(my_tuple[1]) 
print(my_tuple[4]) 

# IndexError: list index out of range
# print(my_tuple[6])

# nested tuple
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

# nested index
print(n_tuple[0][2])       # for 'u'
print(n_tuple[2][2])       # 3

2. Negative Indexing

my_tuple = ('p', 'e', 'r', 'm', 'i', 't')

print(my_tuple[-2])
print(my_tuple[-4])

2. Slicing

my_tuple = ('y', 'e', 'l', 'l', 'o', 'w')

print(my_tuple[1:4])
print(my_tuple[:-7])
print(my_tuple[7:])
print(my_tuple[:])

# Changing tuple values

my_tuple = (4, 2, 3, [6, 5])
my_tuple[3][0] = 9
print(my_tuple)
#Output: (4, 2, 3, [9, 5])

# Concatenations
print((1, 2, 3) + (4, 5, 6))

# Repeat
# Output: ('Repeat', 'Repeat', 'Repeat')
print(("Repeat",) * 3)

# Deleting tuples
my_tuple = ('y', 'e', 'l', 'l', 'o', 'w')

del my_tuple
print(my_tuple)

#Tuple Methods

my_tuple = ('y', 'e', 'l', 'l', 'o', 'w',)

print(my_tuple.count('l'))
print(my_tuple.index('o'))

# In and Not in Keywords
print('w' in my_tuple)

print('b' not in my_tuple)

#Iterating Through a Tuple using for loop

for name in ('Ram', 'Sham'):
    print("Hello", name)
