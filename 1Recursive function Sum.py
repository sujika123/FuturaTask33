# Write a recursive function that will sum all numbers from 1 to n.

def sumSeries(n):
    if (n <= 1):
        return n
    else:
        return n + sumSeries(n-1)

n = int(input("Enter the the value of n : "))
if(n < 0):
    print("Please enter a positive number")
else:
    print(sumSeries(n))
