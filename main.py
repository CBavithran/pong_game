from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from score_board import Score_board

screen = Screen()
screen.setup(800, 600)
screen.title("PONG GAME")
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((360, 0))
l_paddle = Paddle((-365, 0))



screen.listen() 
screen.onkey(r_paddle.go_up, "Up")  
screen.onkey(r_paddle.go_down, "Down")
    
screen.onkey(l_paddle.go_up, "w")  
screen.onkey(l_paddle.go_down, "s")

ball = Ball()
score = Score_board()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320 :
        ball.bounce_x()
        
    if ball.xcor() > 380:
        ball.reset_ball()
        ball.bounce_x()
        score.l_point()
    
    if ball.xcor() < -380:
        ball.reset_ball()
        ball.bounce_x()
        score.r_point()
    
    
    
screen.exitonclick()



