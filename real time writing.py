#creates a new string, that will store the character you have written
import pygame
import time

pygame.init()

screen_width = 1600
screen_height = 800

white = (255,255,255)
black = (0,0,0)

screen = pygame.display.set_mode((screen_width,screen_height)) 

pygame.display.set_caption("Type Attack")
clock = pygame.time.Clock()

number_str = "" 

#create a new Font object that is used to render the string into a Surface object
font_renderer = pygame.font.Font("freesansbold.ttf", 15) 

while True:
    screen.fill(black) # fill the whole screen with a black color
    # create a new Surface object from a string, where the text is white.
    rendered_number = font_renderer.render(number_str, True, white)

    #draws the created Surface onto the screen at position 100,100
    screen.blit(rendered_number, (100, 100))
    # updates the screen to show changes
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: 
            if pygame.K_a <= event.key <= pygame.K_z: # checks the key pressed
                character = chr(event.key) #converts the number to a character
                number_str += str(character) #adds the number to the end of the string
