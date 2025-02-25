# Hirst Painting Generator using Python Turtle

This Python script generates a **Hirst-style painting** using the `turtle` module. It creates a **grid of randomly colored dots**, using **dark colors** to maintain a rich, deep aesthetic.

## Features
- Uses `turtle.teleport()` for **instant movement** without drawing unnecessary lines.
- Generates a **grid of dots** across the screen.
- Randomly selects colors from a predefined list of **dark shades**.
- Automatically adjusts to the **canvas size and world coordinates**.

## Requirements
- Python 3.12
- `turtle` (included by default in Python)
- `random` (included by default in Python)

## How It Works
1. **Sets up the screen and canvas** with a coordinate system.
2. **Positions the turtle at the starting location**.
3. **Loops through and places dots** at fixed intervals.
4. **Uses teleportation instead of drawing lines** for quick movement.
5. **Waits for a click to exit** the screen.

## Code Explanation
```python
import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()

# Enable RGB color mode
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
```

## How to Run the Script
1. Copy the code into a Python file (e.g., `hirst_painting.py`).
2. Run the script using Python:
   ```sh
   python hirst_painting.py
   ```
3. A window will open, and the turtle will generate the painting.
4. Click anywhere on the screen to exit.

## Customization
- **Change dot size:** Modify `tim.dot(20, color)` to a different value.
- **Change grid spacing:** Adjust `teleport_distance`.
- **Add more colors:** Expand the `colors` list with new RGB values.
- **Increase canvas size:** Modify `canvas_width` and `canvas_height`.

## Author
This script was my **first attempt** at creating a Hirst-style painting using Python. 😃

## License
Feel free to modify and use it however you like!

