# Program to generate multiplication table

num = int(input("Enter a number: "))

print("Multiplication Table of", num)
print("---------------------------")

for i in range(1, 11):
    print(num, "x", i, "=", num * i)