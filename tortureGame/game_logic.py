import random

#список слов на тему природа
nature_words = ['лесопарк', 'горы', 'озеро', 'пещера', 'водопады', 'ландшафт', 'природный', 'речной', 'лесной', 'гористый', 'каменист', 'деревня', 'птичник', 'рыболов', 'экосистема']
#случайно выбранное слово из списка nature_words
selected_word = random.choice(nature_words)
unique_letters = set(selected_word)
#количество попыток (жизней) для отгадывания слова, исходя из кол-ва
#уникальных букв в слове
attemtps = len(unique_letters)
guessed_letters = ["_"] * len(selected_word)

#print(selected_word, attemtps, unique_letters)

def find_unique_letter(c, word):
    indices = []
    index = word.find(c)
    while index != -1:
        indices.append(index)
        index = word.find(c, index + 1)
    return indices

for i in range(attemtps):
    letter = input()[:1]
    
    if letter not in unique_letters:
        attemtps -= 1
        print("Осталось попыток:", attemtps)
        print(guessed_letters)
    elif letter in unique_letters:
        

        
        
        





