import random

HANGMAN_PICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +--- +
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = 'абрикос аист акула акварель алмаз анархия апельсин арбуз аргон астра атом бадминтон банан барсук баскетбол белка берет библиотека'.split()

def getRandomWord(wordList):
    # Эта функция выбирает случайное слово из списка.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(HANGMAN_PICS, missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Неправильных букв:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # Замена знаков "_" на угаданные игроком буквы
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: # Отображение букв в строчке для угаданных букв
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    # Если возникают какие либо проблемы при вводе букв игроком и их решения.
    while True:
        print('Угадай букву.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Введите только одну букву.')
        elif guess in alreadyGuessed:
            print('Вы уже писали эту букву. Выберите другую.')
        elif guess not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            print('Введите букву на кирилице.')
        else:
            return guess

def playAgain():
    # Вопрос к игроку в конце игры (хочет ли он сыграть еще).
    print('Сыграть еще? (да или нет)')
    return input().lower().startswith('д')

print('В И С И Л И Ц А')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(HANGMAN_PICS, missedLetters, correctLetters, secretWord)

    # Возможность писать буквы игроку.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Игрок победил
        foundAllLetters = True
        for i in range(len(secretWord)): # Комментирование в случае победы
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Да! Слово: "' + secretWord + '"! Победа!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Объяснение ошибок игроку в конце игры
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(HANGMAN_PICS, missedLetters, correctLetters, secretWord)
            print('Нет больше попыток!\nИтоги: ' + str(len(missedLetters)) + ' неугаданных букв ' + str(len(correctLetters)) + ' угаданных букв, слово - "' + secretWord + '"')
            gameIsDone = True

    # Возможность начать игру заново для игрока.
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break