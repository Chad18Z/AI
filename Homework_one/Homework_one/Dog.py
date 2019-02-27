import pygame
import math
from Agent import Agent
from Vector import Vector

class Dog(Agent):
    def __init__(self, position, size, speed, surface):
        # Passing black as the color to the base class
        super(Dog, self).__init__(position, size, speed, (0,0,0))
        self.dogSurface = surface
        self.activeSurface = surface
        self.currentSpeed = 0

    def update(self, screenBounds):
        pressed = pygame.key.get_pressed()
        self.velocity = Vector(0, 0)
        if pressed[pygame.K_a]: self.velocity.x = -1
        if pressed[pygame.K_d]: self.velocity.x = 1
        if pressed[pygame.K_w]: self.velocity.y = -1
        if pressed[pygame.K_s]: self.velocity.y = 1
        if self.velocity == Vector(0,0):
            currentSpeed = 0
        else:
            currentSpeed = self.speed
            self.faceDirection()
        super(Dog, self).update(screenBounds)

    def draw(self, screen):
        endPos = self.position + self.velocity.scale(self.size.x * 2)
        pygame.draw.rect (screen, self.color, self.agentRect)
        screen.blit(self.activeSurface, [self.position.x, self.position.y])      
        pygame.draw.line(screen, (0, 0, 255), (self.center.x, self.center.y), (endPos.x, endPos.y), 1)

    def faceDirection(self):
        angle = math.degrees(math.atan2(-self.velocity.y, self.velocity.x))
        self.activeSurface = pygame.transform.rotate(self.dogSurface, angle - 90)