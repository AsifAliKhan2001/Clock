import time
import turtle
import random

def clockframe():
    # logo mode sets orientation of the turtle for north to be 0 degree rather than east.
    turtle.Screen().mode("logo")  

    # Creating a new object called circle in order for us to point all the construction towards it since "Turtle" is a class.
    circle = turtle.Turtle(visible=False)
    circle.speed(0)
    circle.penup()
    # logo mode in use to set the turtle's first corrdinate to x.
    circle.setx(200)
    circle.pensize(5)
    circle.pendown()
    circle.circle(200)
    circle.penup()
    circle.setposition(0,0)
    circle.setheading(0)
    circle.forward(175)
    # drawing the numbers around the clock frame
    circle.write('12',font=("Arial", 16, "normal"),align='center')
    circle.setposition(0,0)
    circle.setheading(30)
    circle.forward(175)
    circle.write('1',font=("Arial", 16, "normal"),align='center')
    circle.setposition(0,0)
    circle.setheading(60)
    circle.forward(175)
    circle.write('2',font=("Arial", 16, "normal"),align='center')
    circle.setposition(0,0)
    circle.setheading(90)
    circle.forward(190)
    circle.write('3',font=("Arial", 16, "normal"),align='center')
    circle.setposition(0,0)
    circle.setheading(120)
    circle.forward(190)
    circle.write('4',font=("Arial", 16, "normal"),align='center')
    circle.setposition(0,0)
    circle.setheading(150)
    circle.forward(200)
    circle.write('5',font=("Arial", 16, "normal"),align='center')
    circle.setposition(0,0)
    circle.setheading(180)
    circle.forward(200)
    circle.write('6',font=("Arial", 16, "normal"),align='center')
    circle.setposition(0,0)
    circle.setheading(210)
    circle.forward(200)
    circle.write('7',font=("Arial", 16, "normal"),align='center')
    circle.setposition(0,0)
    circle.setheading(240)
    circle.forward(190)
    circle.write('8',font=("Arial", 16, "normal"),align='center')
    circle.setposition(0,0)
    circle.setheading(270)
    circle.forward(190)
    circle.write('9',font=("Arial", 16, "normal"),align='center')
    circle.setposition(0,0)
    circle.setheading(300)
    circle.forward(175)
    circle.write('10',font=("Arial", 16, "normal"),align='center')
    circle.setposition(0,0)
    circle.setheading(330)
    circle.forward(175)
    circle.write('11',font=("Arial", 16, "normal"),align='center')
    
# 2D vector class found in turtle library. Check references.
midpoint = turtle.Vec2D(0,0)

clockframe()
def clockline(cord, head, len, colour1, colour2, colour3):
    turtle.penup()
    turtle.goto(cord)
    turtle.pendown()
    turtle.pensize(3)
    # logo mode does affect this.
    turtle.setheading(head)
    # Colormode at 255 so we can use the RGB colour sequence.
    turtle.Screen().colormode(255)
    turtle.color(colour1, colour2, colour3)
    turtle.forward(len)
    
# Turns off the screen updates of the turtle drawing every second.
turtle.Screen().tracer(False)

def clocktime():
    # Using global in order to use the variable in another function.
    global timeSec
    global timeMin
    global timeHour
    # Formulas to convert time to angles. Check Clock angle problem in references.
    timeSec = time.localtime().tm_sec * 6
    timeMin = time.localtime().tm_min * 6 + timeSec / 60
    timeHour = time.localtime().tm_hour % 12 * 30 + timeMin / 12

    turtle.clear()

def clockdraw():
    # Calling pervious function to figure out the angle needed.
    clocktime()
    # Calling first function once for each clock hand to be drawn.
    clockline(midpoint, timeSec, 150, random.randint(0,255), random.randint(0,255), random.randint(0,255))
    clockline(midpoint, timeMin, 120, random.randint(0,255), random.randint(0,255), random.randint(0,255))
    clockline(midpoint, timeHour, 80, random.randint(0,255), random.randint(0,255), random.randint(0,255))
    # Updating the turtle screen.
    turtle.Screen().update()
    # Timer to recall clockdraw function every 1 second.
    turtle.Screen().ontimer(clockdraw, 1000)

# Intiating function.
clockdraw()
# Loop to keep canvas and clock animation on forever.
turtle.Screen().mainloop()
