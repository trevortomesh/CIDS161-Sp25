**CS 161 Lecture Summary: April 11, 2025**

### Topics Covered
- Turtle Graphics (Continued)
- Global vs Local Variables (Scope)
- `if __name__ == "__main__"` Pattern in Python

---

### 1. **Why Turtles?**
- Turtle graphics originate from the 1967 LOGO programming language.
- The cursor was designed as a turtle to make programming more tangible for learners, especially children.
- It allowed learners to visualize geometry and movement by controlling a robot turtle that left a trail.

---

### 2. **Python Turtle Recap**
- A turtle can be given a name, a shape (e.g., `turtle`), a color, and a speed.
- Turtle commands include `.penup()`, `.pendown()`, `.goto(x, y)`, `.forward()`, `.right()`, and `.write()`.

Example setup:
```python
import turtle

def main():
    screen = turtle.Screen()
    screen.title("Turtles are fun")
    screen.bgcolor("lightblue")

    leo = turtle.Turtle()
    leo.shape("turtle")
    leo.speed(1)

    turtle.done()

if __name__ == "__main__":
    main()
```

---

### 3. **Global vs Local Scope**

#### Global Variables
- Declared outside any function and accessible anywhere in the program.
```python
color = "red"
```

#### Local Variables
- Declared within a function and only accessible within that function.
```python
def draw_with_local_color(t):
    color = "green"  # This shadows the global 'color'
    t.color(color)
```

#### Key Takeaways
- Local variables shadow global variables with the same name.
- Global variables are discouraged in most cases due to the risk of unintended side effects.
- Use unique names for local variables to avoid confusion and shadowing warnings.

#### Example of Variable Scope Crash:
```python
def draw_with_undefined_color(t):
    t.color(undefined_color)  # This will crash since 'undefined_color' is not defined
```

---

### 4. **Using `if __name__ == "__main__"`**

This construct ensures the code only runs when the file is executed directly and not when imported.
```python
if __name__ == "__main__":
    main()
```
Why it matters:
- Prevents functions from auto-running if imported into another module.
- Keeps code modular and professional.

---

### 5. **Example: Drawing With Turtle & Scoped Variables**
```python
def draw_with_global_color(t):
    t.penup()
    t.goto(-100, 100)
    t.pendown()
    t.color(color)  # Uses global variable
    for _ in range(4):
        t.forward(50)
        t.right(90)
```
```python
def draw_with_local_color(t):
    color = "green"  # Local scope
    t.penup()
    t.goto(100, 100)
    t.pendown()
    t.color(color)
    for _ in range(4):
        t.forward(50)
        t.right(90)
```
```python
def draw_with_new_local_color(t):
    new_color = "blue"
    t.penup()
    t.goto(-50, 0)
    t.pendown()
    t.color(new_color)
    for _ in range(3):
        t.forward(60)
        t.right(120)
```

---

### 6. **Final Concepts**
- Global variables persist through the whole program but can be shadowed.
- Local variables are function-scoped and safer to use.
- Undefined variables not in any scope will crash the program.
- The `if __name__ == "__main__"` pattern prevents unwanted execution during import.

---

### Practice Suggestions
1. Try writing a function that draws a pentagon using local color variables.
2. Modify your turtle to draw a scene with multiple colored shapes using both global and local variables.
3. Refactor your existing turtle projects to use the `if __name__ == "__main__"` guard.

---

Next Class: We return to text-based programming with input/output and continue exploring functions and modularity.

