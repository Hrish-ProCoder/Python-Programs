# Creation of List
my_list = []
my_list = [1, 2, 3]
my_list = ["Hi", 6.2]

# nested list
my_list = ["mouse", [8, 4, 6], ['a']]

# Access List Elements
# List Indexing
my_list = ['y', 'e', 'l', 'l', 'o', 'w']
print(my_list[0]) 
print(my_list[2]) 
print(my_list[4]) 

# Nested List
n_list = ["Happy", [2, 0, 1, 5]]

# Nested indexing
print(n_list[1][3])

# Negative indexing in lists
my_list = ['y', 'e', 'l', 'l', 'o', 'w']
print(my_list[-1])
print(my_list[-5])
print(my_list[-3])

# List slicing in Python

my_list = ['e','n','c','y','c','l','o','p','e','d','i','a']
print(my_list[2:5])
print(my_list[:-5])
print(my_list[5:])
print(my_list[:])

# Add/Change List Elements
odd = [12, 14, 16, 18]
odd[0] = 1            
print(odd)
odd[1:4] = [13, 15, 17]  
print(odd)                   

# Append List
odd = [1, 3, 5]
odd.append(7)
print(odd)

# Extending lists
odd.extend([9, 11, 13])
print(odd)

# Concatenating List
odd = [1, 3, 5]
print(odd + [9, 7, 5])
# Repeting List
print(["Hello"] * 3)

# insert() method
odd = [1, 9]
odd.insert(1,3)
print(odd)

# Deleting list items
my_list = ['e','n','c','y','c','l','o','p','e','d','i','a']
del my_list[2]
print(my_list)
del my_list[1:5]
print(my_list)
del my_list

# Remove method
my_list = ['e','n','c','y','c','l','o','p','e','d','i','a']
my_list.remove('d')
# Output without d
print(my_list)

# Pop Method

print(my_list.pop(1))
print(my_list)
print(my_list.pop())
print(my_list)

# Clear whole list

my_list.clear()
print(my_list)

# Count methods
my_list = [3, 8, 1, 6, 0, 8, 4]
print(my_list.index(8))
print(my_list.count(8))

# Sort Method
my_list.sort()
print(my_list)

# Reverse Method
my_list.reverse()
print(my_list)

# List Comprehension
pow2 = [2 ** x for x in range(10)]
print(pow2)
# The above code is equivalent to 
pow2 = []
for x in range(10):
   pow2.append(2 ** x)
#More Example
pow2 = [2 ** x for x in range(10) if x > 5]
odd = [x for x in range(20) if x % 2 == 1]

# List Membership Test
my_list = ['y', 'e', 'l', 'l', 'o', 'w']
print('o' in my_list)
print('u' in my_list)
print('w' not in my_list)

# Iterating Through a List
for fruit in ['apple','banana','mango']:
    print("I like",fruit)
print('o' in my_list)
my_list.reverse()
print(fruit)
