import pygame
from PodSixNet.Connection import ConnectionListener, connection
import sys
import time
import math
from goal import Goal
from car import Car
from obstacle import Obstacle


class carGame(ConnectionListener):
	def __init__(self):
		self.checkErrors = pygame.init()
		if self.checkErrors[1] > 0:
			print("(!) Had {0} initializign errors...exiting".format(self.checkErrors[1]))
			sys.exit(-1)
		else:
			print("(+) Game initialized successfully")
		self.background = pygame.image.load("bg1.png")
		# Screen
		size = (800, 600)
		self.screen = pygame.display.set_mode(size)
		pygame.display.set_caption("Basic Scenery")
		# List for all the sprites in the game

		self.all_sprites_list = pygame.sprite.Group()
		self.all_blocks_list = pygame.sprite.Group()

		# The player sprite

		self.playerCar = Car("car.png", (100, 100))
		self.all_sprites_list.add(self.playerCar)
		self.goalX = Goal("goalx.png", (694, 490))
		self.all_sprites_list.add(self.goalX)
		self.obstacles = [None] * 1000
		# The obstacle sprite
		# self.obstacles[0] = Obstacle("obstacleType1.png", (300, 200))
		# self.all_sprites_list.add(self.obstacles[0])
		# self.all_blocks_list.add(self.obstacles[0])

		# for i in range(1, 6):
		# 	self.obstacles[i] = Obstacle("obstacleType1.png", self.obstacles[i - 1].rect.topright)
		# 	self.all_sprites_list.add(self.obstacles[i])
		# 	self.all_blocks_list.add(self.obstacles[i])
		# self.obstacles[10] = Obstacle("obstacleType1.png", self.obstacles[5].rect.bottomleft)
		# self.all_sprites_list.add(self.obstacles[10])
		# self.all_blocks_list.add(self.obstacles[10])
		# for i in range(11, 14):
		# 	self.obstacles[i] = Obstacle("obstacleType1.png", self.obstacles[i - 1].rect.bottomleft)
		# 	self.all_sprites_list.add(self.obstacles[i])
		# 	self.all_blocks_list.add(self.obstacles[i])

		self.obstacles[16] = Obstacle("obstacleType1.png", (0, 0))
		self.all_sprites_list.add(self.obstacles[16])
		self.all_blocks_list.add(self.obstacles[16])
		for i in range(17, 36):
			self.obstacles[i] = Obstacle("obstacleType1.png", self.obstacles[i - 1].rect.topright)
			self.all_sprites_list.add(self.obstacles[i])
			self.all_blocks_list.add(self.obstacles[i])

		self.obstacles[37] = Obstacle("obstacleType1.png", self.obstacles[16].rect.bottomleft)
		self.all_sprites_list.add(self.obstacles[37])
		self.all_blocks_list.add(self.obstacles[37])
		for i in range(38, 51):
			self.obstacles[i] = Obstacle("obstacleType1.png", self.obstacles[i - 1].rect.bottomleft)
			self.all_sprites_list.add(self.obstacles[i])
			self.all_blocks_list.add(self.obstacles[i])

		self.obstacles[51] = Obstacle("obstacleType1.png", self.obstacles[50].rect.topright)
		self.all_sprites_list.add(self.obstacles[51])
		self.all_blocks_list.add(self.obstacles[51])
		for i in range(52, 70):
			self.obstacles[i] = Obstacle("obstacleType1.png", self.obstacles[i - 1].rect.topright)
			self.all_sprites_list.add(self.obstacles[i])
			self.all_blocks_list.add(self.obstacles[i])

		self.obstacles[70] = Obstacle("obstacleType1.png", self.obstacles[35].rect.bottomleft)
		self.all_sprites_list.add(self.obstacles[70])
		self.all_blocks_list.add(self.obstacles[70])
		for i in range(71, 83):
			self.obstacles[i] = Obstacle("obstacleType1.png", self.obstacles[i - 1].rect.bottomleft)
			self.all_sprites_list.add(self.obstacles[i])
			self.all_blocks_list.add(self.obstacles[i])
		# self.obstacles[84] = Obstacle("obstacleType1.png", (40, 400))
		# self.all_sprites_list.add(self.obstacles[84])
		# self.all_blocks_list.add(self.obstacles[84])
		# for i in range(85, 88):
		# 	self.obstacles[i] = Obstacle("obstacleType1.png", self.obstacles[i - 1].rect.bottomleft)
		# 	self.all_sprites_list.add(self.obstacles[i])
		# 	self.all_blocks_list.add(self.obstacles[i])
		# self.obstacles[88] = Obstacle("obstacleType1.png", (80, 440))
		# self.all_sprites_list.add(self.obstacles[88])
		# self.all_blocks_list.add(self.obstacles[88])
		# for i in range(89, 91):
		# 	self.obstacles[i] = Obstacle("obstacleType1.png", self.obstacles[i - 1].rect.bottomleft)
		# 	self.all_sprites_list.add(self.obstacles[i])
		# 	self.all_blocks_list.add(self.obstacles[i])
		# self.obstacles[91] = Obstacle("obstacleType1.png", (120, 480))
		# self.all_sprites_list.add(self.obstacles[91])
		# self.all_blocks_list.add(self.obstacles[91])
		# for i in range(92, 93):
		# 	self.obstacles[i] = Obstacle("obstacleType1.png", self.obstacles[i - 1].rect.bottomleft)
		# 	self.all_sprites_list.add(self.obstacles[i])
		# 	self.all_blocks_list.add(self.obstacles[i])
		# self.obstacles[93] = Obstacle("obstacleType1.png", (160, 520))
		# self.all_sprites_list.add(self.obstacles[93])
		# self.all_blocks_list.add(self.obstacles[93])
		# self.obstacles[94] = Obstacle("obstacleType1.png", (720, 40))
		# self.all_sprites_list.add(self.obstacles[94])
		# self.all_blocks_list.add(self.obstacles[94])
		# for i in range(95, 98):
		# 	self.obstacles[i] = Obstacle("obstacleType1.png", self.obstacles[i - 1].rect.bottomleft)
		# 	self.all_sprites_list.add(self.obstacles[i])
		# 	self.all_blocks_list.add(self.obstacles[i])
		# self.obstacles[98] = Obstacle("obstacleType1.png", (680,40))
		# self.all_sprites_list.add(self.obstacles[98])
		# self.all_blocks_list.add(self.obstacles[98])
		# for i in range(99, 101):
		# 	self.obstacles[i] = Obstacle("obstacleType1.png", self.obstacles[i-1].rect.bottomleft)
		# 	self.all_sprites_list.add(self.obstacles[i])
		# 	self.all_blocks_list.add(self.obstacles[i])
		# self.obstacles[101] = Obstacle("obstacleType1.png", (640,40))
		# self.all_sprites_list.add(self.obstacles[101])
		# self.all_blocks_list.add(self.obstacles[101])
		# for i in range(102, 103):
    		# 	self.obstacles[i] = Obstacle("obstacleType1.png", self.obstacles[i-1].rect.bottomleft)
    		# 	self.all_sprites_list.add(self.obstacles[i])
    		# 	self.all_blocks_list.add(self.obstacles[i])

		self.obstacles[0] = Obstacle("square.png",(245, 160))
		self.all_sprites_list.add(self.obstacles[0])
		self.all_blocks_list.add(self.obstacles[0])

		self.obstacles[1] = Obstacle("square.png", (525, 300))
		self.all_sprites_list.add(self.obstacles[1])
		self.all_blocks_list.add(self.obstacles[1])

		# self.obstacles[2] = Obstacle("square.png", (400, 350))
		# self.all_sprites_list.add(self.obstacles[0])
		# self.all_blocks_list.add(self.obstacles[0])

		# self.obstacles[103] = Obstacle("obstacleType1.png", (600,40))
		# self.all_sprites_list.add(self.obstacles[103])
		# self.all_blocks_list.add(self.obstacles[103])
		# self.obstacles[104] = Obstacle("obstacleType1.png", (240,40))
		# self.all_sprites_list.add(self.obstacles[104])
		# self.all_blocks_list.add(self.obstacles[104])
		# self.obstacles[105] = Obstacle("obstacleType1.png", (280,40))
		# self.all_sprites_list.add(self.obstacles[105])
		# self.all_blocks_list.add(self.obstacles[105])
		# self.obstacles[106] = Obstacle("obstacleType1.png", (240,80))
		# self.all_sprites_list.add(self.obstacles[106])
		# self.all_blocks_list.add(self.obstacles[106])
		# self.obstacles[107] = Obstacle("obstacleType1.png", (280,80))
		# self.all_sprites_list.add(self.obstacles[107])
		# self.all_blocks_list.add(self.obstacles[107])
		# self.obstacles[108] = Obstacle("obstacleType1.png", (320,400))
		# self.all_sprites_list.add(self.obstacles[108])
		# self.all_blocks_list.add(self.obstacles[108])
		# self.obstacles[109] = Obstacle("obstacleType1.png", (280,400))
		# self.all_sprites_list.add(self.obstacles[109])
		# self.all_blocks_list.add(self.obstacles[109])
	
		self.carryOn = True  # Game state variable

		self.clock = pygame.time.Clock()
		self.Connect()
	def calculateDist(self, carCenter, sol):
		return math.sqrt((carCenter[0] - sol[0]) ** 2 + (carCenter[1] - sol[1]) ** 2)

	def update(self):
		connection.Pump()
		self.Pump()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.carryOn = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_x:
					self.carryOn = False
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			distList = self.getSolution(self.playerCar, self.obstacles)
			self.playerCar.rotateLeft(3,distList, self.goalX.rect.center)

		if keys[pygame.K_RIGHT]:
			distList = self.getSolution(self.playerCar, self.obstacles)
			self.playerCar.rotateRight(3, distList, self.goalX.rect.center)

		if keys[pygame.K_UP]:
			distList = self.getSolution(self.playerCar, self.obstacles)
			self.playerCar.moveForward(2, distList, self.goalX.rect.center)

		if keys[pygame.K_DOWN]:
			distList = self.getSolution(self.playerCar, self.obstacles)
			self.playerCar.moveBackward(2, distList, self.goalX.rect.center)
		goal_check = pygame.sprite.spritecollide(self.playerCar, [self.goalX], False)
		for car in goal_check:
			print("Mission Accomplished")
			self.carryOn = False
		collision_list = pygame.sprite.spritecollide(self.playerCar, self.all_blocks_list, False)
		self.all_sprites_list.update()
		# Drawing on Screen
		# screen.fill(GREEN)
		self.screen.blit(self.background, (0, 0))

		# Draw The Road
		# pygame.draw.rect(screen, BLACK, [40, 0, 200, 300])
		# Draw Line painting on the road
		# pygame.draw.line(screen, WHITE, [140, 0], [140, 300], 5)

		# Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
		self.all_sprites_list.draw(self.screen)

		# Refresh Screen
		pygame.display.flip()
		self.clock.tick(90)

		for car in collision_list:
			print("Car crash!")
			pygame.event.wait()
			time.sleep(2)
			# End Of Game
			self.carryOn = False
	def getSolution(self, car, obstacleList):
		distList = []
		for obs in obstacleList:
			if obs is None:
				continue
			for k in range(len(car.line)):
				tempDist = []
				for j in range(len(obs.line)):
					if self.isSolutionExists(car.line[k], obs.line[j]):
						sol = self.pointOfIntersection(car.line[k], obs.line[j])
						if j == 0:
							if sol == obs.rect.topleft or sol == obs.rect.topright:
								tempDist.append(self.calculateDist(car.rect.center, sol))
							elif self.isLambda(obs.rect.topleft, obs.rect.topright, sol):
								tempDist.append(self.calculateDist(car.rect.center, sol))
						elif j == 1:
							if sol == obs.rect.bottomleft or sol == obs.rect.bottomright:
								tempDist.append(self.calculateDist(car.rect.center, sol))
							elif self.isLambda(obs.rect.bottomleft, obs.rect.bottomright, sol):
								tempDist.append(self.calculateDist(car.rect.center, sol))
						elif j == 2:
							if sol == obs.rect.topleft or sol == obs.rect.bottomleft:
								tempDist.append(self.calculateDist(car.rect.center, sol))
							elif self.isLambda(obs.rect.topleft, obs.rect.bottomleft, sol):
								tempDist.append(self.calculateDist(car.rect.center, sol))
						elif j == 3:
							if sol == obs.rect.bottomright or sol == obs.rect.topright:
								tempDist.append(self.calculateDist(car.rect.center, sol))
							elif self.isLambda(obs.rect.bottomright, obs.rect.topright, sol):
								tempDist.append(self.calculateDist(car.rect.center, sol))
				if len(tempDist) > 0:
					distList.append(min(tempDist))
		return distList

	def isSolutionExists(self, lineA, lineB):
		if (((lineA[0] * lineB[1]) - (lineA[1] * lineB[0])) == 0):
			return False
		else:
			return True

	def pointOfIntersection(self, lineA, lineB):
		x = ((lineA[1] * lineB[2]) - (lineA[2] * lineB[1])) / ((lineA[0] * lineB[1]) - (lineB[0] * lineA[1]))
		y = ((lineA[2] * lineB[0]) - (lineA[0] * lineB[2])) / ((lineA[0] * lineB[1]) - (lineB[0] * lineA[1]))
		return x, y

	def isLambda(self, A, B, sol):
		if sol[0] == B[0]:
			if 0 <= (A[1] - sol[1]) / (sol[1] - B[1]) <= 1:
				return True
			else:
				False
		else:
			if 0 <= (A[0] - sol[0]) / (sol[0] - B[0]) <= 1:
				return True
			else:
				False

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (100,100,100)
goal = (500, 500)
game = carGame()

while game.carryOn:
	game.update()
	connection.Pump()

pygame.quit()
