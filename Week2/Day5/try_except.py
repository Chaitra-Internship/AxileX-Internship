# Program to demonstrate try-except

try:
    num = int(input("Enter a number: "))
    print("You entered:", num)

except ValueError:
    print("Invalid input! Please enter a number.")

else:
    print("No errors occurred.")

finally:
    print("Execution completed.")