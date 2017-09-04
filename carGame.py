import pygame
import sys
from car import Car
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
playerCar = Car("car.png", (100,100))
# screen.blit(playerCar.image, playerCar.rect)
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(playerCar)
carryOn = True

clock  = pygame.time.Clock()

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type == pygame.KEYDOWN:
            if event.key  == pygame.K_x:
                carryOn=False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playerCar.rotateLeft(1)
    if keys[pygame.K_RIGHT]:
        playerCar.rotateRight(5)
    if keys[pygame.K_UP]:
        playerCar.moveForward(5)

    all_sprites_list.update()
    # Drawing on Screen
    screen.fill(GREEN)
    # Draw The Road
    pygame.draw.rect(screen, BLACK, [40, 0, 200, 300])
    # Draw Line painting on the road
    pygame.draw.line(screen, WHITE, [140, 0], [140, 300], 5)

    # Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
    all_sprites_list.draw(screen)

    # Refresh Screen
    pygame.display.flip()
    clock.tick(60)
pygame.quit()