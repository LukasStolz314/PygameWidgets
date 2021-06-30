import pygame
from pygame import color
import Utils.Colors as Colors
from .UpdateWidget import UpdateWidget

class Tyre(UpdateWidget):
    
    def __init__(this, window, x, y, w, h,fontSize, wheel, valuePointer, packetreader):
        super().__init__(window, x, y, w, h, None, valuePointer, packetreader)
        this.wheel = wheel
        this.fontSize = fontSize
        this.lowerFontSize = this.h * 0.20
        this.font = pygame.font.Font('PygameWidgets/Fonts/ZenDots-Regular.ttf', int(this.fontSize))
        this.lowerFont = pygame.font.Font('PygameWidgets/Fonts/ZenDots-Regular.ttf', int(this.lowerFontSize))


    
    def draw(this):
        super().draw()

        wheelIndex = 0
        if this.wheel == 'RL':
            wheelIndex = 0
        if this.wheel == 'RR':
            wheelIndex = 1
        if this.wheel == 'FL':
            wheelIndex = 2
        if this.wheel == 'FR':
            wheelIndex = 3

        #per = this.value[wheelIndex] # Percentage of the tyre wear
        #innerTemp = this.value[wheelIndex + 1]
        #surfaceTemp = this.value[wheelIndex + 2]

        per = 10 # dummy percentage
        innerTemp = 62
        surfaceTemp = 222


        tyreColor = (round(255 * per/100), round(255 - (255 * per/100)), 0) # Setting the tyre color dynamically for the wear
        lineColor = Colors.WHITE # Color for the lines
        
        circleWidth = this.w # Width of the circle
        lineLength = this.h # Length of the lines
        pygame.draw.circle(this.window, tyreColor, (this.x , this.y), circleWidth) # Draw the tyre

        textOffset = circleWidth + lineLength
        padding = 3
        displayOffset = circleWidth + lineLength * 2

        # If the direction of the lines is right, set the circleWidth and the lineLength to the negative of it
        if this.wheel[1] == 'R':
            circleWidth = -circleWidth
            lineLength = -lineLength
            displayOffset = -displayOffset 
            textOffset = -textOffset - padding

        if this.wheel[1] == 'L':
            displayOffset = displayOffset + this.fontSize * 3.6
            textOffset = textOffset + lineLength

        # Section for the white lines
        pygame.draw.rect(this.window, lineColor, (this.x - (circleWidth + lineLength), this.y, lineLength, 1), 3, 5)
        pygame.draw.rect(this.window, lineColor, (this.x - (circleWidth + lineLength), this.y, 1, lineLength), 3, 5)
        pygame.draw.rect(this.window, lineColor, (this.x - (circleWidth + lineLength), this.y - lineLength, 1, lineLength), 3, 5)
        pygame.draw.rect(this.window, lineColor, (this.x - (circleWidth + lineLength + lineLength), this.y, lineLength, 1), 3, 5)
        pygame.draw.rect(this.window, lineColor, (this.x - (circleWidth + lineLength + lineLength), this.y - lineLength, lineLength, 1), 3, 5)
        pygame.draw.rect(this.window, lineColor, (this.x - (circleWidth + lineLength + lineLength), this.y + lineLength, lineLength, 1), 3, 5)

        # Section for the info-text
        tyresWearText = this.lowerFont.render('WEAR', 1, Colors.WHITE)
        this.window.blit(tyresWearText, (this.x - textOffset + this.h // 8, this.y - this.h - this.lowerFontSize))  
        innerTempText = this.lowerFont.render('INNER', 1, Colors.WHITE)
        this.window.blit(innerTempText, (this.x - textOffset + this.h // 10, this.y - this.lowerFontSize))  
        surfaceTempText = this.lowerFont.render('OUTER', 1, Colors.WHITE)
        this.window.blit(surfaceTempText, (this.x - textOffset, this.y + this.h - this.lowerFontSize))  

        # Section for the tyre wear output
        tyresWearDisplay = this.font.render(str(per) + '%', 1, Colors.WHITE)
        this.window.blit(tyresWearDisplay, (this.x - displayOffset, this.y - this.h - this.fontSize // 2))

        # Section for the tyre inner temperature output
        innerTempDisplay = this.font.render(str(innerTemp) + '°', 1, Colors.WHITE)
        this.window.blit(innerTempDisplay, (this.x - displayOffset, this.y - this.fontSize // 2))

        # Section for the tyre surface temperature output
        surfaceTempDisplay = this.font.render(str(surfaceTemp) + '°', 1, Colors.WHITE)
        this.window.blit(surfaceTempDisplay, (this.x - displayOffset, this.y + this.h - this.fontSize // 2))