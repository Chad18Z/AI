import pygame
import Constants
from Agent import Agent
from Vector import Vector

class Enemy(Agent):

    def update(self, player):
        #a = Vector(self.position.x - player.position.x, self.position.y - player.position.y)
        a = Vector(player.position.x - self.position.x, player.position.y - self.position.y)
        b = a.length()
        if b < Constants.ENEMY_ATTACK_RANGE:
            self.velocity = a.normalize()
        else:
            self.velocity = Vector(0,0)

        self.position += self.velocity.scale(self.speed)