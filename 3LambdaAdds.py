# Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
# also create a lambda function that multiplies argument x with argument y and prints the result.


# Lambda function to add 15 to a given number
add_15 = lambda x: x + 15

# Lambda function to multiply two numbers
multiply = lambda x, y: x * y


result_add = add_15(10)
print("10 + 15 = ",result_add)

result_multiply = multiply(5, 3)
print("5 * 3 = ",result_multiply)
