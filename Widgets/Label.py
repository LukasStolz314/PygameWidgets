from PygameWidgets.Widgets.UpdateWidget import UpdateWidget
import pygame
from .Widget import Widget
from pygame import Rect

class Label(UpdateWidget):
    
    def __init__(this, window, x, y, w, h, backgroundColor, foregroundColor, valuePointer, packetreader):
        super().__init__(window, x, y, w, h, backgroundColor, valuePointer, packetreader)
        this.foregroundColor = foregroundColor
        this.font = pygame.font.Font('PygameWidgets/Fonts/ZenDots-Regular.ttf', int(h/1.229))

    def draw(this):
        super().draw()
        
        labelText = this.font.render(str(this.value), 1, this.foregroundColor)

        x = this.x - labelText.get_width()//2
        y = this.y

        this.window.blit(labelText, (x, y))

        return (this.x, this.y, this.w, this.h)

        