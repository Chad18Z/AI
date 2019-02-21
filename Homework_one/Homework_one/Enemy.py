import pygame
import Constants
from Agent import Agent
from Vector import Vector

class Enemy(Agent):

    def __init__(self, position, size, speed, color):
        super(Enemy, self).__init__(position, size, speed, color)
        self.seeking = True

    def update(self, player, screenBounds):       
        if self.seeking:
            a = Vector(player.position.x - self.position.x, player.position.y - self.position.y)
        else:
            a = Vector(self.position.x - player.position.x, self.position.y - player.position.y)

        b = a.length()
        if b < Constants.ENEMY_ATTACK_RANGE:
            self.velocity = a.normalize()
        else:
            self.velocity = Vector(0,0)
        
        if self.collision(player):
            self.seeking = not self.seeking

        super(Enemy, self).update(screenBounds)      

    def draw(self, screen, player):
        super(Enemy, self).draw(screen)
        if self.velocity.dot(player.velocity) > 0:
            pygame.draw.line(screen, (255, 0, 0), (self.center.x, self.center.y), (player.center.x, player.center.y), 3)