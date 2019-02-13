import pygame
import Constants
from Enemy import Enemy
from Player import Player
from Vector import Vector

pygame.init()
screen = pygame.display.set_mode((Constants.WORLD_WIDTH, Constants.WORLD_HEIGHT))
done = False

clock = pygame.time.Clock()
#enemy = Enemy(Vector(0,0), Vector(1,1), 25)
player = Player(Vector(Constants.WORLD_WIDTH / 2, Constants.WORLD_HEIGHT / 2), Constants.PLAYER_SIZE, 5.5)

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

        screen.fill((Constants.BACKGROUND_COLOR))

        #enemy.update()
        #enemy.draw(screen)
        player.update()
        player.draw(screen)

        pygame.display.flip()
        clock.tick(Constants.FRAME_RATE)