import pygame
from .widget import Widget

class GearWidget(Widget):
    
    def __init__(this, window, x, y, w, h, backgroundColor, foregroundColor, fontSize = 20):
        super().__init__(window, x, y, w, h, backgroundColor)
        this.foregroundColor = foregroundColor
        this.fontSize = fontSize

    def draw(this, value):
        super().draw()
        text = ''
        if value == 0:
            text = 'N'
        elif value == -1:
            text = 'R'
        else:
            text = str(value)
        draw_text = pygame.font.SysFont('comicsans', this.fontSize).render(
            text, 1, this.foregroundColor)
        this.window.blit(draw_text, (
            this.x + this.w//2 - draw_text.get_width()//2, this.y + this.h//2 - draw_text.get_height()//2))
        pygame.display.update()