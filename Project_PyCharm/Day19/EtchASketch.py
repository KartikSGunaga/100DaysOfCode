import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()

def forward():
    tim.forward(25)

def backward():
    tim.backward(25)

def left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.home()
    tim.clear()

screen.listen()
screen.onkey(key = 'w', fun = forward)
screen.onkey(key = 's', fun = backward)
screen.onkey(key = 'a', fun = left)
screen.onkey(key = 'd', fun = right)
screen.onkey(key = 'c', fun = clear)













screen.exitonclick()