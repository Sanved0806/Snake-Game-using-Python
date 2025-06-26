from turtle import Turtle

class Scoreboard:

    def __init__(self):
        self.score=0
        self.score_turtle=Turtle()
        self.score_turtle.hideturtle()
        self.score_turtle.penup()
        self.score_turtle.color("white")
        self.score_turtle.goto(0,275)
        self.write_score()

    def score_update(self):
        self.score+=1
        self.write_score()

    def write_score(self):
        self.score_turtle.clear()
        self.score_turtle.write(f"Score :{self.score}",align="center", font=("Arial", 16, "bold"))
    def game_over(self):
        self.score_turtle.goto(0,0)
        self.score_turtle.write("GAME OVER",align="center", font=("Arial",20,"bold"))



