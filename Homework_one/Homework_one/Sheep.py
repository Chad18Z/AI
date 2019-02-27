import pygame
import Constants
import random
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
        self.agentRect = self.activeSurface.get_bounding_rect()
        self.velocity = Vector((random.uniform(0,1) - .5), (random.uniform(0,1) - .5))
        self.velocity.normalize()
        self.neighbors = []
        self.size = Vector(self.agentRect.width, self.agentRect.height)

    def update(self, player, screenBounds):      
        a = Vector(self.position.x - player.position.x, self.position.y - player.position.y)
        b = a.length()
        if b < Constants.ENEMY_ATTACK_RANGE:
            self.calculateNeighbors()
            self.velocity = a.normalize()
            self.velocity.scale(Constants.SHEEP_DOG_INFLUENCE_WEIGHT)
            self.currentSpeed = self.speed
            self.velocity += self.calculateVelocity(self.velocity)
            self.faceDirection()
            self.updateRect()
        else:
            self.velocity = Vector(0,0)
            self.currentSpeed = 0

        # check to see if this sheep is within the boundary radius
        self.velocity += self.checkBounds(screenBounds)

        super(Sheep, self).update(screenBounds) 

    # If agent is near a boundary, then move it in the other direction
    def checkBounds(self, screenBounds):
        boundsVector = Vector(0,0)
        if self.position.x < Constants.SHEEP_BOUNDARY_RADIUS:
            boundsVector.x += 1
        if (self.position.x > (Constants.WORLD_WIDTH - Constants.SHEEP_BOUNDARY_RADIUS)):
            boundsVector.x -= 1
        if self.position.y < Constants.SHEEP_BOUNDARY_RADIUS:
            boundsVector.y += 1
        if(self.position.y > (Constants.WORLD_HEIGHT - Constants.SHEEP_BOUNDARY_RADIUS)):
            boundsVector.y -= 1
        return boundsVector.normalize()

    def calculateVelocity(self, velocity):       
        velocity += self.align().scale(Constants.SHEEP_ALIGNMENT_WEIGHT)
        velocity += self.cohesion().scale(Constants.SHEEP_COHESION_WEIGHT)
        velocity += self.separation().scale(Constants.SHEEP_SEPARATION_WEIGHT)
        return velocity

    def draw(self, screen, player):

        # calculate the end position of the velocity line
        endPos = self.position + self.velocity.scale(self.size.x * 2)

        # draw the rect
        pygame.draw.rect (screen, self.color, self.agentRect)

        # draw the sprite
        screen.blit(self.activeSurface, [self.position.x, self.position.y]) 
        
        # draw the velocity line
        pygame.draw.line(screen, (0, 0, 255), (self.center.x, self.center.y), (endPos.x, endPos.y), 1)

        # draw lines to neighbors
        self.drawNeighborLines(screen)

        # direction to the player (dog)
        a = Vector(self.position.x - player.position.x, self.position.y - player.position.y)

        # magnitude of the direction vector
        b = a.length()

        # check if dog is in range. If it is, then draw a line to it
        if b < Constants.ENEMY_ATTACK_RANGE:
            pygame.draw.line(screen, (255, 0, 0), (self.center.x, self.center.y), (player.center.x, player.center.y), 1)

    # rotates the sprite into the direction of movement
    def faceDirection(self):
        angle = math.degrees(math.atan2(-self.velocity.y, self.velocity.x))
        self.activeSurface = pygame.transform.rotate(self.sheepSurface, angle - 90)

    # updates the bounding rect around this sheep
    def updateRect(self):
        #self.agentRect = pygame.Rect(self.position.x, self.position.y, self.size.x, self.size.y)
        tempRect = self.activeSurface.get_bounding_rect()
        self.agentRect = pygame.Rect(self.position.x - tempRect.left, self.position.y - tempRect.y, tempRect.w, tempRect.h)
        self.agentRect.move(-4,4)

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

    def drawNeighborLines(self, screen):
        if len(self.neighbors) == 0:
            return
        for neighbor in self.neighbors:
            pygame.draw.line(screen, (0, 0, 255), (self.center.x, self.center.y), (neighbor.center.x, neighbor.center.y), 1)

    def cohesion(self):
        cohesionVector = Vector(0,0)
        if len(self.neighbors) == 0:
            return Vector(0,0)

        for neighbor in self.neighbors:
            cohesionVector += neighbor.position

        x = cohesionVector.x / len(self.neighbors)
        y = cohesionVector.y / len(self.neighbors)

        directionVector = Vector(x - self.position.x, y - self.position.y)
        directionVector.normalize()

        return directionVector

    def separation(self):
        separationVector = Vector(0,0)
        if len(self.neighbors) == 0:
            return Vector(0,0)
        for neighbor in self.neighbors:
            separationVector.x += neighbor.position.x - self.position.x
            separationVector.y += neighbor.position.y - self.position.y

        x = separationVector.x / len(self.neighbors)
        y = separationVector.y / len(self.neighbors)

        separationVector.x = x * -1
        separationVector.y = y * -1

        separationVector.normalize()
        return separationVector
        



