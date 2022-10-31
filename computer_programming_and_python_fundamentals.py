from utils.utils import print_header

edge = """
For some edge-case syntax, see ./control_flow.py
for some one-line conditional statements
"""
print(edge)

###############################################################################
##                       Compilation vs Interpretation                       ##
###############################################################################
print_header('Compilation vs Interpretation')

print("""
Python's 'lexis' is its list of keywords like for, while, def, class,
continue, etc...
""")

print("""
At the end of the day, in order for our program (written in some high-
level programming language) to run, it needs to be converted into
machine language. This is done either via compilation or interpretation.
""")

###############################################################################
##                          Base x Number Systems &                          ##
##                          Floating Point Accuracy                          ##
###############################################################################
print_header('Base x Number Systems &\nFloating Point Accuracy')

num_system_background = """
Our standard arithmetic number system is base 10, or 'Decimal.' The
number 0.125 is equal to (1/10 + 2/100 + 5/1000)

This is *not* how Python stores numbers. Python uses the base 2 number
system, often called 'Binary.' This isn't a bug, it's how numbers are
stored at a hardware level. There are some infinitely repeating decimal
numbers like how the fraction 1/3 can be represented approximately as
0.3333333333333... This decimal representation will never become 1/3,
but as you add more 3's it will become a closer approximation.

This is also the case in base 2. Our first example, 0.125 or 1/8 *can*
be represented exactly as 0.001 which is equal to 
(0/2 + 0/4 + 1/8)

Most machines these days use IEEE-754 floating point arithmetic and most
platforms map Python floats to IEEE-754 "double precision." 754 doubles
contain 53 bits of precision. So when you use a float in Python, the
computer uses the formula J/2**N where J is an integer containing
exactly 53 bits.
1 / 10 ~= J / (2**N)
J ~= 2**N / 10

Because J has *exactly* 53 bits (is >= 2**52 but < 2**53), the best
value for N is 56
"""
print(num_system_background)

x = .1
y = .3
print(y == x * 3)   # We expect this to be True, but it isn't

# This is because .1 isn't really .1, it's a little more
print(f'{x:.17f}')  # This prints out '0.10000000000000001'

###############################################################################
##                           Hexadecimal and Octal                           ##
###############################################################################
print_header('Hexadecimal and Octal')

octal_info = """
The Octal number system isn't widely used today, but it was very useful
with early computing. Words like 8-bit and 16-bit are derived from the
octal number system. Fun fact, it's super easy to convert between binary
and octal numbers! Each group of three binary digits equals one digit in
an octal number. E.g., 111101100010(base 2) == 7542(base 8)
    111 101 100 010
     7   5   4   2
Today, almost all systems use the hexadecimal system these days...
"""
print(octal_info)

hex_info = """
Hexadecimal numbers are super useful. We use them for representing rgb
colors. For example, rgb(233, 150, 122) can be represented as the
hexadecimal grouping #E9967A where E9 == 233, 96 == 150, and 7A == 122.
Hexadecimals are used for device MAC addresses as well, for example,
A0-1D-48-FE-5E-F5. In programming and machine languages, hexadecimals
are used to represent memory locations/addresses. If you've ever printed
a python function without calling it, you've seen something like the
following output:
>>> print(my_function)
<function my_function at 0x000001FF02383E20>
That '0x00...' number is a hexadecimal.

Because English doesn't have 16 distinct numeral signs, hexadecimals are
written out using the digits 0-9 and the letters A-F (not always 
capitalized, but I think it looks nicer). If we count to 20(base 16), 
this is what it looks like:
0 1 2 3 4 5 6 7 8 9 A B C D E F 10 11 12 13 14
"""
print(hex_info)

# HTML color 'darksalmon'
r, g, b = 233, 150, 122

def rgb_to_hex(rgb_tup):
    r = hex(rgb_tup[0]).upper()[2:]
    g = hex(rgb_tup[1]).upper()[2:]
    b = hex(rgb_tup[2]).upper()[2:]
    return f'#{r}{g}{b}'

print(rgb_to_hex((r, g, b)))

###############################################################################
##                            Scientific Notation                            ##
###############################################################################
print_header('Scientific Notation')

pass

###############################################################################
##                                Type Casting                               ##
###############################################################################
print_header('Type Casting')

type_casting = """
Type casting is the process of taking one data type and changing it into
another type. In Python this is done with three (sorta four) different
built-in functions: str(), int(), float(), and maybe bool().
"""
print(type_casting)

int_info = """
int() tries to construct an integer number from an integer literal, a
float literal (by removing all decimals), or a string literal (providing
the string represents a whole number)
"""
print(int_info)

a_string = "12"
a_int = int(a_string)
print(type(a_int), a_int)
# <class 'int'> 12

b_float = 3.14
b_int = int(b_float)
print(type(b_int), b_int)
# <class 'int'> 3

int_errors = """
This would result in a ValueError
c_string = "twenty"
c_int = int(c_string)

This also results in a ValueError
d_string = "15.125"
d_int = int(d_string)
"""
print(int_errors)

# But this does not:
d_string = "15.125"
d_int = int(float(d_string))
print(type(d_int), d_int)
# <class 'int'> 15

float_info = """
float() tries to construct a float number from an integer literal, a
float literal or a string literal (providing the string represents a
float or an integer)
"""
print(float_info)

d_string = "15.125"
d_float = float(d_string)
print(type(d_float), d_float)
# <class 'float'> 15.125

e_int = 200
e_float = float(e_int)
print(type(e_float), e_float)
# <class 'float'> 200.0

str_info = """
str() tries to construct a string from a wide variety of data types,
including strings, integer literals and float literals

This one is pretty robust and way less prone to errors than the previous
two.
"""
print(str_info)

f_int = 42
f_string = str(f_int)
print(type(f_string), f_string)
# <class 'str'> 42

g_float = 35.978
g_string = str(g_float)
print(type(g_string), g_string)
# <class 'str> 35.978

h_list = [1, 2, 3, "hello, there", 4]
h_string = str(h_list)
print(type(h_string), h_string)
# <class 'str'> [1, 2, 3, 'hello, there', 4]

i_tuple = (4, 5, 1)
i_string = str(i_tuple)
print(type(i_string), i_string)
# <class 'str'> (4, 5, 1)

j_dictionary = {
    'one': 1,
    'two': 2,
    'list': [4, 5, 6],
    'dict': {
        'nestable': True,
        'intuitive': False,
    }
}
j_string = str(j_dictionary)
print(type(j_string), j_string)
# <class 'str'> {'one': 1, 'two': 2, 'list': [4, 5, 6], 'dict': {'nestable': True, 'intuitive': False}}

bool_info = """
bool() is a weird one because it will always return either True or False
depending on the 'truthiness' of whatever is passed into it.

Truth testing in Python can be slightly complicated, but you can
summarize it by saying most non-empty, non-zero values evaluate to 
True, while empty sequences/collections, any form of zero, None, and 
False evaluate to False.
"""
print(bool_info)

# This works, but not for the reason you may immediately suspect
# Python doesn't actually recognize or understand the meaning of this
# string
k_string = 'True'
king_k_bool = bool(k_string)
print(type(king_k_bool), king_k_bool)
# <class 'bool'> True

# This illustrates why the above works and why we have to be careful
# with variable names and string content because we can trick ourselves
# into thinking Python is smarter than it is.
l_string = 'False'
l_bool = bool(l_string)
print(type(l_bool), l_bool)
# <class 'bool'> True

# Here's a ridiculous example:
class SuperTrue:
    is_true = True

    def __init__(self, essence=True):
        self.essence = essence
    
    def __str__(self):
        return "You must understand, I am veritably infallible!"
    
    # What's this sneaky little guy?
    def __len__(self):
        return 0

very_very_true = SuperTrue()

print(very_very_true)
# You must understand, I am veritably infallible!
print(bool(very_very_true))
# False