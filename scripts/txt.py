import pygame


class textImage():
    def __init__(self,game,text,size,color,position):
        self.game = game
        self.text = text
        self.size = size
        self.color = color
        self.position = position
        self.font = pygame.font.SysFont(None,self.size)
        self.render = self.font.render(self.text,False,self.color).convert_alpha()

    def draw(self):
        self.game.screen.blit(self.render,[self.position[0]\
        -self.render.get_width()/2,self.position[1]-self.render.get_height()/2])

        
