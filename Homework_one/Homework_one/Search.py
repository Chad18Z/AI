import pygame

class Search:

    def update(self, graph, player, sheep):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_a]:
            graph.findPath_Breadth(player, sheep)
