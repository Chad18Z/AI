import pygame
from Vector import Vector

class Player:

    def __init__(self, position, size, speed):
        self.position = position
        self.velocity = Vector(0, 0)
        self.size = size
        self.speed = speed
        self.center = Vector(position.x + size/2, position.y + size/2)

    def __str__(self):
        print ("Size: " + self.size)
        print ("Position: " + self.position)
        print ("Velocity: " + self.velocity)
        print ("Center: " + self.center)

    def draw(self, screen):
        pygame.draw.rect (screen, (0, 0, 0), pygame.Rect(self.position.x, self.position.y, self.size, self.size)) 
        endPos = self.position + self.velocity
        pygame.draw.line(screen, (0, 0, 255), (self.position.x + self.size / 2, self.position.y + self.size / 2), (endPos.x, endPos.y), 3)

    def update(self):
        pressed = pygame.key.get_pressed()
        self.velocity = Vector(0, 0)
        if pressed[pygame.K_a]: self.velocity.x = -self.speed
        if pressed[pygame.K_d]: self.velocity.x = self.speed
        if pressed[pygame.K_w]: self.velocity.y = -self.speed
        if pressed[pygame.K_s]: self.velocity.y = self.speed
        self.velocity.normalize()
        self.position += self.velocity
