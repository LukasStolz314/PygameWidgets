import pygame
from PygameWidgets.Widgets.Widget import Widget

class Column(Widget):

    def __init__(this, window, x, y, Widgets, maxHeight = None):
        if maxHeight == None:
            maxHeight = window.get_height()
        super().__init__(window, x, y, 0, maxHeight, None)
        for widget in Widgets:
            if widget.w + widget.x > this.w + this.x:
                this.w = widget.w + widget.x
            widget.x += this.x
            widget.y += this.y

        this.Widgets = Widgets

    def draw(this):
        currentHeight = 0
        for widget in this.Widgets:
            currentHeight += widget.h
            if currentHeight <= this.h:
                widget.draw()

    @property
    def bottomPosition(this):
        return this.y + this.h