from turtle import Turtle

ALIGN = "center"
FONT = ("Verdana",10,"normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(-265,265)
        self.write(f"Score: {self.score}",align=ALIGN,font=FONT)
        self.hideturtle()

    def gameOver(self):
        self.home()
        self.write(f"Game Over",align=ALIGN,font=FONT)
    
    def updateScore(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}",align=ALIGN,font=FONT)