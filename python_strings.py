"""Working with Strings in Python"""

# Split() - This method separates words in a sentence into a list.
sentence = "Hello, welcome to the world of Python programming."
words = sentence.split(" ")
print(words)
# Output: ['Hello,', 'welcome', 'to', 'the', 'world', 'of', 'Python', 'programming.']


# Join() - This method combines a list of words or elements of list into a single string.
new_sentence = " ".join(words)
print(new_sentence)
# Output: Hello, welcome to the world of Python programming.

# Replace() - This method replaces a specified phrase with another specified phrase.
modified_sentence = sentence.replace("Python", "Java")
print(modified_sentence)
# Output: Hello, welcome to the world of Java programming.

# Upper() - This method converts all characters in a string to uppercase.
upper_case_sentence = sentence.upper()
print(upper_case_sentence)
# Output: HELLO, WELCOME TO THE WORLD OF PYTHON PROGRAMMING.

# Lower() - This method converts all characters in a string to lowercase.
lower_case_sentence = sentence.lower()
print(lower_case_sentence)
# Output: hello, welcome to the world of python programming.

# Find() - This method searches for a specified substring and returns the index of its first occurrence.
index = sentence.find("world")
print(index)
# Output: 18
# If the substring is not found, it returns -1.

# Count() - This method counts how many times a specified substring appears in the string.
count = sentence.count("o")
print(count)
# Output: 4
# It counts both uppercase and lowercase occurrences.

# Strip() - This method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove).
text_with_spaces = "   Hello, Python!   "
stripped_text = text_with_spaces.strip()
print(stripped_text)
# Output: Hello, Python!
# You can also specify characters to remove.
custom_stripped_text = "xxxyHello, Python!yyxx".strip("xy")
print(custom_stripped_text)
# Output: Hello, Python!

# Format() - This method formats specified values in a string.
name = "Alice"
age = 30
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)
# Output: My name is Alice and I am 30 years old.


# You can also use positional or keyword arguments.
positional_string = "My name is {0} and I am {1} years old.".format(name, age)
print(positional_string)
# Output: My name is Alice and I am 30 years old.


keyword_string = "My name is {name} and I am {age} years old.".format(name=name, age=age)
print(keyword_string)
# Output: My name is Alice and I am 30 years old.


# F-Strings (Python 3.6+) - This is another way to format strings using expressions inside string literals.
f_string = f"My name is {name} and I am {age} years old."
print(f_string)
# Output: My name is Alice and I am 30 years old.


# Escape Characters - These are special characters used to represent certain whitespace or formatting in strings.
escaped_string = "Hello,\nWelcome to the world of Python!\tEnjoy coding."
print(escaped_string)
# Output: Hello,
#         Welcome to the world of Python!    Enjoy coding.
# Here, \n represents a new line and \t represents a tab space.


# Raw Strings - These are strings prefixed with 'r' or 'R' that treat backslashes as literal characters.
raw_string = r"C:\Users\Name\Documents\file.txt"
print(raw_string)
# Output: C:\Users\Name\Documents\file.txt
# Here, the backslashes are not treated as escape characters.


# String Slicing - This allows you to extract a portion of a string using indexing.
sample_string = "Hello, Python!"
sliced_string = sample_string[7:13]
print(sliced_string)
# Output: Python


# You can also use negative indexing.
negative_sliced_string = sample_string[-7:-1]
print(negative_sliced_string)
# Output: Python


# String Concatenation - This is the process of joining two or more strings together using the + operator.
string1 = "Hello"
string2 = "World"
concatenated_string = string1 + ", " + string2 + "!"
print(concatenated_string)
# Output: Hello, World!