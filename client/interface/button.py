import pygame


class Button:
    def __init__(self, app, text: str, rect: pygame.Rect, target: callable, **kwargs):
        self.app = app
        self.text = text
        self.rect = rect
        self.props = kwargs
        self.func = target
        self.font = app.get_font(self.props.get('font-name', None), self.props.get('font-size', 20))
        self.text_color = self.props.get('text-color', (255, 255, 255))
        self.rendered_text = self.font.render(self.text, self.text_color, True)
        self.bg_color = self.props.get('bg-color', (255, 0, 0))
        self.can_execute = False

    def draw(self):
        pygame.draw.rect(self.app.screen, self.bg_color, self.rect)
        self.app.screen.blit(self.rendered_text, self.rendered_text.get_rect(center=self.rect.center))

    def update(self):
        if self.rect.x <= self.app.mouse_pos[0] <= self.rect.x + self.rect.w:
            if self.rect.y <= self.app.mouse_pos[1] <= self.rect.y + self.rect.h:
                self.bg_color = self.props.get('bg-color-pointed', (255, 100, 0))
                if self.app.mouse[0]:
                    self.bg_color = self.props.get('bg-color-click', (255, 200, 0))
                    self.func(*self.props.get('func_args', tuple()))
                return
        self.bg_color = self.props.get('bg-color', (255, 0, 0))

    def update_color(self):
        if self.rect.x <= self.app.mouse_pos[0] <= self.rect.x + self.rect.w:
            if self.rect.y <= self.app.mouse_pos[1] <= self.rect.y + self.rect.h:
                self.bg_color = self.props.get('bg-color-pointed', (255, 100, 0))
                if self.app.mouse[0]:
                    self.bg_color = self.props.get('bg-color-click', (255, 200, 0))
                return
        self.bg_color = self.props.get('bg-color', (255, 0, 0))