from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

canvas = Screen()
canvas.setup(width=600, height=600)
canvas.bgcolor("black")
canvas.title("Snake Game")
canvas.tracer(0)

snake = Snake()
food = Food()
score = Score()

canvas.listen()
canvas.onkey(snake.up, "Up")
canvas.onkey(snake.down, "Down")
canvas.onkey(snake.left, "Left")
canvas.onkey(snake.right, "Right")

isGameOn = True
while isGameOn:
    canvas.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        score.updateScore()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    
    for tail in snake.tails[1:]:
        if snake.head.distance(tail) < 10:
            score.reset()
            snake.reset()

canvas.exitonclick()