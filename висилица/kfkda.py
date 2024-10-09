import tkinter as tk
from random import choice

class Hangman:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Виселица")
        self.word = choice(["Лес", "горы", "река", "озеро", "море", "степь", "дерево", "цветок", "трава", "лесной куст", "плод", "животное", "птица", "рыба", "зверь", "насекомое", "солнце", "луна", "ветер", "дождь", "снег"])
        self.guesses = 5
        self.missed = 0
        self.label = tk.Label(self.root, text="Угадайте слово!", font=("Arial", 24))
        self.label.pack()
        self.entry = tk.Entry(self.root, font=("Arial", 24))
        self.entry.pack()
        self.button = tk.Button(self.root, text="Отправить", command=self.check_answer, font=("Arial", 18))
        self.button.pack()
        self.hangman_image = tk.Label(self.root, text="", font=("Arial", 24))
        self.hangman_image.pack()
        self.word_label = tk.Label(self.root, text="_ " * len(self.word), font=("Arial", 24))
        self.word_label.pack()

    def check_answer(self):
        answer = self.entry.get()
        if answer in self.word:
            self.label.config(text="Правильно!")
            self.update_word(answer)
        else:
            self.guesses -= 1
            self.label.config(text="Неправильно! Осталось попыток: " + str(self.guesses))
            self.draw_hangman()
        self.entry.delete(0, tk.END)

    def update_word(self, answer):
        word_list = list(self.word_label.cget("text"))
        for i in range(len(self.word)):
            if self.word[i] == answer:
                word_list[i*2] = answer
        self.word_label.config(text="".join(word_list))

    def draw_hangman(self):
        if self.guesses == 4:
            self.hangman_image.config(text="______")
        elif self.guesses == 3:
            self.hangman_image.config(text="______\n|")
        elif self.guesses == 2:
            self.hangman_image.config(text="______\n|/\n|")
        elif self.guesses == 1:
            self.hangman_image.config(text="______\n|/\n|/\n|")
        elif self.guesses == 0:
            self.hangman_image.config(text="______\n|/\n|/\n|/\n|")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = Hangman()
    game.run()