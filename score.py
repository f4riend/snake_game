from turtle import Turtle

ALIGN = "center"
FONT = ("Verdana",10,"normal")
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt","r") as file:
            self.highScore = int(file.read())
        self.color("white")
        self.penup()
        self.goto(-230,265)
        self.write(f"POINT: {self.score}  MAX: {self.highScore}",align=ALIGN,font=FONT)
        self.hideturtle()

    def reset(self):
        if self.score > self.highScore:
            self.highScore = self.score
            with open("data.txt","w") as file:
                file.write(f"{self.highScore}")
        self.score = 0
        self.updateScore()
    
    def updateScore(self):
        self.score += 1
        self.clear()
        self.write(f"POINT: {self.score}  MAX: {self.highScore}",align=ALIGN,font=FONT)