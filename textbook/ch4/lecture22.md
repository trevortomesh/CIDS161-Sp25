**CS 161 - Lecture Summary (March 27): Nested Loops, Break and Continue Statements**

---

### Summary:
In today's lecture, we expanded our understanding of loops by diving deeper into **nested loops**, and we introduced two powerful control statements in Python: `break` and `continue`. We used the analogy of a clock to explain nested loops and simulated time in code. We then explored how to exit loops early with `break` and how to skip an iteration with `continue`. We wrapped up with an introduction to prime numbers and a teaser for Friday's lecture, where we will write a program to generate prime numbers.

---

### Topics Covered:

#### 1. **Nested Loops and the Clock Analogy**
- Just like how seconds increment to minutes, and minutes to hours, we can think of nested loops similarly.
- Inner loop runs completely for each iteration of the outer loop.
- Example:
```python
for hours in range(24):
    for minutes in range(60):
        for seconds in range(60):
            print(f"It has been {hours} hours, {minutes} minutes, and {seconds} seconds.")
```
- This simulates a digital clock.

#### 2. **Using `time.sleep()`**
- Introduced to simulate a ticking clock with real-time pauses.
```python
import time
...
time.sleep(1)  # pauses for 1 second between loop iterations
```

#### 3. **Understanding Python's Indentation Rules**
- Python uses indentation to define blocks of code.
- Mixing tabs and spaces can cause errors; consistency is key.
- Nested loops must be properly indented to function correctly.

#### 4. **The `break` Statement**
- Used to exit a loop early.
- Useful for infinite loops or when a certain condition is met.

Example: Stop adding numbers once the sum exceeds 100.
```python
sum = 0
number = 0

while number < 2000:
    number += 1
    sum += number
    if sum >= 100:
        break
    print(f"The number is {number}, the sum is {sum}")
```

#### 5. **The `continue` Statement**
- Skips the current loop iteration and proceeds to the next one.
- Used when a certain condition means skipping processing for that iteration.

Example: Skip adding 10 and 11.
```python
sum = 0
number = 0

while number < 20:
    number += 1
    if number == 10 or number == 11:
        continue
    sum += number
    print(f"The number is {number}, the sum is {sum}")
```

#### 6. **User-Controlled Loop with Input**
- Infinite loop broken with user decision:
```python
while True:
    response = input("Should Mario go again? Y/N: ")
    if response.lower() != 'y':
        break
```

---

### Upcoming: Prime Number Generator
- Friday's lecture will introduce a method to compute the first `n` prime numbers.
- Recap of what a prime number is (only divisible by 1 and itself).
- Teased the unpredictability of prime number distribution and its importance in cryptography.

---

### Optional Exercises:
1. Simulate a clock that prints time in HH:MM:SS format, using nested loops.
2. Write a loop that prints numbers from 1 to 50 but skips all even numbers using `continue`.
3. Create a loop that sums numbers from 1 to 100 but stops if the sum exceeds 300 using `break`.
4. Try mixing a `for` loop nested inside a `while` loop and vice versa.

---

**Fun Fact:** The UNIX epoch starts at January 1, 1970 — all time measurements in most systems are based on seconds since this date.

---

**Next Time:** We'll implement a basic prime number generator using loops and `break`. Don’t miss it!

