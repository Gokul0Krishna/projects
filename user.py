from turtle import Screen
from sanke import Snake
from food import Food
from score_board import Score
import time

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
score=Score()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game=True
while game==True:
    time.sleep(0.1)    
    screen.update()
    snake.Smove()
    if snake.head.distance(food)<15:
        food.move()
        snake.extend()
        score.score()    
    
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
       game=False
       score.game_over()  
        
    for i in snake.list[1::1]:
         if snake.head.distance(i)<10:    
            game=False
            score.game_over()        
        
screen.exitonclick()