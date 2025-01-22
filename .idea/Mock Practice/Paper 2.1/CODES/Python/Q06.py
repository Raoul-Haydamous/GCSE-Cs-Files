# Q06
import random

def generateWord(pWords):
    # Fully completed function that generates and returns a secret word
    randomNum = random.randint(0,len(pWords)-1)
    secretWord = pWords[randomNum]
    return secretWord

# Add your subprograms here




#---------------------------------------------------------------------------------------
# End of subprograms and start of main program from here

# Array of words
words = ["antelope","ape","badger","bear","beaver","bison","crocodile","elephant",
         "elk","ferret","goat","goose","kangaroo","llama","lion","monkey","moose",
         "orangutan","shark","snake","tiger","whale","wombat"]

# Secret word is generated. 
wordToGuess = generateWord(words)

# Add your main program code here