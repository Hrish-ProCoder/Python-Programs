fruits = ["apple", "banana", "cherry"]
cars = ['Ford', 'BMW', 'Volvo']

fruits.append("orange")
print(fruits)

fruits.clear()
print(fruits)

x = fruits.copy()
print(x)

x = fruits.count("cherry")
print(x)

x = fruits.index("cherry")
print(x)

fruits.insert(1, "orange")
print(fruits)

fruits.pop(1)
print(fruits)

fruits.remove("banana")
print(fruits)

fruits.reverse()
print(fruits)

cars.sort()
print(cars)
cars.sort(reverse=True)

del cars[1]
print(cars)

fruits.extend(cars)
print(fruits)

print("cherry" in fruits)
