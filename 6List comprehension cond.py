#Using list comprehension, construct a list from the squares of each element in the list.


# Original list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List comprehension to create a list of squares greater than 50
squares = [x**2 for x in numbers if x**2 > 50]

# Print the result
print(squares)
