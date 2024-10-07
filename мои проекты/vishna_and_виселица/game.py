import tkinter as tk
from graphic import Graphic
import random
from words import get_random_word

class Game:
    def __init__(self, root):
        self.root = root
        self.graphic = Graphic(root)
        self.word = ""
        self.guessed_letters = []
        self.attempts = 6
        self.category = ""

        self.start_menu()

    def start_menu(self):
        self.graphic.word_label.config(text="Добро пожаловать в игру!")
        self.graphic.attempts_label.config(text="")
        self.graphic.canvas.delete("all")
        self.graphic.guess_button.pack_forget()
        self.graphic.play_again_button.pack_forget()
        self.graphic.guess_entry.pack_forget()
        self.graphic.category_frame.pack_forget()

        self.graphic.main_frame.pack(pady=20)

        self.graphic.play_button.pack(pady=10)
        self.graphic.exit_button.pack(pady=10)
        self.graphic.exit_button.config(command=self.root.destroy)

        self.graphic.play_button.config(command=self.category_menu)
    def category_menu(self):
        self.graphic.main_frame.pack_forget()
        self.graphic.category_frame.pack(pady=20)

        self.graphic.animals_button.config(command=lambda: self.start_game("animals"))
        self.graphic.fruits_button.config(command=lambda: self.start_game("fruits"))
        self.graphic.cities_button.config(command=lambda: self.start_game("cities"))
    def start_game(self, category):
        self.graphic.display_game_screen()
        self.category = category
        self.word = get_random_word(category)
        self.guessed_letters = []
        self.attempts = 6
        self.graphic.display_word(self.word, self.guessed_letters)
        self.graphic.attempts_label.config(text="Осталось попыток: " + str(self.attempts))
        self.graphic.canvas.delete("all")
        self.graphic.guess_button.config(state="normal")
        self.graphic.guess_button.config(command=self.guess_letter)
        self.graphic.guess_entry.pack()
        self.graphic.guess_button.pack()

    def guess_letter(self):
        letter = self.graphic.guess_entry.get()
        self.graphic.guess_entry.delete(0, tk.END)
        if letter in self.word:
            self.guessed_letters.append(letter)
            self.graphic.display_word(self.word, self.guessed_letters)
            if set(self.word) == set(self.guessed_letters):
                self.graphic.word_label.config(text="Вы выиграли! Слово было: " + self.word)
                self.graphic.guess_button.config(state="disabled")
                self.graphic.play_again_button.pack()
                self.graphic.play_again_button.config(command=self.play_again)
        else:
            self.attempts -= 1
            self.graphic.attempts_label.config(text="Осталось попыток: " + str(self.attempts))
            self.graphic.canvas.delete("all")
            if self.attempts <= 6:
                self.graphic.canvas.create_line(50, 150, 150, 150)  # основа
            if self.attempts <= 5:
                self.graphic.canvas.create_line(100, 150, 100, 50)  # столб
            if self.attempts <= 4:
                self.graphic.canvas.create_line(100, 50, 150, 50)  # перекладина
            if self.attempts <= 3:
                self.graphic.canvas.create_line(150, 50, 150, 70)  # веревка
            if self.attempts <= 2:
                self.graphic.canvas.create_oval(140, 70, 160, 90)  # голова
            if self.attempts <= 1:
                self.graphic.canvas.create_line(150, 90, 150, 120)  # туловище
            if self.attempts == 0:
                self.graphic.canvas.create_line(150, 100, 130, 110)  # левая рука
                self.graphic.canvas.create_line(150, 100, 170, 110)  # правая рука
                self.graphic.canvas.create_line(150, 120, 130, 130)  # левая нога
                self.graphic.canvas.create_line(150, 120, 170, 130)  # правая нога
            if self.attempts == 0:
                self.graphic.word_label.config(text="Вы проиграли! Слово было: " + self.word)
                self.graphic.guess_button.config(state="disabled")
                self.graphic.play_again_button.pack()
                self.graphic.play_again_button.config(command=self.play_again)

    def play_again(self):
        self.graphic.play_again_button.pack_forget()
        self.graphic.guess_button.pack_forget()
        self.graphic.guess_entry.pack_forget()
        self.graphic.word_label.config(text="")
        self.graphic.attempts_label.config(text="")
        self.graphic.canvas.delete("all")
        self.start_menu()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    game = Game(root)
    game.run()