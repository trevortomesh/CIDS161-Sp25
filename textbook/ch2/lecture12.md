## **Lecture Summary – February 24: Numeric Data Types, Operators, and Order of Operations**

### **Overview:**
Today’s lecture focused on the **assignment due tonight**, the **grading rubric**, and key programming concepts including **numeric data types**, **arithmetic operators**, **order of operations**, and a **time conversion calculator** example.

---

### **1. Assignment and Grading Rubric:**
- **Key Requirements:**
  - Properly handle **user input**.
  - Perform the **correct calculation**.
  - **Output results** accurately.
  - Submit a **Program Write-Up Document (PWUD)** including:
    - Steps taken and challenges faced.
    - Sources referenced.
    - Reflections and improvements.
- **No code comments required** for this assignment, but they will be introduced in future assignments.
- **No resubmissions** allowed, but leniency is applied early in the semester.
- **Office hours:** 3-5 PM today; no appointment needed.

---

### **2. Numeric Data Types:**
Python has **two numeric data types**:
- **Integers (int):** Whole numbers (e.g., `-3, 0, 42`).
- **Floating Point Numbers (float):** Numbers with decimals (e.g., `3.14, -2.7, 0.001`).

Python **defaults to the higher precision** when combining an `int` and a `float` in an operation.

Example:
```python
2 + 2    # 4 (int)
2 + 2.0  # 4.0 (float)
```

---

### **3. Arithmetic Operators in Python:**

| **Operator** | **Name**                | **Example**      | **Result**  |
|--------------|-------------------------|------------------|-------------|
| `+`          | Addition                 | `3 + 4`          | `7`         |
| `-`          | Subtraction              | `10 - 2`         | `8`         |
| `*`          | Multiplication           | `5 * 6`          | `30`        |
| `/`          | Floating Point Division  | `5 / 2`          | `2.5`       |
| `//`         | Integer Division         | `5 // 2`         | `2`         |
| `%`          | Modulus (Remainder)      | `20 % 3`         | `2`         |
| `**`         | Exponentiation           | `2 ** 3`         | `8`         |

#### **Important Notes:**
- **Floating Point Division (`/`)** always returns a float.
- **Integer Division (`//`)** truncates towards zero.
- **Modulus (`%`)** gives the remainder of a division.
- **Exponentiation (`**`)** raises a number to a power.

Example:
```python
3 / 2   # 1.5 (float division)
3 // 2  # 1 (integer division)
5 % 2   # 1 (remainder)
2 ** 3  # 8 (2 raised to the power of 3)
```

---

### **4. Time Conversion Calculator Example:**
We built a program to convert **seconds** into **minutes and seconds**.

#### **Steps:**
1. **Input:** Prompt the user for the number of seconds.
2. **Process:** Calculate minutes and remaining seconds.
3. **Output:** Display the result in the format `X minutes and Y seconds`.

#### **Code Example:**
```python
# Step 1: Input
seconds = int(input("Enter the number of seconds: "))

# Step 2: Process
minutes = seconds // 60
remaining_seconds = seconds % 60

# Step 3: Output
print(f"{seconds} seconds is {minutes} minutes and {remaining_seconds} seconds.")
```

#### **Sample Runs:**
```bash
Enter the number of seconds: 120
120 seconds is 2 minutes and 0 seconds.

Enter the number of seconds: 121
121 seconds is 2 minutes and 1 second.
```

🔑 **Tip:** The modulus operator `%` is useful for extracting remainders, which helps calculate leftover seconds.

---

### **5. Order of Operations (PEMDAS):**
Python follows the **standard mathematical order of operations**:
- **P**arentheses
- **E**xponents (`**`)
- **M**ultiplication & **D**ivision (`*`, `/`, `//`, `%`)
- **A**ddition & **S**ubtraction (`+`, `-`)

#### **Example:**
```python
result = 3 + 4 * 2 / (1 - 5) ** 2  # Evaluates using PEMDAS
print(result)  # Output: 3.5
```

#### **Complex Expression Translation:**
Given this expression:
\[
\frac{3 + 4x}{5 - 10y} - 5(a + b + c) / (x + 9 \times 4) + \frac{x}{y}
\]

Python equivalent:
```python
x, y, a, b, c = 5, 3, 1, 2, 3
result = ((3 + 4 * x) / (5 - 10 * y)) - (5 * (a + b + c) / (x + 9 * 4)) + (x / y)
print(result)  # Output: 77.8
```
> Adding **parentheses** improves readability and ensures correct evaluation.

---

### **Practice Problems:**
1. **Simple Math:**
   - What is the output of:
     ```python
     print(7 // 3)
     print(7 % 3)
     ```

2. **Seconds to Hours:**
   - Expand the time converter to also calculate **hours**, **minutes**, and **seconds**.

3. **Order of Operations:**
   - Predict the result of this expression:
     ```python
     result = (4 + 2) * 3 ** 2 / 6 - 1
     print(result)
     ```

4. **Modulus Application:**
   - Write a function that checks if a number is **even** or **odd** using `%`.
     ```python
     def is_even(number):
         return number % 2 == 0
     ```

5. **Challenge:**
   - Modify the calculator to handle **days**, **hours**, **minutes**, and **seconds** from a given number of seconds.

---

💡 **Next Lecture:** We'll revisit **order of operations** and introduce **assignment operators**.

🕒 **Reminder:** Assignment 1 is **due tonight**! Good luck, and don't hesitate to reach out during office hours.
