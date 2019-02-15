import pygame
import Constants
from Vector import Vector

class Agent:

    def __init__(self, position, size, speed, color):
        self.position = position
        self.velocity = Vector(0,0)
        self.speed = speed
        self.size = size
        self.center = Vector(self.position.x + self.size/2, self.position.y + self.size/2)
        self.agentRect = pygame.Rect(self.position.x, self.position.y, self.size, self.size)
        self.noTagBacks = False
        self.color = color

    def __str__(self):
        a = ("Size: " + str(self.size) + "\n")
        b = ("Position: " + str(self.position) + "\n")
        c = ("Velocity: " + str(self.velocity) + "\n")
        d = ("Center: " + str(self.center) + "\n")
        return a + b + c + d

    def draw(self, screen):
        endPos = self.position + self.velocity.scale(self.size * 2)
        pygame.draw.rect (screen, self.color, self.agentRect)      
        pygame.draw.line(screen, (0, 0, 255), (self.center.x, self.center.y), (endPos.x, endPos.y), 3)

    def update(self, player, screenBounds):
        self.position += self.velocity.scale(self.speed)

        if self.position.x < 0:
            self.position.x = 0
        if self.position.x > (screenBounds.x - self.size):
            self.position.x = (screenBounds.x - self.size)

        if self.position.y < 0:
            self.position.y = 0

        if self.position.y > (screenBounds.y - self.size):
            self.position.y = (screenBounds.y - self.size)

        self.center = Vector(self.position.x + self.size/2, self.position.y + self.size/2)
        self.agentRect = pygame.Rect(self.position.x, self.position.y, self.size, self.size)

    def collision(self, other):
        if self.agentRect.colliderect(other.agentRect) and not self.noTagBacks:
            self.noTagBacks = True
            return True