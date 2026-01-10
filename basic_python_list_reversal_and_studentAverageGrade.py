
# """ A program to reverse a list and remove duplicates using a set """
# # Original list with duplicates
# original_list = [1, 2, 3, 2, 4, 5, 1, 6]
# # Reversing the list and removing duplicates by converting to a set(automatically removes duplicates)
# reversed_unique_list = list(set(original_list[::-1])) 
# # Displaying the result
# print("Reversed list with unique elements:", reversed_unique_list)
# # Note: The order of elements in the output list may vary due to the nature of sets.
# # Output: Reversed list with unique elements: [6, 1, 2, 3, 4, 5]



# """ A program that stores student grades in an initially empty dictionary and calculates the average grade """
# # Initializing an empty dictionary to store student grades
# student_grades = {}
# # Function to add a student's grade
# def add_grade(name, grade):
#     student_grades[name] = grade
# # Function to calculate the average grade
# def calculate_average():
#     if student_grades:
#         total = sum(student_grades.values())
#         average = total / len(student_grades)
#         return average
#     else:
#         return 0
# # Adding some student grades
# add_grade("Alice", 85)
# add_grade("Bob", 90)
# add_grade("Charlie", 78)
# # Calculating and displaying the average grade
# average_grade = calculate_average()
# print("Average Grade:", average_grade)
# # Output: Average Grade: 84.33333333333333


""" A program that stores student grades interactively in an initially empty dictionary and calculates the average grade """
# Initializing an empty dictionary to store student grades
student_grades = {}
# Function to add a student's grade
def add_grade(name, grade):
    student_grades[name] = grade
# Function to calculate the average grade
def calculate_average():
    if student_grades:
        total = sum(student_grades.values())
        average = total / len(student_grades)
        return average
    else:
        return 0
# Interactively adding student grades
while True:
    name = input("Enter student name (or 'done' to finish): ")
    if name.lower() == 'done':
        break
    grade = float(input(f"Enter grade for {name}: "))
    add_grade(name, grade)
# Calculating and displaying the average grade
average_grade = calculate_average()
print("Average Grade:", average_grade)
# Output: Average Grade: (depends on user input)

