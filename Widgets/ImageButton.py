import pygame 
import PygameWidgets.Provider as events
from .Button import Button

class ImageButton(Button):

    def __init__(this, window, x, y, w, h, backgroundColor, hoverColor, image, pageSelector = ""):
        super().__init__(window, x, y, w, h, backgroundColor, hoverColor)
        this.image = image
        this.pageSelector = pageSelector
    
    def draw(this):
        super().draw()
        image = pygame.image.load(this.image)
        image = pygame.transform.scale(image, (this.w, this.h))
        this.window.blit(image, (this.x - image.get_width()//2, this.y - image.get_height()//2))

    def checkClick(this):
        mouse_pos = pygame.mouse.get_pos()
        for event in events.mouseClickEvents:
            if mouse_pos[0] >= this.x - this.w//2 and mouse_pos[0] <= this.x + this.w//2:
                if mouse_pos[1] >= this.y - this.h//2 and mouse_pos[1] <= this.y + this.h//2:
                    return this.pageSelector
        
        return ""
