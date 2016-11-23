import turtle

turtle.speed('slowest')

colors = ['red', 'green', 'blue', 'purple']

for a in range(4):
    turtle.color(colors[a])
    turtle.forward(100)
    turtle.left(90)
