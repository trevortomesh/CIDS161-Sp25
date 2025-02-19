## **Lecture Summary – February 19: Variables and Basic Operators**

### **Overview:**
Today’s lecture covered the fundamentals of variables in Python, focusing on how variables work as storage containers for values. We explored how to assign values, the significance of constants, the concept of scope, and various arithmetic operators.

---

### **Key Concepts:**

#### **1. Variables as Boxes:**
- Think of a variable as a box with a label where you can store a value.
- Values can be numbers, strings, or other data types.
- Example:
  ```python
  radius = 1.0  # Box labeled 'radius' holds the value 1.0
  pi = 3.14159  # Box labeled 'pi' holds the constant value of pi
  area = radius * radius * pi  # Area is calculated using values from the 'radius' and 'pi' boxes
  ```

#### **2. Constants:**
- Variables written in all capital letters represent constants.
- Example: `PI = 3.14159` signifies that `PI` should not change throughout the program.

---

### **3. Assignment and Expressions:**
- The `=` symbol is an **assignment operator**, not an equality sign.
- Pattern: `variable = expression`
- Examples:
  ```python
  y = 1             # Assigns 1 to y
  x = y + 1         # Assigns y + 1 to x
  area = radius ** 2 * pi  # Assigns the area of a circle using radius and pi
  ```

---

### **4. Variable Updates and Computation Order:**
- Python evaluates code **line-by-line**.
- Updating a variable **after** using it does not retroactively change previously computed values.
- Example:
  ```python
  radius = 1.0
  area = radius * radius * pi  # area is computed here with radius = 1.0
  radius = 10.0                # Changing radius now doesn't update area
  print(area)                  # Still shows the result from when radius was 1.0
  ```

#### **To Recompute:**
```python
radius = 10.0
area = radius * radius * pi  # Recalculate with updated radius
print(area)  # Shows updated area
```

---

### **5. Scope of Variables:**
- **Scope** refers to the portion of code where a variable is accessible.
- **Rule:** A variable must be **defined before use**.
- Example:
  ```python
  print(radius)  # Error: radius not defined yet
  radius = 5.0
  print(radius)  # Works: radius is now defined
  ```

---

### **6. Swapping Variables:**

#### **Traditional Method (Using a Temporary Variable):**
```python
x = 1
y = 2
temp = x
x = y
y = temp
```

#### **Pythonic Way (Simultaneous Assignment):**
```python
x, y = y, x  # Swaps values without a temporary variable
```
> 🔑 **Simultaneous assignment** is unique to Python and not available in languages like Java.

---

### **7. Arithmetic Operators:**

| **Operator** | **Name**              | **Example**       | **Result**  |
|--------------|----------------------|-------------------|-------------|
| `+`          | Addition              | `3 + 4`           | `7`         |
| `-`          | Subtraction           | `10 - 2`          | `8`         |
| `*`          | Multiplication        | `5 * 6`           | `30`        |
| `/`          | Floating Point Division | `5 / 2`       | `2.5`       |
| `//`         | Integer Division      | `5 // 2`          | `2`         |
| `%`          | Modulus (Remainder)   | `20 % 3`          | `2`         |
| `**`         | Exponentiation        | `4 ** 2`          | `16`        |

---

### **8. Numeric Data Types:**
- **Integers (int):** Whole numbers (e.g., `-3, 0, 42`)
- **Floating Point Numbers (float):** Numbers with decimals (e.g., `3.14, -2.7, 0.001`)

---

### **Practice Questions:**
1. What will the following code print?
   ```python
   x = 2
   y = 3
   x, y = y, x
   print(x, y)
   ```

2. Predict the output:
   ```python
   radius = 2
   area = radius ** 2 * 3.14159
   radius = 4
   print(area)
   ```

3. Calculate the result:
   ```python
   print(10 // 3)  # Integer division
   print(10 % 3)   # Remainder
   ```

4. Rewrite this code using simultaneous assignment:
   ```python
   temp = x
   x = y
   y = temp
   ```

5. Write a Python expression that calculates the area of a circle with a radius of 7 using a constant for pi.

---

💡 **Next Lecture:** We will dive deeper into variable scope and explore more operators and data types in Python.
