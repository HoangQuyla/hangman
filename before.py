import random
from collections import Counter

wordList = '''Coffee maker
Blender
Mixer
Toaster
Microwave
Crock pot
Rice cooker
Pressure cooker
Bachelor griller (U.K)
Stove
Lamp
Light bulb
Lantern
Torch
Clothes iron
Electric drill
Kettle
Water cooker (U.K)/ Electric kettle/ Hot pot (U.S)
Water purifier
Kitchen hood
Electric guitar
Vacuum cleaner
Electric fan
Evaporative cooler
Air conditioner
Oven
Dishwasher
Television
Speaker
Clothes dryer
Washing machine
Refrigerator '''
wordList = wordList.split(' ')
word = random.choice(wordList)

if __name__=='__main__':
    print('Guess the word! Hint word is a name of a household appliance')
    for i in word: 
         # For printing the empty spaces for letters of the word 
        print('_', end = ' ')         
    print()
    played = True
     # list for storing the letters guessed by the player 
    Guessed = ''                 
    chances = len(word) + 2
    correct = 0
    flag = 0
    try: 
        while (chances != 0) and flag == 0: #flag is updated when the word is correctly guessed  
            print() 
            chances -= 1
  
            try: 
                inputGuess = str(input('Enter a letter to guess: ')) 
            except: 
                print('Enter only a letter!') 
                continue
  
            # Validation of the guess 
            if not inputGuess.isalpha(): 
                print('Enter only a LETTER') 
                continue
            elif len(inputGuess) > 1: 
                print('Enter only a SINGLE letter') 
                continue
            elif inputGuess in Guessed: 
                print('You have already guessed that letter') 
                continue
            # If letter is guessed correctly 
            if inputGuess in word: 
                k = word.count(inputGuess) #k stores the number of times the guessed letter occurs in the word 
                for _ in range(k):     
                    Guessed += inputGuess # The guess letter is added as many times as it occurs 
  
            # Print the word 
            for char in word: 
                if char in Guessed and (Counter(Guessed) != Counter(word)): 
                    print(char, end = ' ') 
                    correct += 1
                # If user has guessed all the letters 
                elif (Counter(Guessed) == Counter(word)): # Once the correct word is guessed fully,  
                                                                # the game ends, even if chances remain 
                    print("The word is: ", end=' ') 
                    print(word) 
                    flag = 1
                    print('Congratulations, You won!') 
                    break # To break out of the for loop 
                    break # To break out of the while loop 
                else: 
                    print('_', end = ' ') 
  
              
  
        # If user has used all of his chances 
        if chances <= 0 and (Counter(Guessed) != Counter(word)): 
            print() 
            print('You lost! Try again..') 
            print('The word was {}'.format(word)) 
  
    except KeyboardInterrupt: 
        print() 
        print('Bye! Try again.') 
        exit() 
