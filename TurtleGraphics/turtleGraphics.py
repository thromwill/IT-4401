#turtleGraphics

import turtle

turtle = turtle.Turtle()
turtle.getscreen().bgcolor("black")

turtle.color("white")

def draw(turtle, size):
    if size <= 50:
        return
    else:
        for i in range(50):
            turtle.forward(size)
            draw(turtle, size/2)
            turtle.left(75)
            
            
draw(turtle, 100)

