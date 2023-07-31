import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        fire_bullets(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
        
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False      
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    
#Keep track of keyboard and mouse events
def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
              
#update postion of bullets and deletes off screen bullets
def update_bullets(bullets):
    bullets.update()
    #Deletes off screen bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullets(ai_settings, screen, ship, bullets):
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
        
def create_fleet(ai_settings, screen, aliens):
    # Create an alien and calucalte number of aliens in the row
    # Spaceing between aliens are 1 alien width
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    availible_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(availible_space_x / (2 * alien_width))
    
    for alien_number in range(number_aliens_x):
        # Create an alien and place it in the row.
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)

#Udate images on screen
def update_screen(ai_settings, screen, ship, bullets, aliens):
    screen.fill(ai_settings.bg_colour)
    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()