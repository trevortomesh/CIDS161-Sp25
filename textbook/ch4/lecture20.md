# Living Textbook Entry: Selections and Loops (CIS 161)

### Summary:
In this unit, we explored the power of **looping and repetition in programming**, particularly using **`while` loops** in Python. We began with a review of **Boolean expressions**, **nested `if` statements**, and **how conditions direct program flow**. We then transitioned into designing programs that automate repetitive tasks through **loop structures**. We also introduced concepts such as **pseudo-random number generation**, **user-controlled loops**, and **sentinel values** for loop termination. Several engaging examples—ranging from classic console games to data summation—were used to illustrate these ideas in practice.

---

### Key Concepts:

#### Boolean Expressions and Flow Control
- Conditional logic drives program execution.
- `if`, `elif`, and `else` statements operate based on Boolean values: `True` or `False`.
- Redundant comparisons like `if gate_open == True:` can be simplified to `if gate_open:`.

#### Introduction to Loops
- Loops allow us to repeat instructions efficiently.
- `while` loops repeat code **as long as a Boolean condition remains true**.
- Common loop structure:
  ```python
  while condition:
      # loop body
  ```

#### Infinite Loops
- `while True:` creates an infinite loop unless explicitly broken with a `break` statement.
- Example: "Are we there yet?" repeated forever.

#### Loop Iteration and Counters
- A **counter variable** tracks how many times a loop has executed:
  ```python
  count = 0
  while count < 100:
      print("Are we there yet?", count)
      count += 1
  ```

#### Pseudo-Random Numbers
- Computers simulate randomness using a **pseudo-random number generator (PRNG)**.
- `random.randint(a, b)` gives a random integer between `a` and `b` (inclusive).
- Seeds (often derived from the system clock) ensure different outcomes on each run.

#### Basic Games with Loops
**Higher or Lower Game:**
1. Computer generates a number using `random.randint(0, 100)`.
2. User guesses a number.
3. Program compares the guess to the target and gives feedback.
4. A loop repeats until the guess is correct.

```python
import random
number = random.randint(0, 100)
guess = -1
while guess != number:
    guess = eval(input("Enter your guess: "))
    if guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")
    else:
        print("Correct!")
```

#### User-Controlled Loops
- Users decide whether to continue a loop:
```python
continue_loop = "Y"
while continue_loop == "Y" or continue_loop == "y":
    # do something
    continue_loop = input("Would you like to continue? Y/N: ")
```

#### Sentinel-Controlled Loops
- A **sentinel value** (like 0) determines when to exit a loop:
```python
sum = 0
data = eval(input("Enter an integer (0 to quit): "))
while data != 0:
    sum += data
    data = eval(input("Enter an integer (0 to quit): "))
print("The sum is", sum)
```

#### Python Built-in Shortcuts
- `sum(range(n))` can be used to calculate the sum of numbers from 0 to `n-1`.
- Avoid hard-coding loops when Python provides built-ins like `sum()` and `range()`.

---

### Practice Exercises:
1. Write a loop that prints "Keep going!" 25 times.
2. Modify the higher/lower guessing game to limit the number of guesses to 5.
3. Create a sentinel-controlled loop that multiplies user input values until 0 is entered.
4. Use a loop to sum even numbers between 1 and 100.
5. Explain the difference between an infinite loop and a sentinel-controlled loop.

---

### Reflection:
This unit emphasizes the power of **automation** and the fundamental importance of control structures. From mundane repetition to interactive games, **loops empower us to build flexible, engaging programs**. As we prepare to move into **functions**, reflect on how loops and conditionals can be used **together** to create rich program behavior.

Next stop: **Functions!**

---

_This lecture summary was created collaboratively through the Living Textbook Initiative._

