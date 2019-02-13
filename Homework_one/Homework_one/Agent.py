import pygame
import Constants
from Vector import Vector

class Agent:

    def __init__(self, position, size, speed):
        self.position = position
        self.velocity = Vector(0,0)
        self.speed = speed
        self.size = size
        self.center = Vector(self.position.x + self.size/2, self.position.y + self.size/2)

    def __str__(self):
        a = ("Size: " + str(self.size) + "\n")
        b = ("Position: " + str(self.position) + "\n")
        c = ("Velocity: " + str(self.velocity) + "\n")
        d = ("Center: " + str(self.center) + "\n")
        return a + b + c + d

    def draw(self, screen):
        endPos = self.position + self.velocity.scale(self.size)
        pygame.draw.rect (screen, (0, 0, 0), pygame.Rect(self.position.x, self.position.y, self.size, self.size))      
        pygame.draw.line(screen, (0, 0, 255), (self.position.x + self.size/2, self.position.y + self.size/2), (endPos.x, endPos.y), 3)
