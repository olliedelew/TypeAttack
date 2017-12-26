import pygame
import time
import random
import math

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

screen = pygame.display.set_mode((screen_width,screen_height)) ## Creates a screen with the dimensions of the variables
                                                               ## screen_width and screen_height

small = pygame.font.SysFont("freesansbold.ttf", 25)
medium = pygame.font.SysFont("freesansbold.ttf", 50)
large = pygame.font.SysFont("freesansbold.ttf", 100)

pygame.display.set_caption("Type Attack")
clock = pygame.time.Clock()

shooter_image = pygame.image.load("shooter.png")
enemy_image = pygame.image.load("enemy.png")
bullet_image = pygame.image.load("bullet.png") 

def Enemies(cordx,cordy,word, isActivated):
    screen.blit(enemy_image,(cordx,cordy))
    if isActivated:
        pygame.draw.rect(screen,white,[cordx+29,cordy+50,110,25])
    else:    
        pygame.draw.rect(screen,green,[cordx+29,cordy+50,110,25])
    word_text(word,black,cordx+29,cordy+50,110,25)

def word_text(text,colour,buttonx,buttony,buttonwidth,buttonheight,size = "small"):
    TextSurf, TextRect = text_objects(text, colour, size)
    TextRect.center = ((buttonx+(buttonwidth/2)), (buttonheight/2)+buttony)
    screen.blit(TextSurf,TextRect)

def text_objects(text, colour, size):

    if size == "small":
        textSurface = small.render(text, True, colour)
    elif size == "medium":
        textSurface = medium.render(text, True, colour)
    elif size == "large":
        textSurface = large.render(text, True, colour)

    return textSurface, textSurface.get_rect()
    
def message_display(text, colour, y_displace=0, size = "large"):

    TextSurf, TextRect = text_objects(text, colour, size)
    TextRect.center = ((screen_width/2),(screen_height/2)+y_displace)
    screen.blit(TextSurf, TextRect)

def pause(score, wave):

    paused = True
    screen.fill(black)
    Scores(score,0,0)
    Wave(wave)
    message_display("Paused",red,-50,"large")
    message_display("Press C to continue", white, 50, "medium")
    pygame.display.update()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
        clock.tick(5)
    
def shooter(x,y):
    screen.blit(shooter_image,(x,y))



def button_text(text,colour,buttonx,buttony,buttonwidth,buttonheight,size = "medium"):
    TextSurf, TextRect = text_objects(text, colour, size)
    TextRect.center = ((buttonx+(buttonwidth/2)), (buttonheight/2)+buttony)
    screen.blit(TextSurf,TextRect)

def button_text2(text,colour,buttonx,buttony,size = "small"):
    TextSurf, TextRect = text_objects(text, colour, size)
    TextRect.center = (buttonx, buttony)
    screen.blit(TextSurf,TextRect)

def button(text,x,y,width,height,darkcolour,lightcolour,action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen,lightcolour,(x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()
            elif action == "wordz":
                txtfilespage()
            elif action == "play":
                textfile = "random.txt"
                with open(textfile,"r") as f:
                    words = f.readlines()
            elif action == "biology":
                textfile = "biology.txt"
                with open(textfile,"r") as f:
                    words = f.readlines()
            elif action == "inputwords":
                choose_words()
            GameLoop(words)

    else:
        pygame.draw.rect(screen,darkcolour,(x,y,width,height))

    button_text(text,black,x,y,width,height)

def Bullet(x,y):
    screen.blit(bullet_image,(x,y))

def MainMenu():
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(white)
        ## Call function "showHighscore" with "high" which is a variable showing the highest score
        showHighscore(high)
        message_display("Type Attack", blueish, -150, "large")
        message_display("Type the words as quick as you can", black, -80, "medium")
        message_display("The more words you type correctly, the higher your score", black, -20, "medium")
        message_display("Dont let the enemies touch you or you will die!", black, 40, "medium")
        message_display("press ESC to pause", black, 100, "medium")

        button("Play", 175, 600, 300, 75, Dgreen, green, action = "play")
        button("Choose words", 650,600,300,75, Dblue, blue, action = "wordz")
        button("Quit", 1125,600,300,75, Dred, red, action = "quit")

        pygame.display.update()
                        
        clock.tick(15)
    MainMenu = False
        
## Create a score function with the score variable and an x and y coordinate
def Scores(score,x,y):
    ## Display the text "Score: (score)"
    text = medium.render("Score: " + str(score), True, white)
    ## Displays the text on the screen
    screen.blit(text, [x,y])

def Wave(wave):
    text = medium.render("Wave: " + str(wave), True, white)
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

def txtfilespage():
    pageopen = True
    while pageopen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(white)
        message_display("Select which kind of words you would like to appear", black, -200, "medium")
        button("Biology keywords", 175,600,300,75, Dblue, blue, action = "biology")
        button("input words", 1125,600,300,75, Dred, red, action = "inputwords")
        pygame.display.update()
                        
        clock.tick(15)
    pageopen = False

def choose_words():
    choosing_words = True
    letters = []
    print("Working")
    while choosing_words:
        screen.fill(white)
        message_display("Press enter to input word", black, -200, "medium")
        message_display("Press escape to play with inputed words", black, 100, "medium")
        message_display("Press backspace to delete a letter", black, -300, "medium")
        pygame.draw.rect(screen,black,(550,300,500,70))
        button("", 550, 300, 500, 70, black, black)
        button("", 1200, 150, 300, 500, black, black)
        word_text("Word list",black,1180,120,110,25)
        wordstring = "".join(letters)
        rendered_word = large.render(wordstring, True, white)
        screen.blit(rendered_word, (570, 300))
        button_text(wordstring,white,1200,150,300,500)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if pygame.K_a <= event.key <= pygame.K_z and (len(letters) < 12): # checks the key pressed
                    letters.append(chr(event.key))
                if event.key == pygame.K_BACKSPACE and (len(letters) > 0):
                    del letters[-1]
                if event.key == pygame.K_RETURN and (len(letters) > 0):
                    f = open("inputwords.txt","a")
                    f.write(wordstring + "\n")
                    f.close()
                    del letters[:]            
                if event.key == pygame.K_ESCAPE:
                    textfile = "inputwords.txt"
                    with open(textfile,"r") as f:
                        words = f.readlines()
                    GameLoop(words)
        clock.tick(60)
        pygame.display.update()

def GameLoop(words, score = 0, wave = 1, numEnemies = 4):
    gameExit = False
    gameOver = False
    # numEnemies = 4
    Enemy_speed_num = -10
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
    anyActivated = False
    activatedIndex = -1
    bullets = [] # array of arrays [current_x, current_y, index of enemy]
    for i in range(numEnemies):
        Enemy_height[i] = 50
        Enemy_width[i] = 50
        Enemy_y[i] = random.randrange(0, screen_height - Enemy_height[i])
        Enemy_x[i] = random.randrange(1750, 1950)
        Enemy_backx[i] = Enemy_x[i] + Enemy_width[i]
        Enemy_topy[i] = Enemy_y[i] + Enemy_height[i]
        Enemy_speed[i] = Enemy_speed_num
        word[i] = random.choice(words)
        splitword[i] = list(word[i])
        splitword[i] = splitword[i][:-1]
        word[i] = "".join(splitword[i])

    # wave = 1
    shooter_x = 0
    shooter_y = 325
    shooter_height = 150
    shooter_width = 150
    shooter_frontx = shooter_x + shooter_width
    shooter_topy = shooter_y + shooter_height
    ## Set the score to 0
    # score = 0
    bullet_x = 150
    bullet_y = 400
    bullet_speed = Enemy_speed[0] * -20
    kills = 0
    while not gameExit:
        screen.fill(black)
        while gameOver == True:
            message_display("You are dead!", red, -50, "large")
            pygame.display.update()
            time.sleep(2)
            ## Show the highscore
            Highscore(score)
            MainMenu()
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
                kills += 1
                word[bullet[2]] = random.choice(words)
                splitword[bullet[2]] = list(word[bullet[2]])
                splitword[bullet[2]] = splitword[bullet[2]][:-1]
                word[bullet[2]] = "".join(splitword[bullet[2]])
                Enemy_x[bullet[2]] = -10
                Enemy_y[bullet[2]] = random.randrange(0, screen_height - Enemy_height[bullet[2]])
                print(Enemy_x[bullet[2]],Enemy_y[bullet[2]])
                if kills == numEnemies:
                    return GameLoop(words,score,wave + 1, numEnemies + 1)
                continue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 gameOver == False
                 gameExit == True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                   pause(score, wave)
            if event.type == pygame.KEYDOWN:
                key = chr(event.key)
                if activatedIndex == -1:
                    bestMatchingIndex = -1 # index, xval
                    bestMatchingValue = 2000 # index, xval
                    for i in range(numEnemies):
                        if len(splitword[i]) > 0:
                            if Enemy_x[i] < bestMatchingValue and  key == splitword[i][0]:
                                bestMatchingIndex = i
                                bestMatchingValue = Enemy_x[i]
                    if bestMatchingIndex > -1:
                        activatedIndex = bestMatchingIndex
                    print(activatedIndex)
                if activatedIndex > -1:
                    print(key)
                    print(activatedIndex)
                    if key == splitword[activatedIndex][0]:
                        word[activatedIndex] = word[activatedIndex][1:]
                        splitword[activatedIndex].pop(0)
                        print("".join(splitword[activatedIndex]))
                        print(len(splitword[activatedIndex]))
                        if not splitword[activatedIndex]:
                            bullets.append([bullet_x,bullet_y,activatedIndex])
                            activatedIndex = -1
        
        ## Call the Score function with the score at coordinates (0,0)
        Scores(score,0,0)
        Wave(wave)
        for i in range(numEnemies):
            if Enemy_x[i] == -10: # magic position where we dont move them from
                continue
            Enemies(Enemy_x[i],Enemy_y[i],word[i], i == activatedIndex)
            distance_x = Enemy_x[i]
            distance_y = Enemy_y[i] - 370
            distance_straight = math.sqrt(pow(distance_x,2) + pow(distance_y,2))
            move_x = (Enemy_speed[i] / distance_straight) * distance_x
            move_y = (Enemy_speed[i] / distance_straight) * distance_y
            Enemy_x[i] += move_x
            Enemy_y[i] += move_y

            if Enemy_x[i] < shooter_frontx and Enemy_x[i] > shooter_x:
                if Enemy_y[i] > shooter_y and Enemy_y[i] < shooter_topy or Enemy_topy[i] < shooter_topy and Enemy_topy[i] > shooter_y:
                    print("dead")
                    gameOver = True
                    open('inputwords.txt', 'w').close()

        shooter(shooter_x,shooter_y)

        pygame.display.update()
        clock.tick(60)
        
MainMenu()
pygame.quit()
quit()