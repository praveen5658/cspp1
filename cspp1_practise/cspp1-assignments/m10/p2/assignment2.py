'''
Author : Praveen
Date : 09-08-2018
'''

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


wordlist = loadWords()

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    str_ing = 'abcdefghijklmnopqrstuvwxyz'
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is ",len(secretWord)," letters long.")
    print("-----------")
    lis_t = list(secretWord)
    list_string = list(str_ing)
    temp_string = ""
    guess = 8
    guess_list = []
    won = 0
    for lo_op in secretWord:
        temp_string += '_'
    alpha = list(temp_string)
    while(guess > 0):
        if ''.join(alpha) == secretWord:
            won = 1
            print("Congratulations, you Won!")
            break
        print("You have ",guess,"guesses left.")
        print("Available Letters : ",''.join(list_string))
        print("Please guess a letter ")
        le_tter = input()
        if le_tter in guess_list:
            print("Oops! You have already entered the letter")
            print("-----------")
        else:
            guess_list.append(le_tter)
            if le_tter in lis_t:
                for lo_op in range(len(secretWord)):
                    if le_tter == secretWord[lo_op]:
                        alpha[lo_op] = le_tter
                list_string.remove(le_tter)
                print("Good Guess : ",''.join(alpha))
            else:
                guess -=1
                list_string.remove(le_tter)
                print("Oops! That letter is not in my word: ",''.join(alpha))
            print("-----------")
    if won == 0:
        print("Sorry, you ran out of guesses. The word was :",secretWord)


def main():
    '''
    Main function for the given program
    
    When you've completed your hangman function, uncomment these two lines
    and run this file to test! (hint: you might want to pick your own
    secretWord while you're testing)
    '''
    secretWord = chooseWord(wordlist).lower()
    hangman(secretWord)


if __name__ == "__main__":
    main()
