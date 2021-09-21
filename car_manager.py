COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

import random
from turtle import Turtle


class CarManager():
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_cars(self, number_of_cars):

        for a in range(number_of_cars):
            new_car = Turtle()
            new_car.penup()
            new_car.shape('square')
            new_car.shapesize(stretch_len=2)
            new_car.color(COLORS[random.randint(0,4)])
            new_car.goto(y=random.randint(-250,280), x=300)
            new_car.setheading(180)
            self.cars.append(new_car)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT

    def move_cars(self):
        for car in self.cars:
            car.forward(self.speed)


