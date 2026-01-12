# check if a string is a palindrome
def is_palindrome(text):
    text = "".join(char.lower() for char in text if char.isalnum())
    return text == text[::-1]
input_text = input("Enter a string: ")
if is_palindrome(input_text):
    print(f'"{input_text}" is a palindrome.')
else:
    print(f'"{input_text}" is not a palindrome.')
"""This module checks if a given string is a palindrome, ignoring case and non-alphanumeric characters."""




# create program to find and replace all email address in a text using regex
import re
def replace_email_addresses(text, replacement="REDACTED"):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.sub(email_pattern, replacement, text)
input_text = "Please contact us at adekoyadamilareofficial@gmail.com for more information."
updated_text = replace_email_addresses(input_text)
print("Updated Text:", updated_text)
# Output: Updated Text: Please contact us at REDACTED for more information.
"""This module provides a function to find and replace all email addresses in a given text using regular expressions."""




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