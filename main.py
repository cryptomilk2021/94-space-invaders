from turtle import Screen, Turtle
from paddle import Paddle
from aliens import Aliens

from my_bullet import MyBullet
from scoreboard import Scoreboard
import time
score = Scoreboard()
screen = Screen()
screen.register_shape('graphics/my_ship.gif')
screen.register_shape('graphics/alien_bullet.gif')
screen.register_shape('graphics/large_inv.gif')
screen.register_shape('graphics/my_bullet.gif')
screen.register_shape('graphics/small_inv.gif')

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Space Doodies")
screen.tracer(0)
bullet = MyBullet()
paddle = Paddle((10, -280))
aliens = Aliens()

def fire():
    print(paddle.xcor(), paddle.ycor())
    bullet.fire(paddle.xcor())

screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")
screen.onkey(fire, " ")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    # ball.move()


    #
    # #detect colision with paddle
    # if ball.distance(paddle) < 35:
    #     ball.bounce_y()

    for i in aliens.all_aliens:

        if bullet.distance(i) < 35:
            i.ht()
            aliens.all_aliens.remove(i)
            # ball.bounce_y()
            bullet.hideturtle()
            bullet.goto(-260, -260)
            score.point()
    bullet.go()
    aliens.move_aliens()
screen.exitonclick()