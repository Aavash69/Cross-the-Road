from turtle import Turtle


class OurTurtle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.color('green')
        self.goto(x=0, y=-280)
        self.setheading(90)

    def up(self):

        self.forward(20)

    def down(self):

        self.back(20)

    def turn_left(self):
        self.setheading(180)
        self.forward(20)
        self.setheading(90)

    def turn_right(self):
        self.setheading(0)
        self.forward(20)
        self.setheading(90)