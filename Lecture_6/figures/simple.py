import math

from .base import Figure


class Circle(Figure):
    def __init__(self, radius, **kwargs):
        super().__init__(**kwargs)
        self.radius = radius

    def draw(self, turtle):
        turtle.penup()
        turtle.goto(self.center_x,
                    self.center_y - self.radius)  # From docs: The center is radius units left of the turtle;
        turtle.pendown()
        turtle.color(self.color)
        turtle.circle(self.radius)


class Square(Figure):
    def __init__(self, side, **kwargs):
        super().__init__(**kwargs)
        self.side = side

    def draw(self, turtle):
        half_side = self.side / 2
        left = self.center_x - half_side
        top = self.center_y + half_side

        turtle.penup()
        turtle.goto(left, top)
        turtle.pendown()
        turtle.color(self.color)
        turtle.forward(1)
        turtle.setheading(270)  # point the turtle down
        for _ in range(4):
            turtle.forward(self.side)
            turtle.left(90)


class Rectangle(Figure):
    def __init__(self, width, height, **kwargs):
        super().__init__(**kwargs)
        self.width = width
        self.height = height

    def draw(self, turtle):
        half_width = self.width / 2
        half_height = self.height / 2
        left = self.center_x - half_width
        top = self.center_y + half_height
        turtle.color(self.color)
        turtle.penup()
        turtle.goto(left, top)
        turtle.pendown()
        turtle.forward(1)
        turtle.setheading(270)  # point the turtle down

        for _ in range(2):
            turtle.forward(self.height)
            turtle.left(90)
            turtle.forward(self.width)
            turtle.left(90)


class Pie(Figure):
    def __init__(self, radius, arg_derees, **kwargs):
        super().__init__(**kwargs)
        self.radius = radius
        self.arg_degrees = arg_derees

    def draw(self, turtle):
        turtle.penup()
        turtle.goto(self.center_x, self.center_y - self.radius)
        turtle.pendown()
        turtle.begin_fill()
        turtle.color(self.color)
        turtle.circle(self.radius, self.arg_degrees)
        turtle.left(self.arg_degrees)
        turtle.forward(self.radius)
        turtle.setheading(270)
        turtle.forward(self.radius)
        turtle.end_fill()


class Polygon(Figure):
    def __init__(self, radius, num_sides, **kwargs):
        super().__init__(**kwargs)
        self.radius = radius
        self.num_sides = num_sides

    def draw(self, turtle):
        _apothem = self.radius * math.cos(math.pi / self.num_sides)
        _side = 2 * _apothem * math.tan(math.pi / self.num_sides)
        _exterior_angle = (360 / self.num_sides)
        turtle.speed('slowest')
        turtle.penup()
        turtle.goto(self.center_x - _side / 2, self.center_y - _apothem)
        turtle.pendown()
        turtle.color(self.color)
        for i in range(self.num_sides):
            turtle.forward(_side)
            turtle.left(_exterior_angle)
