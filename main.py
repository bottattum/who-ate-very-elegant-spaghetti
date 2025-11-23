import pygame
import math
import random
from scripts.obj import object
class game:
    points = 0
    screen = pygame.display.set_mode((800,800))
    objects = []
    pygame.init()
    running = True
    fps = 60
    clock = pygame.time.Clock()
    dt = clock.tick(fps)/1000
    timerEvent = pygame.event.custom_type()
    spgTimer = pygame.time.set_timer(timerEvent,1000)
    #make the timer tick according to delta time


    def run(self):
        #convert alpha is essential, without it, the game lags, HARD
        self.plr = object(self,[400,400],pygame.image.load("assets/guy.png").convert_alpha(),65,"plr")
        def spawnSpaghetto():
            self.position = [random.randrange(0,750),0]
            spg = object(self,self.position,pygame.image.load("assets/spaghetto.png").convert_alpha(),25,"enemy")
            spg.direction["down"] = True

        while self.running:
            
        #inputEvents
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                
                if event.type == game.timerEvent:
                    spawnSpaghetto()

                #plr movement, very clean :D
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.plr.direction["right"] = True
                    if event.key == pygame.K_LEFT:
                        self.plr.direction["left"] = True
                    if event.key == pygame.K_z:
                        pass
                    #if event.key == pygame.K_DOWN:
                        #plr.direction["down"] = True
                    #if event.key == pygame.K_UP:
                        #plr.direction["up"] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.plr.direction["right"] = False
                    if event.key == pygame.K_LEFT:
                        self.plr.direction["left"] = False
                    #if event.key == pygame.K_DOWN:
                        #plr.direction["down"] = False
                    #if event.key == pygame.K_UP:
                        #plr.direction["up"] = False

        #display
            self.screen.fill("pink")
            #render objects
            #for every object in the object list do:
            for obj in self.objects:
                obj.draw()
                obj.move()
                obj.collide()
            pygame.display.update()
game().run()