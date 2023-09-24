import pygame


class ChatWindow:
    def __init__(self, app, rect: pygame.Rect):
        self.app = app
        self.rect = rect
        self.props = self.app.get_config('chat')

        # format: (id, sender, message, time, is_client_message)
        self.messages = [(2, 'sender', 'message', 'time', False), (1, 'sender', 'message', 'time', True)]
        self.font = self.app.get_font(self.props.get('font-name'), self.props.get('font-size', 20))
        self.y = 0

    def draw(self):
        pygame.draw.rect(self.app.screen, self.props.get('bg-color', (0, 255, 0)), self.rect)

        for _id, sender, message, _time, is_client_message in self.messages:
            sender_text = self.font.render(sender, self.props.get('sender-color', (0, 0, 0)), True)
            message_text = self.font.render(message, self.props.get('message-color', (0, 0, 0)), True)
            time_text = self.font.render(_time, self.props.get('time-color', (0, 0, 0)), True)

            topleft = [self.rect.x + self.props.get('message-l-offset', 10)
                       if not is_client_message else self.app.w - sender_text.get_width() - time_text.get_width() - self.props.get('message-r-offset', 20),
                       -_id * self.props.get('message-space', 30) + self.app.h + self.rect.y + self.y]
            sender_rect = sender_text.get_rect()
            sender_rect.topleft = topleft
            self.app.screen.blit(sender_text, sender_rect)
            self.app.screen.blit(time_text, (topleft[0] + sender_rect.w + self.props.get('sender-time-space', 10), topleft[1]))
            self.app.screen.blit(message_text, (topleft[0], topleft[1] + self.props.get('msg-y-space', 5)))
