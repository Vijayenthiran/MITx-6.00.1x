# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import string



def isWordGuessed_(secretWord, lettersGuessed):
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
    


def getGuessedWord_(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    ans = ""
    
    for e in secretWord:
        if e not in lettersGuessed:
            ans = ans + "_"
        else:
            ans = ans + e
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



def getAvailableLetters_(secretWord, lettersGuessed, availableLetter):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    
    ans = ""
    if isWordGuessed_(secretWord, lettersGuessed):
        for e in lettersGuessed:
            if e not in availableLetter:                
                print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)
                return availableLetter
            else:
                print "Good Guess: ",        
                print getGuessedWord_(secretWord, lettersGuessed)
                for e in availableLetter:
                    if e not in lettersGuessed:
                        ans = ans + e
                return ans
    else:
        for e in availableLetter:
            if e not in lettersGuessed:
                        
                        ans = ans + e
                        
        return ans

def isAlreadyGuessed_(secretWord, lettersGuessed, availableLetter,numberOfGuesses):
    #print availableLetter
    
    for e in lettersGuessed:
        if e not in availableLetter:                
            print "prob" 
            return numberOfGuesses+1    #Already guessed
            
        else:
            return numberOfGuesses
    

flag = 0  

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
    global flag
    if numberOfGuesses == 8 and flag != 1:
        # Welcome message...
        print "Welcome to the game, Hangman!"
        print "I am thinking of a word that is " + str(len(secretWord)) + " letters long."
        print "-------------"
        print "You have " +str(8)+ " guesses left."
        lettersGuessed = ""
        availableLetters = string.ascii_lowercase
        flag=0
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
            #print "-------------"
            print "Sorry, you ran out of guesses. The word was " + secretWord
            return None
          
    lettersGuessed = str(raw_input("Please guess a letter: ")) + lettersGuessed
    lettersGuessed = lettersGuessed.lower()
    if numberOfGuesses == 0:
        return None
    else:
        if isWordGuessed_(secretWord, lettersGuessed) :            
            numberOfGuesses = isAlreadyGuessed_(secretWord, lettersGuessed, availableLetters,numberOfGuesses)
            availableLetters = getAvailableLetters_(secretWord, lettersGuessed, availableLetters)
            
            print "-----------"
        else:
            availableLetters = getAvailableLetters_(secretWord, lettersGuessed, availableLetters)
            #print availableLetters
            if numberOfGuesses != isAlreadyGuessed_(secretWord, lettersGuessed, availableLetters,numberOfGuesses):
                numberOfGuesses += 1
                print "Oops! You've already guessed that letter: " +  getGuessedWord_(secretWord, lettersGuessed)                
            else:
                print "Oops! That letter is not in my word: " + getGuessedWord_(secretWord, lettersGuessed)
            print "-----------"
            
            flag=0
            
        if flag == 0:
            hangman(secretWord, numberOfGuesses -1, lettersGuessed,availableLetters)
        else:
            hangman(secretWord, numberOfGuesses, lettersGuessed,availableLetters)
        





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

#secretWord = chooseWord(wordlist).lower()
#hangman(secretWord)
hangman("y")