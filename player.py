import pygame
from circleshape import *
from constants import *


class Player(CircleShape):
    def __init__(self, x, y,):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shots = pygame.sprite.Group()
        self.shot_cooldown = 0 # Use a more descriptive name

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen,"white", self.triangle(),2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if self.shot_cooldown > 0:
            self.shot_cooldown -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot() # Removed dt from the shoot method call

    def shoot(self):
        if self.shot_cooldown <= 0:
            bullet = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            bullet.velocity = forward * PLAYER_SHOOT_SPEED
            self.shots.add(bullet)
            self.shot_cooldown = PLAYER_SHOOT_COOLDOWN