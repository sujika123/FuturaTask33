#  Write a Python program to calculate the sum of a list of numbers using recursion.

def sum_list(list,size):
   if (size == 0):
     return 0
   else:
     return list[size-1] + sum_list(list,size-1)

n = int(input("Enter the number of elements for list: "))
a = []
print("Enter the elements of list : ")
for i in range(0,n):
    # element = int(input("Enter element:"))
    # a.append(element)
    a.append(int(input()))
print("The list is:")
print(a)
print("Sum of items in list:")
b = sum_list(a,n)
print(b)
