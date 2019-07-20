
import turtle

my_turtle = turtle.Turtle()
#defines the speed of turtle
my_turtle.speed(0)
#defines the shape of turtle
my_turtle.shape("turtle")
#defines the color of turtle 
my_turtle.pencolor("red")


#funtion definition and aruguments with circle of squares

def square(length,angle):
 for i in range(4):
  my_turtle.backward(length)
  my_turtle.left(angle)

for i in range(1000):
 square(150,90)

 my_turtle.left(11)
 my_turtle.left(13)
 my_turtle.left(15)
 my_turtle.left(17)
