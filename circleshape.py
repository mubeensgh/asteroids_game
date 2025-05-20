import pygame
from constants import *

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # to be used later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius
    
    def draw(self, screen):
        #sub-classes must override this
        pass
    def update(self, dt):
        #sub-classes must override this
        pass
    def collided(self,cs_object):
        distance = pygame.math.Vector2.distance_to(self.position, cs_object.position)
        if self.radius + cs_object.radius >= distance:
            return True
        else:
            return False

class Shot(CircleShape):
        def __init__(self, x, y, radius):
            super().__init__(x, y, radius) # Call the parent's __init__ with x, y, and radius
            self.velocity = pygame.Vector2(0, 0)
        def draw(self, screen):
            white = (255,255,255)
            pygame.draw.circle(screen, white ,self.position, self.radius ,2) # Use self.radius here
        def update(self,dt):
            self.position += self.velocity * dt