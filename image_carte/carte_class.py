import pygame
from pygame.locals import*
import time


pygame.init()
class carte :
    def __init__(self,zone):
        self.zone=zone
        self.basehero = pygame.image.load("image_carte/hero.png")
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.longueur_ecran = self.screen.get_width()
        self.hauteur_ecran = self.screen.get_height()
        self.fond = pygame.transform.scale(pygame.image.load("image_carte/carte_jeu_jouer_1.png"),(self.longueur_ecran,self.hauteur_ecran))
        self.hero = pygame.transform.scale(self.basehero,(100*self.longueur_ecran/1280,100*self.hauteur_ecran/720))
        self.x_depart = 0
        self.y_depart = 0
        self.x_arrive = 0
        self.y_arrive = 0
    def make_bezier(self,xys):
        # xys pour crée des tupple 
        n = len(xys)
        combinations = self.pascal_row(n-1)
        def bezier(ts):
            k=0
            # formule général
            result = []
            for t in ts:
                tpowers = (t**i for i in range(n))
                upowers = reversed([(1-t)**i for i in range(n)])
                coefs = [c*a*b for c, a, b in zip(combinations, tpowers, upowers)]
                result.append(tuple(sum([coef*p for coef, p in zip(coefs, ps)]) for ps in zip(*xys)))
                k = k + 1
                self.screen.blit(self.fond,(0,0))
                self.screen.blit(self.hero,(result[k-1][0],result[k-1][1]))
                pygame.display.flip()
                time.sleep(0.001)
            return result
        return bezier

    def pascal_row(self,n):
        # This returns the nth row of Pascal's Triangle
        result = [1]
        x, numerator = 1, n
        for denominator in range(1, n//2+1):
            # print(numerator,denominator,x)
            x *= numerator
            x /= denominator
            result.append(x)
            numerator -= 1
        if n&1 == 0:
            # n is even
            result.extend(reversed(result[:-1]))
        else:
            result.extend(reversed(result)) 
        return result
#######################zone1/zone2########################################

        #déplacement de la zone 1 à la zone 2 #
        
    def sprite_zone1_zone2(self):
        self.x_depart = 37
        self.y_depart = 110
        self.x_arrive = 177
        self.y_arrive = 475
        self.screen.blit(self.hero,(self.x_depart,self.y_depart))
        self.zone = 2
        self.ts = [t/100.0 for t in range(101)]
        self.xys = [((self.x_depart*self.longueur_ecran)/1280,(self.y_depart*self.hauteur_ecran)/720), ((82*self.longueur_ecran)/1280,(384*self.hauteur_ecran)/720),((self.x_arrive*self.longueur_ecran)/1280, (self.y_arrive*self.hauteur_ecran)/720)]
        bezier = self.make_bezier(self.xys)
        points = bezier(self.ts)
        #for i in range(self.y_arrive-self.y_depart):
        #    self.screen.blit(self.fond,(0,0))
        #    self.screen.blit(self.hero,(self.x_depart+i*((self.x_arrive-self.x_depart)/(self.y_arrive-self.y_depart)),self.y_depart+i))           
        #    pygame.display.flip()
        #    time.sleep(0.001)
            
        #déplacement de la zone 2 à la zone 1 #
           
    def sprite_zone2_zone1(self):
        self.x_depart = 177
        self.y_depart = 475
        self.x_arrive = 37
        self.y_arrive = 110
        self.screen.blit(self.hero,(self.x_depart*self.longueur_ecran/1280, self.y_depart*self.hauteur_ecran/720))
        self.zone = 1
        self.ts = [t/100.0 for t in range(101)]
        self.xys = [(self.x_depart*self.longueur_ecran/1280, self.y_depart*self.hauteur_ecran/720), (82*self.longueur_ecran/1280,384*self.hauteur_ecran/720),(self.x_arrive*self.longueur_ecran/1280, self.y_arrive*self.hauteur_ecran/720)]
        bezier = self.make_bezier(self.xys)
        points = bezier(self.ts)
        #for i in range(self.y_depart-self.y_arrive):
        #    self.screen.blit(self.fond,(0,0))
        #    self.screen.blit(self.hero,(self.x_depart-i*((self.x_arrive-self.x_depart)/(self.y_arrive-self.y_depart)),self.y_depart-i))         
        #    pygame.display.flip()
        #    time.sleep(0.001)
					
#######################zone2/zone3########################################

	#déplacement de la zone 2 à la zone 3 #

    def sprite_zone2_zone3(self):
        self.x_depart = 177
        self.y_depart = 475
        self.x_arrive = 558
        self.y_arrive = 260
        self.screen.blit(self.hero,(self.x_depart*self.longueur_ecran/1280, self.y_depart*self.hauteur_ecran/720))
        self.zone = 3
        self.ts = [t/100.0 for t in range(101)]
        self.xys = [(self.x_depart*self.longueur_ecran/1280, self.y_depart*self.hauteur_ecran/720), (361*self.longueur_ecran/1280,400*self.hauteur_ecran/720),(484*self.longueur_ecran/1280,250*self.hauteur_ecran/720),(self.x_arrive*self.longueur_ecran/1280, self.y_arrive*self.hauteur_ecran/720)]
        bezier = self.make_bezier(self.xys)
        points = bezier(self.ts)
        #for i in range(self.x_arrive-self.x_depart):
        #    self.screen.blit(self.fond,(0,0))
        #    self.screen.blit(self.hero,(self.x_depart+i,self.y_depart+i*((self.y_arrive-self.y_depart)/(self.x_arrive-self.x_depart))))
        #    pygame.display.flip()
        #    time.sleep(0.001)
            
        #déplacement de la zone 2 à la zone 3 #

    def sprite_zone3_zone2(self):
        self.x_depart = 558
        self.y_depart = 260
        self.x_arrive = 177
        self.y_arrive = 475
        self.screen.blit(self.hero,(self.x_depart*self.longueur_ecran/1280, self.y_depart*self.hauteur_ecran/720))
        self.zone = 2
        self.ts = [t/100.0 for t in range(101)]
        self.xys = [(self.x_depart*self.longueur_ecran/1280, self.y_depart*self.hauteur_ecran/720),(484*self.longueur_ecran/1280,250*self.hauteur_ecran/720),(361*self.longueur_ecran/1280,400*self.hauteur_ecran/720),(self.x_arrive*self.longueur_ecran/1280, self.y_arrive*self.hauteur_ecran/720)]
        bezier = self.make_bezier(self.xys)
        points = bezier(self.ts)
        #for i in range(self.x_depart-self.x_arrive):
        #    self.screen.blit(self.fond,(0,0))
        #    self.screen.blit(self.hero,(self.x_depart-i,self.y_depart-i*((self.y_arrive-self.y_depart)/(self.x_arrive-self.x_depart))))
        #    pygame.display.flip()
        #    time.sleep(0.001)

#######################zone3/zone4########################################

    	#déplacement de la zone 3 à la zone 4 #

    def sprite_zone3_zone4(self):
        self.x_depart = 558
        self.y_depart = 260
        self.x_arrive = 970
        self.y_arrive = 556
        self.screen.blit(self.hero,(self.x_depart*self.longueur_ecran/1280, self.y_depart*self.hauteur_ecran/720))
        self.zone = 4
        self.ts = [t/200.0 for t in range(201)]
        self.xys = [(self.x_depart*self.longueur_ecran/1280, self.y_depart*self.hauteur_ecran/720), (1000*self.longueur_ecran/1280,250*self.hauteur_ecran/720),(650*self.longueur_ecran/1280,600*self.hauteur_ecran/720),(1000*self.longueur_ecran/1280,350*self.hauteur_ecran/720),(self.x_arrive*self.longueur_ecran/1280, self.y_arrive*self.hauteur_ecran/720)]
        bezier = self.make_bezier(self.xys)
        points = bezier(self.ts)
        #for i in range(self.x_arrive-self.x_depart):
        #    self.screen.blit(self.fond,(0,0))
        #    self.screen.blit(self.hero,(self.x_depart+i,self.y_depart+i*((self.y_arrive-self.y_depart)/(self.x_arrive-self.x_depart))))
        #    pygame.display.flip()
        #    time.sleep(0.001)
            
        #déplacement de la zone 4 à la zone 3 #

    def sprite_zone4_zone3(self):
        self.x_depart = 970
        self.y_depart = 556
        self.x_arrive = 558
        self.y_arrive = 260
        self.screen.blit(self.hero,(self.x_depart*self.longueur_ecran/1280, self.y_depart*self.hauteur_ecran/720))
        self.zone = 3
        self.ts = [t/200.0 for t in range(201)]
        self.xys = [(self.x_depart*self.longueur_ecran/1280, self.y_depart*self.hauteur_ecran/720), (940*self.longueur_ecran/1280,200*self.hauteur_ecran/720),(780*self.longueur_ecran/1280,600*self.hauteur_ecran/720),(1000*self.longueur_ecran/1280,350*self.hauteur_ecran/720),(self.x_arrive*self.longueur_ecran/1280, self.y_arrive*self.hauteur_ecran/720)]
        bezier = self.make_bezier(self.xys)
        points = bezier(self.ts)
        #for i in range(self.x_depart-self.x_arrive):
        #    self.screen.blit(self.fond,(0,0))
        #    self.screen.blit(self.hero,(self.x_depart-i,self.y_depart-i*((self.y_arrive-self.y_depart)/(self.x_arrive-self.x_depart))))
        #    pygame.display.flip()
        #    time.sleep(0.001)
        

#######################zone4/zone5########################################

        #déplacement de la zone 4 à la zone 5 #

    def sprite_zone4_zone5(self):
        self.x_depart = 970
        self.y_depart = 556
        self.x_arrive = 1070
        self.y_arrive = 64
        self.screen.blit(self.hero,(self.x_depart*self.longueur_ecran/1280, self.y_depart*self.hauteur_ecran/720))
        self.zone = 5
        self.ts = [t/200.0 for t in range(201)]
        self.xys = [(self.x_depart*self.longueur_ecran/1280, self.y_depart*self.hauteur_ecran/720), (1500*self.longueur_ecran/1280,50*self.hauteur_ecran/720),(1000*self.longueur_ecran/1280,200*self.hauteur_ecran/720),(self.x_arrive*self.longueur_ecran/1280, self.y_arrive*self.hauteur_ecran/720)]
        bezier = self.make_bezier(self.xys)
        points = bezier(self.ts)
        #for i in range(self.y_depart-self.y_arrive):
        #    self.screen.blit(self.fond,(0,0))
        #    self.screen.blit(self.hero,(self.x_depart-i*((self.x_arrive-self.x_depart)/(self.y_arrive-self.y_depart)),self.y_depart-i))           
        #    pygame.display.flip()
        #    time.sleep(0.001)
            
        #déplacement de la zone 5 à la zone 4 #

    def sprite_zone5_zone4(self):
        self.x_depart = 1070
        self.y_depart = 64
        self.x_arrive = 970
        self.y_arrive = 556
        self.screen.blit(self.hero,(self.x_depart*self.longueur_ecran/1280, self.y_depart*self.hauteur_ecran/720))
        self.zone = 4
        self.ts = [t/200.0 for t in range(201)]
        self.xys = [(self.x_depart*self.longueur_ecran/1280, self.y_depart*self.hauteur_ecran/720),(1000*self.longueur_ecran/1280,200*self.hauteur_ecran/720),(1500*self.longueur_ecran/1280,50*self.hauteur_ecran/720),(self.x_arrive*self.longueur_ecran/1280, self.y_arrive*self.hauteur_ecran/720)]
        bezier = self.make_bezier(self.xys)
        points = bezier(self.ts)
        #for i in range(self.y_arrive-self.y_depart):
        #    self.screen.blit(self.fond,(0,0))
        #    self.screen.blit(self.hero,(self.x_depart+i*((self.x_arrive-self.x_depart)/(self.y_arrive-self.y_depart)),self.y_depart+i))         
        #    pygame.display.flip()
        #    time.sleep(0.001)
##########################################################################
