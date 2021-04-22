import pygame
from PygameWidgets.Widgets.Widget import Widget

class Column(Widget):

    def __init__(this, window, x, y, Widgets):
        super().__init__(window, x, y, 0, window.get_height(), None)
        for widget in Widgets:
            if widget.w > this.w:
                this.w = widget.w
            widget.x += this.x
            widget.y += this.y

        this.Widgets = Widgets

    def draw(this):
        for widget in this.Widgets:
            widget.draw()
