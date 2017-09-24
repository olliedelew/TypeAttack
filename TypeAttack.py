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

with open("wordy.txt","r") as f:
    words = f.readlines()
#for i in range (len (words)):
    #print(words[i])
#word = random.choice(words)

##with open("wordy.txt","r") as f:
##    for line in f:
##        for word in line.split():
##           words = f.readlines()
##print(words)

def spaceships(cordx,cordy,word, isActivated):
    #for i in range(numspaceships)
    screen.blit(enemy_image,(cordx,cordy))
    if isActivated:
        pygame.draw.rect(screen,white,[cordx+29,cordy+50,95,40])
    else:    
        pygame.draw.rect(screen,green,[cordx+29,cordy+50,95,40])
    word_text(word,black,cordx+29,cordy+50,95,40)

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

def pause():

    paused = True
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
            if action == "controls":
                pass
            if action == "play":
                GameLoop()
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
        message_display("Type Attack", blueish, -150, "large")
        message_display("Type the words as quick as you can", black, -80, "medium")
        message_display("The more words you type correctly, the higher your score", black, -20, "medium")
        message_display("Dont let the spaceships touch you or you will die!", black, 40, "medium")
        message_display("press ESC to pause", black, 100, "medium")




        button("Play", 333, 600, 300, 75, Dgreen, green, action = "play")
        button("Quit", 966,600,300,75, Dred, red, action = "quit")

        pygame.display.update()
                        
        clock.tick(15)
        
def Scores(score):
    text = small.render("Score: " + str(score), True, white)
    screen.blit(text, [0,0])

with open("Highscore.txt","r") as h:
    high = h.read()
    high = int(high[0])
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

def GameLoop():
    gameExit = False
    gameOver = False
    numspaceships = 4
    spaceship_height = [0]*numspaceships
    spaceship_width = [0]*numspaceships
    spaceship_y = [0]*numspaceships
    spaceship_x = [0]*numspaceships
    spaceship_backx = [0]*numspaceships
    spaceship_topy = [0]*numspaceships
    spaceship_speed = [0]*numspaceships
    word = [0]*numspaceships
    splitword = [0]*numspaceships
    activatedword = [False]*numspaceships
    anyActivated = False
    activatedIndex = -1
    for i in range(numspaceships):
        spaceship_height[i] = 141
        spaceship_width[i] = 148
        spaceship_y[i] = random.randrange(0, screen_height - spaceship_height[i])
        spaceship_x[i] = 1750
        spaceship_backx[i] = spaceship_x[i] + spaceship_width[i]
        spaceship_topy[i] = spaceship_y[i] + spaceship_height[i]
        spaceship_speed[i] = -3
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
    bullet_x = 150
    bullet_y = 400
    bullet_speed = 0.1

    while not gameExit:
        while gameOver == True:
            message_display("You are dead!", red, 0, "large")
            Highscore(score)
            pygame.display.update()
            time.sleep(2)
            MainMenu()
            pygame.display.update
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 gameOver = False
                 gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                   pause()
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
                    for i in range(numspaceships):
                        # print('spaceship:', spaceship_x[i])
                        # print('best', bestMatching[1])
                        if spaceship_x[i] < bestMatchingValue and  key == splitword[i][0]:
                            bestMatchingIndex = i
                            bestMatchingValue = spaceship_x[i]
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
                            while (bullet_x != spaceship_x) and (bullet_y != spaceship_y[activatedIndex]):
                                if bullet_x < spaceship_x[activatedIndex] and bullet_y < spaceship_y[activatedIndex]:
                                    bullet_x += bullet_speed
                                    print("bullet X: ", bullet_x)
                                    print("spaceship X: ", spaceship_x[activatedIndex])
                                    #break
                                    bullet_y += bullet_speed
                                    print("bul Y < spc Y: ", bullet_y)
                                    print("spaceship Y: ", spaceship_y[activatedIndex])
                                    break
                                elif bullet_x < spaceship_x[activatedIndex] and bullet_y > spaceship_y[activatedIndex]:
                                    bullet_x += bullet_speed
                                    print("bullet X: ", bullet_x)
                                    print("spaceship X: ", spaceship_x[activatedIndex])
                                    bullet_y -= bullet_speed
                                    print("bul Y > spc Y: ", bullet_y)
                                    print("spaceship Y: ", spaceship_y[activatedIndex])
                                    break
                                elif bullet_x < spaceship_x[activatedIndex] and bullet_y == spaceship_y[activatedIndex]:
                                    print("bul Y = spc Y", bullet_y)
                                    break
                                pygame.display.update()
                                clock.tick(60)                            
                            print("Score: ", score)
                            print("Enemy destroyed")
                            score += 1
                            word[activatedIndex] = random.choice(words)
                            splitword[activatedIndex] = list(word[activatedIndex])
                            splitword[activatedIndex] = splitword[activatedIndex][:-1]
                            word[activatedIndex] = "".join(splitword[activatedIndex])
                            spaceship_x[activatedIndex] = 1750
                            print(spaceship_x[activatedIndex],spaceship_y[activatedIndex])
                            activatedIndex = -1
                 
        screen.fill(black)
    # do everything after filling screen in
        Scores(score)
        for i in range(numspaceships):
            spaceships(spaceship_x[i],spaceship_y[i],word[i], i == activatedIndex)
            spaceship_x[i] += spaceship_speed[i]
            if spaceship_y[i] > 325:
                spaceship_y[i] -= 0.5
            else:
                spaceship_y[i] += 0.5
            if spaceship_x[i] < -150:
                spaceship_x[i] = 1750 #+ spaceship_width
                spaceship_y[i] = random.randrange(0,screen_height)
            if spaceship_y[i] > 650:
                spaceship_y[i] = random.randrange(0,screen_height)
            elif spaceship_y[i] < 0:
                spaceship_y[i] = random.randrange(0,screen_height)

            if spaceship_x[i] < shooter_frontx and spaceship_x[i] > shooter_x:
                if spaceship_y[i] > shooter_y and spaceship_y[i] < shooter_topy or spaceship_topy[i] < shooter_topy and spaceship_topy[i] > shooter_y:
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
    #if word activated then rotate shooter to enemy spaceship
    #self.image = pygame.transform.rotate(self.image,angle)
##class spaceships(pygame.sprite.Sprite):
##    """Spaceships"""
##    image = pygame.image.load("shooter.png")
##    image = image.convert_alpha()
##    def __init__(self):
##        pygame.sprite.Sprite.__init__(self, self.groups)
##    def spaceships(cordx,cordy,width,height,colour):
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
