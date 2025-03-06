# CS 161 - March 5, 2025

## Announcements
- Today’s class is online due to inclement weather.
- Friday's class is expected to be in person unless conditions change.
- If you have questions, please unmute your mic or use the meeting chat.

---

## **Selections in Python (If-Else Statements)**

### **Introduction to Selections**
- In programming, selection allows us to execute specific blocks of code based on conditions.
- Programs typically execute line by line, but conditions allow for dynamic decision-making.
- Example of a simple sequence:

```python
A = 5
B = 3
print(A + B)  # Outputs: 8
```

- The Python interpreter executes each line sequentially.
- However, with selection statements (if-else), the program can decide which lines to execute based on conditions.

---

### **Basic If-Else Statement**
- We can control program execution using conditional statements.

#### **Example: Voting Eligibility**
```python
age = 18
if age >= 18:
    print("You are allowed to vote.")
else:
    print("You are not allowed to vote.")
```

#### **Output:**
- If `age = 18`, output: `You are allowed to vote.`
- If `age = 17`, output: `You are not allowed to vote.`

---

### **Understanding Indentation in Python**
- Python relies on indentation to define code blocks.
- The `if` statement must be followed by an indented block of code.
- Example of incorrect indentation:

```python
if age >= 18:
print("You are allowed to vote.")  # IndentationError
```

- Correct version:

```python
if age >= 18:
    print("You are allowed to vote.")
```

**Best practice:** Use either **4 spaces** or **tabs** for indentation, but don’t mix them.

---

### **Else-If (Elif) Statements**
- If there are multiple conditions, we use `elif`.
- Example: Determining weather conditions

```python
temperature = 85
if temperature > 80:
    print("It's a hot day.")
elif temperature > 60:
    print("It's a warm day.")
else:
    print("It's a cool day.")
```

#### **Output Examples:**
- `temperature = 85` → `It's a hot day.`
- `temperature = 70` → `It's a warm day.`
- `temperature = 50` → `It's a cool day.`

**Key Rule:** `elif` only executes if the previous `if` condition is false.

---

### **Comparison Operators Recap**
| Operator | Description |
|----------|-------------|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

---

### **Example: Grade Classification**

```python
score = int(input("Enter a score: "))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

#### **Common Errors in If-Else Statements**
1. **Forgetting indentation**
2. **Using `=` instead of `==` in conditions**
3. **Not handling all possible cases** (e.g., missing an `else` clause)

---

## **Nested If Statements**
- An `if` statement inside another `if` statement.
- Example: Concentric Castle Defense

```python
gate1_open = True
gate2_open = True
gate3_open = True

if gate1_open:
    print("Gate 1 has been breached!")
    if gate2_open:
        print("Gate 2 has been breached!")
        if gate3_open:
            print("Gate 3 has been breached!")
            print("The king is dead!")
```

- The attack only succeeds if **all** gates are open.
- Closing any gate prevents the attack from progressing.

---

## **Practice Problems**

### **1. Age Classification**
Write a program that asks the user for their age and classifies them as:
- "Child" (age < 13)
- "Teen" (13-17)
- "Adult" (18+)

### **2. Even or Odd**
Write a program that checks if a number is even or odd.

### **3. Leap Year Checker**
Write a program that asks for a year and determines if it's a leap year.
- A leap year is divisible by 4 but not 100 unless also divisible by 400.

### **4. Discount Calculator**
Ask the user for the price of an item.
- If price > $100, apply a 20% discount.
- If price is between $50 and $100, apply a 10% discount.
- Otherwise, no discount.

### **5. Triangle Type Checker**
Write a program that takes three side lengths and determines if the triangle is:
- Equilateral (all sides equal)
- Isosceles (two sides equal)
- Scalene (no sides equal)

---

## **Next Topics**
- More selection structures
- Logical operators (`and`, `or`, `not`)
- Introduction to loops

---

## **Reminders**
- Watch your indentation when writing if-else statements.
- Make sure conditions cover all possible cases.
- Avoid deeply nested if-statements for better readability.

That’s all for today! Stay safe, and we’ll hopefully be back in person on Friday!

