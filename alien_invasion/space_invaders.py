#Main page that houses while loop to run game.

#import sys to allow command line arguments
import sys
#import pygame to support game objects
import pygame
from settings import Settings
from ship import Ship

def run_game():
    #Stat the game and create the screen objeject
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Space Invaders")
    
    #Crate a ship
    ship = Ship(screen)
    
    #Begin the main game loop
    while True:
        
        #Keep track of keyboard events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        #update the screen
        screen.fill(ai_settings.bg_colour)
        ship.blitme()
        pygame.display.flip()

run_game()