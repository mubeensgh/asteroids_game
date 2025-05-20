from constants import *
import pygame
import random
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import *
import sys

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots)
    asfield = AsteroidField(asteroids)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for i_asteroid in asteroids:
            if i_asteroid.collided(player):
                print("Game over!")
                sys.exit("Bye")
        for shot in player.shots:
            shot.update(dt)
        for d in drawable:
            d.draw(screen)
        for shot in player.shots:
            shot.draw(screen)
        for k_asteroid in asteroids:
            for i_shot in shots:
                if k_asteroid.collided(i_shot):
                    k_asteroid.split()
                    i_shot.kill()
        pygame.display.flip()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()