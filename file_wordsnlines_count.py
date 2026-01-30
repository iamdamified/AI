# Count words and lines in a file
def count_words_and_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            line_count = len(lines)
            word_count = sum(len(line.split()) for line in lines)
        return word_count, line_count
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found!")
        return None, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None
    

# Example usage
stats = count_words_and_lines('text_cleaner.py')
print(stats)


# or using the function and printing results
file_path = 'text_cleaner.py'  # Replace with your file path
words, lines = count_words_and_lines(file_path)

# Print the results
if words is not None and lines is not None:
    print(f"Word Count: {words}")
    print(f"Line Count: {lines}")
