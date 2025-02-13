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

**End of Lecture**

