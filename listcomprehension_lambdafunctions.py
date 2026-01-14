#List Comprhension
# Expression for items in iterable-if-condition

"""create a list of squares"""
squares = [x**2 for x in range(10)]
print("squares:", squares)
#squares: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

"""create a list of even numbers"""
evens = [i for i in range(10) if i % 2 == 0]
print("evens:", evens)
#evens: [0, 2, 4, 6, 8]





#Lambda Functions
"""anonymous, single-expression functions defined with the lambda keyword"""
add = lambda x, y: x + y
result = add(3, 5)
print("result of add lambda function:", result)
#result of add lambda function: 8


"""squares of a list of numbers using lambda and map"""
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print("squared_numbers using lambda and map:", squared_numbers)
#squared_numbers using lambda and map: [1, 4, 9, 16, 25]


"""filter even numbers from a list using lambda and filter"""
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("even_numbers using lambda and filter:", even_numbers)
#even_numbers using lambda and filter: [2, 4]



"""calculate the product of a list of numbers using lambda and reduce"""
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print("product using lambda and reduce:", product)
#product using lambda and reduce: 120
