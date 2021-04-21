import pygame
from .Widget import Widget
from pygame import Rect

class GearDisplay(Widget):
    
    def __init__(this, window, x, y, w, h, backgroundColor, foregroundColor,\
        padding = 0, fontSize = 20):
        super().__init__(window, x, y, w, h, backgroundColor)
        this.foregroundColor = foregroundColor
        this.padding = padding
        this.font = pygame.font.SysFont('century gothic', int(fontSize//1.229))

    def draw(this, value):
        super().draw()

        # Sets the text for the gear label
        text = ''
        if value == 0:
            text = 'N'
        elif value == -1:
            text = 'R'
        else:
            text = str(value)
        
        # Creates the label
        draw_text = this.font.render(text, 1, this.foregroundColor)

        x = this.x - draw_text.get_width()//2
        y = this.y - draw_text.get_height()//2 + this.padding

        this.window.blit(draw_text, (x, y))

        return (this.x, this.y, draw_text.get_width(), draw_text.get_height())