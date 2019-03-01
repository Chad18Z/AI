import pygame
import Constants
import random
from Agent import Agent
from Vector import Vector
from Enemy import Enemy
import math

class Sheep(Agent):

    sheepList = []

    def __init__(self, surface, position, size, color, speed, angularSpeed):
        # Passing black as the color to the base class
        super(Sheep, self).__init__(surface, position, size, color, speed, angularSpeed)
        self.currentSpeed = 0
        self.activeSurface = self.surf
        self.neighbors = []

    def update(self, bounds, graph, dog, herd, GATES):      
        a = self.position - dog.position
        b = a.length()
        if b < Constants.MIN_ATTACK_DIST:
            self.calculateNeighbors()
            self.velocity = a.normalize()
            self.velocity.scale(Constants.SHEEP_DOG_INFLUENCE_WEIGHT)
            self.currentSpeed = self.speed
            self.velocity += self.calculateVelocity(self.velocity)
        else:
            #self.velocity = Vector(0,0)
            self.currentSpeed = 0

        # check to see if this sheep is within the boundary radius
        self.velocity += self.checkBounds(bounds)
        super(Sheep, self).update(bounds, graph, herd, GATES) 

    # If agent is near a boundary, then move it in the other direction
    def checkBounds(self, bounds):
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

    def calculateNeighbors(self):
        self.neighbors = []
        for sheep in Sheep.sheepList:
            a = sheep.position - self.position
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

        



