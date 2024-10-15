import turtle as t
#импортируем модуль turtle
class Shapes:
    #добавляяем класс
    def __init__(self, color = "green", x = 0, y = 0):
        #добавляем конструктор 
        self.color = "green"
        self.x = x
        self.y = y
        self.t = t.Turtle()
        #задаем параметры
        

    def draw_square(self, a: int = 100):
        #добавляем метод рисования квадрата и сторону от которой зависит размер квадрата
        self.t.fillcolor(self.color)
        #говорим о том что нам нужно залить цвет
        self.t.begin_fill()
        for _ in range(4):
            self.t.forward(a)
            self.t.right(90)
            #рисуем
        self.t.end_fill()
        #заканчиваем рисовать и заливаем
    def draw_circle(self, rad: int = 100):
        #добавляем метод рисования круга и прописываем радиус от которого зависит размер круга
        self.t.color(self.color)
        #говорим о том что нам нужно залить цвет
        self.t.begin_fill()
        self.t.circle(rad)
        #рисуем
        self.t.end_fill()
        #заканчиваем рисовать и заливаем
    def goto(self, x, y):
        #метод перемещения черепахи
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()
        self.draw_square()
        #вызываем метод квадрата
    def fill(self, color):
        self.t.color(color)
        self.t.begin_fill()
        self.t.end_fill()
    #заканчиваем рисовать и заливать
               

shape1 = Shapes()
shape1.draw_square(150)
shape1.draw_circle(120)
#задаем размеры координаты и фигуры которые рисуем
