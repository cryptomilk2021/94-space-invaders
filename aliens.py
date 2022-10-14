from turtle import Turtle
import time
ROWS = 5
COLUMNS = 10

class Aliens(Turtle):

    def __init__(self):
        super().__init__()
        self.direction = 1
        self.y_drop = 0
        self.nbr_of_iterations = 0
        self.all_aliens = []
        self.time_delay = 60
        self.create_aliens(6, 11)

    def create_aliens(self, rows, columns):
        x_offset = -354
        y_offset = 280
        x_buffer = 45
        y_buffer = 28

        for i in range(columns):
            for j in range(rows):
                new_alien = Turtle("square")
                if j > 3:
                    new_alien.shape('graphics/large_inv.gif')
                else:
                    new_alien.shape('graphics/small_inv.gif')

                # new_alien.shapesize(stretch_wid=1, stretch_len=3)
                new_alien.penup()
                y_offset = y_offset - y_buffer
                new_alien.goto(x_offset, y_offset)
                self.all_aliens.append(new_alien)

            x_offset = x_offset + x_buffer
            y_offset = 280

    def move_aliens(self):
        time.sleep(self.time_delay /1000)
        ycords = self.all_aliens[0].ycor()
        if self.all_aliens[0].xcor() > -104 or self.all_aliens[0].xcor() < -370:
            self.direction *= -1
            self.nbr_of_iterations += 1
            if self.nbr_of_iterations > 1:
                self.time_delay -= 5
                if self.time_delay < 0:
                    self.time_delay = 0
                self.nbr_of_iterations = 0
                self.y_drop -= 5
                for i in self.all_aliens:
                    i.goto(i.xcor(), i.ycor() + self.y_drop)

        for i in self.all_aliens:
            i.goto(i.xcor() + 5 * self.direction, i.ycor())


