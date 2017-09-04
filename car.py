import pygame
import math

class Car(pygame.sprite.Sprite):
    def __init__(self, img, location):
        super().__init__()
        self.image = pygame.image.load(img)
        self.cleanImage = self.image.copy()
        self.rect = self.image.get_rect()
        self.rect.topleft = location
        self.currentAngle = 0

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def moveForward(self, pixels):
        print(self.currentAngle, math.sin(math.radians(self.currentAngle)), math.cos(math.radians(self.currentAngle)))
        self.rect.x += pixels*math.cos(math.radians(self.currentAngle))
        self.rect.y -= pixels*math.sin(math.radians(self.currentAngle))

    def moveBackward(self, pixels):
        print(self.currentAngle, math.sin(math.radians(self.currentAngle)), math.cos(math.radians(self.currentAngle)))
        self.rect.x -= pixels * math.cos(math.radians(self.currentAngle))
        self.rect.y += pixels * math.sin(math.radians(self.currentAngle))

    def rotateLeft(self, angle):
        print(self.currentAngle, math.sin(self.currentAngle), math.cos(self.currentAngle))
        self.currentAngle += angle
        self.image = pygame.transform.rotate(self.cleanImage, self.currentAngle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def rotateRight(self, angle):
        print(self.currentAngle, math.sin(self.currentAngle), math.cos(self.currentAngle))
        self.currentAngle -= angle
        self.image = pygame.transform.rotate(self.cleanImage, self.currentAngle)
        self.rect = self.image.get_rect(center=self.rect.center)







