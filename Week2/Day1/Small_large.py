# Program to find smallest and largest number in a list

numbers = []

n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

print("List:", numbers)

print("Smallest number:", min(numbers))
print("Largest number:", max(numbers))