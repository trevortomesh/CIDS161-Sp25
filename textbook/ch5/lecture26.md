**CS 161 - April 7, 2025: Introduction to Functions, Scope, and Modules**

---

### Summary
In this lecture, we continued exploring **functions** in Python, focusing on understanding the difference between returning and printing values, defining and invoking functions, and using functions to modularize code. We also introduced how to **create reusable modules**, discussed the concept of **function scope**, and wrote functions to perform various tasks such as converting numeric grades to letter grades and computing the greatest common divisor (GCD). We closed with a teaser on variable scope and shadowing.

---

### Key Topics

#### 1. **Value-Returning vs. Non-Returning Functions**
- A **value-returning function** uses the `return` keyword to send a value back to the caller.
- A **non-returning function** may perform actions like `print()`, but does not send a result back.

**Examples:**
```python
def say_hi():
    return "Hi"

print(say_hi())  # Output: Hi


def say_hello():
    print("Hello")

say_hello()  # Output: Hello
print(say_hello())  # Output: Hello followed by None
```

---

#### 2. **Functions for Letter Grades**
We built two versions:
- `print_grade(score)`: prints the letter grade based on score.
- `get_grade(score)`: returns the letter grade as a value.

**Example (value-returning):**
```python
def get_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
```

---

#### 3. **Greatest Common Divisor (GCD) Function**
- Takes two integers and finds the largest number that evenly divides both.
- Demonstrates loop-based algorithm and use of the `return` keyword.

```python
def gcd(n1, n2):
    gcd = 1
    k = 2
    while k <= n1 and k <= n2:
        if n1 % k == 0 and n2 % k == 0:
            gcd = k
        k += 1
    return gcd
```

---

#### 4. **Modularization: Creating Python Modules**
- Modules allow code reuse across multiple programs.
- A **module** is a `.py` file containing function definitions.
- Use `from module_name import function_name` or `from module_name import *` to access them.

**Steps:**
1. Create `gcd_function.py` containing only the `gcd()` function.
2. Import with `from gcd_function import gcd`.

---

#### 5. **Function Scope (Teaser)**
- Python functions have their own **local scopes**.
- A variable defined inside a function is not accessible outside.
- Shadowing occurs when a local variable has the same name as a global one.

**Example (teaser):**
```python
a = 3

def func1():
    a = 5
    print(a)

def func2():
    a = 12

func1()  # prints 5
func2()
print(a)  # prints 3 (global value)
```
We’ll explore this further in the next class.

---

### Takeaways
- Functions reduce code repetition, improve readability, and help modularize logic.
- `return` allows functions to send back values.
- You can import and reuse functions from modules.
- Function scope determines where variables can be accessed.

---

**Next Lecture Preview:** Scope, shadowing, and more function practice!

---

**Living Textbook Project Note:** This lecture was part of the Living Textbook Initiative. Your feedback on its effectiveness will help shape future CS courses. If approved, you may be asked to participate in a short survey about your experience.

