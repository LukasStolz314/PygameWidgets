import pygame 
from .Widget import Widget

class Button(Widget):

    def __init__(this, window, x, y, w, h, backgroundColor, hoverColor):
        super().__init__(window, x, y, w, h, backgroundColor)
        this.hoverColor = hoverColor

    def draw(this):
        pass

    