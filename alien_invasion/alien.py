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
    
    #Draw alien inc current possion    
    def blitme(self):
        self.screen.blit(self.image, self.rect)