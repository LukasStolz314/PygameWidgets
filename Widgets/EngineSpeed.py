import pygame
import Utils.Colors as Colors
from .Widget import Widget

class EngineSpeed(Widget):
    
    def __init__(this, window, x, y, w, h, value):
        super().__init__(window, x, y, w, h, None)
        this.value = value
    
    def draw(this):
        for count in range(0, this.value):
            color = Colors.WHITE
            if count > 4 and count <= 9:
                color = Colors.RED
                y = this.y - 5
            elif count > 9 and count <= 14: 
                color = Colors.PURPLE
                y = this.y + (5 * (count % 10))
            elif count <= 4 and count >= 0:
                y = this.y + 25 - (5 * (count + 1))
            else: 
                break

            pygame.draw.circle(this.window, color, (this.x + (100*count), y), 25)
        
        for count in range (this.value, 15):
            if count > 4 and count <= 9:
                y = this.y - 5
            elif count > 9 and count <= 15: 
                y = this.y + (5 * (count % 10))
            elif count <= 4 and count >= 0:
                y = this.y + 25 - (5 * (count + 1))
            else: 
                break
            pygame.draw.circle(this.window, Colors.GREY, (this.x + (100*count), y), 10)