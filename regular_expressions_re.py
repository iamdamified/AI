"""re module"""
import re

# re functions
"""1. re.search(pattern, string) using a particular pattern to search within a string and returns a match object if found.
2. re.findall(pattern, string) returns a list of all non-overlapping matches of the pattern in the string.(generally used to extract all occurrences of a pattern
3. re.sub(pattern, repl, string) replaces occurrences of the pattern in the string with a specified replacement string.
4. re.match(pattern, string) checks for a match only at the beginning of the string and returns a match object if found.
5. re.split(pattern, string) splits the string at each occurrence of the pattern and returns a list of substrings."""

# Example usage of re functions
text = "Contact me at 0816-8139-718"
digits = re.findall(r'\d+', text)
print("Extracted digits:", digits)
# updated_text = re.sub(r'0816-8139-718', 'REDACTED', text)
updated_text = re.sub(r'\d', 'X', text)
print("Updated text:", updated_text)
# Output:
# Extracted digits: ['0816', '8139', '718']
# Updated text: Contact me at XXXXXXXX-XXXX-XXX

match = re.match(r'Contact', text)
if match:
    print("Match found at the beginning:", match.group())
split_text = re.split(r'\s+', text)
print("Split text:", split_text)
if match:
    print("Match found at the beginning:", match.group())
# Output:
# Match found at the beginning: Contact
# Split text: ['Contact', 'me', 'at', '0816-8139-718']


search = re.search(r'0816', text)
if search:
    print("Search found:", search.group())
# Output:
# Search found: 0816
print("Regular Expressions module demonstration complete.")

"""This module demonstrates the usage of Python's re module for regular expressions. 
It includes examples of key functions such as re.search, re.findall, re.sub, re.match, and re.split 
to showcase their functionality in pattern matching, extraction, replacement, and splitting of strings."""