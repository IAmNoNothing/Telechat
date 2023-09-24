import pygame

from client.engine.timer import Timer


class InputField:
    def __init__(self, app, rect: pygame.Rect, **kwargs):
        self.app = app
        self.props = kwargs
        self.cfg = self.app.get_config('input_field')
        self.rect = rect

        self._text = ''
        self.text_surf = pygame.Surface((0, 0))
        self.font = self.app.get_font(self.props.get('font-name', None), self.cfg.get('font-size', 20))

        self.active = False
        self.timer = Timer(self.timer_target, self.cfg.get('print-cooldown', 0.1), cyclic=True, exec_first=True)
        self.timer.activate()

    def draw(self):
        if self.active:
            pygame.draw.rect(self.app.screen, self.cfg.get('bg-color-active', (255, 255, 0)), self.rect)
        else:
            pygame.draw.rect(self.app.screen, self.cfg.get('bg-color', (255, 0, 0)), self.rect)
        self.app.screen.blit(self.text_surf, self.text_surf.get_rect(center=self.rect.center))

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
        self.text_surf = self.font.render(self._text, (255, 255, 0), self.cfg.get('anti-ali', True))

    def clear(self):
        self.text = ''

    def clear_some(self, num):
        self.text = self._text[:-num]

    def update(self):
        if self.app.mouse[0]:
            if self.rect.x <= self.app.mouse_pos[0] <= self.rect.x + self.rect.w:
                if self.rect.y <= self.app.mouse_pos[1] <= self.rect.y + self.rect.h:
                    self.active = True
                else:
                    self.active = False
            else:
                self.active = False
        self.timer.update()

    def timer_target(self):
        if self.active:
            if self.cfg.get('max-message-length', 100) > len(self.text):
                for i in self.app.pressed_keys_uni:
                    if i != '\x08':
                        self.text += i
                    else:
                        self.clear_some(1)
