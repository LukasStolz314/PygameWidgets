import pygame
from .Widget import Widget
from pygame import Rect

class Label(Widget):
    
    def __init__(this, window, x, y, w, h, backgroundColor, foregroundColor, fontSize = 20):
        super().__init__(window, x, y, w, h, backgroundColor)
        this.foregroundColor = foregroundColor
        this.font = pygame.font.SysFont('century gothic', fontSize)

    def draw(this, value):
        super().draw()

        labelText = this.font.render(value, 1, this.foregroundColor)

        x = this.x - labelText.get_width()//2
        y = this.y - labelText.get_height()//2

        this.window.blit(labelText, (x, y))

        return (this.x, this.y, this.w, this.h)

    def drawWithBackground(this, value, color):
        super().draw()

        # Draw background
        x, y = this.x - this.w//2, this.y - this.h//2
        w, h = this.w, this.h

        headerRect = Rect(x, y, w, h)
        pygame.draw.rect(this.window, color, headerRect)

        # Draw label
        labelText = this.font.render(value, 1, this.foregroundColor)

        x = this.x - labelText.get_width()//2
        y = this.y - headerRect.size[1]//2

        this.window.blit(labelText, (x, y))

        return (this.x, this.y, this.w, this.h)


        