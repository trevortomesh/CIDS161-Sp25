# CIS 161 - March 3, 2025

## Assignment 1 Feedback
- All grades for Assignment 1 have been returned (if submitted on time).
- Common issues:
  - Some students struggled with the format of the write-up.
  - Future assignments may include a worksheet-style format for better clarity.
  - Most students scored in the B range, with some A’s and a few C’s.
  - Some students went above and beyond; while appreciated, don't stress too much!
- If you have questions, visit office hours from 3-5 PM.

---

## Setting Up a New Python Script in PyCharm
- Renamed `main.py` to `old_main.py`.
- Created a new `main.py` file to start fresh.
- PyCharm automates running Python scripts, but behind the scenes:
  - Python programs are just text files (`.py` files).
  - The Python interpreter reads and executes them line by line.
  - You can run a Python script manually via the command line using `python3 script.py`.

## Selections in Python (if-else Statements)
### Basics of If-Statements
- A decision in programming is based on boolean values (`True` or `False`).
- Example:
  ```python
  if True:
      print("This will always print")
  if False:
      print("This will never print")
  ```

### Comparison Operators
| Operator | Meaning |
|----------|---------|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

#### Example:
```python
x = 5
if x > 3:
    print("x is greater than 3")
```

### Using If-Else
```python
radius = float(input("Enter the radius: "))
if radius < 0:
    print("Incorrect input")
else:
    area = 3.14159 * radius ** 2
    print("Area is", area)
```
- If the radius is negative, the program prints an error message.
- Otherwise, it calculates and prints the area.

### Boolean Expressions and Truthy/Falsy Values
- In Python, nonzero numbers and non-empty strings evaluate to `True`.
- Zero, `None`, empty lists (`[]`), and empty strings (`""`) evaluate to `False`.

Examples:
```python
print(bool(1))  # True
print(bool(0))  # False
print(bool("Hello"))  # True
print(bool(""))  # False
```

## Practice Problems

### **1. Simple If-Else Statement**
Write a program that asks the user for their age and prints whether they are an adult (18+) or not.
```python
# Expected Output Example
# Enter your age: 20
# You are an adult.
```

### **2. Comparing Two Numbers**
Write a program that takes two numbers as input and prints the larger of the two.
```python
# Expected Output Example
# Enter first number: 5
# Enter second number: 10
# 10 is larger.
```

### **3. Even or Odd Checker**
Write a program that checks whether a number is even or odd.
```python
# Expected Output Example
# Enter a number: 7
# The number is odd.
```

### **4. Grading System**
Write a program that takes a numerical grade (0-100) and prints the corresponding letter grade:
- 90+ → A
- 80-89 → B
- 70-79 → C
- 60-69 → D
- Below 60 → F

```python
# Expected Output Example
# Enter your score: 85
# Your grade is B.
```

### **5. Leap Year Checker**
Write a program that determines if a given year is a leap year.
- A year is a leap year if it is divisible by 4 but not by 100, unless it is also divisible by 400.
```python
# Expected Output Example
# Enter a year: 2024
# 2024 is a leap year.
```

---

## Next Steps
- Continue practicing `if` statements and boolean logic.
- Next lecture: More advanced control structures.
- Office hours available for homework questions.
