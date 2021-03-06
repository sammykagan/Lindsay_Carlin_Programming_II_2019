'''
Make a text based version of hangman (25pts)
Use the sample run as an example.  Try to make it as close as possible to the example. (or better)
'''
import random

# PSEUDOCODE
# make a word list for your game
# grab a random word from your list and store it as a variable
# display the hangman
# display the used letters
# display the length of the word to the user using blank spaces
# prompt the user to guess a letter
# if the guess is correct increment correct_guesses by 1
# if the guess is incorrect increment incorrect_guesses by 1 and draw the next part of the hangman
# don't allow the user to select the same letter twice
# if the incorrect_guesses is greater than 6, tell the user they lost and exit the program
# if correct_guesses is equal to the length of the word, tell the user they won
# ask if they want to play again

# Feel free to use this list of ascii art for your game

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
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

word_list = ["python", "javascript", "swift", "ada", "ruby", "html", "css"]
word = word_list[random.randrange(4)]
word_letters = []
guessed_letters = []
incorrect_guesses = 0
hangman_pic = 0
done = False
for i in range(len(word)):
    print("_ ", end="")
while not done:
    correct_guesses = 0
    letters_remaining = len(word)
    print(HANGMANPICS[hangman_pic])
    guess = input("\nYour guess: ")
    if guess.lower() in guessed_letters:
        print("You already guessed that, silly!")
    if guess.lower() not in guessed_letters:
        guessed_letters.append(guess)
    if guess.lower() in word.lower():
        if guess.lower() not in guessed_letters:
            correct_guesses += 1
        word_letters.append(guess.lower())
    else:
        incorrect_guesses += 1
        hangman_pic += 1
    for letter in word.lower():
        if letter in word_letters:
            print(letter + " ", end="")
            letters_remaining -= 1
        else:
            print("_ ", end="")
    if incorrect_guesses > 6:
        print("You lost!")
        print("The word was ", word)
        done = True
    if letters_remaining == 0:
        done = True
        print("\nYou won! Want to play again?")