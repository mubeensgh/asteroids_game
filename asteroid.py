from circleshape import *
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.velocity = pygame.Vector2(0, 0)
    def draw(self, screen):
        white = (255,255,255)
        pygame.draw.circle(screen, white ,self.position, self.radius,2)
    def update(self,dt):
        self.position += self.velocity * dt