import pygame
from Agent import Agent
from Vector import Vector

class Player(Agent):

    def update(self, screenBounds):
        pressed = pygame.key.get_pressed()
        self.velocity = Vector(0, 0)
        if pressed[pygame.K_a]: self.velocity.x = -1
        if pressed[pygame.K_d]: self.velocity.x = 1
        if pressed[pygame.K_w]: self.velocity.y = -1
        if pressed[pygame.K_s]: self.velocity.y = 1

        super(Player, self).update(screenBounds)