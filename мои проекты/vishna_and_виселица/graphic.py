import tkinter as tk

class Graphic:
    def __init__(self, root):
        self.root = root
        self.word_label = None
        self.attempts_label = None
        self.canvas = None
        self.guess_entry = None
        self.guess_button = None
        self.play_again_button = None
        self.exit_button = None
        self.play_button = None
        self.category_label = None
        self.category_frame_buttons = None
        self.main_frame = None
        self.category_frame = None

        self.create_widgets()
        self.display_main_screen()

    def create_widgets(self):
        self.word_label = tk.Label(self.root, text="", font=("Helvetica", 24))
        self.word_label.pack(pady=10)

        self.attempts_label = tk.Label(self.root, text="", font=("Helvetica", 18))
        self.attempts_label.pack()

        self.canvas = tk.Canvas(self.root, width=200, height=200)
        self.canvas.pack()

        self.guess_entry = tk.Entry(self.root, font=("Helvetica", 18))
        self.guess_button = tk.Button(self.root, text="Угадать", font=("Helvetica", 18))
        self.play_again_button = tk.Button(self.root, text="Играть снова", font=("Helvetica", 18))
        self.exit_button = tk.Button(self.root, text="Выход", font=("Helvetica", 18))
        self.play_button = tk.Button(self.root, text="Играть", font=("Helvetica", 18))

        self.guess_button.pack_forget()
        self.play_again_button.pack_forget()
        self.guess_entry.pack_forget()
        self.exit_button.pack_forget()
        self.play_button.pack_forget()

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(pady=20)

        self.category_frame = tk.Frame(self.root)
        self.category_frame.pack_forget()

        self.category_label = tk.Label(self.category_frame, text="Выберите категорию:", font=("Helvetica", 18))
        self.category_label.pack()

        self.category_frame_buttons = tk.Frame(self.category_frame)
        self.category_frame_buttons.pack()

        self.animals_button = tk.Button(self.category_frame_buttons, text="Животные", font=("Helvetica", 18))
        self.animals_button.pack(side=tk.LEFT, padx=10)

        self.fruits_button = tk.Button(self.category_frame_buttons, text="Фрукты", font=("Helvetica", 18))
        self.fruits_button.pack(side=tk.LEFT, padx=10)

        self.cities_button = tk.Button(self.category_frame_buttons, text="Города", font=("Helvetica", 18))
        self.cities_button.pack(side=tk.LEFT, padx=10)

    def display_main_screen(self):
        self.word_label.pack_forget()
        self.attempts_label.pack_forget()
        self.canvas.pack_forget()
        self.guess_entry.pack_forget()
        self.guess_button.pack_forget()
        self.play_again_button.pack_forget()
        self.category_frame.pack_forget()

        self.play_button.pack(pady=10)
        self.exit_button.pack(pady=10)

    def display_game_screen(self):
        self.play_button.pack_forget()
        self.exit_button.pack_forget()

        self.word_label.pack(pady=10)
        self.attempts_label.pack()
        self.canvas.pack()
        self.guess_entry.pack()
        self.guess_button.pack()

    def display_word(self, word, guessed_letters):
        display = ""
        for letter in word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        self.word_label.config(text=display)

def display_win(self, word):
        self.word_label.config(text="Вы выиграли! Слово было: " + word)
        
def display_attempts(self, attempts):
        self.attempts_label.config(text="Осталось попыток: " + str(attempts))
        self.canvas.delete("all")
        if attempts <= 6:
            self.canvas.create_line(50, 150, 150, 150)  # основа
        if attempts <= 5:
            self.canvas.create_line(100, 150, 100, 50)  # столб
        if attempts <= 4:
            self.canvas.create_line(100, 50, 150, 50)  # перекладина
        if attempts <= 3:
            self.canvas.create_line(150, 50, 150, 70)  # веревка
        if attempts <= 2:
            self.canvas.create_oval(140, 70, 160, 90)  # голова
        if attempts <= 1:
            self.canvas.create_line(150, 90, 150, 120)  # туловище
        if attempts == 0:
            self.canvas.create_line(150, 100, 130, 110)  # левая рука
            self.canvas.create_line(150, 100, 170, 110)  # правая рука
            self.canvas.create_line(150, 120, 130, 130)  # левая нога
            self.canvas.create_line(150, 120, 170, 130)  # правая нога