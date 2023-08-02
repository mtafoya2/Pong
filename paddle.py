from turtle import Turtle 

COLOR = "white"
SHAPE = "square"
UP = 90
DOWN = 270

#Inherits from turtle class
class Paddle(Turtle):
    def __init__(self, x_pos = 0, y_pos = 0):
        super().__init__()
        self.shape(SHAPE)
        self.shapesize(stretch_wid= 5, stretch_len=1)
        self.color(COLOR)
        self.penup()
        self.goto(x_pos, y_pos)


    def up(self):
        self.goto(self.xcor(), self.ycor() + 40)
    
    def down(self):
        self.goto(self.xcor(), self.ycor() - 40)