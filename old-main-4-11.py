import turtle

def draw_square(t, side_length):
    t.forward(side_length)
    t.right(90)
    t.forward(side_length)
    t.right(90)
    t.forward(side_length)
    t.right(90)
    t.forward(side_length)
    t.right(90)

def draw_triangle(t, side_length):
    t.forward(side_length)
    t.left(120)
    t.forward(side_length)
    t.left(120)
    t.forward(side_length)
    t.left(120)

def draw_house(t, side_length):
    draw_square(t, side_length)
    draw_triangle(t, side_length)

def main():
    t = turtle.Turtle()
    t.speed(10)
   #  for i in range(10,100,5):
   #      draw_square(t,i)
   # # draw_square(t, 50)
   #  draw_triangle(t, 100)
    draw_house(t, 100)
    turtle.done()

main()