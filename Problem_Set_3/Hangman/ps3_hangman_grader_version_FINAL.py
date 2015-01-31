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
                print "Oops! You've already guessed that letter: " + getGuessedWord_(secretWord, lettersGuessed)
                return availableLetter
            else:
                print "Good Guess: ",        
                print getGuessedWord_(secretWord, lettersGuessed)
                print "-----------"
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
    #if isWordGuessed_(secretWord, lettersGuessed):
        for e in lettersGuessed:
            if e not in availableLetter:                
                return numberOfGuesses+1    #Already guessed
            else:
                return numberOfGuesses
   # else:
       # return numberOfGuesses

    

def hangman(secretWord, numberOfGuesses = 8 , lettersGuessed = "",availableLetters = string.ascii_lowercase, firstTime = 1): #used default value in the functions..
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
    
    if firstTime == 1:
        
        # Welcome message...  and initialiation
        
        print "Welcome to the game, Hangman!"
        print "I am thinking of a word that is " + str(len(secretWord)) + " letters long."
        print "-------------"
        lettersGuessed = ""
        availableLetters = string.ascii_lowercase
        print "You have " +str(8)+ " guesses left."
        print "Available letters: " + string.ascii_lowercase
        
    elif numberOfGuesses == 8 and _getGuessedWord(secretWord, lettersGuessed) != secretWord: #if the first guess word is correct it will enter this loop
               
        print "You have " +str(8)+ " guesses left."        
        print "Available letters: " + availableLetters
        
    elif numberOfGuesses!=0:
        if _getGuessedWord(secretWord, lettersGuessed) == secretWord: #winning condition
            #print "-----------"
            print "Congratulations, you won!"
            return None #Base case for the recurssion function
            
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
            if numberOfGuesses != isAlreadyGuessed_(secretWord, lettersGuessed, availableLetters,numberOfGuesses):
                print "Oops! You've already guessed that letter: " + getGuessedWord_(secretWord, lettersGuessed)
                print "-----------"
                numberOfGuesses = isAlreadyGuessed_(secretWord, lettersGuessed, availableLetters,numberOfGuesses)
            else:                
                numberOfGuesses = isAlreadyGuessed_(secretWord, lettersGuessed, availableLetters,numberOfGuesses)
                availableLetters = getAvailableLetters_(secretWord, lettersGuessed, availableLetters)
                numberOfGuesses += 1
        else:
            #print str(isAlreadyGuessed_(secretWord, lettersGuessed, availableLetters,numberOfGuesses))
            #print str(numberOfGuesses)
            if numberOfGuesses != isAlreadyGuessed_(secretWord, lettersGuessed, availableLetters,numberOfGuesses):
                print "Oops! You've already guessed that letter: " + getGuessedWord_(secretWord, lettersGuessed)
                print "-----------"
                numberOfGuesses = isAlreadyGuessed_(secretWord, lettersGuessed, availableLetters,numberOfGuesses)
            else:                    
                print "Oops! That letter is not in my word: " + getGuessedWord_(secretWord, lettersGuessed)
                print "-----------"
                availableLetters = getAvailableLetters_(secretWord, lettersGuessed, availableLetters)
                
        hangman(secretWord, numberOfGuesses -1, lettersGuessed,availableLetters,0) #recursion function. Note that the number of guesses is reduced by one, the letter guessed and availble letter will be changed, 0 represents not first time.
        





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

#secretWord = chooseWord(wordlist).lower()
#hangman(secretWord)
hangman("sea")