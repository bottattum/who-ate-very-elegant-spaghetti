import pygame


class text:
    def __init__(self,game,text,font,size,color,position):
        self.text = text
        self.font = font
        self.size = size
        self.color = color
        self.position = position


    def draw(self):
        self.font = pygame.font.SysFont("Arial",self.size)
        self.image = font.render(self.text, True, color)
        self.screen.blit(self.image,position)

