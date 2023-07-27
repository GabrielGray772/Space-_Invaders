import sys
import pygame

#Keep track of keyboard and mouse events
def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
        
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
                
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False   
            

#Udate images on screen
def update_screen(ai_settings, screen, ship, alien):
    screen.fill(ai_settings.bg_colour)
    ship.blitme()
    alien.blitme()
    pygame.display.flip()