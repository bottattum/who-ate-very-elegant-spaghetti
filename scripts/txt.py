import pygame


class textImage():
    def __init__(self,game,font,size,color,position):
        self.game = game
        self.font = font
        self.size = size
        self.color = color
        self.position = position
        self.game.textImgs.append(self)




    def draw(self,text):
        self.text = text
        self.typeface = pygame.font.FontType(\
        "assets/My first font.otf",self.size)
        self.image = self.typeface.render(self.text, True, self.color)
        #blit the image at center of the image
        self.game.screen.blit(self.image,[self.position[0]\
        -self.image.get_width()/2,self.position[1]-self.image.get_height()/2])
        



 #[self.image.get_width(),self.image.get_height()]