import pygame
from PodSixNet.Connection import ConnectionListener, connection
import sys
import time
import math
from car import Car
from obstacle import Obstacle
from goal import Goal

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
        pygame.display.set_caption("Car Game")
        # List for all the sprites in the game

        self.all_sprites_list = pygame.sprite.Group()
        self.all_blocks_list = pygame.sprite.Group()

        # The player sprite

        self.playerCar = Car("car.png", (100, 100))
        self.all_sprites_list.add(self.playerCar)
        self.goals = Goal("track_goal.png", (720,200))
        self.all_sprites_list.add(self.goals)

        self.obstacles = {}
        # The obstacle sprite
        """self.obstacles[0] = Obstacle("obstacleType1.png", (300, 200))
        self.all_sprites_list.add(self.obstacles[0])
        self.all_blocks_list.add(self.obstacles[0])

        for i in range(1, 6):
            self.obstacles[i] = Obstacle("obstacleType1.png", self.obstacles[i - 1].rect.topright)
            self.all_sprites_list.add(self.obstacles[i])
            self.all_blocks_list.add(self.obstacles[i])
        self.obstacles[10] = Obstacle("obstacleType1.png", self.obstacles[5].rect.bottomleft)
        self.all_sprites_list.add(self.obstacles[10])
        self.all_blocks_list.add(self.obstacles[10])
        for i in range(11, 14):
            self.obstacles[i] = Obstacle("obstacleType1.png", self.obstacles[i - 1].rect.bottomleft)
            self.all_sprites_list.add(self.obstacles[i])
            self.all_blocks_list.add(self.obstacles[i])"""

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
        """self.obstacles[70] = Obstacle("obstacleType1.png", self.obstacles[35].rect.bottomleft)
        self.all_sprites_list.add(self.obstacles[70])
        self.all_blocks_list.add(self.obstacles[70])
        for i in range(71, 83):
            self.obstacles[i] = Obstacle("obstacleType1.png", self.obstacles[i - 1].rect.bottomleft)
            self.all_sprites_list.add(self.obstacles[i])
            self.all_blocks_list.add(self.obstacles[i])
        self.obstacles[84] = Obstacle("obstacleType1.png", (40, 400))
        self.all_sprites_list.add(self.obstacles[84])
        self.all_blocks_list.add(self.obstacles[84])
        for i in range(85, 88):
            self.obstacles[i] = Obstacle("obstacleType1.png", self.obstacles[i - 1].rect.bottomleft)
            self.all_sprites_list.add(self.obstacles[i])
            self.all_blocks_list.add(self.obstacles[i])
        self.obstacles[88] = Obstacle("obstacleType1.png", (80, 440))
        self.all_sprites_list.add(self.obstacles[88])
        self.all_blocks_list.add(self.obstacles[88])
        for i in range(89, 91):
            self.obstacles[i] = Obstacle("obstacleType1.png", self.obstacles[i - 1].rect.bottomleft)
            self.all_sprites_list.add(self.obstacles[i])
            self.all_blocks_list.add(self.obstacles[i])
        self.obstacles[91] = Obstacle("obstacleType1.png", (120, 480))
        self.all_sprites_list.add(self.obstacles[91])
        self.all_blocks_list.add(self.obstacles[91])
        for i in range(92, 93):
            self.obstacles[i] = Obstacle("obstacleType1.png", self.obstacles[i - 1].rect.bottomleft)
            self.all_sprites_list.add(self.obstacles[i])
            self.all_blocks_list.add(self.obstacles[i])
        self.obstacles[93] = Obstacle("obstacleType1.png", (160, 520))
        self.all_sprites_list.add(self.obstacles[93])
        self.all_blocks_list.add(self.obstacles[93])
        self.obstacles[94] = Obstacle("obstacleType1.png", (720, 40))
        self.all_sprites_list.add(self.obstacles[94])
        self.all_blocks_list.add(self.obstacles[94])
        for i in range(95, 98):
            self.obstacles[i] = Obstacle("obstacleType1.png", self.obstacles[i - 1].rect.bottomleft)
            self.all_sprites_list.add(self.obstacles[i])
            self.all_blocks_list.add(self.obstacles[i])
        self.obstacles[98] = Obstacle("obstacleType1.png", (680, 40))
        self.all_sprites_list.add(self.obstacles[98])
        self.all_blocks_list.add(self.obstacles[98])
        for i in range(99, 101):
            self.obstacles[i] = Obstacle("obstacleType1.png", self.obstacles[i - 1].rect.bottomleft)
            self.all_sprites_list.add(self.obstacles[i])
            self.all_blocks_list.add(self.obstacles[i])
        self.obstacles[101] = Obstacle("obstacleType1.png", (640, 40))
        self.all_sprites_list.add(self.obstacles[101])
        self.all_blocks_list.add(self.obstacles[101])
        for i in range(102, 103):
            self.obstacles[i] = Obstacle("obstacleType1.png", self.obstacles[i - 1].rect.bottomleft)
            self.all_sprites_list.add(self.obstacles[i])
            self.all_blocks_list.add(self.obstacles[i])"""
        """self.obstacles[104] = Obstacle("obstacleType1.png", (240, 40))
        self.all_sprites_list.add(self.obstacles[104])
        self.all_blocks_list.add(self.obstacles[104])
        self.obstacles[105] = Obstacle("obstacleType1.png", (280, 40))
        self.all_sprites_list.add(self.obstacles[105])
        self.all_blocks_list.add(self.obstacles[105])
        self.obstacles[106] = Obstacle("obstacleType1.png", (240, 80))
        self.all_sprites_list.add(self.obstacles[106])
        self.all_blocks_list.add(self.obstacles[106])
        self.obstacles[107] = Obstacle("obstacleType1.png", (280, 80))
        self.all_sprites_list.add(self.obstacles[107])
        self.all_blocks_list.add(self.obstacles[107])"""
        self.obstacles[108] = Obstacle("obstacleType1.png", (320, 400))
        self.all_sprites_list.add(self.obstacles[108])
        self.all_blocks_list.add(self.obstacles[108])
        self.obstacles[109] = Obstacle("obstacleType1.png", (280, 400))
        self.all_sprites_list.add(self.obstacles[109])
        self.all_blocks_list.add(self.obstacles[109])

        self.carryOn = True  # Game state variable

        self.clock = pygame.time.Clock()
        self.Connect()

    def update(self):
        connection.Pump()
        self.Pump()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.carryOn = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    self.carryOn = False
        self.playerCar.previousDistance=self.playerCar.getGoalDistance()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.playerCar.rotateLeft(1)
            print(self.playerCar.getCurrentReward())

        if keys[pygame.K_RIGHT]:
            self.playerCar.rotateRight(1)
            print(self.playerCar.getCurrentReward())

        # self.screen.blit(surf,(100,100))

        if keys[pygame.K_UP]:
            self.playerCar.moveForward(10)
            print(self.playerCar.getCurrentReward())


        if keys[pygame.K_DOWN]:
            self.playerCar.moveBackward(1)
            print(self.playerCar.getCurrentReward())

        reward=self.playerCar.getGoalDistance()-self.playerCar.previousDistance

        if keys[pygame.K_p]:
            print("\nTop left: ", self.playerCar.rect.topleft, "\nBottom Left:" ,self.playerCar.rect.bottomleft,"\nBottom Right:" , self.playerCar.rect.bottomright,
                  "\nTop Right:",self.playerCar.rect.topright)
            print("\nAngle:" ,self.playerCar.currentAngle,"\nTop Left:" ,self.playerCar.topleft, "\nBottom Left:" ,self.playerCar.bottomleft,"\nBottom Right:" , self.playerCar.bottomright,
                  "\nTop right:",self.playerCar.topright)
        if keys[pygame.K_g]:
            x, y = self.playerCar.rect.x, self.playerCar.rect.y
            print("Distance:", math.hypot(x - self.playerCar.goal[0], y - self.playerCar.goal[1]))

        self.screen.blit(self.playerCar.image, self.playerCar.rect.topleft)



        self.playerCar.updateSensors()
        self.all_sprites_list.update()
        self.screen.blit(self.background, (0, 0))

        self.all_sprites_list.draw(self.screen)

        # Refresh Screen
        self.clock.tick(90)
        collision_list = pygame.sprite.spritecollide(self.playerCar, self.all_blocks_list, False)
        if len(collision_list) > 0:
            offset_x, offset_y = (self.playerCar.rect.left - collision_list[0].rect.left), (
                self.playerCar.rect.top - collision_list[0].rect.top)
            if (collision_list[0].mask.overlap(self.playerCar.mask, (offset_x, offset_y)) != None):
                print('Collision Detected!')
            else:
                print('None')
        for car in collision_list:
            print("Car crash!")
        # End Of Game
        # self.carryOn = False
        pygame.display.flip()


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (100, 100, 100)

game = carGame()

while game.carryOn:
    game.update()
    connection.Pump()
time.sleep(2)
pygame.quit()
