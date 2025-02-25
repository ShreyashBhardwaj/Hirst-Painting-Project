import turtle
from turtle import Turtle, Screen
import random
import colorgram

tim = Turtle()
screen = Screen()

# colors = colorgram.extract("hirst.jpg",25)
#
# rgb_colors=[]
#
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     rgb_colors.append([r,g,b])
#
# print(rgb_colors)
#Ensures that turtle module takes color as integer from 1-255. Normally it is in float
turtle.colormode(255)

# List of dark colors
colors = [
    [150, 30, 30], [20, 80, 20], [30, 30, 150],
    [100, 40, 150], [160, 90, 20], [50, 50, 50],
    [90, 20, 100], [10, 60, 90], [130, 70, 20],
    [80, 0, 0]
]

# Set canvas size and world coordinates
canvas_width = 100
canvas_height = 100
screen.screensize(canvas_width, canvas_height)
screen.setworldcoordinates(-canvas_width/2, -canvas_height/2, canvas_width/2, canvas_height/2)

# Turtle settings
tim.pensize(20)
tim.speed("fastest")

teleport_distance = 10

# Set starting coordinates
x, y = 5 - (canvas_width / 2), 5 - (canvas_height / 2)
tim.teleport(x, y)

# Loop to generate dots
for _ in range(canvas_width + 1):
    color = tuple(random.choice(colors))
    tim.dot(20, color)

    if x > (canvas_width / 2):  # If it reaches the end of the row
        y += teleport_distance  # Move to the next row
        x = -(canvas_width / 2) + 5  # Reset X position

    tim.teleport(x, y)
    x += teleport_distance

screen.exitonclick()