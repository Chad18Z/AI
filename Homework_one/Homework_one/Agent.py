import pygame
import Constants
import math
from Vector import Vector
from DrawableObject import DrawableObject

class Agent(DrawableObject):

    def __init__(self, surface, position, size, color, speed, angularSpeed):
        super(Agent, self).__init__(surface, position, size, color)
        self.position = position
        self.velocity = Vector(0,0)
        self.speed = speed
        self.noTagBacks = False
        self.currentSpeed = 0
        self.target = Vector(0,0)
        self.activeSurface = self.surf

    def __str__(self):
        a = ("Size: " + str(self.size.x) + "\n")
        b = ("Position: " + str(self.position) + "\n")
        c = ("Velocity: " + str(self.velocity) + "\n")
        d = ("Center: " + str(self.center) + "\n")
        return a + b + c + d

    def draw(self, screen):
        endPos = self.position + self.velocity.scale(self.size.x * 2)
        # draw the sprite
        screen.blit(self.activeSurface, [self.position.x, self.position.y])      
        pygame.draw.line(screen, (0, 0, 255), (self.center.x, self.center.y), (endPos.x, endPos.y), 3)

    def update(self, bounds, graph, herd, GATES):
        if self.currentSpeed > 0:
            self.position += self.velocity.scale(self.currentSpeed)

        if self.position.x < 0:
            self.position.x = 0
        if self.position.x > (bounds.x - self.size.x):
            self.position.x = (bounds.x - self.size.x)

        if self.position.y < 0:
            self.position.y = 0

        if self.position.y > (bounds.y - self.size.x):
            self.position.y = (bounds.y - self.size.x)

        self.updateCenter()        
        self.calcSurface()
        self.faceDirection()
        
    def collision(self, other):
        if self.agentRect.colliderect(other.agentRect) and not self.noTagBacks:
            self.noTagBacks = True
            return True
        else:
            return False

    def updateCenter(self):
        self.center = self.position + self.size.scale(0.5)

    def updateVelocity(self, velocity):
        self.velocity = velocity.normalize()

        # rotates the sprite into the direction of movement
    def faceDirection(self):
        angle = math.degrees(math.atan2(-self.velocity.y, self.velocity.x))
        self.activeSurface = pygame.transform.rotate(self.surf, angle - 90)
