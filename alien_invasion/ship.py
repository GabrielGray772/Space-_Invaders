import pygame

class Ship():
    
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        
        #Load ship image and set rect (surface rectangle)
        self.image = pygame.image.load("images/Spaceship.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #start each ship at the bottom-centre of the screen
        self.rect.centerx = self.screen_rect.centerx #sets ship centre to the centre of the screen
        self.rect.bottom = self.screen_rect.bottom #sets screen bottom to bottom of the screen
        
        #Store the speed of the ship for ship center
        self.center = float(self.rect.centerx)
        
        #Movement Flags
        self.moving_right = False
        self.moving_left = False    
    
    def update(self):
        #update the ships movement based on movement flag and Ship speed factor
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
            
        #update rect object from self.center
        self.rect.centerx = self.center
        
    #draw the ship in current position    
    def blitme(self):
        self.screen.blit(self.image, self.rect)