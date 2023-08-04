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
def update_bullets(aliens, bullets):
    bullets.update()
    #Deletes off screen bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # Check if bullets hits aliens
    # if yes, delete bullet and alien
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    
def update_aliens(ai_settings, aliens):
    # Update the postion of the alien fleet
    check_fleet_edges(ai_settings,aliens)
    aliens.update()

def fire_bullets(ai_settings, screen, ship, bullets):
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def get_number_aliens_x(ai_settings, alien_width):
    # Determine the number of aliens in a row
    availible_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(availible_space_x / (1.5 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_hight):
    # Determine the number of rows that can fit on screen
    availible_space_y = (ai_settings.screen_height - (3 * alien_hight) - ship_height)
    number_rows = int(availible_space_y / (2 * alien_hight))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    #Create aline and place in row
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 1.5 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 1.5 * alien.rect.height * row_number
    aliens.add(alien)
        
def create_fleet(ai_settings, screen, ship, aliens):
    # Calculate and create a number of alien in a row
    # Spaceing between aliens are 1 alien width
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
                                  alien.rect.height)
    
    # Create the Fleet of aliens
    for row_number in range(number_rows): 
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)
            
def check_fleet_edges(ai_settings, aliens):
    # Check if fleet hits edge then adjusts accordingly
    for alien in aliens.sprites():
        if alien.check_edge():
            change_fleet_direction(ai_settings, aliens)
            break
        
def change_fleet_direction(ai_settings, aliens):
    # Drop the fleet and change direction
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
    

#Udate images on screen
def update_screen(ai_settings, screen, ship, bullets, aliens):
    screen.fill(ai_settings.bg_colour)
    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()