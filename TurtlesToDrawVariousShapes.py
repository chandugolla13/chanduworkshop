import turtle
tina = turtle.Turtle()
tina.shape('turtle')
tina.penup()

def line(words, horiz_pos = -50):
    x,y = tina.pos()
    tina.goto(max(horiz_pos, -190), y)
    tina.write(words)
    x,y = tina.pos()
    tina.goto(x, y - 25)

def by(author):
    x,y = tina.pos()
    tina.goto(x + 70, max( -190, y -30))
    tina.write(author)
    x,y = tina.pos()
    tina.goto(0, y)

tina.goto(-50, 190)
line("BE THE BEST")
line("NEVER GIVE UP")
line("TRY YOUR BEST")
by("DREAM COMES TRUE")
