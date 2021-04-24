import pygame
from PygameWidgets.Widgets.Widget import Widget

class Row(Widget):

    def __init__(this, window, x, y, Widgets, maxWidth = None):
        if maxWidth == None:
            maxWidth = window.get_width()
        super().__init__(window, x, y, maxWidth, 0, None)
        for widget in Widgets:
            if widget.h + widget.y > this.h + this.y:
                this.h = widget.h + widget.y
            widget.x += this.x
            widget.y += this.y

        this.Widgets = Widgets

    def draw(this):
        currentWidth = 0
        for widget in this.Widgets:
            currentWidth += widget.w
            if(currentWidth <= this.w):
                widget.draw()

    @property
    def bottomPosition(this):
        return this.y + this.h
