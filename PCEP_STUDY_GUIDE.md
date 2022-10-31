# Certified Entry-Level Python Programmer Exam — PCEP

(syllabus information is for the PCEP-30-02 version)

### The exam is broken down into 4 sections:
1. [Section 1](#computer-programming-and-python-fundamentals) &rarr; 7 items (18%)
    - [Computer Programming and Python Fundamentals](./computer_programming_and_python_fundamentals.py)
2. [Section 2](#control-flow--conditional-blocks-and-loops) &rarr; 8 items (29%)
    - [Control Flow — Conditional Blocks and Loops](./control_flow.py)
3. [Section 3](#data-collections--tuples-dictionaries-lists-and-strings) &rarr; 7 items (25%)
    - [Data Collections — Tuples, Dictionaries, Lists, and Strings](./data_collections.py)
4. [Section 4](#functions-and-exceptions) &rarr; 8 items (28%)
    - [Functions and Exceptions](./functions_and_exceptions.py)

### The exam will consist of 30 questions which could be:
- single choice
- multiple choice
- drag & drop
- gap fill
- sort
- code fill
- code insertion | Python 3.x

### A passing score is 70% or higher.

---

## [Computer Programming and Python Fundamentals](./computer_programming_and_python_fundamentals.py)

Things I need to study:
- Reading up about the interpretation and compilation.
    - **Compilation:** code is translated into machine code exactly once and must be re-translated any time a change is made to it. You end up with a separate executable file that contains machine language.
    - **Interpretation:** code is translated into machine code each time the code is run even if no changes have been made.
        - Python is an interpreted language.
        - Each line is read from top to bottom, left to right (mostly)
- Reading up about python lexical analysis and edge-case syntax
- Scientific notation
    - You can define float literals using scientific notations like this:
        ```python
        >>> num = 4.5e5
        >>> print(num)
        450000.0
        ```
    - The `e` can be upper or lowercase.
    - This will always be floats. The exponent (after the 'e') ***must always*** be an integer. The base can be a float or an integer.
- Binary, octal, decimal, and hexadecimal numeral systems
    - **Octal Literals:** you can define an octal number by prefixing it with `0o`, as in, `octal_num = 0o123`.
    - **Hexadecimal Literals:** same as above, but with the prefix `0x`, as in, `hex_num = 0xFF`.
- Naming conventions and PEP-8 recommendations
- Operators and data types adequate to the problem
    - unary and binary operators
    - bitwise operators `~&^|<<>>`
- The accuracy of floating-point numbers
    - Not quite an accuracy thing, but you can omit unnecessary zeros:
        ```python
        >>> print(.4)
        0.4
        >>> print(4.)
        4.0
        ```
    - floats are the dominant number type. `4 + 2.0` will evaluate to `6.0`.
        - The exceptions are regular division `/` and floor division `//`:
            ```python
            >>> 10 / 5      # exactly 2
            2.0             # always results in a float
            >>> 10 // 4     # exactly 2.5
            2
            >>> 10 // 4.    # conforms to the float rule
            2.0
            >>> 6 // 4      # result is always rounded to the lesser value integer
            1               # 1 < 1.5
            >>> -6 // 4     
            -2              # -2 < -1.5
            ```
- Most mathematical operations have left-side binding meaning they are evaluated from left to right. The exception is exponentiation `**`, which uses right-side binding. `2 ** 2 ** 3` evaluates to `256`.
- The `input()` and `print()` functions with `sep=` and `end=` keyword params
- Variables and Objects (P3P Python Basics Week 4)

Weird, but fun fact: Python allows for a single underscore between numbers when defining integer and float literals:

```python
>>> num1 = 9999999
>>> num2 = 9_999_999
>>> num3 = 9_9_9_9_9_9_9
>>> print(num1)
9999999
>>> print(num2)
9999999
>>> print(num3)
9999999
>>> print(num1 == num2 == num3)
True
>>> num4 = +9_2_6.1_0   # This feels so wrong, but isn't
>>> print(num4)
926.1
```

---

## [Control Flow — Conditional Blocks and Loops](./control_flow.py)

Things I need to study:
- Conditional statements syntax
    - Specifically weird edge-case/one-line statements
- `while`-`else` and `for`-`else` loops (never seen these before...)
- Revisit `pass`, `break` and `continue`

---

## [Data Collections — Tuples, Dictionaries, Lists, and Strings](./data_collections.py)

Things I need to study:
- Constructing vectors (I don't know what this even means...)
- Go over indexing and slicing (Reread PY4E Data Structures weeks 4 and 5)
- Read up on the `del` instruction
- Review list comprehension (P3P Data Collection Week 2)
- Revisit copying and cloning (P3P Python Basics Week 4)

---

## [Functions and Exceptions](./functions_and_exceptions.py)

Things I need to study:
- `*args` and `**kwargs`
    - Remember: `*` is for tuples/lists. `**` is for dictionaries.
    - If you're passing positional and keyword arguments to a function, the positional arguments must ***always*** come first.
- A function can ever return a single **object**, but that object can be a collection of multiple values, so the following is `True`:
    - A python function can return multiple values.
<<<<<<< HEAD:pcep_study_guide.md

**Function Invocation Order of Operations:**
1. Python checks whether the name is *legal* and is defined in memory.
2. Python checks the function's requirements for the number and type of arguments.
3. Python leaves the current line and goes to the function definition, passing in the arguments present in the invocation.
4. The lines of the function are run.
5. Python returns to where it was (i.e., the line after the invocation) and continues on with the code.
=======
>>>>>>> 9d3fec20b13e9d6697eba36dc384730972bfb5e4:PCEP_STUDY_GUIDE.md
