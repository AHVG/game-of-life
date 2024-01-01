import pygame
import random

import constants


class Grid:

    def __init__(self) -> None:
        self.__tiles: list[list[bool]] = [[random.randint(0, 1) for _ in range(constants.NUMBER_OF_SQUARES)] for _ in range(constants.NUMBER_OF_SQUARES)]

    def update(self):
        print("TODO Grid::update")

    def draw_at(self, surface: pygame.Surface) -> None:
        for line in range(constants.NUMBER_OF_SQUARES):
            for column in range(constants.NUMBER_OF_SQUARES):
                pygame.draw.rect(surface,
                                 constants.SQUARE_COLOR_WHEN_ALIVE if self.__tiles[line][column] else constants.SQUARE_COLOR_WHEN_DEAD, 
                                 pygame.Rect(column * constants.SQUARE_HEIGHT, 
                                             line * constants.SQUARE_WIDTH, 
                                             constants.SQUARE_WIDTH, 
                                             constants.SQUARE_HEIGHT))