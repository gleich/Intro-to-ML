import turtle
import random

colors = ["red", "green", "blue", "yellow", "black", "purple", "orange"]

radius = 100
while True:
    radius -= 3
    random_num = random.randint(0, 6)
    turtle.speed(100)
    turtle.color(colors[random_num])
    turtle.circle(radius)

