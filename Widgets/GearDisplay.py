import pygame
from .Widget import Widget
from pygame import Rect

class GearDisplay(Widget):
    
    def __init__(this, window, x, y, w, h, backgroundColor, foregroundColor,\
        value, padding = 0):
        super().__init__(window, x, y, w, h, backgroundColor)
        this.value = value
        this.foregroundColor = foregroundColor
        this.padding = padding
        this.font = pygame.font.SysFont('arial', int(h*2.222))
        
    def draw(this):
        super().draw()

        # Sets the text for the gear label
        text = ''
        if this.value == 0:
            text = 'N'
        elif this.value == -1:
            text = 'R'
        else:
            text = str(this.value)
        
        # Creates the label
        draw_text = this.font.render(text, 1, this.foregroundColor)

        x = this.x - draw_text.get_width()//2
        y = this.y - draw_text.get_height()//2 + this.padding

        this.window.blit(draw_text, (x, y))

        return (this.x, this.y, draw_text.get_width(), draw_text.get_height())