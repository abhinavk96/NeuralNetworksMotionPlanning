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
size = (1200,800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Basic Scenery")

# List for all the sprites in the game

all_sprites_list = pygame.sprite.Group()
all_blocks_list = pygame.sprite.Group()


# The player sprite

playerCar = Car("car.png", (100,100))
all_sprites_list.add(playerCar)

obstacles = {}
# The obstacle sprite
obstacles[0] = Obstacle("obstacleType1.png", (200, 200))
all_sprites_list.add(obstacles[0])
all_blocks_list.add(obstacles[0])

for i in range(1, 10):
    obstacles[i] = Obstacle("obstacleType1.png", obstacles[i-1].rect.topright)
    all_sprites_list.add(obstacles[i])
    all_blocks_list.add(obstacles[i])
obstacles[10] = Obstacle("obstacleType1.png", obstacles[5].rect.bottomleft)
all_sprites_list.add(obstacles[10])
all_blocks_list.add(obstacles[10])
for i in range(11, 16):
    obstacles[i] = Obstacle("obstacleType1.png", obstacles[i-1].rect.bottomleft)
    all_sprites_list.add(obstacles[i])
    all_blocks_list.add(obstacles[i])
# obstacle5 = Obstacle("obstacleType1.png", obstacle1.rect.bottomleft)
# obstacle6 = Obstacle("obstacleType1.png", obstacle5.rect.topright)
# obstacle7 = Obstacle("obstacleType1.png",obstacle6.rect.topright)
# obstacle8 = Obstacle("obstacleType1.png", obstacle7.rect.topright)


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
        playerCar.rotateLeft(5)

    if keys[pygame.K_RIGHT]:
        playerCar.rotateRight(5)

    if keys[pygame.K_UP]:
        playerCar.moveForward(10)
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