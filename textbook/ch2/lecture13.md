## **Lecture Summary – February 26: Augmented Assignment Operators and Type Conversion**

### **Overview:**
Today's lecture focused on **augmented assignment operators**, how programming differs from traditional mathematics, and **type conversion (casting)** in Python.

---

### **1. Assignment Due Dates Reminder:**
- **Assignment 1 was due on February 24**
  - Late submissions: **5 points deducted per day**
  - Most students have submitted, and grading is in progress.
- **Quiz 1 is due on February 28**
  - Check the syllabus and calendar for future due dates.

---

### **2. Understanding Assignment vs. Mathematical Equations**
- **Mathematical Equation:** `x = x + 1` is **invalid** in traditional math.
- **Programming Expression:** `x = x + 1` **is valid** and means:
  - Take the **current value of `x`**, add `1`, and store the result **back in `x`**.

#### **Example:**
```python
x = 3
x = x + 1  # x now equals 4
```
> **Key Concept:** Variables in programming **store** values but are not equations. They represent **commands** to update values over time.

---

### **3. Augmented Assignment Operators**
Python provides shorthand operators for modifying variables:

| **Operator** | **Name**                 | **Example**       | **Equivalent To**      |
|-------------|-------------------------|------------------|----------------------|
| `+=`        | Addition Assignment      | `x += 2`        | `x = x + 2`         |
| `-=`        | Subtraction Assignment   | `x -= 3`        | `x = x - 3`         |
| `*=`        | Multiplication Assignment| `x *= 4`        | `x = x * 4`         |
| `/=`        | Float Division Assignment| `x /= 5`        | `x = x / 5`         |
| `//=`       | Integer Division Assignment | `x //= 6`   | `x = x // 6`       |
| `%=`        | Modulus Assignment       | `x %= 7`        | `x = x % 7`         |
| `**=`       | Exponentiation Assignment| `x **= 2`       | `x = x ** 2`        |

#### **Example:**
```python
x = 10
x += 5  # x is now 15
x *= 2  # x is now 30
x %= 4  # x is now 2 (remainder when divided by 4)
```

> 🔑 **Why use them?** They make code shorter and easier to read.

---

### **4. Type Conversion (Casting)**
Python automatically **converts data types** in some situations but requires explicit conversion in others.

#### **Implicit Casting** (Automatic Conversion)
- Happens when combining `int` and `float`.
- Example:
  ```python
  x = 5   # int
  y = x + 0.5  # x is implicitly converted to float
  print(y)  # Output: 5.5
  ```

#### **Explicit Casting** (Manual Conversion)
- **Convert float to int:**
  ```python
  x = 5.7
  y = int(x)  # y is now 5 (truncates decimal part)
  ```
- **Convert int to float:**
  ```python
  x = 5
  y = float(x)  # y is now 5.0
  ```
- **Rounding to nearest integer:**
  ```python
  x = 5.6
  y = round(x)  # y is now 6
  ```

#### **Integer Division Implicit Casting Example:**
```python
x = 5.0 // 2  # Implicit conversion to integer
print(x)  # Output: 2.0 (Python converts back to float)
```

> 🔑 **Takeaway:** Python **hides** a lot of type conversion details but allows explicit conversion when needed.

---

### **5. Practice Problems**
1. **Augmented Assignment:**
   - Predict the output:
     ```python
     x = 10
     x += 3
     x *= 2
     print(x)
     ```

2. **Modulus Operator:**
   - What will be printed?
     ```python
     x = 17
     x %= 5
     print(x)
     ```

3. **Type Conversion:**
   - Convert `7.9` to an integer **without rounding**.
   - Convert `8` to a float.

4. **Combining Operators:**
   - What will be the final value of `x`?
     ```python
     x = 12
     x //= 5
     x += 2
     x *= 3
     print(x)
     ```

5. **Bonus Challenge:**
   - Write a program that asks the user for a number, doubles it, and prints the result using an **augmented assignment operator**.

---

💡 **Next Lecture:** We will finish **type conversion** and introduce **flow control** in Python.

🕒 **Reminder:** Quiz 1 is **due on February 28**. Don't forget to complete it on time!
