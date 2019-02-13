import pygame
from Agent import Agent
from Vector import Vector

class Player(Agent):

    def update(self):
        pressed = pygame.key.get_pressed()
        self.velocity = Vector(0, 0)
        if pressed[pygame.K_a]: self.velocity.x = -self.speed
        if pressed[pygame.K_d]: self.velocity.x = self.speed
        if pressed[pygame.K_w]: self.velocity.y = -self.speed
        if pressed[pygame.K_s]: self.velocity.y = self.speed
        self.velocity.normalize()
        self.position += self.velocity
