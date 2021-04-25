import pygame

class Page:

    def __init__(this, window, name, widgetList):
        this.window = window
        this.name = name
        this.widgetList = widgetList
    
    def addWidget(this, widget):
        this.widgetList.append(widget)
    
    def drawWidgets(this):
        windowWidth = this.window.get_width() 
        windowHeigth = this.window.get_height()
        for widget in this.widgetList:
            if widget.x + widget.w//2 < windowWidth and widget.y + widget.h//2 < windowHeigth:
                widget.draw()
        pygame.display.update()