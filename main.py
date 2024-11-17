import pygame 
import sys
from constants import *
from player import Player
from asteroids import Asteroids
from asteroid_field import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen= pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))

    #groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots =pygame.sprite.Group()

    #grouping
    Player.containers = (updatables,drawables)
    Asteroids.containers = (updatables,drawables,asteroids)
    AsteroidField.containers = (updatables)
    Shot.containers=(updatables,drawables,shots)

    player= Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield= AsteroidField()
    dt=0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               return
        screen.fill((0,0,0))
        for updatable in updatables:
            updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player):
                sys.exit("Game over!")
            
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()

        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.flip()

        #frame rate
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()