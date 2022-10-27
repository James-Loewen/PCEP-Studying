from utils.utils import print_header

"""
For some edge-case syntax, see ./control_flow.py
for some one-line conditional statements
"""

###############################################################################
##                          Base x Number Systems &                          ##
##                          Floating Point Accuracy                          ##
###############################################################################
print_header('Base x Number Systems &\nFloating Point Accuracy')

"""
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

x = .1
y = .3
print(y == x * 3)   # We expect this to be True, but it isn't

# This is because .1 isn't really .1, it's a little more
print(f'{x:.17f}')  # This prints out '0.10000000000000001'

###############################################################################
##                           Hexadecimal and Octal                           ##
###############################################################################
print_header('Hexadecimal and Octal')

"""
The Octal number system isn't widely used today, but it was very useful
with early computing. Words like 8-bit and 16-bit are derived from the
octal number system. Fun fact, it's super easy to convert between binary
and octal numbers! Each group of three binary digits equals one digit in
an octal number. E.g., 111101100010(base 2) == 7542(base 8)
    111 101 100 010
     7   5   4   2
Today, almost all systems use the hexadecimal system these days...
"""

"""
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