import time
from turtle import Turtle,Screen
from player import Player
from car import Car
from scoreboard import Scoreboard

player=Player()
screen=Screen()
car=Car()
scoreboard=Scoreboard()

screen.setup(600,600)
screen.tracer(0)
screen.bgcolor("black")


screen.listen()
screen.onkey(player.go_up,"u")
screen.onkey(player.go_down,"j")
screen.onkey(player.go_left,"h")
screen.onkey(player.go_right,"k")

game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_car()

    for cars in car.car_list:
        if cars.distance(player) < 20:
            scoreboard.game_over()
            game_is_on=False


    if player.is_at_finish_line():
        player.go_to_start()
        car.level_up()
        scoreboard.increase_level()






screen.exitonclick()