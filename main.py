from turtle import Turtle, Screen
import random

#manny = Turtle()
screen = Screen()

#higher order function - passing a fucntion as an input for another function


# screen.listen()
# screen.onkey(key="space", fun=move_forwards)



#example of capturing inputs from the keyboard

#
# def move_forwards():
#     manny.forward(10)
#
# def move_backward():
#     manny.backward(10)
#
# def move_left():
#     manny.left(10)
#
# def move_right():
#     manny.right(10)
#
# def move_clear():
#     manny.clear()
#     manny.penup()
#     manny.home()
#     manny.pendown()
#
# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=move_left)
# screen.onkey(key="d", fun=move_right)
# screen.onkey(key="c", fun=move_clear)



#creating multiple states of an object

race = False
screen.setup(width=1000, height=600)
#manny = Turtle("turtle")

colors = ("red", "blue", "green", "orange", "yellow", "purple")

user_guess =screen.textinput(title="Welcome to the Turtle GrandPrix!!!", prompt="Who do you think will win the race?")
speed = [1, 2, 3, 4, 5, 6]
pos = [-250, -200, -150, -100, -50, 0]
my_turtles = []
for obj in range(0, 6):
    manny = Turtle(shape="turtle")
    manny.turtlesize(1.5)
    manny.penup()
    manny.goto(x=-485, y=pos[obj])
    manny.color(colors[obj])
    my_turtles.append(manny)


if user_guess:
    race = True

while user_guess:
    for turtle in my_turtles:
        if turtle.xcor() > 420:
            race = False
            winning_color = turtle.pencolor()
            if winning_color == user_guess:
                print(f"Your turtle with {winning_color} won the race")
            else:
                print("you lost")
        rand_distance = random.randint(0, 15)
        turtle.forward(rand_distance)










screen.exitonclick()