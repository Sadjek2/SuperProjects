from data.filemanager import *

def Main(letter):
    global attempts
    if letter in word:
        for i, char in enumerate(word):
            if char == letter:
                player_word[i] = letter
    else:
        attempts -= 1
        print(f"You have {attempts} attempts left")

    print(" ".join(player_word))

    if "_" not in player_word:
        print("Congratulations, you've guessed the word!")
        time.sleep(5)
        sys.exit()
    if attempts == 0:
        print(f"Sorry, but you are lost the game :(\nThe word is: {"".join(word)}")
        time.sleep(5)
        sys.exit()
