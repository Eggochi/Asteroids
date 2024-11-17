import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroids(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self,screen):
        return pygame.draw.circle(screen,(255,255,255),self.position,self.radius,2)
    
    def update(self, dt):
        self.position += self.velocity*dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        rotation = random.uniform(20,50)
        velocity_1= self.velocity.rotate(rotation)
        velocity_2= self.velocity.rotate(-rotation)
        new_radius= self.radius - ASTEROID_MIN_RADIUS

        new_asteroid_1= Asteroids(self.position[0],self.position[1],new_radius)
        new_asteroid_2= Asteroids(self.position[0],self.position[1],new_radius)

        new_asteroid_1.velocity = velocity_1* 1.2
        new_asteroid_2.velocity = velocity_2* 1.2 