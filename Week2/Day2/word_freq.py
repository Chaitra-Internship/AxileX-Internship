# Program to count word frequency using dictionary

sentence = input("Enter a sentence: ")

# Convert sentence into words
words = sentence.split()

# Create empty dictionary
word_count = {}

# Count frequency
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("\nWord Frequency:")
for key, value in word_count.items():
    print(key, ":", value)