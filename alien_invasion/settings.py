# Stores all settings for SI
class Settings():
    def __init__(self):
        # Screen and ship settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (230,230,230) #off white 
        self.ship_speed_factor = 1.5
        # Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = 60, 60, 60 #Dark Gray
        self.bullets_allowed = 4
        # Alien Settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # Fleet direction of 1 representing Right and -1 representing Left
        self.fleet_direction = 1
        