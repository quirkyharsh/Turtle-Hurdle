from turtle import Turtle
import random
COLOUR=["red","orange","yellow","blue","green","yellow"]
STARTING_MOVE_DISTANCE=5
MOVE_INCREMENT=10

class Car:
    def __init__(self):
        self.car_list = []
        self.car_speed=STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_no = random.randint(1,6)
        if random_no == 6:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLOUR))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.car_list.append(new_car)


    def move_car(self):
        for car in self.car_list:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed+=MOVE_INCREMENT




