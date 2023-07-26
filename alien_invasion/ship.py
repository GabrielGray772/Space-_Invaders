import pygame

class Ship():
    def __init__(self, screen):
        self.screen = screen
        
        #Load ship image and set rect (surface rectangle)
        self.image = pygame.image.load("images/Spaceship.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #start each ship at the bottom-centre of the screen
        self.rect.centerx = self.screen_rect.centerx #sets ship centre to the centre of the screen
        self.rect.bottom = self.screen_rect.bottom #sets screen bottom to bottom of the screen
        
    #draw the ship in current position    
    def blitme(self):
        self.screen.blit(self.image, self.rect)