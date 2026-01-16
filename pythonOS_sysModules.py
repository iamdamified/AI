# OS MODULE - functions to interact with the operating system
import os
print("Current Working Directory:", os.getcwd())
# Current Working Directory: /path/to/current/directory




# List files and directories in the current directory
print("Files and Directories in '", os.getcwd(), "':", os.listdir('.'))
# Files and Directories in ' /path/to/current/directory ': ['file1.txt', 'file2.py', 'dir1', ...]



# Create a new directory
os.mkdir('new_folder')
print("New directory 'new_folder' created.")

#or
new_dir = 'test_directory'
if not os.path.exists(new_dir):
    os.mkdir(new_dir)
    print(f"Directory '{new_dir}' created.")


# Remove the created directory or file
os.remove('new_folder')
print("Directory 'new_folder' removed.")

#or
os.rmdir('new_folder')
print("Directory 'new_folder' removed.")

#or
if os.path.exists(new_dir):
    os.rmdir(new_dir)
    print(f"Directory '{new_dir}' removed.")




#Sys MODULE - functions to interact with the Python runtime environment
""" It provides access to system-specific functions and some variables/parameters used or maintained by the interpreter. """
import sys
print(sys.argv)
# sys.argv is a list in Python, which contains the command-line arguments passed to the script.
# For example, if you run the script as: python script.py arg1 arg2
# The output will be: ['script.py', 'arg1', 'arg2']

print("Python Version:", sys.version)
# Python Version: 3.x.x (default, Month Day Year, HH:MM:SS) [GCC x.x.x]

print("Python Executable Path:", sys.executable)
# Python Executable Path: /path/to/python/executable

print("Module Search Paths:", sys.path)
# Module Search Paths: ['/path/to/current/directory', '/usr/lib/python3.x', ...]
# Add a new path to the module search paths

new_path = '/path/to/custom/modules'
if new_path not in sys.path:
    sys.path.append(new_path)
    print(f"Added '{new_path}' to module search paths.")

print("Updated Module Search Paths:", sys.path)
# Updated Module Search Paths: ['/path/to/current/directory', '/usr/lib/python3.x