import turtle

class Shapes:
    def __init__(self, color = "BLACK"):
        self.color = color
        self.turtle = turtle.Turtle()

    # метод для перемещения черепахи в указанные координаты
    def goto(self, x, y):
        # поднять перо, переместиться, опустить перо
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.pendown()
    
    # метод для установки цвета черепахи
    def set_color(self, cvet: str):
        # установка цвета черепахи
        self.turtle.color(cvet)

    
    # метод для рисования круга
    def draw_circle(self, rad: int):
         # установка цвета заливки, начало заливки, рисование круга, конец заливки
        self.turtle.fillcolor("red") 
        self.turtle.begin_fill()
        self.turtle.fillcolor(self.color)
        self.turtle.circle(100)
        self.turtle.end_fill()

    # метод для рисования квадрата
    def draw_square(self, a: int):
         # установка цвета заливки, начало заливки, рисование квадрата, конец заливки
        self.turtle.fillcolor("red") 
        self.turtle.begin_fill()
        for _ in range(4):
            self.turtle.forward(a)
            self.turtle.left(90) 
        self.turtle.end_fill()
shape = Shapes()

shape.set_color("black")
shape.draw_circle(100)
shape.goto(-100, -200)
shape.draw_square(100)

turtle.done()