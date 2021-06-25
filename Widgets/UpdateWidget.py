from typing import List
import pygame
from .Widget import Widget

class UpdateWidget(Widget):

    def __init__(this, window, x, y, w, h, backgroundColor, valuePointer, packetreader):
        super().__init__(window, x, y, w, h, backgroundColor)
        this.valuePointer = valuePointer
        this.packetreader = packetreader

    def draw(this):
        this.update()
        super().draw()

    def update(this):
        if isinstance(this.valuePointer, str):
            this.value = vars(this.packetreader)[this.valuePointer]
        else:
            counter = 0
            this.value = [None]*5
            for value in this.valuePointer:
                package = vars(this.packetreader)[value]
                if(isinstance(package, tuple)):
                    for item in package:
                        this.value[counter] = item
                        counter += 1
                else:
                    this.value[counter] = package
                    counter += 1
