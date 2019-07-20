import turtle
turtle.bgcolor("green")
turtle.speed(0)
turtle.shape("turtle")

my_turtle = turtle.Turtle()
#funtion definition and aruguments 
def square(length):
    
 my_turtle.backward(length)
 my_turtle.left(90)
 my_turtle.backward(length)
 my_turtle.left(90)
 my_turtle.backward(length)
 my_turtle.left(90)
 my_turtle.backward(length)

#funtion calling (for appearing the input) and looping squares
for i in range (4):
 square(320)
for i in range (4):
 square(300)
for i in range (4):
 square(280)
for i in range (4):
 square(260)
for i in range (4):
 square(240)
for i in range (4):
 square(220)
for i in range (4):
 square(200)
for i in range (4):
 square(180)
for i in range (4):
 square(160)
for i in range (4):
 square(140)
for i in range (4):
 square(120)
for i in range (4):
 square(100)
for i in range (4):
 square(80)
for i in range (4):
 square(60)
for i in range (4):
 square(40)
for i in range (4):
 square(20)
for i in range(4):
 square(5)
