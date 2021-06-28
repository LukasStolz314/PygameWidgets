from PygameWidgets.Widgets.UpdateWidget import UpdateWidget
import pygame
from .UpdateWidget import UpdateWidget
from pygame import Rect


class ProgressBar(UpdateWidget):

    def __init__(this, window, x, y, w, h, backgroundColor, foregroundColor, valuePointer, packetreader):
        super().__init__(window, x, y, w, h, backgroundColor, valuePointer, packetreader)
        this.foregroundColor = foregroundColor

    def draw(this):
        super().draw()

        # Draw Border
        x, y = this.x - this.w//2, this.y - this.h//2
        w, h = this.w, this.h
        borderRect = Rect(x, y, w, h)
        pygame.draw.rect(this.window, this.foregroundColor, borderRect, 2, 10)

        # Draw Progress
        x, y = this.x - this.w//2, this.y - this.h//2
        w, h = this.w/100 * this.value//40000, this.h
        progressRect = Rect(x, y, w, h)
        pygame.draw.rect(this.window, this.foregroundColor, progressRect, 0, 10)

        return (this.x, this.y, this.w, this.h)
