import turtle
from GCDFunction import *

color = "red" #global variable

my_num = 10 #global number


def add_nums():
    local_num = 12
    print(my_num + local_num)

def draw_and_define_new_color(t):
    new_color = "blue"

    t.penup()
    t.goto(100, -50)
    t.pendown()
    t.color(new_color)

    for _ in range(3):
        t.forward(60)
        t.right(120)


def draw_with_undefined_color(t):
    t.penup()
    t.goto(100, 100)
    t.pendown()
    t.color(undefined_color)

    for _ in range(4):
        t.forward(50)
        t.right(90)

def draw_with_local_color(t):
    color = "green"
    t.penup()
    t.goto(100, 100)
    t.pendown()
    t.color(color)

    for _ in range(4):
        t.forward(50)
        t.right(90)

def draw_with_global_color(t):
    t.penup()
    t.goto(-100, 100)
    t.pendown()
    t.color(color)

    for _ in range(4):
        t.forward(50)
        t.right(90)

def main():
    print(my_num)
    add_nums()
    screen = turtle.Screen()
    screen.title("Turtles Are Fun!")
    screen.bgcolor("lightblue")

    leo = turtle.Turtle()
    leo.shape("turtle")
    leo.speed(1)

    draw_with_global_color(leo)
    draw_with_local_color(leo)
    #draw_with_undefined_color(leo)
    draw_and_define_new_color(leo)

    leo.penup()
    leo.goto(0, -150)
    leo.pendown()
    leo.color(color)
    leo.write(f"Global color is: {color}", align="center",
              font=("Arial", 24, "italic"))

    turtle.done()

if __name__ == "__main__":
    main()
