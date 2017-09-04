import pygame
import sys

checkErrors = pygame.init()
if checkErrors[1] > 0:
    print("(!) Had {0} initializign errors...exiting".format(checkErrors[1]))
    sys.exit(-1)
else:
    print("(+) Game initialized successfully")

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (100,100,100)

size = (900,400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Basic Scenery")

carryOn = True

clock  = pygame.time.Clock()

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False

        screen.fill(WHITE)
        pygame.draw.rect(screen, GREEN, [0, 250, 900, 400],0)
        pygame.draw.rect(screen, BROWN, [500,150,40,100], 0)
        pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
        pygame.draw.ellipse(screen, BLACK, [20, 20, 250, 100], 2)
        pygame.display.flip()
        clock.tick(60)
pygame.quit()