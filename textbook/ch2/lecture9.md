# CIS 161: Variable Naming Conventions and Best Practices

## Introduction to PEP 8
PEP 8 (Python Enhancement Proposal 8) is the official style guide for Python code. It exists to ensure Python code is **readable, consistent, and maintainable**. While Python itself does not enforce these conventions, following them helps create clean and professional-looking code.

**Why follow PEP 8?**
- **Improves readability** – Makes code easier to understand.
- **Enhances collaboration** – Encourages consistency across different programmers.
- **Increases maintainability** – Easier to update and modify.
- **Prevents common errors** – Reduces potential mistakes in the code.

## PEP 8 Guidelines for Variable Naming

### 1. **Maximum Line Length**
- Keep each line of code **within 79 characters**.
- If a line is too long, **break it up** using parentheses or backslashes (`\`).

```python
# Correct (breaks a long statement across multiple lines)
total_price = (
    item_price * quantity + shipping_cost - discount
)
```

### 2. **Whitespace Usage**
- Use **single spaces** around operators (`=`, `+`, `-`, `*`, `/`), after commas, and inside lists.
- Avoid extra spaces inside parentheses, brackets, or braces.

```python
# Correct:
result = a + b  # Spaces around operators
data = [1, 2, 3]  # Spaces after commas

# Incorrect:
result=a+b  # No spaces around operators
data = [ 1 , 2 , 3 ]  # Extra spaces inside brackets
```

### 3. **Variable Naming Rules**
- Variables **must** begin with a letter or an underscore (`_`).
- Variables **can** contain letters, numbers, and underscores.
- Variables **cannot** be Python keywords (`print`, `class`, `def`, etc.).
- Variable names are **case-sensitive**.

```python
# Correct:
name = "Alice"
age = 25
_num_items = 10  # Leading underscore is allowed

# Incorrect:
1st_name = "Bob"  # Cannot start with a number
class = "Math"  # 'class' is a reserved keyword
```

### 4. **Use Descriptive Names**
- Variable names should clearly indicate what they store.
- Avoid using single-letter names unless in specific contexts (like loop counters).

```python
# Correct:
num_students = 30
greeting_message = "Hello, world!"

# Incorrect:
x = 30  # Unclear what 'x' represents
y = "Hello"  # Unclear what 'y' represents
```

### 5. **Snake Case vs. Camel Case**
- Python prefers **snake_case** (words separated by underscores).
- Avoid using **camelCase** (capitalizing the first letter of words except the first).

```python
# Correct (Snake Case - Preferred in Python):
num_students = 30

# Incorrect (Camel Case - Used in Java but not Python):
numStudents = 30
```

### 6. **Constants in Uppercase**
- Use **uppercase letters with underscores** for constants (values that don’t change).

```python
PI = 3.14159
MAX_RETRIES = 5
```

### 7. **Avoid Overwriting Built-in Functions**
- Python has built-in functions like `print()`, `sum()`, `max()`, etc.
- Avoid using their names for variables.

```python
# Correct:
total_sum = sum([1, 2, 3])

# Incorrect:
sum = sum([1, 2, 3])  # Overwrites built-in function
```

### 8. **Avoid Special Characters and Spaces**
- Variable names cannot contain spaces or special characters (`@`, `#`, `$`, `-`, etc.).

```python
# Incorrect:
price-in-dollars = 100  # Cannot use hyphen

# Correct:
price_in_dollars = 100  # Use underscores instead
```

## Summary of Best Practices
1. **Use descriptive names** – `num_students`, not `x`.
2. **Follow snake_case for variable names**.
3. **Use UPPER_CASE for constants**.
4. **Avoid overwriting built-in functions**.
5. **Use spaces around operators, but not inside parentheses or brackets**.
6. **Keep lines under 79 characters**.
7. **Do not start variable names with numbers or special characters**.

## Practice Problems
### **Problem 1**
Which of the following variable names are valid in Python? If invalid, explain why.

```python
1st_student = "Alice"
stu_dent_count = 25
total-count = 50
MAX_VALUE = 100
print = "hello"
```

### **Problem 2**
Refactor the following Python code to follow best practices:

```python
x=5
y=10
totalPrice = x+y
totalprice = x+y
print (totalPrice)
```

### **Problem 3**
What will be the output of the following code?

```python
X = 10
x = 20
print(X, x)
```

### **Problem 4**
Which of these naming conventions follow PEP 8 guidelines?

```python
customerAge = 25  # (A)
customer_age = 25  # (B)
CUSTOMER_AGE = 25  # (C)
Customer_Age = 25  # (D)
```

### **Problem 5**
Identify the errors in the following Python code:

```python
class = "Math"
print("Hello")
def = 5
_sum = sum([1, 2, 3])
price in dollars = 20
```

---
This lecture covered **PEP 8 naming conventions, best practices for variable naming, and how to improve code readability and maintainability**. Following these guidelines will make your code more professional and easier to collaborate on!

**Next Topic:** Variables, Assignment Statements, and Expressions.

