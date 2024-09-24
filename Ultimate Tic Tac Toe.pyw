# Импорт библиотек

from json import load
import time
from turtle import * # Графика
from winsound import * # Звуки

# language

RU_l = "Загрузка..."
RU_xsbc = "[X] Выберите БОЛЬШУЮ клетку"
RU_xssc = "[X] Выберите МАЛЕНЬКУЮ клетку"
RU_osbc = "[0] Выберите БОЛЬШУЮ клетку"
RU_ossc = "[0] Выберите МАЛЕНЬКУЮ клетку"
RU_xw = "Игрок X выйграл"
RU_ow = "Игрок 0 выйграл"
RU_d = "НИЧЬЯ"
RU_gn = "Супер\nКрестики-Нолики"
RU_p = "Играть➡"
RU_r = "Правила📗"
RU_lg = "Язык🌐"
RU_ss = "Начальный экран"
RU_ctx = "Нажмите чтобы выйти"

EN_l = "Loading..."
EN_xsbc = "[X] Select BIG cell"
EN_xssc = "[X] Select SMALL cell"
EN_osbc = "[0] Select BIG cell"
EN_ossc = "[0] Select SMALL cell"
EN_xw = "Player X win!"
EN_ow = "Player 0 win!"
EN_d = "DRAW"
EN_gn = "Ultimate\n Tic Tac Toe"
EN_p = "Play➡"
EN_r = "Rules📗"
EN_lg = "Language🌐"
EN_ss = "Start Screen"
EN_ctx = "Click to exit"

# Переменные

player = None
big_selected_cell = None
small_selected_cell = None
last_selected = None
loading = 0
language = "EN"
cells = [[0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0]]
screen = Screen()
xcell = [3,3,3,3,3,3,3,3,3]
ocell = [4,4,4,4,4,4,4,4,4]
Beep(500,50)
status = 0
hideturtle()
# Функции нацеленные на отрисовку

def PrintStartScreen():
    global language, EN_ss, RU_ss, EN_gn, RU_gn, EN_r, RU_r, EN_lg, RU_lg, RU_p, EN_p
    speed(0)
    up()
    if language == "EN":
        title(EN_ss)
    if language == "RU":
        title(RU_ss)
    pensize(5)
    down()
    fd(-200)
    for i in range(3):
        for i in range(2):
            fd(400)
            rt(90)
            fd(50)
            rt(90)   
        up()
        goto(xcor(),ycor()-50)
        down()
    up()
    goto(0,100)
    if language == "EN":
        write(EN_gn, move=False, align="center", font=("Courier New", 60, "italic"))
    if language == "RU":
        write(RU_gn, move=False, align="center", font=("Courier New", 60, "italic"))
    goto(0,-50)
    if language == "EN":
        write(EN_p, move=False, align="center", font=("Courier New", 35, "normal"))
    if language == "RU":
        write(RU_p, move=False, align="center", font=("Courier New", 35, "normal"))
    goto(0,-100)
    if language == "EN":
        write(EN_r, move=False, align="center", font=("Courier New", 35, "normal"))
    if language == "RU":
        write(RU_r, move=False, align="center", font=("Courier New", 35, "normal"))
    goto(0,-150)
    if language == "EN":
        write(EN_lg, move=False, align="center", font=("Courier New", 35, "normal"))
    if language == "RU":
        write(RU_lg, move=False, align="center", font=("Courier New", 35, "normal"))

def PrintMiniCell(x, y): # Отрисовка маленькой части поля
    global EN_l, RU_l
    if language == "EN":
        title(EN_l)
    if language == "RU":
        title(RU_l)
    speed(0)
    up()
    goto(x, y)
    goto(xcor()+25,ycor()+75)
    down()
    fd(150)
    up()
    goto(xcor(),ycor()+50)
    down()
    fd(-150)
    rt(90)
    up()
    goto(xcor()+50,ycor()+50)
    down()
    fd(150)
    up()
    goto(xcor()+50,ycor())
    down()
    fd(-150)
    lt(90)
    up()

def PrintCells(): # Отрисовка поля
    global EN_l, RU_l
    if language == "EN":
        title(EN_l)
    if language == "RU":
        title(RU_l)
    speed(0)
    up()
    pensize(10)
    speed(10)
    goto(-300, 100)
    down()
    fd(600)
    up()
    goto(xcor(),ycor()-200)
    down()
    fd(-600)
    rt(90)
    up()
    goto(-100,300)
    down()
    fd(600)
    up()
    goto(xcor()+200,ycor())
    down()
    fd(-600)
    lt(90)
    up()
    pensize(5)
    PrintMiniCell(-300,100)
    PrintMiniCell(-100,100)
    PrintMiniCell(100,100)
    PrintMiniCell(-300,-100)
    PrintMiniCell(-100,-100)
    PrintMiniCell(100,-100)
    PrintMiniCell(-300,-300)
    PrintMiniCell(-100,-300)
    PrintMiniCell(100,-300)
    hideturtle()

def clear_select(s):
    global EN_l, RU_l
    if language == "EN":
        title(EN_l)
    if language == "RU":
        title(RU_l)
    speed(0)
    up()
    pensize(5)
    color("white")
    if s == 0:
        goto(-300,100)
    if s == 1:
        goto(-100,100)
    if s == 2:
        goto(100,100)
    if s == 3:
        goto(-300,-100)
    if s == 4:
        goto(-100,-100)
    if s == 5:
        goto(100,-100)
    if s == 6:
        goto(-300,-300)
    if s == 7:
        goto(-100,-300)
    if s == 8:
        goto(100,-300)
    goto(xcor()+20,ycor()+20)
    down()
    for i in range(4):
        fd(160)
        lt(90)
    up()

def PrintSelect(): # Отрисовка выбора большой клетки
    global big_selected_cell, last_selected
    speed(0)
    global EN_l, RU_l
    if language == "EN":
        title(EN_l)
    if language == "RU":
        title(RU_l)

    if last_selected == None:
        pass
    else:
        clear_select(last_selected)
    up()
    pensize(5)
    color("black")
    if big_selected_cell == 0:
        goto(-300,100)
    if big_selected_cell == 1:
        goto(-100,100)
    if big_selected_cell == 2:
        goto(100,100)
    if big_selected_cell == 3:
        goto(-300,-100)
    if big_selected_cell == 4:
        goto(-100,-100)
    if big_selected_cell == 5:
        goto(100,-100)
    if big_selected_cell == 6:
        goto(-300,-300)
    if big_selected_cell == 7:
        goto(-100,-300)
    if big_selected_cell == 8:
        goto(100,-300)
    goto(xcor()+20,ycor()+20)
    for i in range(4):
        down()
        fd(30)
        up()
        fd(100)
        down()
        fd(30)
        lt(90)
        up()
    pencolor("yellow")
    pensize(3)
    for i in range(4):
        down()
        fd(30)
        up()
        fd(100)
        down()
        fd(30)
        lt(90)
    up()
    last_selected = big_selected_cell
    hideturtle()

def PrintCross(s, i):
    speed(0)
    global EN_l, RU_l
    if language == "EN":
        title(EN_l)
    if language == "RU":
        title(RU_l)
    Beep(500,50)
    up()
    pensize(5)
    color("black")
    if s == 0:
        goto(-300,100)
    if s == 1:
        goto(-100,100)
    if s == 2:
        goto(100,100)
    if s == 3:
        goto(-300,-100)
    if s == 4:
        goto(-100,-100)
    if s == 5:
        goto(100,-100)
    if s == 6:
        goto(-300,-300)
    if s == 7:
        goto(-100,-300)
    if s == 8:
        goto(100,-300)
    if i == 0:
        goto(xcor()+25,ycor()+125)
    if i == 1:
        goto(xcor()+75,ycor()+125)
    if i == 2:
        goto(xcor()+125,ycor()+125)
    if i == 3:
        goto(xcor()+25,ycor()+75)
    if i == 4:
        goto(xcor()+75,ycor()+75)
    if i == 5:
        goto(xcor()+125,ycor()+75)
    if i == 6:
        goto(xcor()+25,ycor()+25)
    if i == 7:
        goto(xcor()+75,ycor()+25)
    if i == 8:
        goto(xcor()+125,ycor()+25)
    goto(xcor()+5,ycor()+5)
    for s in range(2):
        down()
        goto(xcor()+40,ycor()+40)
        up()
        goto(xcor(),ycor()-40)
        down()
        goto(xcor()-40,ycor()+40)
        up()
        goto(xcor(),ycor()-40)
        pensize(3)
        pencolor("red")
    goto(400, 400)

def PrintCircle(s, i):
    speed(0)
    global EN_l, RU_l
    if language == "EN":
        title(EN_l)
    if language == "RU":
        title(RU_l)
    Beep(500,50)
    up()
    pensize(5)
    color("black")
    if s == 0:
        goto(-300,100)
    if s == 1:
        goto(-100,100)
    if s == 2:
        goto(100,100)
    if s == 3:
        goto(-300,-100)
    if s == 4:
        goto(-100,-100)
    if s == 5:
        goto(100,-100)
    if s == 6:
        goto(-300,-300)
    if s == 7:
        goto(-100,-300)
    if s == 8:
        goto(100,-300)
    if i == 0:
        goto(xcor()+25,ycor()+125)
    if i == 1:
        goto(xcor()+75,ycor()+125)
    if i == 2:
        goto(xcor()+125,ycor()+125)
    if i == 3:
        goto(xcor()+25,ycor()+75)
    if i == 4:
        goto(xcor()+75,ycor()+75)
    if i == 5:
        goto(xcor()+125,ycor()+75)
    if i == 6:
        goto(xcor()+25,ycor()+25)
    if i == 7:
        goto(xcor()+75,ycor()+25)
    if i == 8:
        goto(xcor()+125,ycor()+25)
    goto(xcor()+25,ycor()+5)
    for s in range(2):
        down()
        circle(20)
        up()
        pensize(3)
        pencolor("blue")
    goto(400, 400)

def PrintBigCross(s):
    speed(0)
    global EN_l, RU_l
    if language == "EN":
        title(EN_l)
    if language == "RU":
        title(RU_l)
    up()
    pensize(15)
    color("black")
    if s == 0:
        goto(-300,100)
    if s == 1:
        goto(-100,100)
    if s == 2:
        goto(100,100)
    if s == 3:
        goto(-300,-100)
    if s == 4:
        goto(-100,-100)
    if s == 5:
        goto(100,-100)
    if s == 6:
        goto(-300,-300)
    if s == 7:
        goto(-100,-300)
    if s == 8:
        goto(100,-300)
    goto(xcor()+33,ycor()+33)
    for i in range(2):
        down()
        goto(xcor()+134,ycor()+134)
        up()
        goto(xcor(),ycor()-134)
        down()
        goto(xcor()-134,ycor()+134)
        up()
        goto(xcor(),ycor()-134)
        pencolor("red")
        pensize(9)
    up()

def PrintBigCircle(s):
    speed(0)
    global EN_l, RU_l
    if language == "EN":
        title(EN_l)
    if language == "RU":
        title(RU_l)
    up()
    pensize(15)
    color("black")
    if s == 0:
        goto(-300,100)
    if s == 1:
        goto(-100,100)
    if s == 2:
        goto(100,100)
    if s == 3:
        goto(-300,-100)
    if s == 4:
        goto(-100,-100)
    if s == 5:
        goto(100,-100)
    if s == 6:
        goto(-300,-300)
    if s == 7:
        goto(-100,-300)
    if s == 8:
        goto(100,-300)
    goto(xcor()+100,ycor()+30)
    down()
    for i in range(2):
        circle(70)
        pencolor("blue")
        pensize(9)
    up()

# Функции нацеленные на исплнение

def SmallCellsWinCheck(i):
    if cells[i][0] == 1 and cells[i][3] == 1 and cells[i][6] == 1:
        cells[i] = xcell
        PrintBigCross(i)
    elif cells[i][1] == 1 and cells[i][4] == 1 and cells[i][7] == 1:
        cells[i] = xcell
        PrintBigCross(i)
    elif cells[i][2] == 1 and cells[i][5] == 1 and cells[i][8] == 1:
        cells[i] = xcell
        PrintBigCross(i)
    elif cells[i][0] == 1 and cells[i][1] == 1 and cells[i][2] == 1:
        cells[i] = xcell
        PrintBigCross(i)
    elif cells[i][3] == 1 and cells[i][4] == 1 and cells[i][5] == 1:
        cells[i] = xcell
        PrintBigCross(i)
    elif cells[i][6] == 1 and cells[i][7] == 1 and cells[i][8] == 1:
        cells[i] = xcell
        PrintBigCross(i)
    elif cells[i][0] == 1 and cells[i][4] == 1 and cells[i][8] == 1:
        cells[i] = xcell
        PrintBigCross(i)
    elif cells[i][2] == 1 and cells[i][4] == 1 and cells[i][6] == 1:
        cells[i] = xcell
        PrintBigCross(i)

    if cells[i][0] == 2 and cells[i][3] == 2 and cells[i][6] == 2:
        cells[i] = ocell
        PrintBigCircle(i)
    elif cells[i][1] == 2 and cells[i][4] == 2 and cells[i][7] == 2:
        cells[i] = ocell
        PrintBigCircle(i)
    elif cells[i][2] == 2 and cells[i][5] == 2 and cells[i][8] == 2:
        cells[i] = ocell
        PrintBigCircle(i)
    elif cells[i][0] == 2 and cells[i][1] == 2 and cells[i][2] == 2:
        cells[i] = ocell
        PrintBigCircle(i)
    elif cells[i][3] == 2 and cells[i][4] == 2 and cells[i][5] == 2:
        cells[i] = ocell
        PrintBigCircle(i)
    elif cells[i][6] == 2 and cells[i][7] == 2 and cells[i][8] == 2:
        cells[i] = ocell
        PrintBigCircle(i)
    elif cells[i][0] == 2 and cells[i][4] == 2 and cells[i][8] == 2:
        cells[i] = ocell
        PrintBigCircle(i)
    elif cells[i][2] == 2 and cells[i][4] == 2 and cells[i][6] == 2:
        cells[i] = ocell
        PrintBigCircle(i)

def GoToMenu():
    global big_selected_cell, small_selected_cell, last_selected, cells, status, player, loading
    big_selected_cell = None
    small_selected_cell = None
    last_selected = None
    cells = [[0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]]
    status = -1
    player = 0
    loading = 1
    clearscreen()
    pencolor("black")
    hideturtle()
    PrintStartScreen()

def OWIN(i):
    global last_selected
    clear_select(last_selected)
    global EN_ow, RU_ow, RU_ctx, EN_ctx
    if language == "EN":
        title(EN_ow)
        up()
        pencolor("black")
        goto(0,300)
        write(EN_ow, move=False, align="center", font=("Courier New", 60, "normal"))
        goto(0,-400)
        write(EN_ctx, move=False, align="center", font=("Courier New", 60, "normal"))
    if language == "RU":
        title(RU_ow)
        up()
        pencolor("black")
        goto(0,300)
        write(RU_ow, move=False, align="center", font=("Courier New", 60, "normal"))
        goto(0,-400)
        write(RU_ctx, move=False, align="center", font=("Courier New", 60, "normal"))
    screen.exitonclick()

def XWIN(i):
    global last_selected
    clear_select(last_selected)
    global EN_xw, RU_xw, RU_ctx, EN_ctx
    if language == "EN":
        title(EN_xw)
        up()
        goto(0,300)
        pencolor("black")
        write(EN_xw, move=False, align="center", font=("Courier New", 60, "normal"))
        goto(0,-400)
        write(EN_ctx, move=False, align="center", font=("Courier New", 60, "normal"))
    if language == "RU":
        title(RU_xw)
        up()
        goto(0,300)
        pencolor("black")
        write(RU_xw, move=False, align="center", font=("Courier New", 60, "normal"))
        goto(0,-400)
        write(RU_ctx, move=False, align="center", font=("Courier New", 60, "normal"))
    screen.exitonclick()

def DRAW():
    global last_selected
    clear_select(last_selected)
    global EN_d, RU_d, RU_ctx, EN_ctx
    if language == "EN":
        title(EN_d)
        up()
        goto(0,300)
        pencolor("black")
        write(EN_d, move=False, align="center", font=("Courier New", 60, "normal"))
        goto(0,-400)
        write(EN_ctx, move=False, align="center", font=("Courier New", 60, "normal"))
    if language == "RU":
        title(RU_d)
        up()
        goto(0,300)
        pencolor("black")
        write(RU_d, move=False, align="center", font=("Courier New", 60, "normal"))
        goto(0,-400)
        write(RU_ctx, move=False, align="center", font=("Courier New", 60, "normal"))
    screen.exitonclick()

def WinCheck():
    for i in range(0,9):
        SmallCellsWinCheck(i)
    if cells[0] == ocell and cells[3] == ocell and cells[6] == ocell:
        OWIN(1)
    elif cells[1] == ocell and cells[4] == ocell and cells[7] == ocell:
        OWIN(2)
    elif cells[2] == ocell and cells[5] == ocell and cells[8] == ocell:
        OWIN(3)
    elif cells[0] == ocell and cells[1] == ocell and cells[2] == ocell:
        OWIN(4)
    elif cells[3] == ocell and cells[4] == ocell and cells[5] == ocell:
        OWIN(5)
    elif cells[6] == ocell and cells[7] == ocell and cells[8] == ocell:
        OWIN(6)
    elif cells[0] == ocell and cells[4] == ocell and cells[8] == ocell:
        OWIN(7)
    elif cells[2] == ocell and cells[4] == ocell and cells[6] == ocell:
        OWIN(8)

    if cells[0] == xcell and cells[3] == xcell and cells[6] == xcell:
        XWIN(1)
    elif cells[1] == xcell and cells[4] == xcell and cells[7] == xcell:
        XWIN(2)
    elif cells[2] == xcell and cells[5] == xcell and cells[8] == xcell:
        XWIN(3)
    elif cells[0] == xcell and cells[1] == xcell and cells[2] == xcell:
        XWIN(4)
    elif cells[3] == xcell and cells[4] == xcell and cells[5] == xcell:
        XWIN(5)
    elif cells[6] == xcell and cells[7] == xcell and cells[8] == xcell:
        XWIN(6)
    elif cells[0] == xcell and cells[4] == xcell and cells[8] == xcell:
        XWIN(7)
    elif cells[2] == xcell and cells[4] == xcell and cells[6] == xcell:
        XWIN(8)

    if 0 not in cells[0] and 0 not in cells[1] and 0 not in cells[2] and 0 not in cells[3] and 0 not in cells[4] and 0 not in cells[5] and 0 not in cells[6] and 0 not in cells[7] and 0 not in cells[8]:
        DRAW()

def CheckSelectedBigCell(s): # Проверка содержимого выбранной большой клетки
    global big_selected_cell, player
    global RU_xssc, EN_xssc, RU_ossc, EN_ossc
    if cells[s] == xcell or cells[s] == ocell:
        big_selected_cell = None
    elif 0 not in cells[s]:
        big_selected_cell = None
    else:
        Beep(500,50)
        PrintSelect()
        Beep(250,50)
        
        if player == 0:
            if language == "EN":
                title(EN_xssc)
            if language == "RU":
                title(RU_xssc)
        else:
            if language == "EN":
                title(EN_ossc)
            if language == "RU":
                title(RU_ossc)

def SelectBigCell(x,y): # Выбор большой клетки
    global big_selected_cell

    check = 1

    if x > -300 and x < -100 and y > 100 and y < 300:
        big_selected_cell = 0
    elif x > -100 and x < 100 and y > 100 and y < 300:
        big_selected_cell = 1
    elif x > 100 and x < 300 and y > 100 and y < 300:
        big_selected_cell = 2
    elif x > -300 and x < -100 and y > -100 and y < 100:
        big_selected_cell = 3
    elif x > -100 and x < 100 and y > -100 and y < 100:
        big_selected_cell = 4
    elif x > 100 and x < 300 and y > -100 and y < 100:
        big_selected_cell = 5
    elif x > -300 and x < -100 and y > -300 and y < -100:
        big_selected_cell = 6
    elif x > -100 and x < 100 and y > -300 and y < -100:
        big_selected_cell = 7
    elif x > 100 and x < 300 and y > -300 and y < -100:
        big_selected_cell = 8
    else:
        check = 0
    if check != 0:
        CheckSelectedBigCell(big_selected_cell)

def NextBigCell():
    global big_selected_cell, small_selected_cell, cellsm, player, last_selected
    global RU_xsbc, RU_osbc, EN_xsbc, EN_osbc, RU_xssc, EN_xssc, RU_ossc, EN_ossc
    big_selected_cell = small_selected_cell
    if cells[big_selected_cell] == xcell or cells[big_selected_cell] == ocell:
        big_selected_cell = None
        clear_select(last_selected)
    elif 0 not in cells[big_selected_cell]:
        big_selected_cell = None
        clear_select(last_selected)
    else:
        PrintSelect()

    if player == 1:
        player = 0
        Beep(250,50)
        if language == "EN":
            title(EN_xssc)
        if language == "RU":
            title(RU_xssc)
        if big_selected_cell == None:
            if language == "EN":
                title(EN_xsbc)
            if language == "RU":
                title(RU_xsbc)
    else:
        player = 1
        Beep(250,50)
        if language == "EN":
            title(EN_ossc)
        if language == "RU":
            title(RU_ossc)
        if big_selected_cell == None:
            if language == "EN":
                title(EN_osbc)
            if language == "RU":
                title(RU_osbc)

def CheckSelectedSmallCell(): # Проверка содержимого выбранной маленькой клетки
    global small_selected_cell, cells, player
    if cells[big_selected_cell][small_selected_cell] == 0:
        if player == 0:
            cells[big_selected_cell][small_selected_cell] = 1
            PrintCross(big_selected_cell,small_selected_cell)
        if player == 1:
            cells[big_selected_cell][small_selected_cell] = 2
            PrintCircle(big_selected_cell,small_selected_cell)
        WinCheck()
        NextBigCell()
    else:
        pass

def SelectSmallCell(x,y): # Выбор маленькой клетки
    global big_selected_cell, small_selected_cell
    if big_selected_cell == 0:
        x += 200
        y -= 200
    if big_selected_cell == 1:
        y -= 200
    if big_selected_cell == 2:
        x -= 200
        y -= 200
    if big_selected_cell == 3:
        x += 200
    if big_selected_cell == 5:
        x -= 200
    if big_selected_cell == 6:
        x += 200
        y += 200
    if big_selected_cell == 7:
        y += 200
    if big_selected_cell == 8:
        x -= 200
        y += 200

    check = 1

    if x > -75 and x < -25 and y > 25 and y < 75:
        small_selected_cell = 0
    elif x > -25 and x < 25 and y > 25 and y < 75:
        small_selected_cell = 1
    elif x > 25 and x < 75 and y > 25 and y < 75:
        small_selected_cell = 2
    elif x > -75 and x < -25 and y > -25 and y < 25:
        small_selected_cell = 3
    elif x > -25 and x < 25 and y > -25 and y < 25:
        small_selected_cell = 4
    elif x > 25 and x < 75 and y > -25 and y < 25:
        small_selected_cell = 5
    elif x > -75 and x < -25 and y > -75 and y < -25:
        small_selected_cell = 6
    elif x > -25 and x < 25 and y > -75 and y < -25:
        small_selected_cell = 7
    elif x > 25 and x < 75 and y > -75 and y < -25:
        small_selected_cell = 8
    else:
        check = 0
    if check != 0:
        CheckSelectedSmallCell()

def XPlayer(x,y): # Ход игрока X
    if big_selected_cell == None:
        SelectBigCell(x,y)
    else:
        SelectSmallCell(x,y)

def OPlayer(x,y): # Ход игрока 0
    if big_selected_cell == None:
        SelectBigCell(x,y)
    else:
        SelectSmallCell(x,y)

def StartScreen(x,y):
    global status, language
    if x > -200 and x < 200 and y > -50 and y < 0:
        clear()
        up()
        goto(0,0)
        PrintCells()
        status = 1
    if x > -200 and x < 200 and y > -150 and y < -100:
        clear()
        up()
        goto(0,0)
        if language == "RU":
            language = 2
        elif language == "EN":
            language = "RU"
        if language == 2:
            language = "EN"
        PrintStartScreen()

def Main(x, y): # Основная функция
    global player, loading, status
    if status == 0:
        if loading == 0:
            loading = 1
            StartScreen(x,y)
            loading = 0
        else:
            pass
    elif status == 1:
        if loading == 0:
            loading = 1
            if player == 0:
                XPlayer(x,y)
            else:
                OPlayer(x,y)
            loading = 0
        else:
            pass

# Основной код

player = 0
PrintStartScreen()
Beep(250,50)

screen.onscreenclick(Main)

mainloop()