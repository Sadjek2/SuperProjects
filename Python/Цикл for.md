- #ЦиклFor (For loop)
- #Python (Python)
- #ЯзыкПрограммирования (Programming language)
- #ЦиклыВPython (Loops in Python)
- #УправлениеЦиклами (Loop control)
- #Итерации (Iterations)
- #Итераторы (Iterators)
- #Генераторы (Generators)
- #ЦиклForВPython (For loop in Python)
- #СинтаксисPython (Python syntax)
n = int(input("Enter a natural number: "))
def factorial(n):    
    if n == 0:
        return 1    
    else:
        return n * factorial(n - 1)
print(factorial(n))
Вот как работает этот код:

1. Пользователь вводит натуральное число, которое сохраняется в `n`.
2. Функция `factorial`вызывается `n`с аргументом.
3. Если `n`равно 0, функция возвращает 1.
4. Если `n`не равно 0, функция вызывает себя с `n - 1`аргументом и умножает результат на `n`.
5. Рекурсивные вызовы продолжаются до тех пор, пока `n`не станет равным 0, после чего функция возвращает 1.
6. Окончательный результат выводится на консоль.