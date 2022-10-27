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

###############################################################################
##                          double star and **kwargs                         ##
###############################################################################
print_header('double star and **kwargs')

"""
The ** operator is also used for packing and unpacking, HOWEVER, it is 
ONLY used with python dictionaries.
"""

def print_keys_and_values(**kwargs):
    # kwargs is the name of the dictionary
    for key, value in kwargs.items():
        print(key, value)

print_keys_and_values(boop="beep", snoop="sneep", cat1="Suki", cat2="Mako")
"""
Output:
boop beep
snoop sneep
cat1 Suki
cat2 Mako
"""

###############################################################################
##                                name scopes                                ##
###############################################################################
print_header('name scopes')

"""
The acronym for remembering how Python resolves scope is LEGB, which
stands for "Local, Enclosing, Global, Built-in."

Local (L): The local, or current, scope. This could be the body of a
function or the top-level scope of a script. It always represents the
scope that the Python interpreter is currently working in.

Enclosing (E): The enclosing scope. This is the scope one level up from
the local scope. If the local scope is an inner function, the enclosing
scope is the scope of the outer function. If the scope is a top-level
function, the enclosing scope is the same as the global scope.

Global (G): The global scope, which is the top-most scope in the script.
This contains all of the names defined in the script that are not
contained in a function body.

Built-in (B): The built-in scope contains all of the names, such as
keywords, that are built-in to Python. Functions such as round() and
abs() are in the built-in scope. Anything that you can use without first
defining yourself is contained in the built-in scope.
"""

"""
The keyword global can be used to override a new variable's scope so
that it can be accessed from anywhere within the global scope. The
syntax is a bit weird for Python and looks a little bit like how you
might create an empty variable in JavaScript. It is important to note
that because of the way Python handles function declarations, (i.e.,
doesn't run the function body until it has been called), a global
variable won't exist until the function it's created in is called.
"""

def func():
    global new_var
    new_var = "Available everywhere"

print(new_var)
# NameError because new_var doesn't exist yet.

func()
print(new_var)
# Available everywhere