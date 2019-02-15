import pygame
import Constants
from Agent import Agent
from Vector import Vector

class EnemyHunter(Agent):

   def __init__(self, position, size, speed, color):
        super(EnemyHunter, self).__init__(position, size, speed, color)
        self.futurePlayerPosition = Vector(0,0)
        self.seeking = True 
        
   def update(self, player, screenBounds):
       direction = Vector(player.position.x - self.position.x, player.position.y - self.position.y)
       distance = direction.length()
       time = distance / self.speed
       targetDistance = player.speed * time
       self.futurePlayerPosition = player.position
       self.futurePlayerPosition += player.velocity.scale(distance)
       
       if self.seeking:
            a = Vector(self.futurePlayerPosition.x - self.position.x, self.futurePlayerPosition.y - self.position.y)
       else:
            a = Vector(self.position.x - self.futurePlayerPosition.x, self.position.y - self.futurePlayerPosition.y)

       b = a.length()
       if b < Constants.ENEMY_ATTACK_RANGE:
           
           self.velocity = a.normalize()
           self.position += self.velocity
       else:
            self.velocity = Vector(0,0)
       
       if self.collision(player):
            self.seeking = not self.seeking

       super(EnemyHunter, self).update(player, screenBounds)  

   def draw(self, screen, player):
        super(EnemyHunter, self).draw(screen)
        if self.velocity.dot(player.velocity) > 0:
            pygame.draw.line(screen, (255, 0, 0), (self.center.x, self.center.y), (self.futurePlayerPosition.x, self.futurePlayerPosition.y), 3)