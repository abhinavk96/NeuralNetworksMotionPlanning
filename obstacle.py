import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, img, location):
        super(Obstacle, self).__init__()
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.topleft = location


