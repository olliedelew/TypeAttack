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
#del Pixel
#Pixel[10][10] = red
shooter_image = pygame.image.load("shooter.png")
enemy_image = pygame.image.load("enemy.png")

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

def spaceships(word):
    global spaceship_height
    spaceship_height= 141
    spaceship_width = 148
    global spaceship_y
    spaceship_y = random.randrange(0, screen_height-spaceship_height)
    global spaceship_x
    spaceship_x = 1750
    spaceship_backx = spaceship_x + spaceship_width
    spaceship_topy = spaceship_y + spaceship_height
    global spaceship_speed
    spaceship_speed = -7
    screen.blit(enemy_image,(spaceship_x,spaceship_y))
    pygame.draw.rect(screen,white,[spaceship_x+29,spaceship_y+50,95,40])
    word_text(word,black,spaceship_x+29,spaceship_y+50,95,40)

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




        button("Play", 175, 600, 300, 75, Dgreen, green, action = "play")
        button("Something", 650,600,300,75, Dblue, blue, action = "something")
        button("Quit", 1125,600,300,75, Dred, red, action = "quit")

        pygame.display.update()
                        
        clock.tick(15)
        
def score(score):
    text = smallfont.render("Score: " + str(score), True, white)
    screen.blit(text, [0,0])

def GameLoop():
    gameExit = False
    gameOver = False
    shooter_x = 0
    shooter_y = 325
    shooter_height = 150
    shooter_width = 150
    shooter_frontx = shooter_x + shooter_width
    shooter_topy = shooter_y + shooter_height
    score = 0
    word = random.choice(words)
    splitword = list(word)
    splitword = splitword[:-1]
    word = "".join(splitword)
    while not gameExit:
        while gameOver == True:
            message_display("You are dead!", red, 0, "large")
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
            #for i in range(len(splitword)):
                key = chr(event.key)
                print(key)
                if key == splitword[0]:
                    splitword.pop(0)
                    print("".join(splitword))
                    print(len(splitword))
                    if not splitword:
                        print("Enemy destroyed")
                        score += 1
                        spaceships(word)
                  #      else:
                    #        print("incorrect")
                                                

        screen.fill(black)
    # do everything after filling screen in
        spaceships(word)
        spaceship_x += spaceship_speed
        if spaceship_y > 325:
            spaceship_y -= 0.5
        else:
            spaceship_y += 0.5
        
        shooter(shooter_x,shooter_y)

        if spaceship_x < -150:
            spaceship_x = 1750 #+ spaceship_width
            spaceship_y = random.randrange(0,screen_height)
        if spaceship_y > 650:
            spaceship_y = random.randrange(0,screen_height)
        elif spaceship_y < 0:
            spaceship_y = random.randrange(0,screen_height)

        if spaceship_x < shooter_frontx and spaceship_x > shooter_x:
            if spaceship_y > shooter_y and spaceship_y < shooter_topy or spaceship_topy < shooter_topy and spaceship_topy > shooter_y:
                print("dead")
                gameOver = True


            
                # may have to invert all the > or < signs for y's because y increases as it goes down
#        print("x: ", spaceship_x, "y: ", spaceship_y)

##        if (spaceship_x == 150) and (100<spaceship_y<500):
##            dead()
            
        
        #collisions = detectCollisions(0,225,150,150,spaceship_x,spaceship_y,spaceship_width,spaceship_height)
        #if spaceship_x == 150:
         #  health = health - 10
            #print(health)
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
