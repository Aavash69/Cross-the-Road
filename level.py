from turtle import Turtle

class DisplayLevel(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()

    def display(self):
        self.goto(x=-280, y=260)
        self.clear()
        self.write(f"Level: {self.level}",font=('Courier', 18, 'bold'))

    def increase_level(self):
        self.level += 1

    def game_is_over(self):
        self.goto(x=-50,y=0)
        self.write(f"Game Over!", font=('Courier', 18, 'bold'))

