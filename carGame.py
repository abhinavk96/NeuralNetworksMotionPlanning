import pygame
import sys
import time
from car import Car
from obstacle import Obstacle

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

# Screen
size = (900,400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Basic Scenery")

# List for all the sprites in the game

all_sprites_list = pygame.sprite.Group()
all_blocks_list = pygame.sprite.Group()


# The player sprite

playerCar = Car("car.png", (100,100))
all_sprites_list.add(playerCar)

# The obstacle sprite
obstacle1 = Obstacle("obstacleType1.png", (200, 200))
obstacle2 = Obstacle("obstacleType1.png", obstacle1.rect.topright)

all_sprites_list.add(obstacle1)
all_blocks_list.add(obstacle1)
all_sprites_list.add(obstacle2)
all_blocks_list.add(obstacle2)

carryOn = True # Game state variable

clock  = pygame.time.Clock()

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                carryOn = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playerCar.rotateLeft(1)

    if keys[pygame.K_RIGHT]:
        playerCar.rotateRight(5)

    if keys[pygame.K_UP]:
        playerCar.moveForward(5)
    collision_list = pygame.sprite.spritecollide(playerCar, all_blocks_list, False)

    for car in collision_list:
        print("Car crash!")
        pygame.event.wait()
        time.sleep(2)
        # End Of Game
        carryOn = False

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