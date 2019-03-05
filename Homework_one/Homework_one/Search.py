import pygame
from Vector import Vector

class Search:

    def update(self, graph, player, sheep):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_a]:
            playerNode = graph.getNodeFromPoint(player.position)
            sheepNode = graph.getNodeFromPoint(sheep.position)
            graph.findPath_Breadth(playerNode, sheepNode)
