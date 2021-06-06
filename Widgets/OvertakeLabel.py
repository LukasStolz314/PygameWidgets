from PygameWidgets.Widgets.UpdateWidget import UpdateWidget
import pygame
from .Widget import Widget
from pygame import Rect

class OvertakeLabel(UpdateWidget):
    
    def __init__(this, window, x, y, w, h, backgroundColor, foregroundColor, valuePointer, packetreader):
        super().__init__(window, x, y, w, h, backgroundColor, valuePointer, packetreader)
        this.foregroundColor = foregroundColor
        this.font = pygame.font.Font('PygameWidgets/Fonts/ZenDots-Regular.ttf', int(h/1.229))

    def draw(this):
        super().draw()
        
        # Draw background
        x, y = this.x - this.w//2, this.y
        w, h = this.w, this.h

        headerRect = Rect(x, y, w, h)
        if this.value == 2:
            pygame.draw.rect(this.window, this.backgroundColor, headerRect) 
        else:
            pygame.draw.rect(this.window, this.backgroundColor, headerRect, 1) 


        # Draw label
        labelText = this.font.render("Overtake", 1, this.foregroundColor)

        x = this.x - labelText.get_width()//2
        y = this.y

        this.window.blit(labelText, (x, y))