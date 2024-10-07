import game_logic
import data

#список слов, который задается в файле data.py
list_of_words = data.nature_words
#случайно выбранное слово из списка
random_word = game_logic.select_random_word(list_of_words)

#подсчёт неповторяющихся букв в случайно выбранном раннее слове
set_of_unique_letters = set(random_word)

#количество попыток из длинны сета
attempts = game_logic.count_unique_letters(random_word)

def game_start():
    #глобальные переменные
    global p_lettre, attempts
    print("Давайте сыграем в игру! Я загадал...Слово из", len(random_word),",букв!")
    print("У вас осталось", attempts, "попыток.")

def game_cycle():
    #глобальные переменные 
    global p_letter, attempts

    while attempts != 0:
        p_letter = game_logic.user_input()[1:]
        letter_in_word = game_logic.find_letter(p_letter, random_word)

        if letter_in_word:
            print("Вы отгадали букву!")
        elif not letter_in_word:
            print("Вы ошиблись...")
            attempts -= 1



        
