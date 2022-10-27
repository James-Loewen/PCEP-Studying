from audioop import add
from utils.utils import print_header

###############################################################################
##                          star operator and *args                          ##
###############################################################################
print_header('star operator and *args')

"""
When writing Python functions, there are special ways to accept an
indefinite or unspecified number of parameters. In the function
declaration we use either the `*args` or `**kwargs` keywords (the number
of asterisks before each is important). Truthfully, the asterisks are 
all that matter, but we use 'args' and 'kwargs' because it's convention
and that helps with readability.
"""

"""
The *args keyword/syntax expects 0 or more *positional* parameters. This
means that they cannot be keyword parameters, for example, name="James".
The parameters don't have to be of a specific type, though it is almost
always the case that functions using the *args syntax expect parameters
of the same type.
"""

# parameters passed to this function get 'packed' into the variable args
def add_indef(*args):
    total = 0
    for num in args:
        total += num
    return total

sum_of_two = add_indef(10, 30)          # This works
sum_of_five = add_indef(1, 3, 4, 6, 7)  # This also works
sum_of_zero = add_indef()               # This also works

"""
The asterisk is a unary operator that either 'packs' or 'unpacks' the
variable that it prefixes. Above is an example of packing, below is an 
example of unpacking.
"""

a = ["Hello", "there", "I'm", "a", "list"]

print(' '.join(a))  # <- This does the same
print(*a)           # <- thing this does
# Output:
# Hello there I'm a list
# Hello there I'm a list

# This can get kinda funky...
# This is an example of tuple unpacking where x, y, and z each get a
# value from the tuple that follows the assignment operator.
x, y, z = (1, 2, 3)

# These are ugly, but perfectly fine python code:
*x, y, z = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
x -> [0, 1, 2, 3, 4, 5, 6, 7]
y -> 8
z -> 9
"""
x, *y, z = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
x -> 0
y -> [1, 2, 3, 4, 5, 6, 7, 8]
z -> 9
"""
x, y, *z = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
x -> 0
y -> 1
z -> [2, 3, 4, 5, 6, 7, 8, 9]
"""

"""
This would result in an error:
*x, *y, z = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
SyntaxError: multiple starred expressions in assignment
"""
