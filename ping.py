from turtle import Turtle,Screen
import os
import time
os.system("cls")
#setup window
window = Screen()
window.setup(800,600)
window.bgcolor("black")
window.tracer(0)
# setup object of the game
# ball -----
ball = Turtle("circle")
ball.speed("fast")
ball.color("orange")
ball.shapesize(0.8)
ball.goto(0,0)
ball.penup()
ball_dx, ball_dy = 1, 1
ball_speed = 0.4
# center line
center_line = Turtle()
center_line.color("white")
center_line.hideturtle()
center_line.pensize(5)
center_line.penup()
center_line.goto(0,-300)
center_line.pendown()
center_line.goto(0,260)
center_line.goto(-400,260)
center_line.goto(400,260)
# player 1
player1 = Turtle("square")
player1.speed("fastest")
player1.color("blue")
player1.shapesize(5,1)
player1.penup()
player1.goto(-380,0)
# player 2
player2 = Turtle("square")
player2.speed(0)
player2.color("red")
player2.shapesize(5,1)
player2.penup()
player2.goto(380,0)
# score
score = Turtle()
score.color("white")
score.hideturtle()
score.penup()
score.goto(-118,260)
score1 = 0
score2 = 0
score.write(f"player1: {score1}    player2: {score2}",font=("arial",18,"normal"))
# players movement
def p1_up():
    player1.sety(player1.ycor() + 20)

def p1_down():
    player1.sety(player1.ycor() - 20)

def p2_up():
    player2.sety(player2.ycor() + 20)

def p2_down():
    player2.sety(player2.ycor() - 20)
# control the movement of the 2 players from the keybored
window.listen()
window.onkey(p1_up,"q")
window.onkey(p1_down,"w")
window.onkey(p2_up,"p")
window.onkey(p2_down,"l")
game_on = True
while game_on:
    window.update()

    # ball movement
    ball.setx(ball.xcor() + (ball_dx * ball_speed))
    ball.sety(ball.ycor() + (ball_dy * ball_speed))
    # ball borders
    if ball.ycor() > 250 : # top border
        ball.sety(250)
        ball_dy *= -1 # change ball direction
    if ball.ycor() < -290 : # top border
        ball.sety(-290)
        ball_dy *= -1
    # collision with player 1
    if player1.distance(ball) <= 20:
        ball.setx(-350)
        ball_dx *= -1
    if player2.distance(ball) <= 20:
        ball.setx(350)
        ball_dx *= -1
    if ball.xcor() < -400 :
        score2 += 1
        ball.goto(0,0)
        time.sleep(1.5)
        ball_dx *= -1 # change direction of the ball right or left
    if ball.xcor() > 400 :
        score1 += 1
        ball.goto(0,0)
        time.sleep(1.5)
        ball_dx *= -1
    score.clear()
    score.write(f"player1: {score1}    player2: {score2}",font=("arial",18,"normal"))
window.exitonclick()
