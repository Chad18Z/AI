import pygame
import Constants
from Node import Node
from Vector import Vector

class Search:

    def __init__(self):
        self.path = []
        self.isTracking = False # is the dog currently moving to the next node?
        self.nodeCounter = 0
        self.hasPath = False
        self.currentSearch = 0

    def update(self, graph, player, sheep):
        self.player = player
        pressed = pygame.key.get_pressed()
        # perfrom breadth first search if player presses A key
        if pressed[pygame.K_f]:
            graph.reset()
            playerNode = graph.getNodeFromPoint(player.position)
            sheepNode = graph.getNodeFromPoint(sheep.position)
            self.path = graph.findPath_Breadth(playerNode, sheepNode)
            self.hasPath = True
            self.currentSearch = 1

        # perform Djikstra's search if player presses W key
        elif pressed[pygame.K_d]:
            graph.reset()
            playerNode = graph.getNodeFromPoint(player.position)
            sheepNode = graph.getNodeFromPoint(sheep.position)
            self.path = graph.findPath_Djikstra(playerNode, sheepNode)
            self.hasPath = True
            self.currentSearch = 2

        # perform BEST search if player presses D key
        elif pressed[pygame.K_s]:
            graph.reset()
            playerNode = graph.getNodeFromPoint(player.position)
            sheepNode = graph.getNodeFromPoint(sheep.position)
            self.path = graph.findPath_BestFirst(playerNode, sheepNode)
            self.hasPath = True
            self.currentSearch = 3

        # perform A* search if player presses D key
        elif pressed[pygame.K_a]:
            graph.reset()
            playerNode = graph.getNodeFromPoint(player.position)
            sheepNode = graph.getNodeFromPoint(sheep.position)
            self.path = graph.findPath_AStar(playerNode, sheepNode)
            self.hasPath = True
            self.currentSearch = 4

        # check if the path has been initialized and the dog is not yet moving to the next node
        if self.hasPath and self.isTracking == False:
            self.isTracking = True
            self.nodeCounter += 1
            if self.nodeCounter > (len(self.path) - 1):
                path = []
                self.hasPath = False
                self.nodeCounter = 0
                self.makeNewPath(graph, player, sheep)
            else:
                self.curr = self.path[self.nodeCounter]
                self.player.currentSpeed = Constants.DOG_SPEED
                self.player.velocity = (self.curr.center - self.player.center).normalize()

        # check if close to next node, if we are then let's cycle to the node following the next node
        elif self.hasPath and (self.curr.center - self.player.center).length() < 5:
            self.isTracking = False
            self.player.currentSpeed = 0
        
    def makeNewPath(self, graph, player, sheep):
            playerNode = graph.getNodeFromPoint(player.position)
            sheepNode = graph.getNodeFromPoint(sheep.position)

            if self.currentSearch == 1:
                self.path = graph.findPath_Breadth(playerNode, sheepNode)

            elif self.currentSearch == 2:
                self.path = graph.findPath_Djikstra(playerNode, sheepNode)

            elif self.currentSearch == 3:
                self.path = graph.findPath_BestFirst(playerNode, sheepNode)

            elif self.currentSearch == 4:
                self.path = graph.findPath_AStar(playerNode, sheepNode)             
            else:
                self.path = graph.findPath_AStar(playerNode, sheepNode)
            self.hasPath = True
            self.isTracking = False
