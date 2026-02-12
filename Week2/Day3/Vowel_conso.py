# Program to count vowels and consonants

string = input("Enter a string: ").lower()

vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for char in string:
    if char.isalpha():   # Check if character is a letter
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)