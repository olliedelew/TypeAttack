## Imported classes/dictionaries/functions 
import pygame
import time
import random

# Initialise pygame 
pygame.init()

## Variables for the dimensions of the screen size
screen_width = 1600
screen_height = 800

## Colours list
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
Dred = (175,26,26)
blueish = (33,88,188)
Dblue = (10,65,168) 
blue = (0,0,255)
green = (0,255,0)
Dgreen = (26,153,24)

## Creates a screen with the dimensions of the variables screen_width and screen_height
screen = pygame.display.set_mode((screen_width,screen_height)) 

## Create different size fonts
small = pygame.font.SysFont("freesansbold.ttf", 25)
medium = pygame.font.SysFont("freesansbold.ttf", 50)
large = pygame.font.SysFont("freesansbold.ttf", 100)

## Creates a caption at the top of the screen saying the name of the game.
pygame.display.set_caption("Type Attack")
## Creates a clock  
clock = pygame.time.Clock()

## Create the images for the sprites
shooter_image = pygame.image.load("shooter.png")
enemy_image = pygame.image.load("enemy.png")

## Create an enemy function at a given x and y coordinate and a given word
def Enemies(cordx,cordy,word, isActivated):
    screen.blit(enemy_image,(cordx,cordy))
    ## Checks if the enemy has been activated due to the user typing the
    ## first character of the corrosponding word
    if isActivated:
        ## Draws a white rectangle
        pygame.draw.rect(screen,white,[cordx+29,cordy+50,110,25])
    else:
        ## Draws a green rectangle    
        pygame.draw.rect(screen,green,[cordx+29,cordy+50,110,25])
    ## Displays the word text in the rectangles
    word_text(word,black,cordx+29,cordy+50,110,25)

## Display word text function
def word_text(text,colour,buttonx,buttony,buttonwidth,buttonheight,size = "small"):
    TextSurf, TextRect = text_objects(text, colour, size)
    ## Centres the text in the middle of the rectangle
    TextRect.center = ((buttonx+(buttonwidth/2)), (buttonheight/2)+buttony)
    ## Displays the text
    screen.blit(TextSurf,TextRect)

## Renders the text depending on the size given
def text_objects(text, colour, size):
    if size == "small":
        textSurface = small.render(text, True, colour)
    elif size == "medium":
        textSurface = medium.render(text, True, colour)
    elif size == "large":
        textSurface = large.render(text, True, colour)

    return textSurface, textSurface.get_rect()

## Displays a message on the screen at a given position in large font
def message_display(text, colour, y_displace=0, size = "large"):
    TextSurf, TextRect = text_objects(text, colour, size)
    ## Centers the text in the middle of the screen but moves it up or down depending on the y displacement
    TextRect.center = ((screen_width/2),(screen_height/2)+y_displace)
    ## Displays the text to the screen
    screen.blit(TextSurf, TextRect)

## Create the shooter at a given x and y coordinate
def shooter(x,y):
    ## Displays the shoote image
    screen.blit(shooter_image,(x,y))

## Display text in the middle of a button function
def button_text(text,colour,buttonx,buttony,buttonwidth,buttonheight,size = "medium"):
    TextSurf, TextRect = text_objects(text, colour, size)
    ## Finds the midpoint of the button and writes the text there
    TextRect.center = ((buttonx+(buttonwidth/2)), (buttonheight/2)+buttony)
    ## Displays the text to the screen
    screen.blit(TextSurf,TextRect)

## Create a button function with a given text, x and y coordinate, height, colour and action
def button(text,x,y,width,height,darkcolour,lightcolour,action = None):
    ## Gets the mouse position on the screen and saves it to the mouse variable
    mouse = pygame.mouse.get_pos()
    ## Checks if the mouse has been clicked and saves it to the click variable
    click = pygame.mouse.get_pressed()
    ## Checks if the mouse is inside the button    
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        ## Makes colour of the button lighter
        pygame.draw.rect(screen,lightcolour,(x,y,width,height))
        ## Checks if the button has been clicked
        if click[0] == 1 and action != None:
            ## If the quit button is clicked then the action "Quit" is started
            if action == "quit":
                ## Quits the game
                pygame.quit()
                quit()
            ## If the biology button is clicked then the action "biology" is started
            elif action == "biology":
                textfile = "biology.txt"
                ## Open and read the biology textfile
                with open(textfile,"r") as f:
                    words = f.readlines()
            ## If the play button is clicked then the action "play" is started
            elif action == "play":
                textfile = "random.txt"
                ## Open and read the random words textfile
                with open(textfile,"r") as f:
                    words = f.readlines()
            ## Start the GameLoop depending on the action started
            GameLoop(words)
    else:
        ## Makes the colour of the button dark
        pygame.draw.rect(screen,darkcolour,(x,y,width,height))
    ## Displays the button text
    button_text(text,black,x,y,width,height)

## Function to create and use the Main Menu screen
def MainMenu():
    ## Set the boolean variable "menu" to true
    menu = True
    ## While loop that continues until the "menu" variable is false
    while menu:
        ## Checks if the game has been exited
        for event in pygame.event.get():
            ## If the game has been exited then
            if event.type == pygame.QUIT:
                ## Quit pygame and quit python
                pygame.quit()
                quit()

        ## Fill the background of the screen in white
        screen.fill(white)
        ## List of messages to be displayed on screen
        message_display("Type Attack", blueish, -150, "large")
        message_display("Type the words as quick as you can", black, -80, "medium")
        message_display("Dont let the enemies touch you or you will die!", black, -20, "medium")
        ## Creating "Random words" button, "Biology keywords" button and "Quit" button
        ## Which, when clicked, start a specific action
        button("Random words", 175, 600, 300, 75, Dgreen, green, action = "play")
        button("Biology keywords", 650,600,300,75, Dblue, blue, action = "biology")
        button("Quit", 1125,600,300,75, Dred, red, action = "quit")
        ## Update the display
        pygame.display.update()
        ## FPS                
        clock.tick(15)

    ## Ends the while loop
    Menu = False

## Create a score function with the score variable and an x and y coordinate
def Scores(score,x,y):
    ## Display the text "Score: (score)"
    text = medium.render("Score: " + str(score), True, white)
    ## Displays the text on the screen
    screen.blit(text, [x,y])

## Create a loop that runs the game
def GameLoop(words):
    ## Set boolean gameExit to "False"
    gameExit = False
    ## Set boolean gameOver to "False"
    gameOver = False
    ## Set integer numEnemies to 4 which is how many enemys appear
    numEnemies = 4
    ## Create lists with the length of numEnemies
    Enemy_height = [0]*numEnemies
    Enemy_width = [0]*numEnemies
    Enemy_y = [0]*numEnemies
    Enemy_x = [0]*numEnemies
    Enemy_backx = [0]*numEnemies
    Enemy_topy = [0]*numEnemies
    Enemy_speed = [0]*numEnemies
    word = [0]*numEnemies
    splitword = [0]*numEnemies
    activatedword = [False]*numEnemies
    ## Set boolean anyActivated (words) to "False"
    anyActivated = False
    ## Set activatedIndex equal to -1
    activatedIndex = -1
    ## for loop from 0 to numEnemies
    for i in range(numEnemies):
        ## Set each Enemy_height to 50
        Enemy_height[i] = 50
        ## Set each Enemy_width to 50
        Enemy_width[i] = 50
        ## Set each Enemy_y to any random value between 0 and the screen height (- Enemy_height)
        Enemy_y[i] = random.randrange(0, screen_height - Enemy_height[i])
        ## Set each Enemy_x to a random value between 1750 and 1950
        Enemy_x[i] = random.randrange(1750, 1950)
        ## Set each enemy bottom right x coordinate to the bottom left x coordinate + the enemy width 
        Enemy_backx[i] = Enemy_x[i] + Enemy_width[i]
        ## Set each enemy top y coordinate to the bottom y coordinate plus enemy height
        Enemy_topy[i] = Enemy_y[i] + Enemy_height[i]
        ## Set each enemy's speed to -2
        Enemy_speed[i] = 2
        ## Give each Enemy a random word from the chosen textfile
        word[i] = random.choice(words)
        ## Set each splitword to the corrosponding word split up 
        splitword[i] = list(word[i])
        ## Delete the last element of the splitword as it is an incorrect character
        splitword[i] = splitword[i][:-1]
        ## Set each word to the joined up splitword
        word[i] = "".join(splitword[i])
    ## Set the shooter x and y coordinates
    shooter_x = 0
    shooter_y = 325
    ## Set the shooter height and width
    shooter_height = 150
    shooter_width = 150
    ## Set the shooter front x to the shooter x + the shooter width
    shooter_frontx = shooter_x + shooter_width
    ## Set the shooter top y to the shooter y + the shooter height
    shooter_topy = shooter_y + shooter_height
    ## Set the score to 0
    score = 0

    ## While loop that continues until gameExit is set to "True"
    while not gameExit:
        ## While loop for when the enemy touches the "shooter"
        while gameOver == True:
            ## Display a death message
            message_display("You are dead!", red, -50, "large")
            ## Update the screen
            pygame.display.update()
            ## Wait 2 seconds
            time.sleep(2)
            ## Take the user to the Main menu screen
            MainMenu()
            ## Update the screen
            pygame.display.update()
        ## Collects all the events that are happening
        for event in pygame.event.get():
            ## If the game is Quit
            if event.type == pygame.QUIT:
                ## Quit Pygame
                pygame.quit()
                ## Quit Python
                quit()
            ## Checks if a key has been pressed
            if event.type == pygame.KEYDOWN:
                ## Set the variable key equal to the ASCII value turned into a character
                key = chr(event.key)
                ## if the activatedIndex is equal to -1
                if activatedIndex == -1:
                    ## Set variable bestMatchingIndex equal to -1, this is the Enemy that is
                    ## activated
                    bestMatchingIndex = -1 # index, xval
                    ## Set variable bestMatchingValue equal to 2000, this is the furthest distance
                    ## the enemy can be from the "shooter"
                    bestMatchingValue = 2000
                    ## for loop from 0 to numEnemies
                    for i in range(numEnemies):
                        ## If the Enemy_x is less than the furthest distance away (which it must be)
                        ## and the key typed is equal to the corrosponding element in the splitwords
                        ## list
                        if Enemy_x[i] < bestMatchingValue and  key == splitword[i][0]:
                            ## Set bestMatchingIndex equal to the "i" of whichever enemy
                            ## has the corrosponding starting character equal to key
                            bestMatchingIndex = i
                            ## Set the bestMatchingValue equal to the Enemy_x value
                            bestMatchingValue = Enemy_x[i]
                    ## If the bestMatchingIndex is greater than -1
                    if bestMatchingIndex > -1:
                        ## Set activatedIndex equal to bestMatching index
                        activatedIndex = bestMatchingIndex
                    print(activatedIndex)
                ## If activatedIndex is greater than -1
                if activatedIndex > -1:
                    print(key)
                    print(activatedIndex)
                    ## If the key is equal to the first element in the splitwords[activatedIndex] list
                    if key == splitword[activatedIndex][0]:
                        ## Delete the first character from the word[activatedIndex] string
                        word[activatedIndex] = word[activatedIndex][1:]
                        ## Delete the first element from the splitword[activatedIndex] list
                        splitword[activatedIndex].pop(0)
                        print("".join(splitword[activatedIndex]))
                        print(len(splitword[activatedIndex]))
                        ## If the splitwords[activatedIndex] list is empty
                        if not splitword[activatedIndex]:
                            ## Increase the score by 1 point 
                            score += 1
                            ## Set the word for the Enemy equal to a new random word
                            word[activatedIndex] = random.choice(words)
                            ## Split the word up
                            splitword[activatedIndex] = list(word[activatedIndex])
                            ## Delete the last element of the splitword
                            splitword[activatedIndex] = splitword[activatedIndex][:-1]
                            word[activatedIndex] = "".join(splitword[activatedIndex])
                            ## Move the Enemy back to the starting x coordinate of 1750
                            Enemy_x[activatedIndex] = 1750
                            ## Give the Enemy a new random y coordinate
                            Enemy_y[activatedIndex] = random.randrange(0, screen_height - Enemy_height[activatedIndex])
                            print(Enemy_x[activatedIndex],Enemy_y[activatedIndex])
                            ## Set activatedIndex back to -1
                            activatedIndex = -1
        ## Fill the screen in black
        screen.fill(black)
        ## Call the Score function with the score at coordinates (0,0)
        Scores(score,0,0)
        ## Call the shooter function to display the "shooter" at the defined shooter x and shooter y coordinates
        shooter(shooter_x,shooter_y)
        ## For loop from 0 to numEnemies
        for i in range(numEnemies):
            ## Call the Enemies function to create an numEnemies (n) number of Enemies
            Enemies(Enemy_x[i],Enemy_y[i],word[i], i == activatedIndex)
            ## Make the Enemy x coordinate reduce by the value of the variable Enemy_speed each clock tick
            Enemy_x[i] -= Enemy_speed[i]
            ## Checks if the y coordinate is greater than 370
            if Enemy_y[i] > 370:
                ## If it is, reduce the y coordinate by 0.5 each clock tick
                Enemy_y[i] -= 0.5
            else:
                ## If it isn't, increase the y coordinate by 0.5 each clock tick
                Enemy_y[i] += 0.5

            ## Checks if the Enemy x is less than the shooter x
            if Enemy_x[i] < shooter_frontx and Enemy_x[i] > shooter_x:
                ## Then Checks if the enemy y is in between the shooter y
                if Enemy_y[i] > shooter_y and Enemy_y[i] < shooter_topy or Enemy_topy[i] < shooter_topy and Enemy_topy[i] > shooter_y:
                    ## If both are true then set the gameOver variable to "True"
                    print("dead")
                    gameOver = True


        ## Update the display
        pygame.display.update()
        ## Set the FPS to 60
        clock.tick(60)

## Start the MainMenu function
MainMenu()
## Quit Pygame
pygame.quit()
## Quit Python
quit()