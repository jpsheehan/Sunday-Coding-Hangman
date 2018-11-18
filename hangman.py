'''A simple game of Hangman for one person.
The original wordlists are from https://github.com/first20hours/google-10000-english'''

from random import choice
from utils import HANGED_MAN, NUM_STAGES

def main():
    '''The main function where we start the game.'''
    words = read_word_file('wordlists/google-10000-english.txt')
    secret_word = choice(words)

    print('Welcome to Hangman!')

    guesses = []
    failures = 0

    while True:
        print(HANGED_MAN[failures])
        print_guessed_word(secret_word, guesses)
        if len(guesses) > 0:
            print('You\'ve already tried', ', '.join(guesses))

        if failures == NUM_STAGES - 1:
            print('He ded. You lose')
            break

        print('Enter your guess:')
        guess = input('> ').lower()

        # check the length of the guess
        if len(guess) is not 1:
            print('One letter at a time!!!')
            continue

        # check if the player has guesses this before
        if guess in guesses:
            print('You already tried that!')
            continue
        
        # make sure that the guess is a letter
        if guess.isalpha() is not True:
            print('You must guess a letter!')
            continue
        
        # we know that we have a valid guess
        guesses.append(guess)

        if guess in secret_word:
            print('That letter is in the word!')
        else:
            print('That letter was wrong.')
            failures = failures + 1
        
        if check_victory(secret_word, guesses) is True:
            print('Congratulations! You\'ve won the game!')
            break
    
    print('The secret word was', secret_word)
    

        
def check_victory(secret_word, guesses):
    '''Checks whether the game has been won. Returns True if the game is won.'''
    for secret_letter in secret_word:
        if secret_letter not in guesses:
            return False
    return True

def print_guessed_word(secret_word, guesses):
    '''Prints the secret_word with underscores where the letter has not been guessed.'''
    for secret_letter in secret_word:
        if secret_letter in guesses:
            print(secret_letter, end='')
        else:
            print('-', end='')
    print()

def read_word_file(filename):
    '''Reads a file containing words and returns a list of words.'''
    wordfile = open(filename)
    lines = wordfile.readlines()
    newlist = []
    for line in lines:
        word = line.strip()
        if len(word) >= 5:
            newlist.append(word)
    wordfile.close()
    return newlist
    # return [line.strip() for line in open(filename).readlines() if len(line.strip()) >= 5]


if __name__ == '__main__':
    main()