# Compound Conditions in Python (CIDS 161)

In today's CIDS 161 lecture, we focused on compound conditions and logical operators in Python. This is a critical concept in programming, allowing you to check multiple conditions at once and control the flow of your program accordingly.

## Review of Boolean Expressions
So far, you've used basic Boolean expressions with `if`, `elif`, and `else` statements to control the behavior of your program based on one condition. Examples include:

```python
if x > y:
    print("x is greater than y")
```

But often, you need to evaluate multiple conditions at the same time. That's where compound conditions come in.

## Logical Operators
Python provides three main logical operators to build compound conditions:

- `and`: Both conditions must be true
- `or`: At least one condition must be true
- `not`: Negates a condition (true becomes false and vice versa)

### Example: Using `and`
```python
x = 5
y = 10

if x > 0 and y > 0:
    print("Both x and y are positive")
```
This prints the message only if BOTH `x > 0` AND `y > 0` are true.

### Example: Using `or`
```python
x = -5
y = 10

if x > 0 or y > 0:
    print("At least one value is positive")
```
This prints the message if EITHER condition is true.

### Example: Using `not`
```python
x = -5

if not x > 0:
    print("x is not positive")
```
`not` reverses the truth value of the expression.

## Truth Tables
We reviewed how logical operators work using truth tables:

### `and` Truth Table
| A     | B     | A and B |
|-------|-------|---------|
| True  | True  | True    |
| True  | False | False   |
| False | True  | False   |
| False | False | False   |

### `or` Truth Table
| A     | B     | A or B  |
|-------|-------|---------|
| True  | True  | True    |
| True  | False | True    |
| False | True  | True    |
| False | False | False   |

### `not` Truth Table
| A     | not A |
|-------|-------|
| True  | False |
| False | True  |

## Compound Conditions Example: Divisibility
We wrote a program to check if a number is divisible by 2 and/or 3.

### Divisible by 2 and 3
```python
if number % 2 == 0 and number % 3 == 0:
    print("Divisible by 2 and 3")
```

### Divisible by 2 or 3
```python
if number % 2 == 0 or number % 3 == 0:
    print("Divisible by 2 or 3")
```

### Divisible by 2 or 3 but not both
```python
if (number % 2 == 0 or number % 3 == 0) and not (number % 2 == 0 and number % 3 == 0):
    print("Divisible by 2 or 3, but not both")
```

This last condition combines `or`, `and`, and `not` to express a more complex logic: true if divisible by either 2 or 3, but false if divisible by both.

## Summary
- Compound conditions allow you to express more complex logic.
- `and`, `or`, and `not` are the building blocks for combining conditions.
- Use parentheses to make compound conditions clear and to control operator precedence.

## Practice Questions
1. Write a condition that checks whether a number is between 10 and 20 (inclusive).
2. Write a condition that checks if a number is negative or even.
3. Write a condition that checks if a string is not empty and starts with the letter 'A'.
4. Rewrite a compound condition using `not` that inverts the result of `(x > 5 and y < 10)`.

We'll continue with loops next class!