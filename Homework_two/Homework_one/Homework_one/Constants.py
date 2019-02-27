from Vector import Vector


FRAME_RATE = 60
WORLD_WIDTH = 1024
WORLD_HEIGHT = 768
BACKGROUND_COLOR = (100, 149, 237)
PLAYER_SIZE = 10
PLAYER_SPEED = 5.5
ENEMY_ATTACK_RANGE = 200
ENEMY_SIZE = 10
ENEMY_SPEED = 5
SHEEP_SIZE = Vector(16,32)
DOG_SIZE = Vector(16,32)


# Flocking Behavior
SHEEP_NEIGHBOR_RADIUS = 50
SHEEP_BOUNDARY_RADIUS = 50
SHEEP_ALIGNMENT_WEIGHT = 0.3
SHEEP_SEPARATION_WEIGHT = 0.3125
SHEEP_COHESION_WEIGHT = 0.3
SHEEP_DOG_INFLUENCE_WEIGHT = 0.2
SHEEP_BOUNDARY_INFLUENCE_WEIGHT = 0.2
MIN_ATTACK_DIST = 200