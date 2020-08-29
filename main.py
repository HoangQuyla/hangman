import pygame
import random
##Displaying window size and drawing a window of a game
pygame.init()
win_height = 480
winWidth = 700
win=pygame.display.set_mode((winWidth,win_height))

# initialize global variables/constants #
BLACK = (0,0, 0)
WHITE = (255,255,255)
RED = (255,0, 0)
GREEN = (0,255,0)
BLUE = (0,0,255)
LIGHT_BLUE = (102,255,255)

btn_font = pygame.font.SysFont("arial", 20)
guess_font = pygame.font.SysFont("monospace", 24)
lost_font = pygame.font.SysFont('arial', 45)
word = ''
buttons = []
guessed = []
lostTxt = 'You Lost, press any key to play again...'
winTxt = 'WINNER!, press any key to play again...'
hangmanPics = [pygame.image.load('hangman0.png'), pygame.image.load('hangman1.png'), pygame.image.load('hangman2.png'), pygame.image.load('hangman3.png'), pygame.image.load('hangman4.png'), pygame.image.load('hangman5.png'), pygame.image.load('hangman6.png')]

limbs = 0

## The function is used to draw a backgrond of the game and all the buttons which representing a letter inside the game
def redraw():
    global guessed
    global hangmanPics
    global limbs
    win.fill(GREEN)
    # Buttons. The for loop will is used to draw all buttons and label them
    for i in range(len(buttons)):
        if buttons[i][4]:
            pygame.draw.circle(win, BLACK, (buttons[i][1], buttons[i][2]), buttons[i][3])
            pygame.draw.circle(win, buttons[i][0], (buttons[i][1], buttons[i][2]), buttons[i][3] - 2
                               )
            label = btn_font.render(chr(buttons[i][5]), 1, BLACK)
            win.blit(label, (buttons[i][1] - (label.get_width() / 2), buttons[i][2] - (label.get_height() / 2)))

    spaced = spacedOut(word, guessed)## this variable is stored a word after comparing a guess letter with a word from a list
    label1 = guess_font.render(spaced, 1, BLACK)## label letters
    rect = label1.get_rect()
    long = rect[2]
    
    win.blit(label1,(winWidth/2 - long/2, 400))

    picture = hangmanPics[limbs]## storing picture of hanging a man
    win.blit(picture, (winWidth/2 - picture.get_width()/2 + 20, 150))
    pygame.display.update()
    
##This function will generate a word from a file words.txt and it will return that word
def randomWord():
    file = open('words.txt')
    f = file.readlines()
    i = random.randrange(0, len(f) - 1)
    word = f[i][:-1]

    return word

##This function will check if any guess word imported from a player will be in lower case or not
def hang(guess):
    global word
    if guess.lower() not in word.lower():
        return True
    else:
        return False

## This function will compare a generated word with any guess letter from a player. If a player guess correctly a letter it will be replaced and if not, it will remain "_"
def spacedOut(word, guessed=[]):
    spacedWord = ''
    guessedLetters = guessed
    for x in range(len(word)):
        if word[x] != ' ':
            spacedWord += '_ '
            for i in range(len(guessedLetters)):
                if word[x].upper() == guessedLetters[i]:
                    spacedWord = spacedWord[:-2]
                    spacedWord += word[x].upper() + ' '
        elif word[x] == ' ':
            spacedWord += ' '
    return spacedWord

##This function will check if buttons are pressed or not. If a button is pressed the function will return that button, otherwise it will return non.            
def button_pressed(x, y):
    for i in range(len(buttons)):
        if x < buttons[i][1] + 20 and x > buttons[i][1] - 20:
            if y < buttons[i][2] + 20 and y > buttons[i][2] - 20:
                return buttons[i][5]
    return None

##This function will end the game.
def end(winner=False):
    global limbs
    lostTxt = 'You Lost, press any key to play again...'
    winTxt = 'WINNER!, press any key to play again...'
    redraw()
    pygame.time.delay(1000)
    win.fill(GREEN)
## If a winner guess all correct word, a winning word word will be displayed, otherwise, the losing text will be displayed
    if winner == True:
        label = lost_font.render(winTxt, 1, BLACK)
    else:
        label = lost_font.render(lostTxt, 1, BLACK)

    wordTxt = lost_font.render(word.upper(), 1, BLACK)
    wordWas = lost_font.render('The phrase was: ', 1, BLACK)

    win.blit(wordTxt, (winWidth/2 - wordTxt.get_width()/2, 295))
    win.blit(wordWas, (winWidth/2 - wordWas.get_width()/2, 245))
    win.blit(label, (winWidth / 2 - label.get_width() / 2, 140))
    pygame.display.update()
    ## The function below will keep the game playing if a player wants to play more. Either winning or losing, a player can continue to play
    again = True
    while again:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                again = False
    reset()

## This function will reset the game if the player wants to replay the game
def reset():
    global limbs
    global guessed
    global buttons
    global word
    for i in range(len(buttons)):
        buttons[i][4] = True

    limbs = 0
    guessed = []
    word = randomWord()


# Setup buttons
increase = round(winWidth / 13)
for i in range(26):
    if i < 13:
        y = 40
        x = 25 + (increase * i)
    else:
        x = 25 + (increase * (i - 13))
        y = 85
    buttons.append([LIGHT_BLUE, x, y, 20, True, 65 + i])
    # buttons.append([color, x_pos, y_pos, radius, visible, char])

word = randomWord()
##The main function to play the game
def play():
    global limbs
    inPlay = True
    while inPlay:
        ##function redraw is call
        redraw()
        ## setting the time delay of the game
        pygame.time.delay(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                inPlay = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    inPlay = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                ##Geting the mouse possition and compared it and stored in a letter variable
                clickPos = pygame.mouse.get_pos()
                letter = button_pressed(clickPos[0], clickPos[1])
                ## if the letter is not none, the guess will append the letter
                if letter != None:
                    guessed.append(chr(letter))
                    buttons[letter - 65][4] = False
                    ## if the hang function is called, the limbs variable continues to increase until it reach 5 otherwise the program will end if the limbs variable = 5
                    if hang(chr(letter)):
                        if limbs != 5:
                            limbs += 1
                        else:
                            end()
                    else:
                        ##print a comparation ofa generated word with a guessed 
                        print(spacedOut(word, guessed))
                        ## if the count of  "_"  is zero, the game will end
                        if spacedOut(word, guessed).count('_') == 0:
                            end(True)

play()
#quit a game
pygame.quit()

