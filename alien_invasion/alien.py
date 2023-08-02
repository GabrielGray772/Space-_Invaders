import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        #Load Alien image and set serface properties
        self.image = pygame.image.load("images/Alien_1.png")
        self.rect = self.image.get_rect()
        
        #Set alien at the top
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #Store alien exact location
        self.x = float(self.rect.x)
    
    def check_edge(self):
        # Return true if alien at the edge of the screen
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        
    def update(self):
        # Move the alien left or right
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
    
        
    def blitme(self):
        # Draw alien inc current possion
        self.screen.blit(self.image, self.rect)