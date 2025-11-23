import pygame

class object:
    
    position = ()
    def __init__(self,game,position,image,speed,objType):
        self.game = game
        self.position = position
        self.image = image
        self.direction = {"right":False, "left":False, "up":False, "down":False}
        self.speed = speed
        self.type = objType
        game.objects.append(self)

    def move(self):
        if self.direction["right"] == True:
            self.position[0] += self.speed * self.game.dt
        if self.direction["left"] == True:
            self.position[0] -= self.speed * self.game.dt
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
        if self.type == "enemy":
            if self.rect.colliderect(self.game.plr):
                self.game.points += 1
                print(self.game.points)
                self.game.objects.remove(self)