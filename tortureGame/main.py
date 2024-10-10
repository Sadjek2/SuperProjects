import random 
 
class HangmanGame: 
    def __init__(self, word_list): 
        self.word_list = word_list 
        self.random_word = random.choice(word_list) 
        self.unique_letters = set(self.random_word) 
        self.attempts = len(self.unique_letters) 
        self.unguessed_list = ["_"] * len(self.random_word) 
        self.guessed_letters = set() 
 
    def user_input(self): 
        while True: 
            user_input = input("Введите букву: ").lower() 
            if len(user_input) != 1: 
                print("Пожалуйста, введите одну букву.") 
            elif not user_input.isalpha(): 
                print("Пожалуйста, введите букву, а не число или специальный символ.") 
            elif user_input in self.guessed_letters: 
                print("Вы уже угадали эту букву. Попробуйте другую.") 
            else: 
                self.guessed_letters.add(user_input) 
                return user_input 
 
    def find_letter_in_word(self, letter): 
        return letter in self.random_word 
 
    def letter_indices(self, letter): 
        return [i for i, x in enumerate(self.random_word) if x == letter] 
 
    def update_unguessed_list(self, letter): 
        indices = self.letter_indices(letter) 
        for index in indices: 
            self.unguessed_list[index] = letter 
 
    def game_start(self): 
        print("Давайте сыграем в игру! Я загадал... Слово из", len(self.random_word), "букв!") 
        self.game_cycle() 
 
    def game_cycle(self): 
        while self.attempts > 0: 
            print("У вас осталось", self.attempts, "попыток.") 
            print(" ".join(self.unguessed_list)) 
            user_letter = self.user_input() 
            if self.find_letter_in_word(user_letter): 
                print("Вы отгадали букву!") 
                self.update_unguessed_list(user_letter) 
                if "_" not in self.unguessed_list: 
                    print(" ".join(self.unguessed_list)) 
                    print("Поздравляем! Вы выиграли!") 
                    return 
            else: 
                print("Вы ошиблись...") 
                self.attempts -= 1 
        print("У вас закончились попытки. Слово было:", self.random_word) 
 
import data 
game = HangmanGame(data.nature_words) 
game.game_start()