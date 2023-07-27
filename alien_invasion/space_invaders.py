#Main page that houses while loop to run game.

import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien

def run_game():
    #Stat the game and create the screen objeject
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Space Invaders")
    
    #Crate a ship
    ship = Ship(ai_settings, screen)
    alien = Alien(screen)
    
    #Begin the main game loop
    while True:
        
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship, alien)
       

        #update the screen
        

run_game()