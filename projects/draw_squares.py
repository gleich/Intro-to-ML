from random import randint
import turtle


def draw_square(side_length, angle, color):
    """
    Draws a square using turtle
    :param side_length: the side lengths for the square
    :param angle: the angle of rotation for the square
    :param color: the color of the lines (RGB values)
    :return: none
    """
    for i in range(4):
        turtle.speed(100)
        turtle.colormode(255)
        turtle.color(color[0], color[1], color[2])
        turtle.forward(side_length)
        turtle.right(angle)

turtle.hideturtle()
turtle.bgcolor("black")
sl = 0.5
angle = 90
times = 0
colors = {"red": 0, "green": 0, "blue": 0}
while True:
    times += 1
    if times < 255:
        colors["red"] += 1
    elif times >= 255 * 1 and times < 255 * 2 - 1:
        colors["green"] += 1
    elif times >= 225 * 2 and times < 255 * 3 - 1:
        colors["red"] -= 1
        colors["blue"] += 1
    elif times >= 255 * 3 and times < 255 * 4 - 1:
        colors["red"] += 1
        colors["green"] -= 1
    elif times >= 255 * 4 and times < 255 * 5 - 1:
        colors["red"] -= 1
    elif times > 255 * 5 and times < 255 * 6 - 1:
        colors["blue"] -= 1
    else:
        times = 0

    sl += 0.5
    draw_square(sl, angle, [colors["red"], colors["green"], colors["blue"]])
    turtle.right(1)

