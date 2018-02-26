## Imported classes/dictionaries/functions 
import pygame
import time
import random
import math

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
bullet_image = pygame.image.load("bullet.png") 

## Create an enemy function at a given x and y coordinate and a given word
def Enemies(cordx,cordy,word, isActivated):
    screen.blit(enemy_image,(cordx,cordy))
    ## Checks if the enemy has been activated due to the user typing the
    ## first character of the corrosponding word
    if isActivated:
        ## Draws a white rectangle
        pygame.draw.rect(screen,Dgreen,[cordx+29,cordy+50,110,25])
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

## Pauses the game
def pause(score, wave):
    ## Set Boolean variable paused equal to True
    paused = True
    ## Fill the background of the screen in black
    screen.fill(black)
    ## Call the Scores function so that the score shows up in the top left corner
    Scores(score,0,0)
    ## Call the wave function so that the wave number shows up in the top middle
    Wave(wave)
    ## Display messages to be displayed on screen
    message_display("Paused",red,-50,"large")
    message_display("Press C to continue", white, 50, "medium")
    ## Update the display
    pygame.display.update()
    ## While loop that continues until paused variable equals False
    while paused:
        ## Collects all the events that are happening
        for event in pygame.event.get():
            ## If the game has been exited then
            if event.type == pygame.QUIT:
                ## Quit pygame and quit python
                pygame.quit()
                quit()
            ## If the game senses a keypress
            if event.type == pygame.KEYDOWN:
                ## And that keypress is "C" then
                if event.key == pygame.K_c:
                    ## End the loop and set paused to False
                    paused = False
        ## FPS
        clock.tick(5)
    
## Create the shooter at a given x and y coordinate
def shooter(x,y):
    ## Displays the shooter image
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
            ## If the Choose words button is clicked then the "wordz" action is started
            elif action == "wordz":
                ## Takes the user to the page where they can pick an alternative word file
                txtfilespage()
            ## If the Play button is clicked then the game is started with random words
            elif action == "play":
                ## Set the textfile variable to the textfile where the random words are stored
                textfile = "random.txt"
                ## Open the textfile and read it
                with open(textfile,"r") as f:
                    ## Set the variable words to the lines of words inside of the textfile
                    words = f.readlines()
            ## If the Biology button is clicked then the game is started with Biology keywords
            elif action == "biology":
                ## Set the textfile variable to the textfile where the Biology keywords are stored
                textfile = "biology.txt"
                ## Open the textfile and read it
                with open(textfile,"r") as f:
                    ## Set the variable words to the lines of words inside of the textfile
                    words = f.readlines()
            ## If the Input words button is clicked then the action "inputwords" is started
            elif action == "inputwords":
                ## Takes the user to the page where they can input their own words
                choose_words()
            ## Start the game with whatever the words variable is set to
            GameLoop(words)
    ## If the mouse is not over any buttons then
    else:
        ## Makes the colour of the button dark
        pygame.draw.rect(screen,darkcolour,(x,y,width,height))
    ## Displays the button text
    button_text(text,black,x,y,width,height)


## Create the bullet at a given x and y coordiante
def Bullet(x,y):
    ## Displays the bullet image
    screen.blit(bullet_image,(x,y))

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
        ## Call function "showHighscore" with "high" which is a variable showing the highest score
        showHighscore(high)
        ## List of messages to be displayed on screen
        message_display("Type Attack", blueish, -150, "large")
        message_display("Type the words as quick as you can", black, -80, "medium")
        message_display("The more words you type correctly, the higher your score", black, -20, "medium")
        message_display("Dont let the enemies touch you or you will die!", black, 40, "medium")
        message_display("press ESC to pause", black, 100, "medium")
        ## Creates "Play", "Choose words" and "Quit" buttons, which, when clicked, start a specific action            
        button("Play", 175, 600, 300, 75, Dgreen, green, action = "play")
        button("Choose words", 650,600,300,75, Dblue, blue, action = "wordz")
        button("Quit", 1125,600,300,75, Dred, red, action = "quit")
        ## Update the display
        pygame.display.update()
        ## FPS
        clock.tick(15)
    ## Ends while loop
    Menu = False
        
## Create a score function with the score variable and an x and y coordinate
def Scores(score,x,y):
    ## Display the text "Score: (score)"
    text = medium.render("Score: " + str(score), True, white)
    ## Displays the text on the screen
    screen.blit(text, [x,y])

## Create a wave function which outputs the wave number the user has reached
def Wave(wave):
    ## Display the text "Wave: (wave)"
    text = medium.render("Wave: " + str(wave), True, white)
    ## Display the text on screen at coordinates (800,0)
    screen.blit(text, [800,0])

## Open and read the "Highscore" file
with open("Highscore.txt","r") as h:
    ## Set variable high to the highscore
    high = h.read()
    print(high)
    ## Set variable high to an integer
    high = int(high)
    print(high)

## Create a highscore function with the score variable
def Highscore(score):
    ## Set variable overwrite to open the "Highscore" file
    overwrite = open("Highscore.txt","w")
    ## Set variable highscre to high
    highscre = high
    ## If the score is greater than the highscore
    if score > highscre:
        ## Set the highscore equal to the score
        highscre = score 
        ## Overwrite the highscore textfile
        overwrite.write(str(highscre))
        ## Print highscre
        return highscre
    else:
        ## If score is less than the highscore
        overwrite.write(str(highscre))

## Create a showHighscore function to show the highscore
def showHighscore(highscre):
    ## Display the text "Score: (score)"
    text = medium.render("Highscore: " + str(high), True, black)
    ## Displays the text on the screen at coordinates (700,0)
    screen.blit(text, [700,0])

## Create a txtfilespage function where the user can choose a textfile to use instead of the random words textfile
def txtfilespage():
    ## Set the Boolean variable pageopen to True
    pageopen = True
    ## While loop that continues until the pageopen variable is False
    while pageopen:
        ## Checks if the game has been exited
        for event in pygame.event.get():
            ## If the game has been exited then
            if event.type == pygame.QUIT:
                ## Quit pygame and quit python
                pygame.quit()
                quit()
        ## Fill the background of the screen in white
        screen.fill(white)
        ## Display message on screen
        message_display("Select which kind of words you would like to appear", black, -200, "medium")
        ## Create buttons for biology keywords and input words which take the user to the designated pages/game
        button("Biology keywords", 175,600,300,75, Dblue, blue, action = "biology")
        button("input words", 1125,600,300,75, Dred, red, action = "inputwords")
        ## Update the display
        pygame.display.update()
        ## FPS
        clock.tick(15)
    ## End while loop
    pageopen = False

## Create a page which allows the user to input their own words to an empty textfile which they can then play
def choose_words():
    ## Set the Boolean variable choosing_words to True
    choosing_words = True
    ## Create an empty list "letters"
    letters = []
    ## While loop that continues until the choosing_words variable is False
    while choosing_words:
        ## Fill the background of the screen in white
        screen.fill(white)
        ## List of messages to be displayed on screen
        message_display("Press enter to input word", black, -200, "medium")
        message_display("Press escape to play with inputed words", black, 100, "medium")
        message_display("Press backspace to delete a letter", black, -300, "medium")
        ## Draw a black rectangle in the middle of the screen
        pygame.draw.rect(screen,black,(550,300,500,70))
        button("", 550, 300, 500, 70, black, black)
        button("", 1200, 150, 300, 500, black, black)
        word_text("Word list",black,1180,120,110,25)
        ## Create a variable wordstring which holds the joined letters
        wordstring = "".join(letters)
        ## 
        rendered_word = large.render(wordstring, True, white)
        ## Display the variable rendered_word onto the screen 
        screen.blit(rendered_word, (570, 300))
        ## Create text on the screen that shows the letters the user has typed
        button_text(wordstring,white,1200,150,300,500)
        ## Collects all the events that are happening
        for event in pygame.event.get():
            ## If the game has been exited then
            if event.type == pygame.QUIT:
                ## Quit pygame and quit python
                pygame.quit()
                quit()
            ## If the game senses a keypress 
            if event.type == pygame.KEYDOWN:
                ## If the key that was pressed was a character in the range a to z AND the length of the "letters" list is less than 12 then
                if pygame.K_a <= event.key <= pygame.K_z and (len(letters) < 12):
                    ## Append the character to the "letters" list
                    letters.append(chr(event.key))
                ## If the key that was pressed was backspace and the length of the "letters" list is greater than 0 then
                if event.key == pygame.K_BACKSPACE and (len(letters) > 0):
                    ## Delete the last element of the "letters" list
                    del letters[-1]
                ## If the key that was pressed was enter and the length of the "letters" list is greater than 0 then
                if event.key == pygame.K_RETURN and (len(letters) > 0):
                    ## Open the inputwords textfile
                    f = open("inputwords.txt","a")
                    ## Write the word into the textfile and add a new line after it
                    f.write(wordstring + "\n")
                    ## Close the textfile
                    f.close()
                    ## Delete all the elements in the "letters" list
                    del letters[:]
                ## If the key that was pressed was escape then            
                if event.key == pygame.K_ESCAPE:
                    ## Set the textfile variable to the inputwords textfile 
                    textfile = "inputwords.txt"
                    ## Open the textfile and read it
                    with open(textfile,"r") as f:
                        ## Set the words variable to the lines of words inside of the textfile
                        words = f.readlines()
                    ## Start the game with whatever the words variable is set to 
                    GameLoop(words)
        ## FPS
        clock.tick(60)
        ## Update the display
        pygame.display.update()

## Create a loop that runs the game
def GameLoop(words, score = 0, wave = 1, numEnemies = 4):
    ## Set the Boolean variable gameExit to False
    gameExit = False
    ## Set the Boolean variable gameOver to False
    gameOver = False
    ## Set Enemy speed 
    Enemy_speed_num = -1.5
    ## Set the bullet speed multiplier
    bullet_speed_multiplier = -3
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
    ## Set boolean variable anyActivated (words) to False
    anyActivated = False
    ## Set activatedIndex equal to -1
    activatedIndex = -1
    bullets = [] # array of arrays [current_x, current_y, index of enemy]
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
        ## Set each enemy's speed to Enemy speed
        Enemy_speed[i] = Enemy_speed_num
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
    ## Set the bullet x and y coordinates
    bullet_x = 150
    bullet_y = 400
    ## Set the bullet speed to the enemy's speed timesed by the bullet speed multiplier as the bullet
    ## Has to be faster than the enemy speed or else it wont reach the enemy in time 
    ## and will have to go backwards to catch up
    bullet_speed = Enemy_speed[0] * bullet_speed_multiplier 
    ## Set kills to zero at the start of the game 
    kills = 0
    ## While loop that ends when the game is exited (gameExit = True) 
    while not gameExit:
        ## Fill the background of the screen in white
        screen.fill(white)
        ## While loop for when the game ends (enemy touches the user)
        while gameOver == True:
            ## Display an end game message
            message_display("You are dead!", red, -50, "large")
            ## Update the screen
            pygame.display.update()
            ## Wait 2 seconds
            time.sleep(2)
            ## Show the highscore
            Highscore(score)
            ## Take the user to the Main menu screen
            MainMenu()
            ## Update the screen
            pygame.display.update()

        for i in range(len(bullets)):
            bullet = bullets[i]
            if bullets[i] == [-1,-1,-1]:
                continue
            Bullet(bullet[0],bullet[1])
            bullet_distance_x = Enemy_x[bullet[2]] - bullet[0]
            bullet_distance_y = Enemy_y[bullet[2]] - bullet[1]
            bullet_distance_straight = math.sqrt(pow(bullet_distance_x,2) + pow(bullet_distance_y,2))
            bullet_move_x = abs((bullet_speed / bullet_distance_straight) * bullet_distance_x)
            bullet_move_y = abs((bullet_speed / bullet_distance_straight) * bullet_distance_y)
            if bullet[0] < Enemy_x[bullet[2]]:
                bullet[0] = min(bullet[0] + bullet_move_x,Enemy_x[bullet[2]])
                print("bullet X: ", bullet[0])
                print("Enemy X: ", Enemy_x[bullet[2]])
            if bullet[0] > Enemy_x[bullet[2]]:
                bullet[0] = max(bullet[0] - bullet_move_x,Enemy_x[bullet[2]])
                print("bullet X: ", bullet[0])
                print("Enemy X: ", Enemy_x[bullet[2]])
            if bullet[1] > Enemy_y[bullet[2]]:
                bullet[1] = max(bullet[1] - bullet_move_y,Enemy_y[bullet[2]])
                print("bul Y < spc Y: ", bullet[1]) #(y is inverted in pygame)
                print("Enemy Y: ", Enemy_y[bullet[2]])
            if bullet[1] < Enemy_y[bullet[2]]:
                bullet[1] = min(bullet[1] + bullet_move_y,Enemy_y[bullet[2]])
                print("bul Y < spc Y: ", bullet[1]) #(y is inverted in pygame)
                print("Enemy Y: ", Enemy_y[bullet[2]])
            if bullet[0] == Enemy_x[bullet[2]] and bullet[1] == Enemy_y[bullet[2]]:
                bullets[i] = [-1,-1,-1]
                ## Increase the score by 1 point                         
                score += 1
                ## Increase the kills by 1
                kills += 1
                word[bullet[2]] = random.choice(words)
                splitword[bullet[2]] = list(word[bullet[2]])
                splitword[bullet[2]] = splitword[bullet[2]][:-1]
                word[bullet[2]] = "".join(splitword[bullet[2]])
                Enemy_x[bullet[2]] = -10
                Enemy_y[bullet[2]] = random.randrange(0, screen_height - Enemy_height[bullet[2]])
                print(Enemy_x[bullet[2]],Enemy_y[bullet[2]])
                ## If all the enemies in the wave are killed
                if kills == numEnemies:
                    ## Use recursion to run the GameLoop again with an increased wave number and enemy number
                    return GameLoop(words,score,wave + 1, numEnemies + 1)
                ## If not then continue the loop
                continue
        ## Collects all the events that are happening
        for event in pygame.event.get():
            ## If the game is quit
            if event.type == pygame.QUIT:
                ## Set gameExit to True to end the loop 
                gameExit == True
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
                ## If activatedIndex is greater than -1
                if activatedIndex > -1:
                    ## If the key is equal to the first element in the splitwords[activatedIndex] list
                    if key == splitword[activatedIndex][0]:
                        ## Delete the first character from the word[activatedIndex] string
                        word[activatedIndex] = word[activatedIndex][1:]
                        ## Delete the first element from the splitword[activatedIndex] list
                        splitword[activatedIndex].pop(0)
                        ## If the splitwords[activatedIndex] list is empty
                        if not splitword[activatedIndex]:
                            ## Load a bullet to be sent to destroy the enemy
                            bullets.append([bullet_x,bullet_y,activatedIndex])
                            ## Set activatedIndex back to -1
                            activatedIndex = -1
                ## If the key pressed was escape then
                if event.key == pygame.K_ESCAPE:
                    ## Pause the game using the pause function which saves the current score and wave
                    pause(score, wave)
            
        ## Call the Score function with the score at coordinates (0,0)
        Scores(score,0,0)
        ## Call the Wave function with the wave value
        Wave(wave)
        ## For loop from 0 top num Enemies
        for i in range(numEnemies):
            ## magic position where we dont move them from
            if Enemy_x[i] == -10:
                ## Continue the loop 
                continue
            ## Call the Enemies function to create an enemy in a given x and y with a random word and an index number
            Enemies(Enemy_x[i],Enemy_y[i],word[i], i == activatedIndex)
            ## Set the distance_x variable equal to enemy_x
            distance_x = Enemy_x[i]
            ## Set the distance_y variable equal to enemy_y minus 370
            distance_y = Enemy_y[i] - 370
            ## Set the distance_straight equal to distance_x squared plus distance_y squared and the answer square rooted
            distance_straight = math.sqrt(pow(distance_x,2) + pow(distance_y,2))
            ## Set the variable move_x equal to enemy_speed divided by distance_straight timesed by distance_x
            move_x = (Enemy_speed[i] / distance_straight) * distance_x
            ## Set the variable move_y equal to enemy_speed divided by distance_straight timesed by distance_y
            move_y = (Enemy_speed[i] / distance_straight) * distance_y
            ## Add the value of move_x to Enemy_x to move the enemy
            Enemy_x[i] += move_x
            ## Add the value of move_y to Enemy_y to move the enemy
            Enemy_y[i] += move_y
            ## Checks if the Enemy x is less than the shooter x
            if Enemy_x[i] < shooter_frontx and Enemy_x[i] > shooter_x:
                ## Then Checks if the enemy y is in between the shooter y
                if Enemy_y[i] > shooter_y and Enemy_y[i] < shooter_topy or Enemy_topy[i] < shooter_topy and Enemy_topy[i] > shooter_y:
                    ## If both are true then set the gameOver variable to True
                    gameOver = True
                    ## Open and clear the inputwords textfile then close it
                    open('inputwords.txt', 'w').close()
        ## Call the shooter function to create the shooter at the given x and y
        shooter(shooter_x,shooter_y)
        ## Update the display
        pygame.display.update()
        ## Set the FPS to 60
        clock.tick(60)
## Start the game at the Main Menu by calling the MainMenu function
MainMenu()
## Quit Pygame
pygame.quit()
## Quit Python
quit()