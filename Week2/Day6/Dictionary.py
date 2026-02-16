# Dictionary Application

dictionary = {}

# Add word
def add_word():
    word = input("Enter word: ")
    meaning = input("Enter meaning: ")

    dictionary[word] = meaning
    print("Word added successfully.\n")


# Search word
def search_word():
    word = input("Enter word to search: ")

    if word in dictionary:
        print("Meaning:", dictionary[word], "\n")
    else:
        print("Word not found.\n")


# Update word
def update_word():
    word = input("Enter word to update: ")

    if word in dictionary:
        new_meaning = input("Enter new meaning: ")
        dictionary[word] = new_meaning
        print("Word updated successfully.\n")
    else:
        print("Word not found.\n")


# Delete word
def delete_word():
    word = input("Enter word to delete: ")

    if word in dictionary:
        del dictionary[word]
        print("Word deleted successfully.\n")
    else:
        print("Word not found.\n")


# Display dictionary
def display_dictionary():
    if not dictionary:
        print("Dictionary is empty.\n")
    else:
        print("\n--- Dictionary Contents ---")
        for word, meaning in dictionary.items():
            print(word, ":", meaning)
        print()


# Menu-driven system
while True:
    print("===== Dictionary Application =====")
    print("1. Add Word")
    print("2. Search Word")
    print("3. Update Word")
    print("4. Delete Word")
    print("5. Display All Words")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_word()
    elif choice == "2":
        search_word()
    elif choice == "3":
        update_word()
    elif choice == "4":
        delete_word()
    elif choice == "5":
        display_dictionary()
    elif choice == "6":
        print("Exiting program.")
        break
    else:
        print("Invalid choice.\n")