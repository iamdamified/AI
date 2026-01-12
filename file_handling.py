# # Read
with open("text_cleaner.py", "r") as file:
    content = file.read() # or file.readline(), file.readlines() for a list of lines
    print(content)

# # Write
with open("text_cleaner.py", "w") as file:
    file.write("# This is a new line added to the file.\n")
    file.write("print('Hello, World!')\n")
    file.writelines(["# Another line.\n", "print('Goodbye, World!')\n"])
    file.writelines(["Alice", "Bob", "Cherry"])


# # Append
with open("text_cleaner.py", "a") as file:
    file.write("# This line is appended to the file.\n")
    file.write("print('Appending new content!')\n")



# Note: Using 'with' automatically handles closing the file, even if exceptions occur.()
# 1. reduces risk of file corruption 2. simplifies code
# Always ensure to handle exceptions in production code for better reliability.
# File Handling in Python
# Modes: 'r' - read, 'w' - write, 'a' - append, 'b' - binary



""" Exception Handling in File Operations to prevent crashing"""

# Using "try-except" block to handle potential errors
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: The file was not found!")




# Exceptions Includes:# FileNotFoundError - when trying to read a non-existent file
# IOError - for general input/output errors
# PermissionError - when lacking permissions to access a file
