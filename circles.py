import turtle

def draw_circle(turtle, color, size, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(size)
    turtle.end_fill()

tommy = turtle.Turtle()
tommy.shape("turtle")
tommy.speed(10)

draw_circle(tommy, "green", 50, 25, 0)
draw_circle(tommy, "white", 50, 0, 0)
draw_circle(tommy, "orange", 50, -25, 0)

tommy.penup()
tommy.goto(0,-50)
tommy.color('black')
tommy.write("HELLO WORLD!", align="center", font=(None, 16, "italic"))
tommy.goto(0,-80)
tommy.write("Hii Everyone", align="center", font=(None, 16, "italic"))
tommy.goto(0,-110)
