# Import PyGame 
import pygame
from pygame.locals import *

# Initalize PyGame
pygame.init()

# colours 
ROT = (255, 0, 0)
ORANGE  = ( 255, 140, 0)
GRÜN   = ( 0, 255, 0)
SCHWARZ = ( 0, 0, 0)
WEISS = (255, 255, 255)

# Player variables
player_y = 20
player_x = 20
player_movement_y = 0
player_movement_x = 0

# Open window
screen = pygame.display.set_mode((640, 480), pygame.RESIZABLE)
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
                player_movement_y = 6
            elif event.key == pygame.K_a:
                player_movement_x = -6
            elif event.key == pygame.K_s:
                player_movement_y = -6
            elif event.key == pygame.K_d:
                player_movement_x = 6

    # Gamelogic
    if player_movement_y != 0:
        player_movement_y += player_y
    if player_movement_x != 0:
        player_movement_x += player_x
    # Playground & figures 
    screen.fill(WEISS) # reset screen

    pygame.draw.rect(screen, ROT, [10, 10, 20, 35]) # x-position, y-position, x-axis, y-axis 
    # Update window
    pygame.display.flip()

    # tick refresh time
    clock = pygame.time.Clock()
    clock.tick(60)

pygame.quit()
