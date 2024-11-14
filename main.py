import pygame as pg
from constants import *
from player import Player

def main():
    pg.init()
    clock = pg.time.Clock()
    dt=0
    screen= pg.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))
    player= Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
               return
        screen.fill((0,0,0))
        player.draw(screen)
        pg.display.flip()

        #frame rate
        det = clock.tick(60) / 1000

if __name__ == "__main__":
    main()