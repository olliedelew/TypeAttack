import pygame
import time
import random

pygame.init()

screen_width = 1600
screen_height = 800

#MainLoop = True
#Loop1 = True
#Loop2 = False

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
Dred = (175,26,26)
blueish = (33,88,188)
Dblue = (10,65,168) 
blue = (0,0,255)
green = (0,255,0)
Dgreen = (26,153,24)

screen = pygame.display.set_mode((screen_width,screen_height)) 

small = pygame.font.SysFont("freesansbold.ttf", 25)
medium = pygame.font.SysFont("freesansbold.ttf", 50)
large = pygame.font.SysFont("freesansbold.ttf", 100)

pygame.display.set_caption("Type Attack")
clock = pygame.time.Clock()
#Pixel = pygame.PixelArray(screen)
#del Pixela
#Pixel[10][10] = red
shooter_image = pygame.image.load("shooter.png")
enemy_image = pygame.image.load("enemy.png")
bullet_image = pygame.image.load("bullet.png") 


#for i in range (len (words)):
    #print(words[i])
#word = random.choice(words)

##with open("wordy.txt","r") as f:
##    for line in f:
##        for word in line.split():
##           words = f.readlines()
##print(words)

def Enemies(cordx,cordy,word, isActivated):
    #for i in range(numEnemies)
    screen.blit(enemy_image,(cordx,cordy))
    if isActivated:
        pygame.draw.rect(screen,white,[cordx+29,cordy+50,110,25])
    else:    
        pygame.draw.rect(screen,green,[cordx+29,cordy+50,110,25])
    word_text(word,black,cordx+29,cordy+50,110,25)

    #pygame.display.update()

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
    Scores(score)
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
        #screen.fill(black)

        clock.tick(5)
    
def shooter(x,y):
    screen.blit(shooter_image,(x,y))



def button_text(text,colour,buttonx,buttony,buttonwidth,buttonheight,size = "medium"):
    TextSurf, TextRect = text_objects(text, colour, size)
    TextRect.center = ((buttonx+(buttonwidth/2)), (buttonheight/2)+buttony)
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
            if action == "choosewords":
                txtfilespage()
            if action == "play":
                textfile = "random.txt"
                with open(textfile,"r") as f:
                    words = f.readlines()
                    GameLoop(words)
            if action == "randomwords":
                textfile = "random.txt"
                with open(textfile,"r") as f:
                    words = f.readlines()
                    GameLoop(words)
            if action == "biology":
                textfile = "biology.txt"
                with open(textfile,"r") as f:
                    words = f.readlines()
                    GameLoop(words)
            if action == "inputwords":
                choose_words()
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
        showHighscore(high)
        message_display("Type Attack", blueish, -150, "large")
        message_display("Type the words as quick as you can", black, -80, "medium")
        message_display("The more words you type correctly, the higher your score", black, -20, "medium")
        message_display("Dont let the enemies touch you or you will die!", black, 40, "medium")
        message_display("press ESC to pause", black, 100, "medium")

        button("Play", 175, 600, 300, 75, Dgreen, green, action = "play")
        button("Choose words", 650,600,300,75, Dblue, blue, action = "choosewords")
        button("Quit", 1125,600,300,75, Dred, red, action = "quit")

        pygame.display.update()
                        
        clock.tick(15)
    #return menu
    #remove menu by setting it to false
        
def Scores(score):
    text = medium.render("Score: " + str(score), True, white)
    screen.blit(text, [0,0])

def Wave(wave):
    text = medium.render("Wave: " + str(wave), True, white)
    screen.blit(text, [800,0])


with open("Highscore.txt","r") as h:
    high = h.read()
    print(high)
    high = int(high)
    print(high)

def Highscore(score):
    overwrite = open("Highscore.txt","w")
    highscre = high
    if score > highscre:
        highscre = score 
        overwrite.write(str(highscre))
        return highscre
    else:
        overwrite.write(str(highscre))

def showHighscore(highscre):
    text = medium.render("Highscore: " + str(high), True, black)
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
        button("Random words", 175, 600, 300, 75, Dgreen, green, action = "randomwords")
        button("Biology keywords", 650,600,300,75, Dblue, blue, action = "biology")
        button("input words", 1125,600,300,75, Dred, red, action = "inputwords")
        pygame.display.update()
                        
        clock.tick(15)
    #return pageopen
    #remove pageopen screen by setting it to false
def choose_words():
    choosing_words = True
    letters = []
    screen.fill(white)
    while choosing_words:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                letters.append(chr(event.key))
                if event.key == pygame.K_BACKSPACE:
                    del letters[-1]
                if event.key == pygame.K_KP_ENTER:
                    "".join(letters)
                    with open("inputwords.txt","a") as f:
                        file.write(letters)
                    del letters[:]
                message_display("Press escape to exit", black, -100, "medium")
                if event.key == pygame.K_ESCAPE:
                    textfile == "inputwords.txt"
                    with open(textfile,"r") as f:
                        words = f.readlines()
                
                GameLoop(words)
    pygame.display.update()
    clock.tick(15)

def GameLoop(words):
    gameExit = False
    gameOver = False
    numEnemies = 4
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
    for i in range(numEnemies):
        Enemy_height[i] = 50
        Enemy_width[i] = 50
        Enemy_y[i] = random.randrange(0, screen_height - Enemy_height[i])
        Enemy_x[i] = random.randrange(1750, 1950)
        Enemy_backx[i] = Enemy_x[i] + Enemy_width[i]
        Enemy_topy[i] = Enemy_y[i] + Enemy_height[i]
        Enemy_speed[i] = -3
        word[i] = random.choice(words)
        splitword[i] = list(word[i])
        splitword[i] = splitword[i][:-1]
        word[i] = "".join(splitword[i])

    shooter_x = 0
    shooter_y = 325
    shooter_height = 150
    shooter_width = 150
    shooter_frontx = shooter_x + shooter_width
    shooter_topy = shooter_y + shooter_height
    score = 0
    wave = 1
    bullet_x = 150
    bullet_y = 400
    bullet_speed = 0.1

    while not gameExit:
        while gameOver == True:
            message_display("You are dead!", red, 0, "large")
            # pygame.display.update()
            time.sleep(2)
            Highscore(score)
            MainMenu()
            pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 gameOver = False
                 gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                   pause(score, wave)
        #for i in range(len(splitword)):
            #for event in pygame.event.get():
##                if event.type == pygame.KEYDOWN:
##                    key = chr(event.key)
##                    print(key)
##                    if key == splitword[0]:
##                        key2 = chr(event.key)
##                        print(key)
##                        if key2 == splitword[1]:
##                            key3 = chr(event.key)

        #for event in pygame.event.get():
            #print(event)
            if event.type == pygame.KEYDOWN:
                key = chr(event.key)
                if activatedIndex == -1:
                    bestMatchingIndex = -1 # index, xval
                    bestMatchingValue = 2000 # index, xval
                    for i in range(numEnemies):
                        # print('Enemy:', Enemy_x[i])
                        # print('best', bestMatching[1])
                        if Enemy_x[i] < bestMatchingValue and  key == splitword[i][0]:
                            bestMatchingIndex = i
                            bestMatchingValue = Enemy_x[i]
                    if bestMatchingIndex > -1:
                        activatedIndex = bestMatchingIndex
                    print(activatedIndex)
                # print
                if activatedIndex > -1:
                    print(key)
                    print(activatedIndex)
                    if key == splitword[activatedIndex][0]:
                        splitword[activatedIndex].pop(0)
                        print("".join(splitword[activatedIndex]))
                        print(len(splitword[activatedIndex]))
                        if not splitword[activatedIndex]:
                            Bullet(bullet_x,bullet_y)
                            while (bullet_x != Enemy_x) and (bullet_y != Enemy_y[activatedIndex]):
                                if bullet_x < Enemy_x[activatedIndex] and bullet_y < Enemy_y[activatedIndex]:
                                    bullet_x += bullet_speed
                                    print("bullet X: ", bullet_x)
                                    print("Enemy X: ", Enemy_x[activatedIndex])
                                    #break
                                    bullet_y += bullet_speed
                                    print("bul Y < spc Y: ", bullet_y) #(y is inverted in pygame)
                                    print("Enemy Y: ", Enemy_y[activatedIndex])
                                    break
                                elif bullet_x < Enemy_x[activatedIndex] and bullet_y > Enemy_y[activatedIndex]:
                                    bullet_x += bullet_speed
                                    print("bullet X: ", bullet_x)
                                    print("Enemy X: ", Enemy_x[activatedIndex])
                                    bullet_y -= bullet_speed
                                    print("bul Y > spc Y: ", bullet_y) #(y is inverted in pygame)
                                    print("Enemy Y: ", Enemy_y[activatedIndex])
                                    break
                                elif bullet_x < Enemy_x[activatedIndex] and bullet_y == Enemy_y[activatedIndex]:
                                    bullet_x += bullet_speed
                                    print("bul Y = spc Y", bullet_y)
                                    break
                                pygame.display.update()
                                clock.tick(60)                            
                            # print("Score: ", score)
                            # print("Enemy destroyed")
                            score += 1
                            word[activatedIndex] = random.choice(words)
                            splitword[activatedIndex] = list(word[activatedIndex])
                            splitword[activatedIndex] = splitword[activatedIndex][:-1]
                            word[activatedIndex] = "".join(splitword[activatedIndex])
                            Enemy_x[activatedIndex] = 1750
                            Enemy_y[activatedIndex] = random.randrange(0, screen_height - Enemy_height[activatedIndex])
                            print(Enemy_x[activatedIndex],Enemy_y[activatedIndex])
                            activatedIndex = -1
                 
        screen.fill(black)
    # do everything after filling screen in
        Scores(score)
        Wave(wave)
        for i in range(numEnemies):
            Enemies(Enemy_x[i],Enemy_y[i],word[i], i == activatedIndex)
            Enemy_x[i] += Enemy_speed[i]
            # if Enemy_y[i] > 0:
            #     Enemy_y[i] = random.uniform(-0.5,0)
            # elif Enemy_y[i] < 625:
            #     Enemy_y[i] = random.uniform(0,0.5)
            if Enemy_y[i] > 325:
                Enemy_y[i] -= 0.5
            else:
                Enemy_y[i] += 0.5
            # if Enemy_x[i] < -(Enemy_y:
            #     Enemy_x[i] = screen_width + Enemy_width
            #     Enemy_y[i] = random.randrange(0,screen_height)
            if Enemy_y[i] > screen_height - Enemy_height[i]:
                Enemy_y[i] = random.randrange(0,screen_height)
            elif Enemy_y[i] < 0:
                Enemy_y[i] = random.randrange(0,screen_height)

            if Enemy_x[i] < shooter_frontx and Enemy_x[i] > shooter_x:
                if Enemy_y[i] > shooter_y and Enemy_y[i] < shooter_topy or Enemy_topy[i] < shooter_topy and Enemy_topy[i] > shooter_y:
                    print("dead")
                    gameOver = True

        shooter(shooter_x,shooter_y)


        pygame.display.update()
        clock.tick(60)

class Shooter(pygame.sprite.Sprite):
    """Shooter"""
    image = pygame.image.load("shooter.png")
    image = image.convert_alpha()
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = Shooter.image
        self.rect = self.image.get_rect()

    #def render(self,collision):
        #if (collision==True):
            #message_display("You have crashed!")
    #def update(self):
    #if word activated then rotate shooter to enemy Enemy
    #self.image = pygame.transform.rotate(self.image,angle)
##class Enemies(pygame.sprite.Sprite):
##    """Enemies"""
##    image = pygame.image.load("shooter.png")
##    image = image.convert_alpha()
##    def __init__(self):
##        pygame.sprite.Sprite.__init__(self, self.groups)
##    def Enemies(cordx,cordy,width,height,colour):
##        pygame.draw.rect(screen,colour, [cordx,cordy,width,height])
##    def moveEnemy(self,Shooter):
##        dx, dy = self.rect.x - player.rect.x, self.rect.y - player.rect.y
##        dist = math.hypot(dx, dy)
##        dx, dy = dx / dist, dy / dist
##        self.rect.x += dx * self.speed
##        self.rect.y += dy * self.speed
MainMenu()
GameLoop()
pygame.quit()
quit()


#class Bullet(pygame.sprite.Sprite):
 #   def __init__(self):
  #      pygame.sprite.Sprite.__init__(self)

##def Points(count):
##    font = pygame.font.SysFont(None, 25)
##    text = font.render("Dodged: "+str(count), True, black)
##    gameDisplay.blit(text,(0,0))
    
##def text_objects(text, font):
##    textSurface = font.render(text, True, black)
##    return textSurface, textSurface.get_rect()
##    
##def MainMenu():
##    menu = True
##    TextSurf, TextRect = text_objects(text, largeText)
##    while menu:
##        for event in pygame.event.get():
##            if event.type == pygame.QUIT:
##                pygame.quit()
##                quit()
##        screen.fill(white)
##        largeText = pygame.font.Font("freesansbold.ttf",115)
##        TextSurf, TextRect = text_objects("Type Attack", largeText)
##        TextRect.center = ((display_width/2),(display_height/2))
##        screen.blit(TextSurf, TextRect)
##        pygame.display.update()
##        clock.tick(15)
