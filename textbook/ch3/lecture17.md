# CS 161 - March 7, 2025

## Midterm Exam Date Change
I have decided to move the midterm exam date from **March 12th** to **April 2nd** to ensure that you have had more than one quiz before the midterm. If this change interferes with any plans you've already made, please let me know so we can make arrangements.

## Recap: Flow Control and Boolean Expressions
We have been discussing flow control in Python, focusing on `if` statements, `if-else` statements, `if-elif-else` structures, and **nested if statements**.

### Reducing Boolean Comparisons
Previously, we used expressions like:
```python
if gate1_open == True:
```
This is **redundant** because `gate1_open` is already a boolean (`True` or `False`). Instead, we can simplify it:
```python
if gate1_open:
```
This makes the code cleaner and easier to read.

## Randomness in Computing
One way to make programs more interesting is by incorporating **randomness**. However, computers are **deterministic**, meaning they follow predictable cause-effect relationships. This contradicts the concept of randomness, where the outcome is uncertain.

To simulate randomness, computers use **pseudo-random number generators (PRNGs)**, which apply mathematical transformations to an initial **seed** value.

### Example: Generating Random Numbers in Python
Python provides the `random` module for generating pseudo-random numbers:
```python
import random
print(random.randint(0, 100))  # Random integer between 0 and 100 (inclusive)
```
This outputs a different number each time the script runs.

### The Issue with Randomness
- If you **provide the same seed**, you get the **same sequence of random numbers**.
- Some systems use the **Unix Epoch (January 1, 1970, in milliseconds)** as the seed to ensure randomness.

## Example: Simple Addition Quiz
We will write a program that generates two random numbers, asks the user for the sum, and evaluates whether their answer is correct.

### Steps:
1. **Generate two random numbers**.
2. **Ask the user for the result**.
3. **Determine if the answer is correct**.
4. **Report the result**.

### Code Implementation:
```python
import random

# Step 1: Generate two random numbers
num1 = random.randint(0, 9)
num2 = random.randint(0, 9)

# Step 2: Ask the user for the answer
answer = int(input(f"What is {num1} + {num2}? "))

# Step 3: Determine if the answer is correct
correct_answer = num1 + num2

# Step 4: Report result
if answer == correct_answer:
    print("That is correct!")
else:
    print(f"Incorrect. The correct answer is {correct_answer}.")
```

## Random Floating-Point Numbers
To generate a random floating-point number between **0 and 1**, use:
```python
import random
print(random.random())
```
This generates a number in the range `[0,1)`, meaning it includes `0` but **excludes** `1`.

### The Mersenne Twister Algorithm
Python's `random` module uses the **Mersenne Twister**, a widely-used PRNG with **53-bit precision**.

## True Randomness: Quantum Mechanics
Most real-world processes are **deterministic**, except **quantum mechanics**. The decay of **radioactive particles** is one of the only truly random events in nature. Some advanced computers use **radiation sensors** to generate **truly** random numbers.

## Next Class
- We will continue discussing **if-elif-else** statements.
- We will begin learning about **loops**.

### Office Hours
- Today at **3:00 PM** (in the basement, with all the radon!).

