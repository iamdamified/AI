# Create a Text Cleaner
import re


def clean_text(text):
    # Remove Punctuation
    text = re.sub(r'[^\w\s]', '', text)
    # Remove Extra Whitespaces
    text = ' '.join(text.strip())
    # convert to lowercase
    return text.lower()
input_text = " Hello, World.!!! Welcome to Python, the programming language.   "
cleaned_text = clean_text(input_text)
print("Cleaned Text: ", cleaned_text)
# Output: Cleaned Text:  hello world welcome to python the programming language
"""This module provides a simple text cleaner function that removes punctuation, extra whitespaces, and converts text to lowercase using regular expressions."""