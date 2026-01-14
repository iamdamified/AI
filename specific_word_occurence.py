""" Program that counts nnumber of occurencies of a specific word in a text file """
def count_word_in_file(filename, word):
    """Count occurrences of a specific word in a file."""
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            word_count = contents.lower().split().count(word.lower())
            print(f"The word '{word}' occurs {word_count} times in the file {filename}.")
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
count_word_in_file('fruits.txt', 'apple')# The word 'apple' occurs 1 times in the file fruits.txt.
# The word 'apple' occurs 1 times in the file fruits.txt.