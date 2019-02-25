import pygame
import Constants
from Agent import Agent
from Vector import Vector
from Enemy import Enemy
import math

class Sheep(Agent):

    sheepList = []

    def __init__(self, position, size, speed, surface):
        # Passing black as the color to the base class
        super(Sheep, self).__init__(position, size, speed, (0,0,0))
        self.sheepSurface = surface
        self.currentSpeed = 0
        self.activeSurface = surface
        self.agentRect = self.sheepSurface.get_bounding_rect(min_alpha = 1)
        self.neighbors = []

    def update(self, player, screenBounds):      
        a = Vector(self.position.x - player.position.x, self.position.y - player.position.y)
        b = a.length()
        if b < Constants.ENEMY_ATTACK_RANGE:
            self.velocity = a.normalize()
            self.currentSpeed = self.speed
        else:
            self.velocity = Vector(0,0) 
            self.currentSpeed = 0
        #if self.collision(player):
        #    self.seeking = not self.seeking
        if self.currentSpeed > 0:
            self.faceDirection()
        self.calculateNeighbors()

        #self.velocity += self.align()
        self.velocity += self.cohesion()
       
        super(Sheep, self).update(screenBounds) 

    def draw(self, screen, player):
        endPos = self.position + self.velocity.scale(self.size.x * 2)
        pygame.draw.rect (screen, self.color, self.agentRect)
        screen.blit(self.activeSurface, [self.position.x, self.position.y])      
        pygame.draw.line(screen, (0, 0, 255), (self.center.x, self.center.y), (endPos.x, endPos.y), 3)

    def faceDirection(self):
        angle = math.degrees(math.atan2(-self.velocity.y, self.velocity.x))
        self.activeSurface = pygame.transform.rotate(self.sheepSurface, angle - 90)

    def updateRect(self):
        #self.agentRect = pygame.Rect(self.position.x, self.position.y, self.size.x, self.size.y)
        self.agentRect = self.sheepSurface.get_bounding_rect()
        #print(self.agentRect)

    def calculateNeighbors(self):
        self.neighbors = []
        for sheep in Sheep.sheepList:
            a = Vector(sheep.position.x - self.position.x, sheep.position.y - self.position.y)
            b = a.length()
            if b < Constants.SHEEP_NEIGHBOR_RADIUS:
                self.neighbors.append(sheep)

    def align(self):
        alignmentVector = Vector(0,0)
        if len(self.neighbors) == 0:
            return Vector(0,0)
        for neighbor in self.neighbors:
            alignmentVector += neighbor.velocity

        x = alignmentVector.x / len(self.neighbors)
        y = alignmentVector.y / len(self.neighbors)

        alignmentVector.x = x
        alignmentVector.y = y
        alignmentVector.normalize()


        return alignmentVector

    def cohesion(self):
        cohesionVector = Vector(0,0)
        if len(self.neighbors) == 0:
            return Vector(0,0)

        for neighbor in self.neighbors:
            cohesionVector += neighbor.position

        x = cohesionVector.x / len(self.neighbors)
        y = cohesionVector.y / len(self.neighbors)

        cohesionVector.x = x
        cohesionVector.y = y
        cohesionVector.normalize()

        return cohesionVector

#    def separation(self):
        #something

