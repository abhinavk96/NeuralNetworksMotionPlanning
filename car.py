import pygame
import math
import goal
import writerUtil
from PodSixNet.Connection import ConnectionListener, connection

class Car(pygame.sprite.Sprite):
    def __init__(self, img, location):
        super().__init__()
        self.image = pygame.image.load(img)
        self.cleanImage = self.image.copy()
        self.rect = self.image.get_rect()
        #self.rect = pygame.draw.rect(pygame.Surface((800, 600)), (255, 0, 0), (location[0], location[1], 10, 10), 0)
        self.rect.topleft = location
        #distance of car sensors from obstacle identified
        self.dist_topleft = 0
        self.dist_topright = 0
        self.dist_bottomleft = 0
        self.dist_bottomright = 0
        self.dist_midleft = 0
        self.dist_midright= 0
        self.dist_midtop = 0
        self.dist_midbottom = 0
        self.line = [None] * 4
        self.line[0] = ((self.rect.topleft[1] - self.rect.bottomright[1]),(self.rect.bottomright[0] - self.rect.topleft[0]),(self.rect.bottomright[1] * (self.rect.topleft[0] - self.rect.bottomright[0])) - (self.rect.bottomright[0] * (self.rect.topleft[1] - self.rect.bottomright[1])))

        self.line[1] = ((self.rect.bottomleft[1] - self.rect.topright[1]),
                      (self.rect.topright[0] - self.rect.bottomleft[0]),
                      self.rect.topright[1] * (self.rect.bottomleft[0] - self.rect.topright[0]) - self.rect.topright[0] * (self.rect.bottomleft[1] - self.rect.topright[1]))

        self.line[2] = ((self.rect.midtop[1] - self.rect.midbottom[1]),
                      (self.rect.midbottom[1] - self.rect.midtop[0]),
                      (self.rect.midbottom[1] * (self.rect.midtop[0] - self.rect.midbottom[0])) - (self.rect.midbottom[0] * (self.rect.midtop[1] - self.rect.midbottom[1])))

        self.line[3] = ((self.rect.midleft[1] - self.rect.midright[1]),
                      (self.rect.midright[0] - self.rect.midleft[0]),
                      self.rect.midright[1] * (self.rect.midleft[0] - self.rect.midright[0]) - self.rect.midright[0] * (self.rect.midleft[1] - self.rect.midright[1]))
        self.currentAngle = 0
        # self.Connect()
        # writerUtil.writerF(self.currentAngle, (500, 500), self.rect.x, self.rect.y, "forward")

    def moveRight(self, pixels):
        self.rect.x += pixels


    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def moveForward(self, pixels, distList, goalpos):
        #print(self.currentAngle, math.sin(math.radians(self.currentAngle)), math.cos(math.radians(self.currentAngle)))
        self.rect.x += pixels*math.cos(math.radians(self.currentAngle))
        self.rect.y -= pixels*math.sin(math.radians(self.currentAngle))
        writerUtil.writerF(self.currentAngle, goalpos, self.rect.x, self.rect.y, distList, "forward")
        #print(self.rect.center)
        #print(self.rect.topright[0] - self.rect.topleft[0])
        #print(self.rect.bottomleft, self.rect.midtop, self.rect.bottomright, self.rect.midleft, self.rect.midtop)

    def moveBackward(self, pixels, distList, goalpos):
        #print(self.currentAngle, math.sin(math.radians(self.currentAngle)), math.cos(math.radians(self.currentAngle)))
        self.rect.x -= pixels * math.cos(math.radians(self.currentAngle))
        self.rect.y += pixels * math.sin(math.radians(self.currentAngle))
        writerUtil.writerF(self.currentAngle, goalpos, self.rect.x, self.rect.y, distList, "backward")
        #print(self.rect.center)

    def rotateLeft(self, angle, distList, goalpos):
        #print(self.currentAngle, math.sin(self.currentAngle), math.cos(self.currentAngle))
        self.currentAngle += angle
        self.image = pygame.transform.rotate(self.cleanImage, self.currentAngle)
        self.rect = self.image.get_rect(center=self.rect.center)
        writerUtil.writerF(self.currentAngle, goalpos, self.rect.x, self.rect.y, distList, "turn_left")

    def rotateRight(self, angle, distList, goalpos):
        # print(self.currentAngle, math.sin(self.currentAngle), math.cos(self.currentAngle))
        self.currentAngle -= angle
        self.image = pygame.transform.rotate(self.cleanImage, self.currentAngle)
        self.rect = self.image.get_rect(center=self.rect.center)
        writerUtil.writerF(self.currentAngle, goalpos, self.rect.x, self.rect.y, distList, "turn_right")