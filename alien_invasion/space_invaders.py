#Main page that houses while loop to run game.

import pygame
from pygame.sprite import Group
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
    # Make a group to store bullets in.
    bullets = Group()
    
    #Begin the main game loop
    while True:
        
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        
        #Delete old bullets
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        gf.update_screen(ai_settings, screen, ship, bullets, alien)
       

        #update the screen
        

run_game()