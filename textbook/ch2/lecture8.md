**CS 161 - February 12, 2025**

### Using Python as a Calculator and Basic Operations

#### Office Hours Reminder
- Monday & Friday, 3-5 PM, in the basement
- Additional meeting times available upon request

### Review of Previous Topics
- Inputting information from the user
- Converting strings to numbers using `eval()`
- Running Python programs and debugging output

#### Example: Converting Fahrenheit to Celsius
```python
fahrenheit = eval(input("Enter degrees Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print("Temperature in Celsius:", celsius)
```
- `input()` gathers user input as a string
- `eval()` converts the string into a number
- Computation follows the formula for temperature conversion

### Evaluating Mathematical Expressions with `eval()`
#### Example:
```python
expression = input("Enter a mathematical expression (e.g., 2+2): ")
result = eval(expression)
print("Result:", result)
```
- Allows users to enter an operation in string format
- Evaluates and computes the result dynamically

### Calculating the Area of a Circle
#### Steps:
1. Prompt the user for the radius
2. Compute the area using the formula: `π * r^2`
3. Display the result

#### Example Code:
```python
radius = eval(input("Enter a value for radius: "))
area = radius * radius * 3.14159  # Approximation of π
print("The area for the circle of radius", radius, "is", area)
```
- Demonstrates structured problem-solving: input → computation → output
- Introduces the importance of breaking problems into steps

### Computing an Average
#### Steps:
1. Prompt the user for three numbers
2. Compute the average
3. Print the result

#### Example Code:
```python
num1 = eval(input("Enter the first number: "))
num2 = eval(input("Enter the second number: "))
num3 = eval(input("Enter the third number: "))

average = (num1 + num2 + num3) / 3
print("The average of", num1, num2, num3, "is", average)
```
- Discussed the importance of clear variable names
- Mentioned best practices in formatting and spacing for readability

### Python Variable Naming Conventions
- Use descriptive names: `radius`, `num1`, `average`
- Avoid starting variable names with numbers (`3dogs` is invalid)
- **CamelCase** (e.g., `numberOfCookies`) vs. **snake_case** (`number_of_cookies`)
- Python standard favors **snake_case**

### Introduction of Course Chat Feature
- Available in Canvas
- Enables students to ask questions discreetly
- Will be monitored during lectures for real-time interaction

### Future Topics
- Using loops to handle an arbitrary number of inputs
- Introduction to functions for reusable code
- More advanced string formatting (`f-strings`)

# Practice Problems: Using Python as a Calculator and Basic Operations

## Section 1: Basic Arithmetic Operations

1. Write a Python expression to add 15 and 27.
2. Subtract 34 from 92 using Python.
3. Multiply 8 by 13 and print the result.
4. Divide 144 by 12 and store the result in a variable. Print the variable.
5. What happens if you divide 10 by 3? Try it in Python.
6. Calculate the result of the following expression in Python: `(20 + 5) * 3`

## Section 2: Using `eval()` for Expressions

1. Use `eval()` to compute the result of the user-inputted expression: `"5 + 10 - 2"`.
2. Modify the previous program so the user can enter their own expression.
3. What happens if the user enters a string instead of a mathematical expression? Try it and note the error message.
4. Use `eval()` to evaluate the following input: `"(30 - 5) / 5"`.

## Section 3: Problem Solving with Arithmetic

1. A store is offering a 20% discount on an item that costs $50. Write a Python expression to calculate the final price.
2. If you buy 3 apples for $0.75 each, how much will the total cost be? Write a Python expression.
3. You drive 150 miles using 5 gallons of gas. Write an expression to compute your miles per gallon (MPG).
4. If a rectangle has a width of 7 units and a height of 12 units, write a Python expression to compute its area.
5. A person runs 5 miles in 40 minutes. Write an expression to compute their speed in miles per minute.

Try writing the solutions for each of these problems in Python, and test them in an interpreter! 🚀



**End of Lecture**

