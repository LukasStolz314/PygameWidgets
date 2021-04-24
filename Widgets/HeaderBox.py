import pygame
from .Widget import Widget
from pygame import Rect

GREY = (107, 107, 107)


class HeaderBox(Widget):

    def __init__(this, window, x, y, w, h, backgroundColor, foregroundColor,\
            values, borderThickness = 2, padding = 5, fontSize = 35):
        super().__init__(window, x, y, w, h, backgroundColor)
        this.foregroundColor = foregroundColor
        this.values = values
        this.borderThickness = borderThickness
        this.padding = padding
        this.fontSize = fontSize
        this.font = pygame.font.Font('PygameWidgets/Fonts/ZenDots-Regular.ttf', int(fontSize//1.229))


    def draw(this):
        super().draw()
        
        this.drawHeader(this.values[0])
        this.drawBox()
        this.drawBoxValues(this.values[1], this.values[2])
        return (this.x, this.y, this.w, this.h)

    def drawHeader(this, headerValue):
        # Draw header rect
        x, y, w, h = this.x, this.y, this.w, this.h//3

        headerRect = Rect(x, y, w, h)
        pygame.draw.rect(this.window, GREY, headerRect)
        
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

    
    def drawBoxValues(this, topValues, bottomValues):

        #Draw Top-Left text
        topLeftText = this.font.render(topValues[0], 1, this.foregroundColor)

        x = this.x + this.borderThickness + this.padding
        y = this.y + this.h//3 - this.padding

        fSize = this.fontSize
        while topLeftText.get_width() > (this.w - this.borderThickness*2)/2:
            fSize -= 10
            this.font = pygame.font.SysFont('century gothic', int(fSize//1.229))
            topLeftText = this.font.render(topValues[0], 1, this.foregroundColor)   
            
        this.window.blit(topLeftText, (x, y))
        
        #Draw Bottom-Left text
        bottomLeftText = this.font.render(bottomValues[0], 1, this.foregroundColor)

        x = this.x + this.borderThickness + this.padding
        y = this.y + this.h - bottomLeftText.get_height() + 2 - this.padding

        this.window.blit(bottomLeftText, (x, y))

        #Draw Top-Right text
        topRightText = this.font.render(topValues[1], 1, this.foregroundColor)

        x = this.x + this.w - topRightText.get_width() - this.padding - this.borderThickness
        y = this.y + this.h//3 - this.padding

        this.window.blit(topRightText, (x, y))

        #Draw Bottom-Right text
        bottomRightText = this.font.render(bottomValues[1], 1, this.foregroundColor)

        x = this.x + this.w - bottomRightText.get_width() \
            - this.padding - this.borderThickness
        y = this.y + this.h - bottomLeftText.get_height() + 2 \
            - this.padding - this.borderThickness 

        this.window.blit(bottomRightText, (x, y))