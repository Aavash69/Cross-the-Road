from turtle import Screen
from create_turtle import OurTurtle
from car_manager import CarManager
from level import DisplayLevel
import time
import random

screen = Screen()
screen.bgcolor('white')
screen.setup(width=600, height=600)
screen.tracer(0)
tim = OurTurtle()
cars = CarManager()
game_is_on = True
level = DisplayLevel()


def increase_level():
    cars.increase_speed()
    tim.goto(x=0, y=-280)


cars.create_cars(random.randint(0,10))
while game_is_on:
    screen.update()
    time.sleep(0.1)

    create_cars = True
    level.display()
    for car in cars.cars:
        if tim.distance(car) < 18:
            level.game_is_over()
            game_is_on = False



        if car.xcor() > 225:
            create_cars = False
    if create_cars == True:
        cars.create_cars(random.randint(0, 3))

    cars.move_cars()

    screen.listen()
    screen.onkey(tim.up, key="Up")
    screen.onkey(tim.down,key="Down")
    screen.onkey(tim.turn_right,key="Right")
    screen.onkey(tim.turn_left,key="Left")

    if tim.ycor() == 300:
        increase_level()
        level.increase_level()
        level.display()























screen.exitonclick()
