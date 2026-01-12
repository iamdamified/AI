# create program that reverse the words in a sentence(not letters)
def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence
input_sentence = "Hello World! Welcome to Python programming."
reversed_sentence = reverse_words(input_sentence)
print("Reversed Sentence:", reversed_sentence)
# Output: Reversed Sentence: programming. Python to Welcome World! Hello
"""This module reverses the order of words in a given sentence while keeping the letters in each word intact."""