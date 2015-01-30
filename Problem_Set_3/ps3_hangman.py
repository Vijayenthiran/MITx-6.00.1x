# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string



WORDLIST_FILENAME = "C:\Users\Vijayenthiran\Documents\MITx_6.00.1x_Files\Problem_Set_3\words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
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
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    ans = False
    
    for e in secretWord:
        if e == lettersGuessed [:1]:
            ans = True
    return ans
    


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    ans = ""
    
    for e in secretWord:
        if e not in lettersGuessed:
            ans = ans + "_ "
        else:
            ans = ans + e + " "
    return ans

def _getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    ans = ""
    
    for e in secretWord:
        if e not in lettersGuessed:
            ans = ans + "_ "
        else:
            ans = ans + e
    return ans



def getAvailableLetters(secretWord, lettersGuessed, availableLetter):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    
    ans = ""
    if isWordGuessed(secretWord, lettersGuessed):
        for e in lettersGuessed:
            if e not in availableLetter:                
                print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)
                return availableLetter
            else:
                print "Good Guess: ",        
                print getGuessedWord(secretWord, lettersGuessed)
                for e in availableLetter:
                    if e not in lettersGuessed:
                        ans = ans + e
                return ans
    else:
        for e in availableLetter:
            if e not in lettersGuessed:
                        ans = ans + e
        return ans

def isAlreadyGuessed(secretWord, lettersGuessed, availableLetter,numberOfGuesses):
    
    if isWordGuessed(secretWord, lettersGuessed):
        for e in lettersGuessed:
            if e not in availableLetter:                
                #print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)
                return numberOfGuesses+1
            else:
                return numberOfGuesses
    else:
        return numberOfGuesses

    

def hangman(secretWord, numberOfGuesses = 8 , lettersGuessed = "",availableLetters = string.ascii_lowercase):
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

    if numberOfGuesses == 8:
        # Welcome message...
        print "Welcome to the game, Hangman!"
        print "I am thinking of a word that is " + str(len(secretWord)) + " letters long."
        print "-------------"
        print "You have " +str(8)+ " guesses left."
        lettersGuessed = ""
        availableLetters = string.ascii_lowercase
        print "Available letters: " + string.ascii_lowercase
        
    elif numberOfGuesses!=0:
        if _getGuessedWord(secretWord, lettersGuessed) == secretWord:
            print "-------------"
            print "Congratulations, you won!"
            return None
            
        print "You have " +str(numberOfGuesses)+ " guesses left."
        print "Available letters: " + availableLetters
        
    else:
        if _getGuessedWord(secretWord, lettersGuessed) == secretWord:
            print "-------------"
            print "Congratulations, you won!"
            return None
        else:
            print "-------------"
            print "Sorry, you ran out of guesses. The word was " + secretWord
            return None
          
    lettersGuessed = str(raw_input("Please guess a letter: ")).lower() + lettersGuessed
    
    if numberOfGuesses == 0:
        return None
    else:
        if isWordGuessed(secretWord, lettersGuessed) :            
            numberOfGuesses = isAlreadyGuessed(secretWord, lettersGuessed, availableLetters,numberOfGuesses)
            availableLetters = getAvailableLetters(secretWord, lettersGuessed, availableLetters)
            
        else:
            print "Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed)
            availableLetters = getAvailableLetters(secretWord, lettersGuessed, availableLetters)
        
        hangman(secretWord, numberOfGuesses -1, lettersGuessed,availableLetters)
        





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
#hangman("vijayen")