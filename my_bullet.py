from turtle import Turtle

class MyBullet(Turtle):
    def __init__(self):
        super().__init__()

        self.shape('graphics/my_bullet.gif')
        self.penup()
        self.x_move = 6
        self.y_move = 6
        self.hideturtle()
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def go(self):
        if self.isvisible():
            self.showturtle()
            self.goto(self.xcor(), self.ycor() + 10)
            if self.ycor() > 270:
                self.hideturtle()

    def fire(self, x_cord):
        if not self.isvisible():
            self.goto(x_cord, -260)
            self.showturtle()
            self.move_speed = 0.1


