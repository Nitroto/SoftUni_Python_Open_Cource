import turtle

while True:
    angle = input("Enter an angle: ")
    length = input("Enter a length: ")
    direction = input("Enter direction left/right: ")

    if direction == 'left':
        turtle.left(int(angle))
    else:
        turtle.right(int(angle))
    turtle.forward(int(length))
