
import math

# Task1
import turtle
window = turtle.Screen()
window.setup(500, 500)
t = turtle.Turtle()
t.seth(0)
t.color("#9409af")
t.speed(0)
t.pendown()

#            shapes
# square
# for i in range(4):
#     t.forward(100)
#     t.right(90)

# triangle
# for i in range(3):
#     t.forward(100)
#     t.left(120)

# hexagon
# for i in range(6):
#     t.forward(100)
#     t.left(60)

# circle
# for i in range(360):
#     t.forward(3)
#     t.left(1)

#            spirographs1
# square
# for i in range(36):
#     for i in range(4):
#         t.forward(100)
#         t.right(90)
#     t.right(10)

# star
# for j in range(72):
#     for i in range(5):
#         t.forward(100)
#         t.right(144)
#     t.right(5)

#            spirographs2
# hexagon
colours = ["#fc0505", "#fc8d05", "#fcfc05", "#70fc05", "#04942d", "#00ffea", "#0011ff", "#9409af", "#ff00f2", "#ff0099"]
length = 3
for i in range(30):
    for colour in colours:
        t.color(colour)
        t.forward(length)
        t.right(61)
        length += 2
turtle.done()