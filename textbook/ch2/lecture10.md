# CIDS 161 - February 17, 2025

## Overview
In today's lecture, we continued discussing variables, their assignment, best practices, and how Python processes them. We also briefly revisited the Living Textbook Initiative and its availability for students seeking additional practice problems. 

## Key Topics
### Variables and Identifiers
- **Variables** store values and can be reassigned.
- **Identifiers** are names that identify variables, functions, and other program elements.
- Identifiers must begin with a letter or an underscore and cannot be Python keywords.

#### Example of Identifiers:
```python
variable_guy = 12  # Identifier: 'variable_guy'
print = "Hello"  # Invalid as 'print' is a keyword
```

### Python Keywords
- Python has reserved keywords that cannot be used as identifiers.
- To list Python keywords, use:
```python
import keyword
print(keyword.kwlist)
```

### Variable Naming Best Practices
- Descriptive names improve readability:
    - `temp_now = -16` (Good)
    - `t = -16` (Bad)
- Constants should use uppercase letters (e.g., `PI = 3.14159`).

### Assigning and Reassigning Variables
- Variables can store different data types dynamically:
```python
boxy = "I am a box"
print(boxy)  # Output: I am a box
boxy = 5
print(boxy)  # Output: 5
```
- Python allows reassignment but does not enforce type safety like Java.

### Computing the Area of a Circle
```python
PI = 3.14159  # Constant (by convention)
radius = 1.0
area = radius * radius * PI
print(area)  # Output: 3.14159
```
- The calculation uses stored values without modifying the original variables.
- Updating `radius` does **not** automatically update `area` unless explicitly recalculated.

### Python Execution Flow
- Python executes line-by-line, updating variables in sequence.
- Example:
```python
radius = 1.0
area = radius * radius * PI
radius = 10  # Does NOT retroactively update area
print(area)  # Output: 3.14159 (not updated)
```

## Expressions and Assignment Statements
- **Assignment Statement Format:**
  ```python
  variable = expression
  ```
- **Expressions:** Computations involving values, variables, and operators:
  ```python
  x = 5 * (3 / 2) + 3 + 3 * 2
  y = x + 1
  ```
- Python treats `=` as the **assignment operator**, not equality.

## Review Questions
1. What is an identifier in Python?
2. Why can’t a variable be named `import`?
3. What is the difference between a variable and an identifier?
4. What will the following code output?
   ```python
   x = 10
   y = x
   x = 20
   print(y)
   ```
5. How does Python handle constants?
6. What will happen if you try to assign a value to a Python keyword?
7. Why does updating a variable’s value not retroactively update calculations that used it?

### Next Class Preview
- We will explore the behavior of:
  ```python
  x = x + 1
  ```
- Introduction to expressions, evaluation, and the importance of order of operations.

**See you on Wednesday!**