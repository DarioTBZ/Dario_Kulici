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

# Player 1
player_1_x = 20
player_1_y = 20
player_1_movement = 0

# Player 2
player_2_x = WINDOWLENGTH - (2 * 20)
player_2_y = 20
player_2_movement = 0

schlägerhöhe = 60
ballwechsel = 0

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
            
            # Player 1 
            if event.key == pygame.K_DOWN:
                player_1_movement = 6
            elif event.key == pygame.K_UP:
                player_1_movement = -6

            # Player 2
            if event.key == pygame.K_s:
                player_2_movement = 6
            elif event.key == pygame.K_w:
                player_2_movement = -6


        # Stop Player Movement
        if event.type == pygame.KEYUP:
            
            # Keys for Player 1
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_1_movement = 0


            # Keys for Player 2
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player_2_movement = 0


    # Gamelogic
    if player_1_movement != 0:
        player_1_y += player_1_movement

    if player_1_y < 0:
        player_1_y = 0

    if player_1_y > WINDOWHEIGHT - schlägerhöhe:
        player_1_y = WINDOWHEIGHT - schlägerhöhe

    if player_2_movement != 0:
        player_2_y += player_2_movement
    
    if player_2_y < 0:
        player_2_y = 0
    
    if player_2_y > WINDOWHEIGHT - schlägerhöhe:
        player_2_y = WINDOWHEIGHT - schlägerhöhe

    if ballpos_x < 1: # Versuch zu erweitern (gescheitert)
        print("Links nach aussen")
    if ballpos_x > 630:
        print("Rechts nach aussen")

    # Screen Reset
    screen.fill(SCHWARZ) # reset screen


    # Playground & figures 
    ball = pygame.draw.ellipse(screen, WEISS, [ballpos_x, ballpos_y, BALL_DURCHMESSER, BALL_DURCHMESSER]) # x-position, y-position, x-axis, y-axis 

    
    player1 = pygame.draw.rect(screen, WEISS, [player_1_x, player_1_y, 20, 100])

    player2 = pygame.draw.rect(screen, WEISS, [player_2_x, player_2_y, 20, 100])


    # Ball Movement
    ballpos_x += movement_x
    ballpos_y += movement_y

    if ballpos_x <= 0 or ballpos_x >= WINDOWLENGTH - BALL_DURCHMESSER:
        movement_x = -movement_x
    if ballpos_y <= 0 or ballpos_y >= WINDOWHEIGHT - BALL_DURCHMESSER:
        movement_y = -movement_y

    
    # Kollision Check
    if player1.colliderect(ball):
            print("Zussamenstoss Spieler 1 und Ball ")
            movement_x = movement_x * -1
            ballpos_x = 40
            
            # Stats
            print(ballwechsel)
        
    if player2.colliderect(ball):
            print("Zussamenstoss Player 2 und Ball ")
            movement_x = movement_x * -1
            ballpos_x = player_2_x - 20
            
            # Stats
            ballwechsel += 1
            print(ballwechsel)


    ausgabetext = "Ballwechsel: " + str(ballwechsel)
    font = pygame.font.SysFont(None, 30)
    text = font.render(ausgabetext, True, ROT)
    screen.blit(text, [(WINDOWLENGTH / 2 - 70), 10])

    # Update window
    pygame.display.flip()

    # tick refresh time
    clock = pygame.time.Clock()
    clock.tick(60)

pygame.quit()
quit()
