import pygame
import Constants
import random
from Enemy import Enemy
from EnemyHunter import EnemyHunter
from Player import Player
from Vector import Vector
from Sheep import Sheep
from Dog import Dog

pygame.init()
screen = pygame.display.set_mode((Constants.WORLD_WIDTH, Constants.WORLD_HEIGHT))
done = False

clock = pygame.time.Clock()

#enemy = Enemy(Vector(random.randint(0, Constants.WORLD_WIDTH), random.randint(0, Constants.WORLD_HEIGHT)), Constants.ENEMY_SIZE, Constants.ENEMY_SPEED, (0,255,0))
#enemyHunter = EnemyHunter(Vector(random.randint(0, Constants.WORLD_WIDTH), random.randint(0, Constants.WORLD_HEIGHT)), Constants.ENEMY_SIZE, 5, (255,0,255))

sheepSurface = pygame.image.load("sheep.png")
dogSurface = pygame.image.load("collie.png")

player = Dog(Vector(Constants.WORLD_WIDTH / 2, Constants.WORLD_HEIGHT / 2), Constants.DOG_SIZE, Constants.PLAYER_SPEED, dogSurface)

enemyList = []

for i in range (100):
    #enemy = Enemy(Vector(random.randint(0, Constants.WORLD_WIDTH), random.randint(0, Constants.WORLD_HEIGHT)), Constants.ENEMY_SIZE, Constants.ENEMY_SPEED, (0,255,0))
    #enemyHunter = EnemyHunter(Vector(random.randint(0, Constants.WORLD_WIDTH), random.randint(0, Constants.WORLD_HEIGHT)), Constants.ENEMY_SIZE, Constants.ENEMY_SPEED, (255,0,255))
    #enemyList.append(enemy)
    #enemyList.append(enemyHunter)
    sheep = Sheep(Vector(random.randint(0, Constants.WORLD_WIDTH), random.randint(0, Constants.WORLD_HEIGHT)), Constants.SHEEP_SIZE, Constants.ENEMY_SPEED, sheepSurface)
    enemyList.append(sheep)

Sheep.sheepList = enemyList

TAGEVENT = pygame.USEREVENT
tagBack = False

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == TAGEVENT:
                    for enemy in enemyList:
                        enemy.noTagBacks = False

                    tagBack = False
                    TAGEVENT = pygame.USEREVENT

        screen.fill((Constants.BACKGROUND_COLOR))

        player.update(Vector(Constants.WORLD_WIDTH, Constants.WORLD_HEIGHT))
        player.draw(screen)

        for sheep in enemyList:
            #enemy.update(player, Vector(Constants.WORLD_WIDTH, Constants.WORLD_HEIGHT))
            #enemy.draw(screen, player)
            sheep.update(player, Vector(Constants.WORLD_WIDTH, Constants.WORLD_HEIGHT))
            sheep.draw(screen, player)
            #if enemy.noTagBacks and not tagBack: 
            #    tagBack = True
                #pygame.time.set_timer(TAGEVENT, 1000)

        pygame.display.flip()
        clock.tick(Constants.FRAME_RATE)