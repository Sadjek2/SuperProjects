import logic
import words
import tkinter as tk
from graphic import Graphic

class Game:
    def __init__(self, root):
        self.root = root
        self.category = None
        self.word = None
        self.attempts = 6
        self.guessed_letters = []
        self.language = "Русский"
        self.graphic = Graphic(self)
        self.start_menu()

    def start_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        if self.language == "English":
            category_label = tk.Label(self.root, text="Choose a category:", font=("Helvetica", 24))
        else:
            category_label = tk.Label(self.root, text="Выберите категорию:", font=("Helvetica", 24))
        category_label.pack()
        categories = list(words.CATEGORIES.keys())
        if self.language == "Русский":
            categories = [category for category in categories if category.isalpha() and not category.isascii()]
        elif self.language == "English":
            categories = [category for category in categories if category.isascii()]
        for category in categories:
            category_button = tk.Button(self.root, text=category, command=lambda category=category: self.start_game(category))
            category_button.pack()
        if self.language == "English":
            self.multiplayer_button = tk.Button(self.root, text="Multiplayer", command=self.start_multiplayer)
        else:
            self.multiplayer_button = tk.Button(self.root, text="Мультиплеер", command=self.start_multiplayer)
        self.multiplayer_button.pack()
        if self.language == "English":
            self.settings_button = tk.Button(self.root, text="Settings", command=self.start_settings)
        else:
            self.settings_button = tk.Button(self.root, text="Настройки", command=self.start_settings)
        self.settings_button.pack()

    def start_game(self, category):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.category = category
        self.word = words.get_random_word(category)
        self.attempts = 6
        self.guessed_letters = []
        self.graphic.word_label = tk.Label(self.root, text="", font=("Helvetica", 24))
        self.graphic.word_label.pack()
        self.graphic.attempts_label = tk.Label(self.root, text="Осталось попыток: 6", font=("Helvetica", 18))
        self.graphic.attempts_label.pack()
        self.graphic.canvas = tk.Canvas(self.root, width=200, height=200)
        self.graphic.canvas.pack()
        self.graphic.guess_entry = tk.Entry(self.root, width=20)
        self.graphic.guess_entry.pack()
        self.graphic.guess_button = tk.Button(self.root, text="Guess", command=self.graphic.guess_letter)
        self.graphic.guess_button.pack()
        self.graphic.display_word(self.word, self.guessed_letters)

    def start_multiplayer(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        if self.language == "English":
            self.graphic.word_label = tk.Label(self.root, text="Player 1, enter a word:", font=("Helvetica", 24))
        else:
            self.graphic.word_label = tk.Label(self.root, text="Игрок 1, введите слово:", font=("Helvetica", 24))
        self.graphic.word_label.pack()
        self.graphic.guess_entry = tk.Entry(self.root, width=20)
        self.graphic.guess_entry.pack()
        self.graphic.guess_button = tk.Button(self.root, text="Guess", command=self.get_word)
        self.graphic.guess_button.pack()

    def get_word(self):
        self.word = self.graphic.guess_entry.get()
        self.graphic.word_label.config(text="")
        self.graphic.guess_entry.delete(0, tk.END)
        self.graphic.guess_button.config(command=self.graphic.guess_letter)
        self.attempts = 6
        self.guessed_letters = []
        self.graphic.attempts_label = tk.Label(self.root, text="Осталось попыток: 6", font=("Helvetica", 18))
        self.graphic.attempts_label.pack()
        self.graphic.canvas = tk.Canvas(self.root, width=200, height=200)
        self.graphic.canvas.pack()
        self.graphic.display_word(self.word, self.guessed_letters)

    def start_settings(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        if self.language == "English":
            settings_label = tk.Label(self.root, text="Settings:", font=("Helvetica", 24))
        else:
            settings_label = tk.Label(self.root, text="Настройки:", font=("Helvetica", 24))
        settings_label.pack()
        if self.language == "English":
            language_button = tk.Button(self.root, text="Language: English", command=self.change_language)
        else:
            language_button = tk.Button(self.root, text="Язык: Русский", command=self.change_language)
        language_button.pack()
        if self.language == "English":
            self.back_button = tk.Button(self.root, text="Back", command=self.start_menu)
        else:
            self.back_button = tk.Button(self.root, text="Назад", command=self.start_menu)
        self.back_button.pack()

    def change_language(self):
        if self.language == "English":
            self.language = "Русский"
        else:
            self.language = "English"
        self.start_settings()

    def guess_letter(self, letter):
        if logic.is_valid_guess(letter, self.word, self.guessed_letters):
            self.guessed_letters.append(letter)
            self.graphic.display_word(self.word, self.guessed_letters)
            if logic.has_won(self.word, self.guessed_letters):
                self.win()
            else:
                self.attempts -= 1
                self.graphic.attempts_label.config(text="Осталось попыток: " + str(self.attempts))
                if self.attempts == 0:
                    self.lose()
        self.graphic.guess_entry.delete(0, tk.END)

    def win(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        if self.language == "English":
            win_label = tk.Label(self.root, text="Congratulations, you won!", font=("Helvetica", 24))
        else:
            win_label = tk.Label(self.root, text="Поздравляем, вы выиграли!", font=("Helvetica", 24))
        win_label.pack()
        if self.language == "English":
            self.back_button = tk.Button(self.root, text="Back", command=self.start_menu)
        else:
            self.back_button = tk.Button(self.root, text="Назад", command=self.start_menu)
        self.back_button.pack()

    def lose(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        if self.language == "English":
            lose_label = tk.Label(self.root, text="Sorry, you lost. The word was " + self.word, font=("Helvetica", 24))
        else:
            lose_label = tk.Label(self.root, text="Извините, вы проиграли. Слово было " + self.word, font=("Helvetica", 24))
        lose_label.pack()
        if self.language == "English":
            self.back_button = tk.Button(self.root, text="Back", command=self.start_menu)
        else:
            self.back_button = tk.Button(self.root, text="Назад", command=self.start_menu)
        self.back_button.pack()

class Graphic:
    def __init__(self, game):
        self.game = game

    def display_word(self, word, guessed_letters):
        self.game.graphic.word_label.config(text=" ".join([letter if letter in guessed_letters else "_" for letter in word]))

    def guess_letter(self):
        letter = self.game.graphic.guess_entry.get()
        self.game.guess_letter(letter)