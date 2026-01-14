"""Program to copy the contents of one file to another file."""
def copy_file_contents(source_file, destination_file):
    """Copy contents from source_file to destination_file."""
    try:
        with open(source_file, 'r') as src:
            contents = src.read()
        with open(destination_file, 'w') as dest:
            dest.write(contents)
        print(f"Contents copied from {source_file} to {destination_file}.")
    except FileNotFoundError:
        print(f"The file {source_file} does not exist.")
source = 'fruits.txt'
destination = 'fruits_copy.txt'
copy_file_contents(source, destination)