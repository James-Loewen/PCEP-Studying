from utils.utils import print_header
################################################################################
##                             List Comprehension                             ##
################################################################################
print_header('List Comprehensions')

# This creates a list of 50 even numbers from 0 to 98
even_nums = [num for num in range(100) if num % 2 == 0]
# print(even_nums)

# This is harder to read, but it still works. 
# It creates a list of 100 items. The even numbers
# from 0 to 98 separated by the string 'odd'
wonky = [num if num % 2 == 0 else 'odd' for num in range(100)]
# print(wonky)

# Here's the blueprint for a list comprehension with conditionals
# ls = [f(x) if condition else g(x) for x in sequence]
# where f() and g() are either manipulations of the iteration
# variable, or entirely unrelated values:
odd_even = [f'{num} is even' if num % 2 == 0 else f'{num} is odd' for num in range(100)]
# print(odd_even)