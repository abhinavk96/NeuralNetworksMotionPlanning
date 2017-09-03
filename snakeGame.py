# model game to be used to create the actual game

# game imports
import pygame
import sys


checkErrors = pygame.init()
if checkErrors[1] > 0:
    print("(!) Had {0} initializign errors...exiting".format(checkErrors[1]))
    sys.exit(-1)
else:
    print("(+) Game initialized successfully")
