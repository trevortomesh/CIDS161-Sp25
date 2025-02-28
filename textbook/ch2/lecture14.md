# CS 161 - February 28, 2025

## Type Casting and Conversion

Last time, we discussed type casting and conversion, focusing on rounding and explicit vs. implicit conversions. When converting a float to an integer, we have two main options:

- Using `int()`, which truncates the decimal portion.
- Using `round()`, which rounds to the nearest whole number.

For example:

```python
A = 1.5
print("A as a float is:", A)
print("A as an integer is:", int(A))
print("A rounded is:", round(A))
```

### Key Takeaways:
- `int()` truncates the decimal (e.g., `int(3.9)` → `3`).
- `round()` rounds to the nearest whole number (e.g., `round(3.9)` → `4`).
- Implicit type conversion happens when an integer interacts with a float in an operation.

## Primitive Data Types in Python

### 1. Integer (`int`)
- Whole numbers (positive, negative, or zero).
- Example:

```python
x = 5
y = -3
z = 0
print(type(x), type(y), type(z))  # Output: <class 'int'>
```

### 2. Floating Point (`float`)
- Represents decimal numbers.
- Example:

```python
A = 3.4
B = -0.5
C = 10.0  # Still a float
print(type(A), type(B), type(C))  # Output: <class 'float'>
```

### 3. String (`str`)
- Sequence of characters enclosed in quotes.
- Example:

```python
greeting = "Hello, World!"
name = 'Python'
multi_line = """This is a
multi-line string."""
print(type(greeting))  # Output: <class 'str'>
```

- Strings can be concatenated using `+`:

```python
joined = greeting + " " + name
print(joined)  # Output: Hello, World! Python
```

### 4. Boolean (`bool`)
- Represents `True` or `False`.
- Example:

```python
is_sunny = True
is_raining = False
print(type(is_sunny), type(is_raining))  # Output: <class 'bool'>
```

### 5. Complex Numbers (`complex`)
- Python supports imaginary numbers using `j`.
- Example:

```python
c1 = 2 + 3j
c2 = 1 - 4j
print(type(c1), c1 + c2)  # Output: <class 'complex'>, (3-1j)
```

## Boolean Logic and Conditional Statements

Computers make decisions using boolean logic. Example:

```python
answer = input("Is it nice outside? (True/False): ")
if answer == "True":
    print("You should go for a walk!")
```

This is an `if` statement, which allows Python to execute a block of code based on a condition.

---

## **Practice Problems**

### **1. Type Conversion**
Convert the following to the specified type and print the result:

```python
# Convert to integer
a = 7.8
# Convert to float
b = 10
# Convert to string
c = 42
# Convert to boolean
d = 0
```

### **2. String Operations**
Write a Python program that takes two string inputs from the user and prints:
- The concatenated string.
- The length of the combined string.
- The uppercase version of the combined string.

### **3. Boolean Logic**
Write a program that asks the user:

```python
is_hot = input("Is it hot outside? (True/False): ")
is_raining = input("Is it raining? (True/False): ")
```

Then print whether or not they should go outside based on the following rules:
- If it is hot and not raining, print "Go outside, but stay hydrated."
- If it is hot and raining, print "Stay inside; it's muggy."
- If it is cold and not raining, print "Wear a jacket and go outside."
- If it is cold and raining, print "Stay inside and stay warm."

### **4. Arithmetic Operations**
Write a program that asks for two numbers and then prints:
- Their sum
- Their product
- The result of integer division
- The remainder (modulus)

### **5. Complex Numbers** *(Advanced)*
Create two complex numbers, add them together, and print the result:

```python
c1 = 4 + 5j
c2 = 2 - 3j
```

### **6. If Statements**
Write a simple program that asks the user for their age and prints:
- "You're a minor." if they're under 18.
- "You're an adult." if they're 18 or older.

---

These problems will help reinforce your understanding of Python's primitive data types and conditional logic. Let me know if you have any questions!

