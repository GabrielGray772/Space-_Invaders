import pygame

class Alien():
    def __init__(self, screen):
        self.screen = screen
        
        #Load Alien image and set serface properties
        self.image = pygame.image.load("images/Alien_1.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        self.rect.centerx = self.screen_rect.centerx
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)