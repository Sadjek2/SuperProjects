import random

# List of words
list_of_words = ["apple", "banana", "cherry", "date", "elderberry"]

# Select a random word from the list
def select_random_word(list_of_words):
    return random.choice(list_of_words)

# Count unique letters in a word
def count_unique_letters(word):
    return len(set(word))

# Get user input (a single letter)
def user_input():
    while True:
        user_input = input("Enter a letter: ").strip().lower()
        if len(user_input) == 1:
            return user_input
        else:
            print("Please enter a single letter.")

# Count attempts
def count_attempts(attempts):
    return attempts + 1

# Find indices of a letter in a word
def letter_indices(c: str, word: str):
    indices = [i for i, letter in enumerate(word) if letter == c]
    return indices

# Find a letter in a set of unique letters
def find_letter_in_set(c: str, unique_letters_set: set):
    return c in unique_letters_set

# Main game loop
def hangman():
    word = select_random_word(list_of_words)
    unique_letters = set(word)
    attempts = 0
    guessed_letters = set()

    while True:
        letter = user_input()
        attempts = count_attempts(attempts)
        if find_letter_in_set(letter, unique_letters):
            guessed_letters.add(letter)
            print("Good guess!")
        else:
            print("Oops, try again!")

        # Check if the user has guessed the word
        if all(letter in guessed_letters for letter in unique_letters):
            print("Congratulations, you won!")
            break

        # Print the current state of the word
        print(" ".join([letter if letter in guessed_letters else "_" for letter in word]))

if __name__ == "__main__":
    hangman()

        
            

