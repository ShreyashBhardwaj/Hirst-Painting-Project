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
#All the colors extracted from the colorgram module
colors = [
    [150, 30, 30],    # Dark Red
    [20, 80, 20],     # Deep Green
    [30, 30, 150],    # Dark Blue
    [100, 40, 150],   # Dark Purple
    [160, 90, 20],    # Brownish Orange
    [50, 50, 50],     # Dark Gray
    [90, 20, 100],    # Deep Magenta
    [10, 60, 90],     # Dark Teal
    [130, 70, 20],    # Rust
    [80, 0, 0]        # Very Dark Red
]


#Setting Canvas_width and Height
canvas_width=100
canvas_height=100

#Setting Screen size using canvas height and width
screen.screensize(canvas_width,canvas_height)
screen.setworldcoordinates(-canvas_width/2,-canvas_height/2,canvas_width/2,canvas_height/2)

#setting the pensize and speed
tim.speed("fastest")
tim.hideturtle()

#setting the distance for teleport
teleport_distance=10


#setting the start coordinates -45 -45
x,y=5-(canvas_width/2),5-(canvas_height/2)

#Teleporting to the starting coordinates
tim.teleport(x,y)

#The loop that will create Hirst Painting
for _ in range(canvas_width+1):
    color=tuple(random.choice(colors))
    tim.dot(20,color)

    if x > (canvas_width/2):
        y += teleport_distance
        x = 5-(canvas_width/2)

    tim.teleport(x,y)
    x+=teleport_distance

screen.exitonclick()