import turtle
import random
import time

# -------------------- Setup Screen --------------------
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("🐢 TURBO TURTLE SHOWDOWN 🏁")
screen.setup(width=800, height=600)

# -------------------- Colors --------------------
vibrant_colors = [
    "red", "orange", "orangered", "gold", "yellow",
    "lime", "springgreen", "cyan", "deepskyblue", "dodgerblue",
    "blue", "magenta", "fuchsia", "hotpink", "violet",
    "mediumvioletred", "purple", "turquoise", "chartreuse"
]

# -------------------- Draw Track --------------------

Track = turtle.Turtle()
Track.color("white")
Track.penup()
Track.speed(5)
Track.goto(200,200)
Track.left(270)
Track.pendown()
Track.forward(400)

def Lines():
    Track.penup()
    Track.forward(40)
    Track.pendown()
    Track.forward(40)

def TrackLines():
    X_Cod = 200
    Y_cord = 150
    for I in range(5):
        Track.speed(20)
        Track.penup()
        Track.goto(X_Cod,Y_cord)
        Track.setheading(180)
        for I in range (5):
            Lines()

        Y_cord = Y_cord - 75
turtles = []
def CreatingTurtles():
    y_cord = 180
    x_cord = -200
    for I in range(6):
        t = turtle.Turtle()
        t.shape("turtle")
        t.color("white")
        t.speed(random.randint(0,100))
        t.penup()
        t.goto(x_cord,y_cord)
        t.pendown()
        y_cord = y_cord - 75
        turtles.append(t)



TrackLines()
Track.hideturtle()
CreatingTurtles()

finish_line = 200
positions = []

while len(positions) < 5:
    for t in turtles:
        if t not in positions:
            t.forward(random.randint(1, 15))
            # Change trail color
            #t.pencolor(random.choice(vibrant_colors))
            if t.xcor() > finish_line:
                positions.append(t)
                t.speed(0)
                break




screen.exitonclick()
