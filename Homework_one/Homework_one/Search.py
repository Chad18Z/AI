import pygame
from Vector import Vector

class Search:

    def update(self, graph, player, sheep):
        pressed = pygame.key.get_pressed()
        # perfrom breadth first search if player presses A key
        if pressed[pygame.K_a]:
            playerNode = graph.getNodeFromPoint(player.position)
            sheepNode = graph.getNodeFromPoint(sheep.position)
            graph.findPath_Breadth(playerNode, sheepNode)

        # perform Djikstra's search if player presses W key
        elif pressed[pygame.K_w]:
            playerNode = graph.getNodeFromPoint(player.position)
            sheepNode = graph.getNodeFromPoint(sheep.position)
            graph.findPath_Djikstra(playerNode, sheepNode)