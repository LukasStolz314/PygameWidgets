from PygameWidgets.Widgets.UpdateWidget import UpdateWidget
import pygame
from datetime import *
from .UpdateWidget import UpdateWidget
from pygame import Rect

GREY = (107, 107, 107)


class HeaderBox(UpdateWidget):

    def __init__(this, window, x, y, w, h, backgroundColor, foregroundColor,\
            valuePointer, packetreader, borderThickness = 2, fontSize = 35, isTime = False):
        super().__init__(window, x, y, w, h, backgroundColor, valuePointer, packetreader)
        this.foregroundColor = foregroundColor
        this.borderThickness = borderThickness
        this.fontSize = fontSize
        this.isTime = isTime
        this.font = pygame.font.Font('PygameWidgets/Fonts/ZenDots-Regular.ttf', int(fontSize//1.229))


    def draw(this):
        super().draw()
        
        this.drawHeader(str(this.value[0]))
        this.drawBox()
        this.drawBoxValues(str(this.value[3]), str(this.value[4]), str(this.value[1]), str(this.value[2]))
        return (this.x, this.y, this.w, this.h)

    def drawHeader(this, headerValue):
        # Draw header rect
        x, y, w, h = this.x, this.y, this.w, this.h//3

        headerRect = Rect(x, y, w, h)
        pygame.draw.rect(this.window, GREY, headerRect)

        if(this.isTime):
            date_time = datetime.fromtimestamp(int(headerValue))
            micro = int(date_time.strftime("%f"))//1000
            headerValue = date_time.strftime("%M:%S") + ":" + str(micro)
        
        # Draw text
        headerText = this.font.render(headerValue, 1, this.foregroundColor)

        x = this.x + this.w//2 - headerText.get_width()//2
        y = this.y + this.h//6 - headerText.get_height()//2 - 2

        this.window.blit(headerText, (x, y))


    def drawBox(this):
        # Draw border rect
        x, y, w, h = this.x, this.y + this.h//3, this.w, this.h * (2/3)

        borderRect = Rect(x, y, w, h)
        pygame.draw.rect(this.window, GREY, borderRect)

        #Draw box rect
        x = this.x + this.borderThickness
        y = this.y + this.h//3
        w = this.w - (2*this.borderThickness)
        h = this.h * (2/3) - this.borderThickness

        boxRect = Rect(x, y, w, h)
        pygame.draw.rect(this.window, this.backgroundColor, boxRect)

    
    def drawBoxValues(this, topLeft, topRight, bottomLeft, bottomRight):

        #Draw Top-Left text
        topLeftText = this.font.render(topLeft, 1, this.foregroundColor)
        
        x = this.x + this.borderThickness + 5
        y = this.y + this.h//3 - 5

        fSize = this.fontSize
        while topLeftText.get_width() > (this.w - this.borderThickness*2)/2:
            fSize -= 10
            this.font = pygame.font.SysFont('century gothic', int(fSize//1.229))
            topLeftText = this.font.render(topLeft, 1, this.foregroundColor)   
            
        this.window.blit(topLeftText, (x, y))
        
        #Draw Bottom-Left text
        bottomLeftText = this.font.render(bottomLeft, 1, this.foregroundColor)

        x = this.x + this.borderThickness + 5
        y = this.y + this.h - bottomLeftText.get_height() + 2 - 5

        this.window.blit(bottomLeftText, (x, y))

        #Draw Top-Right text
        topRightText = this.font.render(topRight, 1, this.foregroundColor)

        x = this.x + this.w - topRightText.get_width() - 5 - this.borderThickness
        y = this.y + this.h//3 - 5

        this.window.blit(topRightText, (x, y))

        #Draw Bottom-Right text
        bottomRightText = this.font.render(bottomRight, 1, this.foregroundColor)

        x = this.x + this.w - bottomRightText.get_width() \
            - 5 - this.borderThickness
        y = this.y + this.h - bottomLeftText.get_height() + 2 \
            - 5 - this.borderThickness 

        this.window.blit(bottomRightText, (x, y))