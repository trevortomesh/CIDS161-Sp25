# Introduction to Python Programming (CIDS 161)

## Overview
In this session, we introduced Python, an **interpreted high-level programming language**, and explored fundamental programming concepts such as **print statements, variables, arithmetic operations, and user input** using an Integrated Development Environment (IDE), specifically **PyCharm**.

---
## 1. What is Python?
Python is a **high-level programming language** designed to be **readable** and **easy to learn**. Unlike low-level languages such as **C or Assembly**, Python **abstracts** many complexities, making it more like English.

### Features of Python:
- **Interpreted** (Runs line by line, no need for compilation)
- **Dynamically typed** (No need to declare variable types explicitly)
- **Beginner-friendly**
- **Portable** (Runs on Windows, macOS, Linux)

---
## 2. Setting Up Python
### Integrated Development Environment (IDE)
An **IDE** (Integrated Development Environment) is a tool that helps programmers write, run, and debug code efficiently.

In this course, we use **PyCharm** because it:
- Provides a **text editor** to write Python programs
- Has built-in **debugging tools**
- Allows easy **execution** of Python scripts

### Installing Python
If Python is not installed:
1. Visit [python.org](https://www.python.org/downloads/)
2. Download and install the latest version (e.g., **Python 3.12**)
3. Ensure PyCharm detects the installed version

---
## 3. Writing and Running Python Code

### 3.1 Print Statements
The `print()` function is used to display output.

#### Example:
```python
print("Hello, world!")
print("Welcome to Python programming!")
```
**Output:**
```
Hello, world!
Welcome to Python programming!
```

### Practice Problems:
1. Write a Python program to print **"Learning Python is fun!"**
2. Modify the above program to print **your name and favorite hobby** on separate lines.

---
## 4. Variables and Data Types
A **variable** is a container for storing values.

### Example:
```python
name = "Alice"
age = 25
print("Name:", name)
print("Age:", age)
```
**Output:**
```
Name: Alice
Age: 25
```
### Rules for Naming Variables:
- Must start with a **letter** or **underscore** (`_`)
- Cannot start with a **number**
- Cannot contain spaces or special characters
- Should be **descriptive** (e.g., `user_name`, not `x`)

### Practice Problems:
1. Declare variables for your **name, age, and favorite color**, then print them.
2. Create two variables `a = 10` and `b = 20`, swap their values, and print them.

---
## 5. Basic Arithmetic Operations
Python supports basic math operations:

| Operator | Symbol | Example |
|----------|--------|---------|
| Addition | `+` | `3 + 2 = 5` |
| Subtraction | `-` | `5 - 2 = 3` |
| Multiplication | `*` | `3 * 2 = 6` |
| Division | `/` | `10 / 2 = 5.0` |
| Modulus | `%` | `10 % 3 = 1` (Remainder) |

### Example:
```python
x = 15
y = 4
print("Sum:", x + y)
print("Difference:", x - y)
print("Product:", x * y)
print("Quotient:", x / y)
print("Remainder:", x % y)
```

### Practice Problems:
1. Write a program to calculate and print the **area of a rectangle** (length × width).
2. Modify the above program to compute the **area of a circle** given its radius (`π * r^2`). Use `pi = 3.1416`.

---
## 6. Getting User Input
Python allows user interaction via the `input()` function.

### Example:
```python
name = input("Enter your name: ")
print("Hello, " + name + "!")
```

### Practice Problems:
1. Write a program that asks the user for their **name and age**, then prints:
   **"Hello [name], you are [age] years old!"**
2. Write a program that prompts the user to enter two numbers, then prints their sum, difference, product, and quotient.

---
## 7. Fahrenheit to Celsius Conversion
We wrote a program to convert **Fahrenheit to Celsius**:

### Formula:
```
C = (F - 32) * 5/9
```

### Python Code:
```python
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print(fahrenheit, "degrees Fahrenheit is", round(celsius, 2), "degrees Celsius")
```

### Practice Problems:
1. Modify the program to convert **Celsius to Fahrenheit** (`F = C * 9/5 + 32`).
2. Allow the user to **enter multiple temperatures** and display the converted values.

---
## Summary
- Python is a **high-level, interpreted programming language**.
- We use **PyCharm** as our IDE.
- The `print()` function **displays output**.
- **Variables** store values, and Python handles different **data types** automatically.
- We can perform **basic arithmetic operations**.
- The `input()` function allows users to **enter values dynamically**.
- We created a **Fahrenheit to Celsius converter**.

### Next Steps:
In the next lecture, we will explore **conditional logic** (if-statements) to make our programs more interactive and dynamic.

---
## Additional Practice
Try the following exercises:
1. Write a program that takes three numbers as input and prints their **average**.
2. Write a program that asks the user for two numbers and **prints the larger number**.
3. Modify the **temperature converter** to ask the user if they want to convert **Fahrenheit to Celsius or Celsius to Fahrenheit** before performing the calculation.

---
### End of Lecture
**Questions?**
Make sure you practice these concepts before the next session! 🚀

