import pygame
from .Widget import Widget
from pygame import Rect

class ProgressBar(Widget):
    
    def __init__(this, window, x, y, w, h, backgroundColor, foregroundColor):
        super().__init__(window, x, y, w, h, backgroundColor)
        this.foregroundColor = foregroundColor

    def draw(this, value):
        super().draw()

        # Draw Border
        x, y = this.x - this.w//2, this.y - this.h//2
        w, h = this.w, this.h
        borderRect = Rect(x, y, w, h)
        pygame.draw.rect(this.window, this.foregroundColor, borderRect, 2, 3)

        # Draw Progress
        x, y = this.x - this.w//2, this.y - this.h//2
        w, h = this.w/100 * value, this.h
        progressRect = Rect(x, y, w, h)
        pygame.draw.rect(this.window, this.foregroundColor, progressRect, 0, 3)

        return (this.x, this.y, this.w, this.h)