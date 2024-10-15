import turtle  # Импортируем модуль turtle для графики

# Базовый класс для фигур
class Shape:
    def __init__(self, color, x, y):
        self.color = color  # Устанавливаем цвет фигуры
        self.x = x          # Устанавливаем координату x для позиции фигуры
        self.y = y          # Устанавливаем координату y для позиции фигуры
        self.turtle = turtle.Turtle()  # Создаем объект черепахи для рисования
        self.turtle.speed(1)  # Устанавливаем скорость рисования черепахи
        self.turtle.penup()    # Поднимаем перо, чтобы не рисовать при перемещении к начальной позиции
        self.turtle.goto(x, y) # Перемещаем черепаху к указанной позиции (x, y)
        self.turtle.pendown()  # Опускаем перо, чтобы начать рисование

    def draw(self):
        pass  # Метод для рисования фигур (будет реализован в подклассах)

# Класс для рисования кругов
class Circle(Shape):
    def __init__(self, color, x, y, radius):
        super().__init__(color, x, y)  # Инициализируем базовый класс с цветом и позицией
        self.radius = radius  # Устанавливаем радиус круга

    def draw(self):
        self.turtle.fillcolor(self.color)  # Устанавливаем цвет заливки для круга
        self.turtle.begin_fill()            # Начинаем заливку фигуры
        self.turtle.circle(self.radius)     # Рисуем круг с указанным радиусом
        self.turtle.end_fill()              # Заканчиваем заливку фигуры

# Класс для рисования прямоугольников
class Rectangle(Shape):
    def __init__(self, color, x, y, width, height):
        super().__init__(color, x, y)  # Инициализируем базовый класс с цветом и позицией
        self.width = width    # Устанавливаем ширину прямоугольника
        self.height = height  # Устанавливаем высоту прямоугольника

    def draw(self):
        self.turtle.fillcolor(self.color)  # Устанавливаем цвет заливки для прямоугольника
        self.turtle.begin_fill()            # Начинаем заливку фигуры
        for _ in range(2):                  # Рисуем прямоугольник
            self.turtle.forward(self.width)  # Двигаемся вперед на ширину
            self.turtle.right(90)           # Поворачиваемся на 90 градусов
            self.turtle.forward(self.height) # Двигаемся вперед на высоту
            self.turtle.right(90)           # Поворачиваемся на 90 градусов
        self.turtle.end_fill()              # Заканчиваем заливку фигуры

# Класс для рисования треугольников
class Triangle(Shape):
    def __init__(self, color, x, y, side_length):
        super().__init__(color, x, y)  # Инициализируем базовый класс с цветом и позицией
        self.side_length = side_length  # Устанавливаем длину стороны треугольника

    def draw(self):
        self.turtle.fillcolor(self.color)  # Устанавливаем цвет заливки для треугольника
        self.turtle.begin_fill()            # Начинаем заливку фигуры
        for _ in range(3):                  # Рисуем треугольник
            self.turtle.forward(self.side_length)  # Двигаемся вперед на длину стороны
            self.turtle.left(120)           # Поворачиваемся на 120 градусов
        self.turtle.end_fill()              # Заканчиваем заливку фигуры

# Создаем и рисуем синий круг
circle = Circle("blue", 0, 0, 50)
circle.draw()

# Создаем и рисуем красный прямоугольник
rectangle = Rectangle("red", -100, 50, 100, 100)
rectangle.draw()

# Создаем