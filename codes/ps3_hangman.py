# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

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

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
word_list = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
#    won = None
#    
#    for l in secretWord:
#        if l in lettersGuessed:
#            won = True
#        else:
#            won = False
#            break
#        
#    return won

    return set(secretWord).issubset(lettersGuessed)



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    
    ltr = []
    
    for l in secretWord:
        if l not in lettersGuessed:
            ltr.append('_ ')
        else:
            ltr.append(l)
            
    return ''.join(ltr)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    
    return ''.join(sorted(set(string.ascii_lowercase) - set(lettersGuessed)))
    

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
    
    print('Welcome to the game Hangman!')
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    
    
    lettersGuessed = []
    nGuesses = 8
    #availableLetters = string.ascii_lowercase
    
    while True:
        print('-' * 13)
        print('You have', nGuesses, 'guesses left.')
        print('Available letters: ' + getAvailableLetters(lettersGuessed), end='')
        lg = input('Please guess a letter: ').lower()
        
        if lg not in lettersGuessed:
            lettersGuessed.append(lg)
            
            if lg in secret_word:
                print('Good guess:', getGuessedWord(secret_word, lettersGuessed))
            
            else:
                print('Oops! That letter is not in my word:', getGuessedWord(secret_word, lettersGuessed))
                nGuesses -= 1
        
        else:
            print("Oops! You've already guessed that letter:", getGuessedWord(secret_word, lettersGuessed))
            
        
        if isWordGuessed(secret_word, lettersGuessed):
            print('-' * 13)
            print('Congratulations, you won!')
            break
        
        if nGuesses <= 0:
            print('-' * 13)
            print('Sorry, you ran out of guesses. The word was ' + secret_word + '.')
            break


secret_word = chooseWord(word_list)
hangman(secret_word)


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
