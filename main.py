from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

scoreboard=Scoreboard()

screen.tracer(0)

snake=Snake()
food=Food()

screen.listen()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


is_game_on=True
while is_game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    #detecting collision

    if snake.head.distance(food)<15:
        food.refresh()
        scoreboard.score_update()
        snake.extend()

    #detect collision with wall

    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>300 or snake.head.ycor()<-280:
        scoreboard.game_over()
        is_game_on=False

    #detect collision with tail

    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            is_game_on=False
            scoreboard.game_over()
screen.exitonclick()