# write and read a list of items

def write_items_to_file(items, filename):
    """Write a list of items to a file, one item per line."""
    with open(filename, 'w') as file:
        for item in items:
            file.write(f"{item}\n")
def read_items_from_file(filename):
    """Read a list of items from a file, one item per line."""
    try:
        with open(filename, 'r') as file:
            # items = [line.strip() for line in file.readlines()]
            # or
            items = file.readlines()
            print("items in the file: ", items)
            for item in items:
                print(item.strip())
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")


fruits = ['apple', 'banana', 'cherry', 'date']
filename = 'fruits.txt'
write_items_to_file(fruits, filename)#file does not exist in first instance running, however, the file was created with the expected contents.
read_items_from_file(filename) # displays the file content as expected with friuts items expected.

# Output:
# items in the file:  ['apple\n', 'banana\n', 'cherry\n', 'date\n']




