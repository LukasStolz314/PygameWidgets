import pygame

class Page:

    def __init__(this, window, name):
        this.window = window
        this.name = name
        this.widgets = [] 
    
    def addWidget(this, widget):
        this.widgets.append(widget)
    
    def drawWidgets(this):
        windowWidth = this.window.get_width() 
        windowHeigth = this.window.get_height()
        for widget in this.widgets:
            if widget.x + widget.w//2 < windowWidth and widget.y + widget.h//2 < windowHeigth:
                widget.draw()
        pygame.display.update()