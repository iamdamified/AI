# Word Frequency Counter

sentence = input("Enter a sentence: ")
# sentence " Hello, world! Welcome to Python programming. Hello again."

# Splitting sentence into words accurately
words = sentence.split()
# Creating an empty dictionary to hold word counts
word_count = {}
# Counting occurrences of each word, and add existing words count when repeated
for word in words:
    word = word.lower()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
# Displaying the word counts
print("Word Frequency Count:", word_count)
# for word, count in word_count.items():
#     print(f"{word}: {count}")