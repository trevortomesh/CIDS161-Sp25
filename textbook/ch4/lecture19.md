# CS 161 — March 13, 2025 Lecture Summary: Introduction to Loops and Iteration

## Summary
In this lecture, we introduced the concept of **loops**, particularly the **`while` loop**, and explored how loops allow us to automate repetitive tasks in a program. We also learned about **loop continuation conditions**, **loop bodies**, and **iteration**. The class walked through multiple examples ranging from a simple repeating question to summing numbers and implementing a fun drinking song.

---

## Key Concepts

### Why Loops Matter
- Computers are ideal for repetition — they don’t get bored, distracted, or make copy-paste mistakes like humans.
- Loops allow code to run repeatedly based on a condition (a Boolean expression).

### `while` Loop Syntax
```python
while <condition>:
    <loop body>
```
- The **condition** is a Boolean expression.
- The **loop body** is executed repeatedly *as long as the condition is True*.

### Example 1: Infinite Loop
```python
while True:
    print("Are we there yet?")
```
This loop runs forever unless manually interrupted.

### Example 2: Counting with a Loop
```python
count = 0
while count < 100:
    print("Are we there yet?", count)
    count = count + 1
print("We're there!")
```
- We used a variable `count` to keep track of how many iterations we’ve gone through.

### Loop Continuation Condition
- The condition after `while` that determines whether the loop continues or not.
- If the condition is False, the loop stops.

### Example 3: Summing Numbers from 1 to 99
```python
sum = 0
count = 1
while count < 100:
    sum = sum + count
    count = count + 1
print("Total sum is:", sum)
```
- This accumulates the sum of all numbers from 1 to 99.

### Alternative: Using Built-in `sum()`
```python
total = sum(range(100))
print("Total sum is:", total)
```
- Python’s built-in `sum()` and `range()` functions can replace loops in some cases.

### Example 4: 99 Bottles of Beer Song Generator
```python
beers = 99
while beers > 0:
    print(beers, "bottles of beer on the wall,", beers, "bottles of beer.")
    print("Take one down, pass it around.")
    beers = beers - 1
    print(beers, "bottles of beer on the wall.")
```
- Demonstrates looping in reverse by decrementing `beers` each time.

---

## Vocabulary
- **Iteration**: A single pass through a loop.
- **Loop Continuation Condition**: The Boolean expression that determines if the loop continues.
- **Loop Body**: The indented block of code that runs for each iteration.
- **Infinite Loop**: A loop whose condition never becomes False.

---

## Practice Problems

1. **Basic Loop Practice**
   Write a loop that prints numbers from 1 to 50.

2. **Even Numbers Only**
   Write a loop that prints only even numbers from 0 to 100.

3. **Countdown Loop**
   Write a program that counts down from 10 to 1, then prints "Blastoff!".

4. **Sum of Odd Numbers**
   Write a loop that calculates the sum of all odd numbers between 1 and 99.

5. **User-Controlled Loop**
   Write a program that asks the user repeatedly for input until they type "quit".

```python
user_input = ""
while user_input != "quit":
    user_input = input("Type something (or 'quit' to stop): ")
```

6. **Multiplication Table Generator**
   Ask the user for a number and then print the multiplication table for that number up to 12x.

---

