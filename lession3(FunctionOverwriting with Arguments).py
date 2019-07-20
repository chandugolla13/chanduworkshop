import turtle

my_turtle = turtle.Turtle()

#funtion definition and aruguments 
def square(length,angle):
    
 my_turtle.backward(length)
 my_turtle.left(angle)
 my_turtle.backward(length)
 my_turtle.left(angle)
 my_turtle.backward(length)
 my_turtle.left(angle)
 my_turtle.backward(length)

#funtion calling (for appearing the input)                   
square(100,90)
#function overwriting with arguments
square(80,45)
square(80,30)
square(80,30)
square(80,30)
square(80,30)

