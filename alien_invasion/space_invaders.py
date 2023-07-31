#Main page that houses while loop to run game.

import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
# from alien import Alien   -Do i still need this??



def run_game():
    #Stat the game and create the screen objeject
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Space Invaders")
    
    #Crate a ship, group of bullets and Group of Aliens
    ship = Ship(ai_settings, screen)
    # alien = Alien(ai_settings, screen) - Do i need this??
    bullets = Group()
    aliens = Group()
    
    #Create the flee of aliens
    gf.create_fleet(ai_settings, screen, aliens)
    
    
    #Begin the main game loop
    while True:
        
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets, aliens)
       

        #update the screen
        

run_game()