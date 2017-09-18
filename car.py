import pygame
import math

WHITE = (255, 255, 255)


class Car(pygame.sprite.Sprite):
    def __init__(self, img, location):
        super().__init__()
        self.image = pygame.image.load(img).convert()
        self.cleanImage = self.image.copy()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.width = self.rect.width
        self.height = self.rect.height
        self.geometricangle = math.atan(self.width / self.height)
        self.rect.topleft = location
        self.topleft = self.rect.topleft
        self.bottomleft = self.rect.bottomleft
        self.topright = self.rect.topright
        self.cornersensor = math.hypot(self.rect.centerx - self.topright[0], self.rect.centery - self.topright[1])
        self.bottomright = self.rect.bottomright
        self.screen = pygame.display.get_surface()
        self.currentAngle = 0
        self.goal = (600, 100)
        self.previousDistance = math.hypot(self.rect.centerx - self.goal[0], self.rect.centery - self.goal[1])
        self.previousAngle = 0

    def getGoalDistance(self):
        return math.hypot(self.rect.centerx - self.goal[0], self.rect.centery - self.goal[1])

    def updateSensors(self):
        self.bottomright = (
        self.rect.centerx + self.cornersensor * math.sin(math.radians(self.currentAngle) + self.geometricangle),
        self.rect.centery + self.cornersensor * math.cos(math.radians(self.currentAngle) + self.geometricangle))
        self.topright = (self.bottomright[0] - self.height * math.sin(math.radians(self.currentAngle)),
                         self.bottomright[1] - self.height * math.cos(math.radians(self.currentAngle)))
        self.bottomleft = (self.bottomright[0] - self.width * math.cos(math.radians(self.currentAngle)),
                           self.bottomright[1] + self.width * math.sin(math.radians(self.currentAngle)))
        self.topleft = (
        self.rect.centerx - self.cornersensor * math.sin(math.radians(self.currentAngle) + self.geometricangle),
        self.rect.centery - self.cornersensor * math.cos(math.radians(self.currentAngle) + self.geometricangle))
        # self.topmid=((self.topleft[0]+self.topright[0])/2, (self.topleft[1]+self.topright[1])/2)


        # self.bottomleft=(self.rect.centerx - self.cornersensor*math.sin(math.radians(self.currentAngle)+self.geometricangle) ,self.rect.centery+self.cornersensor*math.cos(math.radians(self.currentAngle)+self.geometricangle))
        # print(5)

    def getCurrentReward(self):
        return self.previousDistance - self.getGoalDistance()
    def getAngles(self):
        alpha = math.atan2(self.goal[1] - self.rect.y, self.goal[0]- self.rect.x)
        # print(math.degrees(alpha), self.currentAngle)
        return math.atan2(math.sin(math.radians(self.currentAngle)-alpha), math.cos(math.radians(self.currentAngle)-alpha))


    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def moveForward(self, pixels):
        # print(self.currentAngle, math.sin(math.radians(self.currentAngle)), math.cos(math.radians(self.currentAngle)))
        self.rect.x += pixels * math.cos(math.radians(self.currentAngle))
        self.rect.y -= pixels * math.sin(math.radians(self.currentAngle))
        # print(self.rect.topright)

    def moveBackward(self, pixels):
        # print(self.currentAngle, math.sin(math.radians(self.currentAngle)), math.cos(math.radians(self.currentAngle)))
        self.rect.x -= pixels * math.cos(math.radians(self.currentAngle))
        self.rect.y += pixels * math.sin(math.radians(self.currentAngle))
        # print(self.rect.topright)

    def rotateLeft(self, angle):
        self.currentAngle += angle
        self.currentAngle %= 360
        self.image, self.rect = self.rot_center(self.cleanImage, self.rect, self.currentAngle)

    def rot_center(self, image, rect, angle):
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return rot_image, rot_rect

    def rotateRight(self, angle):
        self.currentAngle -= angle
        self.currentAngle %= 360
        self.image, self.rect = self.rot_center(self.cleanImage, self.rect, self.currentAngle)
