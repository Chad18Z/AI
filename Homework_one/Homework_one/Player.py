import pygame
import Constants
from Graph import Graph
from Agent import Agent
from Vector import Vector

class Player(Agent):

    def update(self, screenBounds, graph, herd, GATES):
        #pressed = pygame.key.get_pressed()
        #self.velocity = Vector(0, 0)
        #if pressed[pygame.K_a]: self.velocity.x = -1
        #if pressed[pygame.K_d]: self.velocity.x = 1
        #if pressed[pygame.K_w]: self.velocity.y = -1
        #if pressed[pygame.K_s]: self.velocity.y = 1
        #if self.velocity != Vector(0,0):
            #self.currentSpeed = Constants.DOG_SPEED
        super(Player, self).update(screenBounds, graph, herd, GATES)