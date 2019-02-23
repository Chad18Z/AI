import pygame
import Constants
from Agent import Agent
from Vector import Vector
from Enemy import Enemy

class Sheep(Agent):

    def __init__(self, position, size, speed, surface):
        # Passing black as the color to the base class
        super(Sheep, self).__init__(position, size, speed, (0,0,0))
        self.sheepSurface = surface

    def update(self, player, screenBounds):      
        a = Vector(self.position.x - player.position.x, self.position.y - player.position.y)
        b = a.length()
        if b < Constants.ENEMY_ATTACK_RANGE:
            self.velocity = a.normalize()
        else:
            self.velocity = Vector(0,0)        
        #if self.collision(player):
        #    self.seeking = not self.seeking
        super(Sheep, self).update(screenBounds) 

    def draw(self, screen, player):
        endPos = self.position + self.velocity.scale(self.size.x * 2)
        #pygame.draw.rect (screen, self.color, self.agentRect)
        screen.blit(self.sheepSurface, [self.position.x, self.position.y])      
        pygame.draw.line(screen, (0, 0, 255), (self.center.x, self.center.y), (endPos.x, endPos.y), 3)