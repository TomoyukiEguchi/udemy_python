from turtle import Turtle, Screen
import random
import turtle

# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")

timmy = Turtle()
screen = Screen()
timmy.shape("turtle")
turtle.colormode(255)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def isInScreen(w, t):
    leftBound = - w.window_width() / 2
    rightBound = w.window_width() / 2
    topBound = w.window_height() / 2
    bottomBound = -w.window_height() / 2

    turtleX = t.xcor()
    turtleY = t.ycor()

    stillIn = True
    if turtleX > rightBound or turtleX < leftBound:
        stillIn = False
    if turtleY > topBound or turtleY < bottomBound:
        stillIn = False

    return stillIn


# colors = ["cyan", "pale green", "yellow", "orange red", "magenta", "medium purple", "dark salmon", "navajo white"]
directions = [0, 90, 180, 270]
timmy.pensize(10)

while isInScreen(screen, timmy):
    # coin = random.randrange(0, 2)
    # if coin == 0:
    #     timmy.left(90)
    # else:
    #     timmy.right(90)

    timmy.setheading(random.choice(directions))
    timmy.color(random_color())
    timmy.speed("slow")
    timmy.forward(50)

screen.exitonclick()

# colors = ["cyan", "pale green", "yellow", "orange red", "magenta", "medium purple", "dark salmon", "navajo white"]
#
#
# def draw_shape(num_sides):
#     for i in range(num_sides):
#         angle = 360 / num_sides
#         timmy.forward(100)
#         timmy.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     timmy.color(random.choice(colors))
#     draw_shape(shape_side_n)

# for i in range(10):
#     timmy_the_turtle.forward(15)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(15)
#     timmy_the_turtle.pendown()

# for _ in range(4):
#     timmy_the_turtle.right(90)
#     timmy_the_turtle.forward(100)


