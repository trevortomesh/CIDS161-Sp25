**CS 161 — April 9, 2025 Lecture Summary: Functions, Turtle Graphics, and Modular Code**

---

### Summary:
In this highly interactive lecture, we deepened our understanding of **functions**, explored **modular programming** using **custom functions**, and introduced a fun **graphical Python module** called `turtle`. We used `turtle` to draw shapes like squares and triangles, and then abstracted that behavior into reusable functions. Finally, we composed these functions to draw more complex shapes, like houses, and looped them to create visual patterns.

---

### Key Concepts:

#### 1. **Course Logistics**
- The last in-person class is April 23. After that, class will move online via Zoom.
- April 25 class might be asynchronous due to the instructor's family medical situation.
- Zoom links will be posted on Canvas.

#### 2. **Function Review**
- Functions are **reusable blocks of code**.
- Help avoid repetition ("Don't Repeat Yourself" - DRY principle).
- Allow for modularity and cleaner, shorter code.
- Python functions are defined using the `def` keyword.

#### 3. **Python Modules**
- Modules are files that contain reusable code (usually functions).
- You can **import built-in modules** (e.g. `turtle`) or **custom modules**.

```python
import turtle  # Brings in turtle graphics module
```

#### 4. **Turtle Graphics Introduction**
- A turtle is a graphical cursor that moves on a canvas.
- It can draw by moving and turning.
- Useful turtle commands:
```python
import turtle

t = turtle.Turtle()
t.forward(100)     # move forward by 100 units
t.right(90)        # turn right by 90 degrees
turtle.done()      # keeps the window open
```

#### 5. **Creating a Square with Turtle**
To draw a square:
```python
def draw_square(t, side_length):
    for _ in range(4):
        t.forward(side_length)
        t.right(90)
```

Call it in your `main` function:
```python
def main():
    t = turtle.Turtle()
    draw_square(t, 100)
    turtle.done()
```

#### 6. **Looping to Draw Patterns**
We used a `for` loop to draw multiple squares of increasing size:
```python
for i in range(10, 100, 5):
    draw_square(t, i)
```
This creates a spiral or fractal-like visual.

#### 7. **Drawing Triangles and Houses**
We extended our logic to:
- Draw an equilateral triangle (three sides, 120-degree turns):
```python
def draw_triangle(t, side_length):
    for _ in range(3):
        t.forward(side_length)
        t.left(120)
```

- Compose a house using the two shape functions:
```python
def draw_house(t, side_length):
    draw_square(t, side_length)
    draw_triangle(t, side_length)
```

#### 8. **Parameterization and Function Design**
- Functions like `draw_house(t, side_length)` demonstrate parameter passing.
- Functions can be combined and reused inside one another.
- Promotes cleaner, modular, readable code.

#### 9. **Speeding up the Turtle**
```python
t.speed(10)  # Speed range: 0 (fastest) to 10
```
This allows animations to render faster when drawing many shapes.

#### 10. **Visual Debugging**
- We used step-by-step experimentation to diagnose and fix turtle orientation and shape positioning.
- This is a form of **visual debugging**, crucial in graphics programming.

---

### Takeaways:
- Functions are powerful tools for organizing and reusing code.
- You can pass arguments into functions, return values, or simply perform tasks.
- Graphical modules like `turtle` make abstract programming concepts tangible.
- Modular design helps separate logic, enabling cleaner and more flexible code.
- Combining loops and functions can yield surprisingly complex and beautiful patterns.

---

### Practice Challenges:
1. Write a function `draw_star(t, size)` that draws a 5-pointed star.
2. Use a loop to draw 10 houses in a row with increasing sizes.
3. Modify `draw_house` to draw a door in the center of the square.
4. Experiment with `t.goto(x, y)` to draw houses in different screen locations.
5. Create a colorful neighborhood using `t.color()` to change fill and outline colors.

---

**Next Topic: Variable Scope and Lifetime**
On Friday, we will revisit the idea of variable visibility (scope), especially how variables behave **inside** and **outside** of functions. We'll answer: *Which `a` gets printed?*

