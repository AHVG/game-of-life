import pygame 

import constants
import grid


class App:

    # TODO: Arrumar o desenho do grid (colocar as teclas possiveis para utilizar)
    # TODO: Colocar hover no tile antes de clicar?
    # TODO: Criar uma classe que gerenciará a redenrização?

    def __init__(self) -> None:
        pygame.init()
        
        self.__running: bool = True
        
        self.__grid: grid.Grid = grid.Grid()

        self.__surface: pygame.Surface = pygame.display.set_mode(constants.WINDOW_SIZE) 
        pygame.display.set_caption("Game of Life")
        
        self.__clock = pygame.time.Clock()


    def is_running(self) -> bool:
        return self.__running


    def handle_events(self) -> None:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.__running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.__grid.handle_click()

            elif event.type == pygame.KEYDOWN:
                self.__grid.handle_keydown(event.key)


    def handle_update(self) -> None:
        self.__grid.update()


    def handle_render(self) -> None:
        self.__surface.fill((100, 100, 100))

        self.__grid.draw_at(self.__surface)
        
        pygame.display.flip()


    def run(self) -> None:

        while self.is_running():
            self.handle_events()
            self.handle_update()
            self.handle_render()
            self.__clock.tick(constants.FPS)

        pygame.quit()
