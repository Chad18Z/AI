import pygame
from Vector import Vector

class Search:

    def update(self, graph, player, sheep):
        pressed = pygame.key.get_pressed()
        # perfrom breadth first search if player presses A key
        if pressed[pygame.K_a]:
            graph.reset()
            playerNode = graph.getNodeFromPoint(player.position)
            sheepNode = graph.getNodeFromPoint(sheep.position)
            graph.findPath_Breadth(playerNode, sheepNode)

        # perform Djikstra's search if player presses W key
        elif pressed[pygame.K_w]:
            graph.reset()
            playerNode = graph.getNodeFromPoint(player.position)
            sheepNode = graph.getNodeFromPoint(sheep.position)
            graph.findPath_Djikstra(playerNode, sheepNode)

        # perform BEST search if player presses D key
        elif pressed[pygame.K_d]:
            graph.reset()
            playerNode = graph.getNodeFromPoint(player.position)
            sheepNode = graph.getNodeFromPoint(sheep.position)
            graph.findPath_BestFirst(playerNode, sheepNode)

        # perform BEST search if player presses D key
        elif pressed[pygame.K_s]:
            graph.reset()
            playerNode = graph.getNodeFromPoint(player.position)
            sheepNode = graph.getNodeFromPoint(sheep.position)
            graph.findPath_AStar(playerNode, sheepNode)