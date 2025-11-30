import pygame
import time

class object:
    
    position = ()
    def __init__(self,game,position,image,speed,objType):
        self.game = game
        self.position = position
        self.image = image
        self.direction = {"right":False, "left":False, "up":False, "down":False}
        self.speed = speed
        self.objType = objType
        game.objects.append(self)
    def move(self):
        if self.direction["right"] == True:
            self.position[0] += self.speed * self.game.dt
            if self.game.dash == True and self.game.points >= 5:
                self.position[0] += 150
                self.game.dash = False
                self.game.points -= 5


        if self.direction["left"] == True:
            self.position[0] -= self.speed * self.game.dt
            if self.game.dash == True and self.game.points >= 5:
                self.position[0] -= 150
                self.game.dash = False
                self.game.points -= 5

                
        if self.direction["down"] == True:
            self.position[1] += self.speed * self.game.dt
        if self.direction["up"] == True:
            self.position[1] -= self.speed * self.game.dt
    def draw(self):
        pygame.surface.Surface.blit(self.game.screen,self.image,self.position)
    def collide(self):
        self.rect = pygame.Rect(self.position[0],self.position[1],\
        self.image.get_width(),self.image.get_height())
        pygame.draw.rect(self.game.screen,"red",self.rect,2)
        
        
        if self.objType == "enemy":
            #eat
            if self.rect.colliderect(self.game.plr):
                #add points
                self.game.points += 1
                #remove spaghetto
                self.game.objects.remove(self)
                #subtract spaghetti
                self.game.spgCount -= 1


        #lose
            if self.rect.colliderect(self.game.loseDown):
                self.game.lost = True
        if self.objType == "plr":
            if self.rect.colliderect(self.game.loseRight) or\
                self.rect.colliderect(self.game.loseLeft):
                self.game.lost = True


