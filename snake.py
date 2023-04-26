from turtle import Turtle
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.tails = []
        self.createSnake()
        self.head = self.tails[0]

    def createSnake(self):
        for position in POSITIONS:
            self.createTail(position)
    
    
    def createTail(self,position):
        tail = Turtle("square")
        tail.color("white")
        tail.penup()
        tail.goto(position)
        self.tails.append(tail)

    def reset(self):
        for tail in self.tails:
            tail.goto(1000,1000)

        self.tails.clear()
        self.createSnake()
        self.head = self.tails[0]

    def extend(self):
        self.createTail(self.tails[-1].position())

    def move(self):
        for i in range(len(self.tails) - 1, 0, -1):
            x = self.tails[i - 1].xcor()
            y = self.tails[i - 1].ycor()
            self.tails[i].goto(x, y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
