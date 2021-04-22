import pygame
from PygameWidgets.Widgets.Widget import Widget

class Row(Widget):

    def __init__(this, window, x, y, Widgets):
        super().__init__(window, x, y, window.get_width(), 0, None)
        for widget in Widgets:
            if widget.h > this.h:
                this.h = widget.h
            widget.x += this.x
            widget.y += this.y

        this.Widgets = Widgets

    def draw(this):
        for widget in this.Widgets:
            widget.draw()
