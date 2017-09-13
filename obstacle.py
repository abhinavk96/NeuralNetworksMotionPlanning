import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, img, location):
        super().__init__()
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.topleft = location
        self.line = [None] * 4
        self.line[0] = ((self.rect.topleft[1] - self.rect.topright[1]),
                      (self.rect.topright[0] - self.rect.topleft[0]),
                      self.rect.topright[1] * (self.rect.topleft[0] - self.rect.topright[0]) - self.rect.topright[0] *(self.rect.topleft[1] - self.rect.topright[1]))

        self.line[1] = ((self.rect.bottomleft[1] - self.rect.bottomright[1]),
                      (self.rect.bottomright[0] - self.rect.bottomleft[0]),
                      self.rect.bottomright[1] * (self.rect.bottomleft[0] - self.rect.bottomright[0]) - self.rect.bottomright[0] * (self.rect.bottomleft[1] - self.rect.bottomright[1]))

        self.line[2] = ((self.rect.topleft[1] - self.rect.bottomleft[1]),
                      (self.rect.bottomleft[0] - self.rect.topleft[0]),
                      (self.rect.bottomleft[1] * (self.rect.topleft[0] - self.rect.bottomleft[0])) - (self.rect.bottomleft[0] * (self.rect.topleft[1] - self.rect.bottomleft[1])))

        self.line[3] = ((self.rect.topright[1] - self.rect.bottomright[1]), (self.rect.bottomright[0] - self.rect.topright[0]), self.rect.bottomright[1] * (self.rect.topright[0] - self.rect.bottomright[0]) - self.rect.bottomright[0] * (self.rect.topright[1] - self.rect.bottomright[1]))



