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

background = pygame.image.load("bg1.png")
# Screen
size = (800,600)
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
obstacles[0] = Obstacle("obstacleType1.png", (300, 200))
all_sprites_list.add(obstacles[0])
all_blocks_list.add(obstacles[0])

for i in range(1, 6):
    obstacles[i] = Obstacle("obstacleType1.png", obstacles[i-1].rect.topright)
    all_sprites_list.add(obstacles[i])
    all_blocks_list.add(obstacles[i])
obstacles[10] = Obstacle("obstacleType1.png", obstacles[5].rect.bottomleft)
all_sprites_list.add(obstacles[10])
all_blocks_list.add(obstacles[10])
for i in range(11, 14):
    obstacles[i] = Obstacle("obstacleType1.png", obstacles[i-1].rect.bottomleft)
    all_sprites_list.add(obstacles[i])
    all_blocks_list.add(obstacles[i])

obstacles[16] = Obstacle("obstacleType1.png", (0,0))
all_sprites_list.add(obstacles[16])
all_blocks_list.add(obstacles[16])
for i in range(17,36):
    obstacles[i] = Obstacle("obstacleType1.png", obstacles[i-1].rect.topright)
    all_sprites_list.add(obstacles[i])
    all_blocks_list.add(obstacles[i])

obstacles[37] = Obstacle("obstacleType1.png", obstacles[16].rect.bottomleft)
all_sprites_list.add(obstacles[37])
all_blocks_list.add(obstacles[37])
for i in range(38, 51):
    obstacles[i] = Obstacle("obstacleType1.png", obstacles[i-1].rect.bottomleft)
    all_sprites_list.add(obstacles[i])
    all_blocks_list.add(obstacles[i])

obstacles[51] = Obstacle("obstacleType1.png", obstacles[50].rect.topright)
all_sprites_list.add(obstacles[51])
all_blocks_list.add(obstacles[51])
for i in range(52,70):
    obstacles[i] = Obstacle("obstacleType1.png", obstacles[i-1].rect.topright)
    all_sprites_list.add(obstacles[i])
    all_blocks_list.add(obstacles[i])

obstacles[70] = Obstacle("obstacleType1.png", obstacles[35].rect.bottomleft)
all_sprites_list.add(obstacles[70])
all_blocks_list.add(obstacles[70])
for i in range(71, 83):
    obstacles[i] = Obstacle("obstacleType1.png", obstacles[i-1].rect.bottomleft)
    all_sprites_list.add(obstacles[i])
    all_blocks_list.add(obstacles[i])
obstacles[84] = Obstacle("obstacleType1.png", (40,400))
all_sprites_list.add(obstacles[84])
all_blocks_list.add(obstacles[84])
for i in range(85, 88):
    obstacles[i] = Obstacle("obstacleType1.png", obstacles[i-1].rect.bottomleft)
    all_sprites_list.add(obstacles[i])
    all_blocks_list.add(obstacles[i])
obstacles[88] = Obstacle("obstacleType1.png", (80,440))
all_sprites_list.add(obstacles[88])
all_blocks_list.add(obstacles[88])
for i in range(89, 91):
    obstacles[i] = Obstacle("obstacleType1.png", obstacles[i-1].rect.bottomleft)
    all_sprites_list.add(obstacles[i])
    all_blocks_list.add(obstacles[i])
obstacles[91] = Obstacle("obstacleType1.png", (120,480))
all_sprites_list.add(obstacles[91])
all_blocks_list.add(obstacles[91])
for i in range(92, 93):
    obstacles[i] = Obstacle("obstacleType1.png", obstacles[i-1].rect.bottomleft)
    all_sprites_list.add(obstacles[i])
    all_blocks_list.add(obstacles[i])
obstacles[93] = Obstacle("obstacleType1.png", (160,520))
all_sprites_list.add(obstacles[93])
all_blocks_list.add(obstacles[93])
obstacles[94] = Obstacle("obstacleType1.png", (720,40))
all_sprites_list.add(obstacles[94])
all_blocks_list.add(obstacles[94])
for i in range(95, 98):
    obstacles[i] = Obstacle("obstacleType1.png", obstacles[i-1].rect.bottomleft)
    all_sprites_list.add(obstacles[i])
    all_blocks_list.add(obstacles[i])
obstacles[98] = Obstacle("obstacleType1.png", (680,40))
all_sprites_list.add(obstacles[98])
all_blocks_list.add(obstacles[98])
for i in range(99, 101):
    obstacles[i] = Obstacle("obstacleType1.png", obstacles[i-1].rect.bottomleft)
    all_sprites_list.add(obstacles[i])
    all_blocks_list.add(obstacles[i])
obstacles[101] = Obstacle("obstacleType1.png", (640,40))
all_sprites_list.add(obstacles[101])
all_blocks_list.add(obstacles[101])
for i in range(102, 103):
    obstacles[i] = Obstacle("obstacleType1.png", obstacles[i-1].rect.bottomleft)
    all_sprites_list.add(obstacles[i])
    all_blocks_list.add(obstacles[i])
obstacles[103] = Obstacle("obstacleType1.png", (600,40))
all_sprites_list.add(obstacles[103])
all_blocks_list.add(obstacles[103])
obstacles[104] = Obstacle("obstacleType1.png", (240,40))
all_sprites_list.add(obstacles[104])
all_blocks_list.add(obstacles[104])
obstacles[105] = Obstacle("obstacleType1.png", (280,40))
all_sprites_list.add(obstacles[105])
all_blocks_list.add(obstacles[105])
obstacles[106] = Obstacle("obstacleType1.png", (240,80))
all_sprites_list.add(obstacles[106])
all_blocks_list.add(obstacles[106])
obstacles[107] = Obstacle("obstacleType1.png", (280,80))
all_sprites_list.add(obstacles[107])
all_blocks_list.add(obstacles[107])
obstacles[108] = Obstacle("obstacleType1.png", (320,400))
all_sprites_list.add(obstacles[108])
all_blocks_list.add(obstacles[108])
obstacles[109] = Obstacle("obstacleType1.png", (280,400))
all_sprites_list.add(obstacles[109])
all_blocks_list.add(obstacles[109])
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

    if keys[pygame.K_DOWN]:
        playerCar.moveBackward(10)
    collision_list = pygame.sprite.spritecollide(playerCar, all_blocks_list, False)
    all_sprites_list.update()
    # Drawing on Screen
    # screen.fill(GREEN)
    screen.blit(background, (0, 0))

    # Draw The Road
    # pygame.draw.rect(screen, BLACK, [40, 0, 200, 300])
    # Draw Line painting on the road
    # pygame.draw.line(screen, WHITE, [140, 0], [140, 300], 5)

    # Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
    all_sprites_list.draw(screen)

    # Refresh Screen
    pygame.display.flip()
    for car in collision_list:
        print("Car crash!")
        pygame.event.wait()
        time.sleep(2)
        # End Of Game
        carryOn = False
    clock.tick(90)
pygame.quit()
