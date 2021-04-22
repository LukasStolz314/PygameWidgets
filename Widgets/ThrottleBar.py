import pygame
from pygame import Rect
from .Widget import Widget

GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

LINE_COUNT = 15
LINE_PADDING = 10

class ThrottleBar(Widget):

    def __init__(this, window, x, y, w, h, backgroundColor, values):
        super().__init__(window, x, y, w, h, backgroundColor)
        this.lineSize = (this.h - LINE_COUNT * LINE_PADDING) / LINE_COUNT
        this.values = values

    def draw(this):
        super().draw()

        # Returns count of green rectangles
        count = ThrottleWidget.getThrottleLineCount(values[0])

        # Draw all green rectangles
        for filledLines in range(count):
            yPosition = this.h - (filledLines * (this.lineSize + LINE_PADDING))
            rect = Rect(this.x, yPosition, this.w, this.lineSize)
            pygame.draw.rect(this.window, GREEN, rect)

        # Draw all empty rectangles
        for notFilledLines in range(count, LINE_COUNT + 1):
            yPosition = this.h - (notFilledLines * (this.lineSize + LINE_PADDING))
            rect = Rect(this.x, yPosition, this.w, this.lineSize)
            pygame.draw.rect(this.window, WHITE, rect)

        return (this.x, this.y, this.w, this.h)
    
    def getThrottleLineCount(value):
        return int(value / 1000)