import turtle

i = 10
colors = ['red', 'green', 'blue', 'purple', 'green', 'yellow']

while True:
    turtle.color(colors[i % 6])
    turtle.pensize(i % 10)
    if i % 13:
        turtle.right(i % 48)
    else:
        turtle.left(i % 48)
    turtle.forward(10)
    i += 1
