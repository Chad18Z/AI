import pygame
from Agent import Agent
from Vector import Vector

class Dog(Agent):
    def __init__(self, position, size, speed, surface):
        # Passing black as the color to the base class
        super(Dog, self).__init__(position, size, speed, (0,0,0))
        self.dogSurface = surface

    def update(self, screenBounds):
        pressed = pygame.key.get_pressed()
        self.velocity = Vector(0, 0)
        if pressed[pygame.K_a]: self.velocity.x = -1
        if pressed[pygame.K_d]: self.velocity.x = 1
        if pressed[pygame.K_w]: self.velocity.y = -1
        if pressed[pygame.K_s]: self.velocity.y = 1

        super(Dog, self).update(screenBounds)

    def draw(self, screen):
        endPos = self.position + self.velocity.scale(self.size.x * 2)
        #pygame.draw.rect (screen, self.color, self.agentRect)
        screen.blit(self.dogSurface, [self.position.x, self.position.y])      
        pygame.draw.line(screen, (0, 0, 255), (self.center.x, self.center.y), (endPos.x, endPos.y), 3)
