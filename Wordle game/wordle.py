import random # This is a library so we can use random words for our list 
print ('Welcome to the word guessing game!')

attempts = 0 #Attempts the user is going to have 
resolved = False #Is the game solved? 
word_list = ["nephi", "mouse", "phone", "oreos", "words", "beach", "dance", "earth"] #lists of words 
word = random.choice(word_list).lower() #Choosing a random word from the list 


# This is a list and it generates a list of underscores with the same length as the word
hint = ["_" for i in range(len(word))] 


#We are printing the underscores and the method join is to put spaces in between 
print("Hint: " + " ".join(hint)) 

while resolved == False: # As long as the word is not solved...
    
    guess = input('What is your guess? ').lower()
        
    # If the guess has the same length as the word then we will look for it, 
    # if not, then display message and plus an attempt 
    if len(guess) == len(word):

        attempts = attempts + 1 #Attempt every time we look for the word 

        for letter in guess:     #For every letter in guess       
            if letter in word:

            # Replacing the underscores with the letter found  
                for i in range(len(word)):
                    if word[i] == letter:
                        hint[i] = letter     
                
            pass #if the letter is not the correct one then we will pass to the next step 
                  
        #If the hint is the same as the word then the game is complete and we will display the attempts    
        if "".join(hint) == word:
            print(' '.join(hint))
            print('Congratulations You guessed it ')
            print(f'It took you {attempts} guesses')
            resolved = True    

        print(' '.join(hint)) #Printing the word    
    else:
        print ('Sorry, the guess must have the same number of letters as the secret word.')    
        attempts = attempts + 1 
        resolved = False # Go back again