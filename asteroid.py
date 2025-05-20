from circleshape import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.velocity = pygame.Vector2(0, 0)
    def draw(self, screen):
        white = (255,255,255)
        pygame.draw.circle(screen, white ,self.position, self.radius,2)
    def update(self,dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            angle_rot = random.uniform(20, 50)
            vector_1 = pygame.math.Vector2.rotate(self.position, angle_rot)
            vector_2 = pygame.math.Vector2.rotate(self.position, -angle_rot)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            small_one = Asteroid(self.position.x, self.position.y, new_radius)
            small_two = Asteroid(self.position.x, self.position.y, new_radius)
            small_one.velocity = vector_1 * 1.2
            small_two.velocity = vector_2 * 1.2
        pass