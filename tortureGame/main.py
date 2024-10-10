import game_logic
import data

#список слов, который задаётся в файле data.py
list_of_words = data.nature_words
 
#случайно выбранное слово из списка 
random_word = game_logic.select_random_word(list_of_words)

#подсчёт неповторяющихся букв в случайно выбранном раннее слове
set_of_unique_letters = set(random_word)

#количество попыток из длины сета 
attempts = game_logic.count_unique_letters(random_word)

#буква, введённая пользователем
p_letter = None

unguessed_list = ["_"] * len(random_word)
unguessed_string = "  ".join(unguessed_list)


def game_start():
    #глобальные переменные
    global p_letter, attempts,  unguessed_list, unguessed_string

    
    print("Давайте сыграем в игру! Я загадал... Слово из", len(random_word), "букв!")
    print("У вас осталось", attempts, "попыток.")  
    
    game_cycle() 

def game_cycle():
    #глобальные переменные
    global p_letter, attempts, unguessed_list, unguessed_string
    
    while attempts != 0:
        p_letter = game_logic.user_input()[:1]
        letter_in_word = game_logic.find_letter_in_set(p_letter, random_word) 
        
        if letter_in_word:
            print("Вы отгадали букву!")
            indices = game_logic.letter_indices(p_letter, random_word)
            unguessed_list = game_logic.replace_unguessed(indices, unguessed_list, p_letter)
            print(" ".join(unguessed_list))
        elif not letter_in_word:
            print("Вы ошиблись...")
            print(" ".join(unguessed_list))
            attempts -= 1
            
game_start()