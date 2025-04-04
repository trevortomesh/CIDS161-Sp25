# CS 161 - April 4, 2025
## Introduction to Functions and the Call Stack

---

### Summary
In this lecture, we transitioned from loops to **functions**, learning how to define, call, and understand functions in Python. We discussed the **benefits of reusability** in programming and explored how functions help **eliminate redundancy**. We also examined the **call stack** metaphor using tennis balls and Pringles cans, illustrating how Python manages function calls and returns.

---

### Topics Covered

#### 1. **Announcements and Administrative Notes**
- Midterm exam grades are back (overall performance was solid).
- Some students still need to take the exam; general feedback will be postponed.
- Possible format change for the end of the semester due to instructor caregiving duties (wife’s surgery on April 24). Classes may shift online or be delivered via pre-recorded lectures.
- Quiz due next Friday covering post-Quiz 2 and pre-midterm content.

#### 2. **Motivation for Functions**
- Functions allow **reusability** and **modular code design**.
- Avoid writing repetitive code by isolating blocks into callable functions.

Example problem:
Calculate the sum of numbers in three separate ranges:
- 1 to 10
- 20 to 37
- 35 to 49

Initial solution: Copy/paste repeated `for` loops with small changes.
Problem: This approach introduces redundancy and makes code harder to maintain.

#### 3. **Defining a Function**

Basic syntax:
```python
def function_name(parameters):
    # function body
    return value
```

Example - Function to calculate sum between two numbers:
```python
def sum_range(start, end):
    result = 0
    for i in range(start, end + 1):
        result += i
    return result
```

#### 4. **Calling a Function**
- Functions must be called to execute.
- Calls can be made directly or within another function (e.g., `main()`):

```python
def main():
    print("Sum from 1 to 10:", sum_range(1, 10))
    print("Sum from 20 to 37:", sum_range(20, 37))
    print("Sum from 35 to 49:", sum_range(35, 49))

main()
```

#### 5. **Function Terminology**
- **Header**: The line starting with `def`, includes function name and parameters.
- **Body**: The indented block of code inside the function.
- **Parameters**: Placeholders for values passed to the function.
- **Arguments**: Actual values passed when calling the function.
- **Return Value**: The result that the function sends back to the caller.
- **Calling a Function**: Using the function by name with arguments.

#### 6. **Value-Returning vs Non-Returning Functions**
- **Value-Returning**: Returns a result using the `return` keyword.
- **Non-Returning (Void)**: Performs an action like `print()` without returning a result.

Examples:
```python
def say_hi():
    return "Hi"

def say_hello():
    print("Hello")
```

#### 7. **Calling Functions in Different Ways**
```python
z = max(2, 5)      # Store return value in variable
print(max(1, 4))   # Directly print the return value
```

#### 8. **Nested Function Calls**
- Functions can call other functions (e.g., `main` calls `sum_range`, `max` calls `say_hi`).
- Python tracks function calls using a **call stack**.

#### 9. **Understanding the Call Stack**
- A data structure that stores function calls in a LIFO (Last In, First Out) order.
- Think of it like a stack of tennis balls or a Pringles can:
  - Push function calls onto the stack.
  - Pop them off as functions return.

Visualization:
- `main()` is called and pushed onto the stack.
- Within `main()`, `sum_range()` is called → it goes on top.
- When `sum_range()` returns, it pops off.
- This continues until all functions complete and `main()` returns.

---

### Key Takeaways
- Functions reduce redundancy and make code more modular.
- Use `def` to define a function, `return` to send back a result.
- Value-returning functions and void (non-returning) functions serve different roles.
- The call stack manages which function is currently executing.
- Python programs often start with a `main()` function that calls others.

---

### Optional Exercises
1. Write a function that returns the product of two numbers.
2. Write a function that prints "Goodbye" three times without returning anything.
3. Modify `sum_range` to skip even numbers.
4. Define a `max_of_three` function that returns the largest of three numbers.
5. Simulate a call stack using print statements (show order of execution).

---

### Coming Up Next:
- Deeper look at parameter passing and scope.
- Functions within modules.
- Using return values in logic and conditionals.

---

**Living Textbook Entry Created: April 4, 2025**

