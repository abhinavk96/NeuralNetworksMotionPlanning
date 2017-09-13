import pygame

class Goal(pygame.sprite.Sprite):
    def __init__(self, img, location):
        super().__init__()
        self.image = pygame.image.load(img)
        self.cleanImage = self.image.copy()
        self.rect = self.image.get_rect()
        #self.rect = pygame.draw.rect(pygame.Surface((800, 600)), (255, 0, 0), (location[0], location[1], 10, 10), 0)
        self.rect.topleft = location