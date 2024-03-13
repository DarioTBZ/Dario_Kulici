# Import PyGame 
import pygame
from pygame.locals import *

# Initalize PyGame
pygame.init()


# Constants
WINDOWLENGTH = 640
WINDOWHEIGHT = 480

BALL_DURCHMESSER = 20

# Variables
ballpos_x = 10
ballpos_y = 30

movement_x = 4
movement_y = 4



# colours 
ROT = (255, 0, 0)
ORANGE  = ( 255, 140, 0)
GRÜN   = ( 0, 255, 0)
SCHWARZ = ( 0, 0, 0)
WEISS = (255, 255, 255)

# Open window
screen = pygame.display.set_mode((WINDOWLENGTH, WINDOWHEIGHT))
# title for window
pygame.display.set_caption("Project 54")

# Runtime
activgame = True
# Mainloop
while activgame: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            activgame = False
            print("Game was closed")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print("W was pressed")


    # Gamelogic


    # Screen Reset
    screen.fill(SCHWARZ) # reset screen


    # Playground & figures 
    pygame.draw.ellipse(screen, WEISS, [ballpos_x, ballpos_y, BALL_DURCHMESSER, BALL_DURCHMESSER]) # x-position, y-position, x-axis, y-axis 


    # Ball Movement
    ballpos_x += movement_x
    ballpos_y += movement_y

    if ballpos_x <= 0 or ballpos_x >= WINDOWLENGTH - BALL_DURCHMESSER:
        movement_x = -movement_x
    if ballpos_y <= 0 or ballpos_y >= WINDOWHEIGHT - BALL_DURCHMESSER:
        movement_y = -movement_y

    # Update window
    pygame.display.flip()

    # tick refresh time
    clock = pygame.time.Clock()
    clock.tick(60)

pygame.quit()
quit()
