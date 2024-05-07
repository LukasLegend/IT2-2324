from skip import Skip
from laser import Laser
import pygame
import os

RED_SPACE_SHIP = pygame.image.load(os.path.join("bilder", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("bilder", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("bilder", "pixel_ship_blue_small.png"))

RED_LASER = pygame.image.load(os.path.join("bilder", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("bilder", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("bilder", "pixel_laser_blue.png"))

FARGER = {
    "red": (RED_SPACE_SHIP, RED_LASER),
    "green": (GREEN_SPACE_SHIP, GREEN_LASER),
    "blue": (BLUE_SPACE_SHIP, BLUE_LASER)
}


class Fiende(Skip): #Arver fra skip
    def __init__(self, x, y, farge, health):
        super().__init__(x, y, health)
        self.skip_img, self.laser_img = FARGER[farge]
        self.mask = pygame.mask.from_surface(self.skip_img) #Lager mask

    def flytt(self, fart): #Flytter fienden nedover
        self.y += fart

    