import sys
import pygame


class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE | pygame.DOUBLEBUF, vsync=1)
        self.clock = pygame.time.Clock()

        self.w, self.h = self.screen.get_size()

        self.fonts = dict()

    def update(self):
        pygame.display.flip()
        self.screen.fill((0, 0, 0))

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

    def input(self):
        pass

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.input()

    @property
    def mouse_pos(self):
        return pygame.mouse.get_pos()

    @property
    def mouse(self):
        return pygame.mouse.get_pressed()

    @property
    def mouse_rel(self):
        return pygame.mouse.get_rel()

    @property
    def keys(self):
        return pygame.key.get_pressed()

    @property
    def screen_size(self):
        self.w, self.h = self.screen.get_size()
        return self.w, self.h

    def get_font(self, fontname, size) -> pygame.font.Font:
        if (fontname, size) not in self.fonts.keys():
            self.fonts.update({(fontname, size): pygame.font.Font(fontname, size)})
        return self.fonts.get((fontname, size))
