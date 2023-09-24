import json
import sys
import pygame

from client.interface.chat_window import ChatWindow
from client.interface.input_field import InputField


class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE | pygame.DOUBLEBUF, vsync=1)
        self.clock = pygame.time.Clock()
        self.w, self.h = self.screen.get_size()
        self.running = True
        self.fonts = dict()
        self.configs = dict()
        self.cfg = self.get_config('main_config')
        self.pressed_keys_uni = set()
        self.pressed_keys = set()
        self.message_input_field = InputField(self, pygame.Rect(0, self.h - 50, self.w, 50))
        self.chat = ChatWindow(self, pygame.Rect(0, 0, self.w, self.h - 50))

    def update(self):
        pygame.display.flip()
        self.screen.fill((0, 0, 0))
        self.message_input_field.update()
        self.chat.draw()
        self.message_input_field.draw()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                self.pressed_keys_uni.add(event.unicode)
                self.pressed_keys.add(event.key)
            elif event.type == pygame.KEYUP:
                self.pressed_keys_uni.discard(event.unicode)
                self.pressed_keys.discard(event.key)
            if event.type == pygame.MOUSEWHEEL:
                self.chat.y -= event.y * self.cfg.get('wheel-speed', 5.0)

    def input(self):
        pass

    def run(self):
        while self.running:
            self.check_events()
            self.update()
            self.input()

    def get_config(self, config) -> dict:
        if config not in self.configs.keys():
            with open(f'./config/{config}.json', 'r') as file:
                self.configs.update({config: json.load(file)})
        return self.configs.get(config, {})

    @property
    def mouse_pos(self) -> tuple[int, int]:
        return pygame.mouse.get_pos()

    @property
    def mouse(self) -> tuple[int, ...]:
        return pygame.mouse.get_pressed()

    @property
    def mouse_rel(self) -> tuple[int, int]:
        return pygame.mouse.get_rel()

    @property
    def keys(self):
        return pygame.key.get_pressed()

    @property
    def screen_size(self) -> tuple[int, int]:
        self.w, self.h = self.screen.get_size()
        return self.w, self.h

    @property
    def events(self):
        return pygame.event.get()

    def get_font(self, fontname, size) -> pygame.font.Font:
        if (fontname, size) not in self.fonts.keys():
            self.fonts.update({(fontname, size): pygame.font.Font(fontname, size)})
        return self.fonts.get((fontname, size))
