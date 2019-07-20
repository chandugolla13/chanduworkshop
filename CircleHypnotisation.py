import turtle
wn = turtle.Screen()
wn.bgcolor("green")
tess = turtle.Turtle()
tess.color("sky blue")
tess.shape("turtle")

print(list(range(5, 900, 2)))
tess.up()# this is new
for size in range(5, 900, 2):    # start with size = 5 and grow by 2
    tess.stamp()                # leave an impression on the canvas
    tess.backward(size)          # move tess along
    tess.right(40)              # and turn her

wn.exitonclick()
