# Program to handle file errors

try:
    file = open("sample.txt", "r")
    content = file.read()
    print("File Content:")
    print(content)
    file.close()

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: You don't have permission to access this file.")

except Exception as e:
    print("An unexpected error occurred:", e)

finally:
    print("File operation completed.")