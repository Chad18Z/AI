import pygame
from Vector import Vector

class Enemy:

    def __init__(self, position, velocity, size):
        self.position = position
        self.velocity = velocity
        velocity.normalize();
        self.size = size

    def draw(self, screen):
        pygame.draw.rect (screen, (0, 0, 0), pygame.Rect(self.position.x, self.position.y, self.size, self.size)) 
        endPos = self.position + self.velocity.scale(self.size * 2)
        pygame.draw.line(screen, (0, 0, 0), (self.position.x, self.position.y), (endPos.x, endPos.y), 3)

    def update(self):
        self.position += self.velocity

      