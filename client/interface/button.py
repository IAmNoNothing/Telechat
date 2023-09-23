import pygame


class Button:
    def __init__(self, app, text: str, rect: pygame.Rect, **kwargs):
        self.app = app
        self.text = text
        self.rect = rect
        self.font = app.get_font(None, 20)
        self.props = kwargs
        self.text_color = self.props.get('text-color', (255, 255, 255))
        self.rendered_text = self.font.render(self.text, self.text_color, True)
        self.bg_color = self.props.get('bg-color', (255, 0, 0))

    def draw(self):
        pygame.draw.rect(self.app.screen, self.bg_color, self.rect)
        self.app.screen.blit(self.rendered_text, self.rendered_text.get_rect(center=self.rect.center))

    def update(self):
        if self.rect.x <= self.app.mouse_pos[0] <= self.rect.x + self.rect.w:
            if self.rect.y <= self.app.mouse[1] <= self.rect.y + self.rect.h:
                self.text_color = self.props.get('text-color-pointed', (255, 255, 255))
                self.bg_color = self.props.get('bg-color-pointer', (255, 0, 0))
                if self.app.mouse[0]:
                    self.text_color = self.props.get('text-color-click', (255, 255, 255))
                    self.bg_color = self.props.get('bg-color-click', (255, 0, 0))
                return
        self.text_color = self.props.get('text-color', (255, 255, 255))
        self.bg_color = self.props.get('bg-color', (255, 0, 0))
