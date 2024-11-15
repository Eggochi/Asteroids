import pygame 
from constants import *
from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen= pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))

    #groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    #grouping
    Player.containers = (updatables,drawables)

    player= Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    dt=0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               return
        screen.fill((0,0,0))
        for updatable in updatables:
            updatable.update(dt)
        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.flip()

        #frame rate
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()