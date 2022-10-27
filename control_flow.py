from utils.utils import print_header

################################################################################
##                       for/else and while/else loops                        ##
################################################################################
print_header('for/else and while/else loops')

loop_else = """
An else clause after a for or while loop will be executed:
- if the loop is fully completed (i.e., not broken with a break statement)
- after the loop completes
- exactly once
"""
print(loop_else)

# Without for/else:
fruits = ['apple', 'pear', 'grapefruit', 'orange', 'mango', 'kiwi']
has_cado = False

for fruit in fruits:
    if fruit == 'avocado':
        has_cado = True
        print("Avocado toast is one the menu, boys.")
        break

if not has_cado:
    print("Looks like you're just having toast.")

# With for/else:
fruits = ['apple', 'pear', 'grapefruit', 'orange', 'mango', 'kiwi']

for fruit in fruits:
    if fruit == 'avocado':
        print('Oh boy, guac!')
        break
else:
    print('Oh no, no guac!')

# Another example:
for i in range(10):
    print(i)
else:
    # else block still has access to local variable i.
    print(f'This loop iterated {i + 1} times.')

################################################################################
##                     Weird/one-line conditionals/loops                      ##
################################################################################
print_header('Weird/one-line conditionals/loops')

# One-line conditional:
is_weird = True
if is_weird: print("I don't like how this looks, but it's syntactically correct.")

# One-line if/else: (I don't think this is the most readable)
is_friend = True
print("Hello, my friend") if is_friend else print("Hello, weirdo")

# One-line multi-else conditional — This one is particularly ugly
curr_hour = 12
print("It's morning") if curr_hour < 12 else print("It's exactly noon") if curr_hour == 12 else print("It's afternoon")

# Ternary assignment: (This is actually like in certain situations)
a, b = 10, 20
min = a if a < b else b
print('min:', min)

