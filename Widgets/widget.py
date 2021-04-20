import pygame

class Widget():

    def __init__(this, window, x, y, w, h, backgroundColor):
        this.window = window
        this.x = x
        this.y = y
        this.w = w
        this.h = h
        this.rect = pygame.Rect(x, y, w, h)
        this.backgroundColor = backgroundColor

    def draw(this):
        pygame.draw.rect(this.window, this.backgroundColor, this.rect)