import pygame
import math
import random
import time
from scripts.obj import object
from scripts.txt import textImage

class game:
    points = 0
    screen = pygame.display.set_mode((800,800))

    #collsionBox
    screenRect = screen.get_rect()

    #object list
    objects = []

    #text image list
    textImgs = []

    running = True
    fps = 60
    clock = pygame.time.Clock()
    dt = clock.tick(fps)/1000
    spawnEvent = pygame.event.custom_type()
    spgTimer = pygame.time.set_timer(spawnEvent,1000)
    spgCount = 0
    lost = False
    pygame.init()
    #make the timer tick according to delta time






    def run(self):
        #convert alpha is essential, without it, the game lags, HARD
        self.plr = object(self,[400,400],pygame.image.load("assets/guy.png").convert_alpha(),65,"plr")
        self.text = textImage(self,"Arial",200,"white",[400,100])
            


        def restart():
            #while there are spaghetti, delete spaghetti
            while self.spgCount != 0:
                self.spgCount -= 1
                del self.objects[1]
            time.sleep(1)
            if self.lost == True:
                self.lost = False



        def spawnSpaghetto():
            if self.lost == False:
                self.position = [random.randrange(0,750),0]
                spg = object(self,self.position,pygame.image.load("assets/spaghetto.png").convert_alpha(),25,"enemy")
                spg.direction["down"] = True
                self.spgCount += 1



        while self.running:

        #inputEvents
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                
                #spawn spaghetti
                if event.type == game.spawnEvent:
                    spawnSpaghetto()

                #restart
                if self.lost == True:
                    restart()


                #plr movement, very clean :D
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.plr.direction["right"] = True
                    if event.key == pygame.K_LEFT:
                        self.plr.direction["left"] = True


                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.plr.direction["right"] = False
                    if event.key == pygame.K_LEFT:
                        self.plr.direction["left"] = False


        #display
            self.screen.fill("pink")

            #lose rect
            self.lose = pygame.Rect(0,700,800,100)


            #for every object in the object list do:
            for obj in self.objects:
                obj.draw()

                if self.lost == False:
                    obj.move()
                    obj.collide()

            #for every text image in the text img list do:
            for txt in self.textImgs:
                txt.draw(str(self.points))



            pygame.display.update()
game().run()