import turtle
import random
from turtle import Screen

vibrant_colors = [
    "red", "orange", "orangered", "gold", "yellow",
    "lime", "limegreen", "springgreen", "cyan", "deepskyblue",
    "blue", "dodgerblue", "magenta", "fuchsia", "hotpink",
    "mediumvioletred", "violet", "purple", "turquoise", "chartreuse"
]

Random_angles = [90,180,270]

tutle1 = turtle.Turtle()
tutle1.speed(1)
tutle1.shape("turtle")
tutle1.color("green")
tutle1.penup()
tutle1.goto(-250,100)
tutle1.pendown()

tutle2 = turtle.Turtle()
tutle2.speed(1)
tutle2.shape("turtle")
tutle2.color("red")
tutle2.penup()
tutle2.goto(-250,50)
tutle2.pendown()

tutle3 = turtle.Turtle()
tutle3.speed(1)
tutle3.shape("turtle")
tutle3.color("orange")
tutle3.penup()
tutle3.goto(-250,0)
tutle3.pendown()

tutle4 = turtle.Turtle()
tutle4.speed(1)
tutle4.shape("turtle")
tutle4.color("blue")
tutle4.penup()
tutle4.goto(-250,-50)
tutle4.pendown()

tutle5 = turtle.Turtle()
tutle5.speed(1)
tutle5.shape("turtle")
tutle5.color("lime")
tutle5.penup()
tutle5.goto(-250,-100)
tutle5.pendown()

def RandomSpeed():
    return random.randint(1,100)


def Moveforward():

    speed = random.randint(1,25)
    tutle1.forward(speed)
    speed = random.randint(1, 25)
    tutle2.forward(speed)
    speed = random.randint(1, 25)
    tutle3.forward(speed)
    speed = random.randint(1, 25)
    tutle4.forward(speed)
    speed = random.randint(1, 25)
    tutle5.forward(speed)


for I in range (30):
    Moveforward()
    X_coordinate = tutle1.xcor()
    X_coordinate2 = tutle2.xcor()
    X_coordinate3 = tutle3.xcor()
    X_coordinate4 = tutle4.xcor()
    X_coordinate5 = tutle5.xcor()


    if X_coordinate > 100 or X_coordinate2 > 100 or X_coordinate3 > 100 or X_coordinate4 > 100 or X_coordinate5 > 100 :
        print(f"You won")
        break



My_screen = Screen()
My_screen.listen()




Screen().exitonclick()
