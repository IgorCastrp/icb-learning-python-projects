# Hangman Game
# OOP

# Import
import random

# Board
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

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
/|\\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\\  |
/ \\  |
     |
=========''']


# Class
class Hangman:

# Constructor Method
    def __init__(self, word):
        self.word = word
        print(self.word)
        self.word_list = ["_" for _ in word]
        self.correct_chars = []
        self.wrong_chars = []

# Method to guess the letter

    def guess(self):
        char_guessed = input('Type a letter: ')
        if char_guessed in self.correct_chars or char_guessed in self.wrong_chars:
            print('Character already guessed, type a different character')
            self.guess()
        else:
            for index, char in enumerate(self.word):
                if char_guessed == char:
                    self.word_list[index] = char_guessed
            if char_guessed in self.word and char_guessed not in self.correct_chars:
                    self.correct_chars.append(char_guessed)
            elif char_guessed not in self.wrong_chars:
                self.wrong_chars.append(char_guessed)


# Method to check if the game is over
    def game_over(self):
        if self.game_won() or len(self.wrong_chars) == 6:
            self.board()
            if len(self.wrong_chars) == 6:
                print(f'You Lost, the correct word is: {self.word}')
            else:
                print(f'You Win, the correct word is: {self.word}')
            return True
        else:
            return False

# Method to check if the player won
    def game_won(self):
        if "_" not in self.word_list:
            return True
        else:
            return False

# Method to hide the letter on the board

# Method to check the game status and print the board on the screen

    def board(self):
        print(board[len(self.wrong_chars)])
        print(f'Word: {self.word_list}')
        print(f'Correct chars: {self.correct_chars}\tWrong chars: {self.wrong_chars}')

def random_word():
    list_words = ['apple', 'banana', 'orange', 'pineapple', 'strawberry', 'lemon']
    return random.choice(list_words)

def main():
    game = Hangman(random_word())
    while not game.game_over():
        game.board()
        game.guess()

if __name__ == '__main__':
    main()

