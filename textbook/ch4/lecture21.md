**Living Textbook Entry: Loops and Nested Loops (CS 161 - March 24, 2025)**

---

### Summary
In this lecture, we continued our exploration of loops in Python, focusing on `while` loops and `for` loops. We reviewed key concepts like loop control using Boolean expressions, sentinel values, user confirmation, and introduced nested loops. We reinforced the importance of indentation and consistent whitespace in Python, discussed practical loop structures (like summing user inputs and counting down), and drew analogies between loops and real-world cycles like clocks and calendars.

---

### Topics Covered

#### 1. **Administrative Notes**
- Midterm Exam: April 2 (Scantron, in-person, no notes or computers)
- Quiz due: March 28
- PDF generator bug reported for assignments; fix in progress
- Office Hours: M/F 3-5 PM, no appointment needed

#### 2. **Recap: Boolean Expressions and Loops**
- Boolean expression: evaluates to `True` or `False`
- Loops continue as long as the condition is `True`

Example:
```python
while data != 0:
    # loop body
```

#### 3. **Sentinel-Controlled Loops**
Loops that watch for a special value (e.g., 0) to terminate:
```python
sum = 0

# Get first input
data = eval(input("Enter an integer (0 to end): "))

while data != 0:
    sum += data
    data = eval(input("Enter an integer (0 to end): "))

print("The sum is", sum)
```

#### 4. **User Confirmation Loops**
Loops that continue based on user input:
```python
continue_loop = "Y"

while continue_loop == "Y" or continue_loop == "y":
    continue_loop = input("Would you like to continue? (Y/N): ")
```

#### 5. **Loop Structure & Indentation in Python**
- Python uses indentation to determine block structure
- All loop body statements must be indented equally
- Avoid mixing tabs and spaces

#### 6. **While Loop vs For Loop**
`while` loops are good when the number of iterations is not known in advance.
`for` loops are better when the number of iterations is known.

```python
# while loop
count = 0
while count <= 100:
    print(count)
    count += 1

# for loop
for i in range(101):
    print(i)
```

The `range(start, stop, step)` function is commonly used with `for` loops:
```python
for i in range(0, 100, 2):
    print(i)  # prints even numbers from 0 to 98
```

#### 7. **Counting Down with For Loops**
```python
for i in range(100, -1, -1):
    print(i)  # counts from 100 to 0
```

#### 8. **Grammatically Correct Beer Song (Conditionals in Loops)**
Using `if/else` inside a loop:
```python
for beers in range(99, 0, -1):
    if beers == 1:
        print("1 bottle of beer on the wall...")
    else:
        print(f"{beers} bottles of beer on the wall...")
```

#### 9. **Nested Loops**
Loops inside other loops, like a clock:
```python
for hour in range(24):
    for minute in range(60):
        print(f"{hour}:{minute:02}")
```

Nested `while` loops example:
```python
outer = 0
while outer < 5:
    inner = 0
    while inner < 3:
        print(inner)
        inner += 1
    outer += 1
```
This prints 0, 1, 2 five times.

#### 10. **Analogy: Time as a Nested Loop**
- 60 seconds → 1 minute
- 60 minutes → 1 hour
- 24 hours → 1 day
- Months, years, etc.

This structure is similar to how loops operate within each other.

---

### Key Takeaways
- Loops let computers repeat tasks without boredom or error.
- `while` loops are great for indefinite repetition.
- `for` loops are ideal for controlled, finite iteration.
- Use sentinel values and user confirmation to control loop exit.
- Understand indentation and block scoping in Python.
- Nested loops are powerful but must be used with care.
- Real-world processes like clocks mirror nested loop behavior.

---

### Optional Exercises
1. Write a `while` loop that keeps asking the user for numbers and adds them until they enter `-1`.
2. Modify the beer song to go from 10 bottles down to 0.
3. Use a nested loop to print every hour and minute in a day.
4. Create a guessing game where the computer picks a number between 1 and 50.
5. Refactor a `while` loop into a `for` loop that prints the numbers from 1 to 10.

---