import pygame
import math
from obstacle import Obstacle
class Track():
	def drawTrack():
		# List for all the sprites in the game
        	all_sprites_list = pygame.sprite.Group()
        	all_blocks_list = pygame.sprite.Group()
        	# The player sprite
        	obstacles = {}
        	# The obstacle sprite
        	obstacles[0] = Obstacle("obstacleType1.png", (300, 200))
        	all_sprites_list.add(obstacles[0])
        	all_blocks_list.add(obstacles[0])
		for i in range(1,6):
			obstacles[i] = Obstacle("obstacleType1.png", obstacles[i-1].rect.topright)
                	all_sprites_list.add(obstacles[i])
                	all_blocks_list.add(obstacles[i])
            	obstacles[10] = Obstacle("obstacleType1.png", obstacles[5].rect.bottomleft)
            	all_sprites_list.add(obstacles[10])
            	all_blocks_list.add(obstacles[10])
            	for i in range(11, 14):
                	obstacles[i] = Obstacle("obstacleType1.png", obstacles[i-1].rect.bottomleft)
                	all_sprites_list.add(obstacles[i])
                	all_blocks_list.add(obstacles[i])

            	obstacles[16] = Obstacle("obstacleType1.png", (0,0))
            	all_sprites_list.add(obstacles[16])
            	all_blocks_list.add(obstacles[16])
            	for i in range(17,36):
                	obstacles[i] = Obstacle("obstacleType1.png", obstacles[i-1].rect.topright)
                	all_sprites_list.add(obstacles[i])
                	all_blocks_list.add(obstacles[i])

            	obstacles[37] = Obstacle("obstacleType1.png", obstacles[16].rect.bottomleft)
            	all_sprites_list.add(obstacles[37])
            	all_blocks_list.add(obstacles[37])
            	for i in range(38, 51):
                	obstacles[i] = Obstacle("obstacleType1.png", obstacles[i-1].rect.bottomleft)
                	all_sprites_list.add(obstacles[i])
                	all_blocks_list.add(obstacles[i])

            	obstacles[51] = Obstacle("obstacleType1.png", obstacles[50].rect.topright)
            	all_sprites_list.add(obstacles[51])
            	all_blocks_list.add(obstacles[51])
            	for i in range(52,70):
                	obstacles[i] = Obstacle("obstacleType1.png", obstacles[i-1].rect.topright)
                	all_sprites_list.add(obstacles[i])
                	all_blocks_list.add(obstacles[i])

            	obstacles[70] = Obstacle("obstacleType1.png", obstacles[35].rect.bottomleft)
            	all_sprites_list.add(obstacles[70])
            	all_blocks_list.add(obstacles[70])
            	for i in range(71, 83):
                	obstacles[i] = Obstacle("obstacleType1.png", obstacles[i-1].rect.bottomleft)
                	all_sprites_list.add(obstacles[i])
                	all_blocks_list.add(obstacles[i])
            	obstacles[83] = Obstacle("obstacleType1.png", (600,100))
            	all_sprites_list.add(obstacles[83])
            	all_blocks_list.add(obstacles[83])
            	obstacles[84] = Obstacle("obstacleType1.png", (40,400))
            	all_sprites_list.add(obstacles[84])
            	all_blocks_list.add(obstacles[84])
            	for i in range(85, 88):
                	obstacles[i] = Obstacle("obstacleType1.png", obstacles[i-1].rect.bottomleft)
                	all_sprites_list.add(obstacles[i])
                	all_blocks_list.add(obstacles[i])
            	obstacles[88] = Obstacle("obstacleType1.png", (80,440))
            	all_sprites_list.add(obstacles[88])
            	all_blocks_list.add(obstacles[88])
            	for i in range(89, 91):
                	obstacles[i] = Obstacle("obstacleType1.png", obstacles[i-1].rect.bottomleft)
                	all_sprites_list.add(obstacles[i])
                	all_blocks_list.add(obstacles[i])
            	obstacles[91] = Obstacle("obstacleType1.png", (120,480))
            	all_sprites_list.add(obstacles[91])
            	all_blocks_list.add(obstacles[91])
            	for i in range(92, 93):
                	obstacles[i] = Obstacle("obstacleType1.png", obstacles[i-1].rect.bottomleft)
                	all_sprites_list.add(obstacles[i])
                	all_blocks_list.add(obstacles[i])
            	obstacles[93] = Obstacle("obstacleType1.png", (160,520))
            	all_sprites_list.add(obstacles[93])
            	all_blocks_list.add(obstacles[93])
