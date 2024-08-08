# Generating odd number with their cube values with using dictionary comprehension
# dictdemo = [1, 2, 3, 4, 5, 6, 7].


# Original list
dictdemo = [1, 2, 3, 4, 5, 6, 7]

# Dictionary comprehension to generate odd numbers with their cube values
odd_cubes = {x: x**3 for x in dictdemo if x % 2 != 0}

# Print the result
print(odd_cubes)
