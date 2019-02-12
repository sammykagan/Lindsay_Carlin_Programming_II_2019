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

word_list = ["two", "three", "four", "eleven"]
word = word_list[random.randrange(4)]
correct_guesses = 0
word_letters = []
guessed_letters = []
incorrect_guesses = 0
hangman_pic = 0
done = False
for i in range(len(word)):
    print("_ ", end="")
while not done:
    print(HANGMANPICS[hangman_pic])
    guess = input("\nYour guess: ")
    if guess.lower() in guessed_letters:
        print("You already guessed that, silly!")
    guessed_letters.append(guess)
    if guess.lower() in word.lower():
        correct_guesses += 1
        word_letters.append(guess.lower())
        for letter in word.lower():
            if letter in word_letters:
                print(letter + " ", end = "")
            else:
                print("_ ", end = "")
    else:
        incorrect_guesses += 1
        hangman_pic += 1
        print(HANGMANPICS[hangman_pic])
    if incorrect_guesses > 6:
        print("You lost!")
        print("The word was ", + word)
        done = True
    if correct_guesses == len(word):
        done = True
        print("\nYou won! Want to play again?")


# if the guess is correct, add it to the word in the corresponding blank
# if the incorrect_guesses is greater than 6, tell the user they lost and exit the program
# if correct_guesses is equal to the length of the word, tell the user they won
# ask if they want to play again


