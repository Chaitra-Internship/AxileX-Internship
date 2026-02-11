# Program to sort a list in ascending and descending order

numbers = []

n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

print("Original List:", numbers)

# Ascending order
numbers.sort()
print("Ascending Order:", numbers)

# Descending order
numbers.sort(reverse=True)
print("Descending Order:", numbers)