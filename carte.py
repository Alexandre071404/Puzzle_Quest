import pygame
from pygame.locals import*
import time
import sys
sys.path.insert(0, "image_carte")
from carte_class import*
sys.path.insert(0, "boules")
from boules import*
from stats import*
from jeux import*
from sauvegarde import sauvegarderobj
sys.path.insert(0, "menu")

############################################################INITIALISATION########################################################################################################################################

def carte_monde(perso):
    #initialisation de la carte#
    map_monde = carte(1) # je crée la carte 
    screen = map_monde.screen # je change l'écran pour qu'il corresponde a l'écran de ma carte
    longueur_ecran = screen.get_width() #je prend la longueur et le largeur de l'écran
    hauteur_ecran = screen.get_height()

    #je crée des images que je met dans des variable grace a une boucle
    tab=[1,2,3,4,5]
    for i in tab:
        globals()["monde"+str(i)+"_jouer"] = pygame.transform.scale(pygame.image.load("image_carte/carte_jeu_jouer_"+str(i)+".png"),(longueur_ecran,hauteur_ecran))
    for i in tab:
        globals()["monde"+str(i)] = pygame.transform.scale(pygame.image.load("image_carte/carte_jeu_jouer_"+str(i)+".png"),(longueur_ecran,hauteur_ecran))

    #change le fond
    fond = pygame.image.load("image_carte/carte_jeu_jouer_1.png")
    map_monde.screen.blit(map_monde.fond,(0,0))
    map_monde.screen.blit(map_monde.hero,(37*map_monde.longueur_ecran/1280,110*map_monde.hauteur_ecran/720))
    pygame.display.flip()

    #permet de savoir le niveau max 
    personnage = perso
    niveau_max = personnage.carte_max
    
    #initialisation des zones clickable en utilisant la même méthode que précédament avec des tuples 
    tab_xy = [(489*map_monde.longueur_ecran/1280,637*map_monde.hauteur_ecran/720),(757*map_monde.longueur_ecran/1280,631*map_monde.hauteur_ecran/720),(53*map_monde.longueur_ecran/1280,111*map_monde.hauteur_ecran/720),(194*map_monde.longueur_ecran/1280,473*map_monde.hauteur_ecran/720),(575*map_monde.longueur_ecran/1280,259*map_monde.hauteur_ecran/720),(991*map_monde.longueur_ecran/1280,557*map_monde.hauteur_ecran/720),(1086*map_monde.longueur_ecran/1280,62*map_monde.hauteur_ecran/720)]
    tab_taille = [(264*map_monde.longueur_ecran/1280,59*map_monde.hauteur_ecran/720),(40*map_monde.longueur_ecran/1280,40*map_monde.hauteur_ecran/720),(150*map_monde.longueur_ecran/1280,150*map_monde.hauteur_ecran/720),(150*map_monde.longueur_ecran/1280,150*map_monde.hauteur_ecran/720),(150*map_monde.longueur_ecran/1280,150*map_monde.hauteur_ecran/720),(150*map_monde.longueur_ecran/1280,150*map_monde.hauteur_ecran/720),(150*map_monde.longueur_ecran/1280,150*map_monde.hauteur_ecran/720)]
    for i in range(len(tab_xy)):
        globals()["zone_clickable_"+str(i)]= pygame.Rect((tab_xy[i][0],tab_xy[i][1]),(tab_taille[i][0],tab_taille[i][1]))

    #initialisation des listes pour la boucle
    tab_ratio = [(37*map_monde.longueur_ecran/1280,110*map_monde.hauteur_ecran/720),(177*map_monde.longueur_ecran/1280,475*map_monde.hauteur_ecran/720),(558*map_monde.longueur_ecran/1280,260*map_monde.hauteur_ecran/720),(970*map_monde.longueur_ecran/1280,556*map_monde.hauteur_ecran/720),(1070*map_monde.longueur_ecran/1280,64*map_monde.hauteur_ecran/720)] #zone_clickable_0

    font = pygame.font.Font("font/verdana.ttf", 15)#ajout de la police d'écriture
    
####################################################################################################################################################################################################

####################################################LANCEMENT DU JEU################################################################################################################################################

    continuer = True
    while continuer:
        #Affichage Expérience
        pygame.draw.rect(screen,pygame.Color(100, 50, 0),((longueur_ecran/6.05,longueur_ecran/16.2),((0.3030*longueur_ecran),24)))
        pygame.draw.rect(screen,pygame.Color(0, 0, 0),((longueur_ecran/6,longueur_ecran/16),((0.3*longueur_ecran),20)))
        pygame.draw.rect(screen,pygame.Color(5, 205, 30),((longueur_ecran/6,longueur_ecran/16),((0.3*longueur_ecran)*(personnage.experience/personnage.experienceMax),20)))
        afficher = font.render(str(personnage.experience)+"/"+str(personnage.experienceMax), 1, (255, 255, 255))
        screen.blit(afficher,(longueur_ecran/6,longueur_ecran/16))
        pygame.draw.rect(screen,pygame.Color(100, 50, 0),((longueur_ecran/6.05,longueur_ecran/20.2),((0.048*longueur_ecran),24)))
        afficher = font.render("Level "+str(personnage.niveau), 1, (255, 255, 255))
        screen.blit(afficher,(longueur_ecran/6,longueur_ecran/20))
        pygame.display.update()
        #fin de l'affichage
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if zone_clickable_0.collidepoint(event.pos) or pygame.Rect((752*map_monde.longueur_ecran/1280,672*map_monde.hauteur_ecran/720),(40*map_monde.longueur_ecran/1280,24*map_monde.hauteur_ecran/720)).collidepoint(event.pos): #permet le click sur le bouton jouer 

                        #permet la création des statistiques de l'enemie avec un ration par rapport au niveau ou l'on est 
                        ratio = 1+0.40*(map_monde.zone-2)
                        jeu(personnage,enemie(100*ratio,100*ratio,15*ratio,10*ratio,10*ratio,7.5*ratio),consmatrice(8,8),map_monde.zone)

                        #permet l'affichage de la carte apres avoir fait un niveau
                        niveau_max = personnage.carte_max
                        map_monde.fond = globals()["monde"+str(map_monde.zone)+"_jouer"]
                        map_monde.screen.blit(map_monde.fond,(0,0))
                        map_monde.screen.blit(map_monde.hero,(tab_ratio[map_monde.zone-1][0],tab_ratio[map_monde.zone-1][1]))
                        sauvegarderobj(personnage)
                        continuer = True
                        pygame.display.update()

                        
                       # if map_monde.zone == 1:
                       #     jeu(personnage,enemie(100*ratio,100*ratio,15*ratio,10*ratio,10*ratio,7.5*ratio),consmatrice(8,8),map_monde.zone)
                       #     niveau_max = personnage.carte_max
                       #     map_monde.fond = monde1_jouer
                      #      map_monde.screen.blit(map_monde.fond,(0,0))
                     #       map_monde.screen.blit(map_monde.hero,(37*map_monde.longueur_ecran/1280,110*map_monde.hauteur_ecran/720))
                     #   if map_monde.zone == 2:
                      #      jeu(personnage,enemie(100*ratio,100*ratio,15*ratio,10*ratio,10*ratio,7.5*ratio),consmatrice(8,8),map_monde.zone)
                     #       niveau_max = personnage.carte_max
                     #       map_monde.fond = monde2_jouer
                     #       map_monde.screen.blit(map_monde.fond,(0,0))
                     #       map_monde.screen.blit(map_monde.hero,(177*map_monde.longueur_ecran/1280,475*map_monde.hauteur_ecran/720))
                     #   if map_monde.zone == 3:
                     #       jeu(personnage,enemie(100*ratio,100*ratio,15*ratio,10*ratio,10*ratio,7.5*ratio),consmatrice(8,8),map_monde.zone)
                    #        niveau_max = personnage.carte_max
                     #       map_monde.fond = monde3_jouer
                      #      map_monde.screen.blit(map_monde.fond,(0,0))
                      #      map_monde.screen.blit(map_monde.hero,(558*map_monde.longueur_ecran/1280,260*map_monde.hauteur_ecran/720))
                      #  if map_monde.zone == 4:
                     #       jeu(personnage,enemie(100*ratio,100*ratio,15*ratio,10*ratio,10*ratio,7.5*ratio),consmatrice(8,8),map_monde.zone)
                      #      niveau_max = personnage.carte_max
                      #      map_monde.fond = monde4_jouer
                       #     map_monde.screen.blit(map_monde.fond,(0,0))
                       #     map_monde.screen.blit(map_monde.hero,(970*map_monde.longueur_ecran/1280,556*map_monde.hauteur_ecran/720))
                      #  if map_monde.zone == 5:
                      #      jeu(personnage,enemie(100*ratio,100*ratio,15*ratio,10*ratio,10*ratio,7.5*ratio),consmatrice(8,8),map_monde.zone)
                       #     niveau_max = personnage.carte_max
                      #      map_monde.fond = monde5_jouer
                      #      map_monde.screen.blit(map_monde.fond,(0,0))
                       #     map_monde.screen.blit(map_monde.hero,(1070*map_monde.longueur_ecran/1280,64*map_monde.hauteur_ecran/720))

####################################################################################################################################################################################################

###########################################DEPLACEMENT SUR LA CARTE#########################################################################################################################################################

            #permet d'aller a la zone 1#
                if event.button == 1:
                    if zone_clickable_2.collidepoint(event.pos) :
                        zone_depart = map_monde.zone
                        zone_depart_temp = zone_depart
                        zone_arrive = 1
                        if zone_depart > zone_arrive :
                            while zone_depart_temp != zone_arrive:
                                trajet = "map_monde.sprite_zone"+str(zone_depart_temp)+"_zone"+str(zone_depart_temp-1)+"()"
                                exec(trajet)
                                zone_depart_temp = zone_depart_temp-1
                        map_monde.fond = monde1_jouer
                        map_monde.screen.blit(map_monde.fond,(0,0))
                        map_monde.screen.blit(map_monde.hero,(tab_ratio[map_monde.zone-1][0],tab_ratio[map_monde.zone-1][1]))
                        pygame.event.clear()
                        pygame.display.flip()

            #permet d'aller a la zone 2#
                if event.button == 1:
                    if zone_clickable_3.collidepoint(event.pos) and niveau_max >= 2:
                        zone_depart = map_monde.zone
                        zone_depart_temp = zone_depart
                        zone_arrive = 2
                        if zone_depart > zone_arrive :
                            while zone_depart_temp != zone_arrive:
                                trajet = "map_monde.sprite_zone"+str(zone_depart_temp)+"_zone"+str(zone_depart_temp-1)+"()"
                                exec(trajet)
                                zone_depart_temp = zone_depart_temp-1
                        if zone_depart < zone_arrive :
                            while zone_depart_temp != zone_arrive:
                                trajet = "map_monde.sprite_zone"+str(zone_depart_temp)+"_zone"+str(zone_depart_temp+1)+"()"
                                exec(trajet)
                                zone_depart_temp = zone_depart_temp+1
                        map_monde.fond = monde2_jouer
                        map_monde.screen.blit(map_monde.fond,(0,0))
                        map_monde.screen.blit(map_monde.hero,(tab_ratio[map_monde.zone-1][0],tab_ratio[map_monde.zone-1][1]))
                        pygame.event.clear()
                        pygame.display.flip()

            #permet d'aller a la zone 3#
                if event.button == 1:
                    if zone_clickable_4.collidepoint(event.pos) and niveau_max >= 3:
                        zone_depart = map_monde.zone
                        zone_depart_temp = zone_depart
                        zone_arrive = 3
                        if zone_depart > zone_arrive :
                            while zone_depart_temp != zone_arrive:
                                trajet = "map_monde.sprite_zone"+str(zone_depart_temp)+"_zone"+str(zone_depart_temp-1)+"()"
                                exec(trajet)
                                zone_depart_temp = zone_depart_temp-1
                        if zone_depart < zone_arrive :
                            while zone_depart_temp != zone_arrive:
                                trajet = "map_monde.sprite_zone"+str(zone_depart_temp)+"_zone"+str(zone_depart_temp+1)+"()"
                                exec(trajet)
                                zone_depart_temp = zone_depart_temp+1
                        map_monde.fond = monde3_jouer
                        map_monde.screen.blit(map_monde.fond,(0,0))
                        map_monde.screen.blit(map_monde.hero,(tab_ratio[map_monde.zone-1][0],tab_ratio[map_monde.zone-1][1]))
                        pygame.event.clear()
                        pygame.display.flip()

            #permet d'aller a la zone 4#
                if event.button == 1:
                    if zone_clickable_5.collidepoint(event.pos) and niveau_max >= 4:
                        zone_depart = map_monde.zone
                        zone_depart_temp = zone_depart
                        zone_arrive = 4
                        if zone_depart > zone_arrive :
                            while zone_depart_temp != zone_arrive:
                                trajet = "map_monde.sprite_zone"+str(zone_depart_temp)+"_zone"+str(zone_depart_temp-1)+"()"
                                exec(trajet)
                                zone_depart_temp = zone_depart_temp-1
                        if zone_depart < zone_arrive :
                            while zone_depart_temp != zone_arrive:
                                trajet = "map_monde.sprite_zone"+str(zone_depart_temp)+"_zone"+str(zone_depart_temp+1)+"()"
                                exec(trajet)
                                zone_depart_temp = zone_depart_temp+1
                        map_monde.fond = monde4_jouer
                        map_monde.screen.blit(map_monde.fond,(0,0))
                        map_monde.screen.blit(map_monde.hero,(tab_ratio[map_monde.zone-1][0],tab_ratio[map_monde.zone-1][1]))
                        pygame.event.clear()
                        pygame.display.flip()

            #permet d'aller a la zone 5#
                if event.button == 1:
                    if zone_clickable_6.collidepoint(event.pos) and niveau_max >= 5:
                        zone_depart = map_monde.zone
                        zone_depart_temp = zone_depart
                        zone_arrive = 5
                        if zone_depart > zone_arrive :
                            while zone_depart_temp != zone_arrive:
                                trajet = "map_monde.sprite_zone"+str(zone_depart_temp)+"_zone"+str(zone_depart_temp-1)+"()"
                                exec(trajet)
                                zone_depart_temp = zone_depart_temp-1
                        if zone_depart < zone_arrive :
                            while zone_depart_temp != zone_arrive:
                                trajet = "map_monde.sprite_zone"+str(zone_depart_temp)+"_zone"+str(zone_depart_temp+1)+"()"
                                exec(trajet)
                                zone_depart_temp = zone_depart_temp+1
                        map_monde.fond = monde5_jouer
                        map_monde.screen.blit(map_monde.fond,(0,0))
                        map_monde.screen.blit(map_monde.hero,(tab_ratio[map_monde.zone-1][0],tab_ratio[map_monde.zone-1][1]))
                        pygame.event.clear()
                        pygame.display.flip()
							





               # if event.button == 1:
               #     if zone_clickable_2.collidepoint(event.pos):
               #         #-2-#
               #         if map_monde.zone == 2:
               #             map_monde.zone = 1
               #             map_monde.fond = monde2
               #             map_monde.sprite_zone2_zone1()
               #             map_monde.fond = monde1_jouer
               #             map_monde.screen.blit(map_monde.fond,(0,0))
               #             map_monde.screen.blit(map_monde.hero,(37*map_monde.longueur_ecran/1280,110*map_monde.hauteur_ecran/720))
               #             pygame.event.clear()
               #             pygame.display.flip()
               #             level = 1
               #         #-3-#
               #         if map_monde.zone == 3:
               #             map_monde.zone = 1
               #             map_monde.fond = monde3
               #             map_monde.sprite_zone3_zone2()
               #             map_monde.sprite_zone2_zone1()
               #             map_monde.fond = monde1_jouer
               #             map_monde.screen.blit(map_monde.fond,(0,0))
               #             map_monde.screen.blit(map_monde.hero,(37*map_monde.longueur_ecran/1280,110*map_monde.hauteur_ecran/720))
               #             pygame.event.clear()
               #             pygame.display.flip()
               #             level = 1
               #
               #         #-4-#
               #         if map_monde.zone == 4:
               #             map_monde.zone = 1
               #             map_monde.fond = monde4
               #             map_monde.sprite_zone4_zone3()
               #             map_monde.sprite_zone3_zone2()
               #             map_monde.sprite_zone2_zone1()
               #             map_monde.fond = monde1_jouer
               #             map_monde.screen.blit(map_monde.fond,(0,0))
               #             map_monde.screen.blit(map_monde.hero,(37*map_monde.longueur_ecran/1280,110*map_monde.hauteur_ecran/720))
               #             pygame.event.clear()
               #             pygame.display.flip()
               #             level = 1
               #
               # 
               #
               #             #-5-#
               #         if map_monde.zone == 5:
               #             map_monde.zone = 1
               #             map_monde.fond = monde5
               #             map_monde.sprite_zone5_zone4()
               #             map_monde.sprite_zone4_zone3()
               #             map_monde.sprite_zone3_zone2()
               #             map_monde.sprite_zone2_zone1()
               #             map_monde.fond = monde1_jouer
               #             map_monde.screen.blit(map_monde.fond,(0,0))
               #             map_monde.screen.blit(map_monde.hero,(37*map_monde.longueur_ecran/1280,110*map_monde.hauteur_ecran/720))
               #             pygame.event.clear()
               #             pygame.display.flip()
               #             level = 1 


            #GO ZONE2#
               #     if event.button == 1:
               #         if zone_clickable_3.collidepoint(event.pos):
               #             #-1-#
               #             if map_monde.zone == 1 and niveau_max >= 2:
               #                 map_monde.zone = 2
               #                 map_monde.fond = monde1
               #                 map_monde.sprite_zone1_zone2()
               #                 map_monde.fond = monde2_jouer
               #                 map_monde.screen.blit(map_monde.fond,(0,0))
               #                 map_monde.screen.blit(map_monde.hero,(177*map_monde.longueur_ecran/1280,475*map_monde.hauteur_ecran/720))
               #                 pygame.event.clear()
               #                 pygame.display.flip()
               #                 level = 2


               #              #-3-#
               #             if map_monde.zone == 3:
               #                 map_monde.zone = 2
               #                 map_monde.fond = monde3
               #                 map_monde.sprite_zone3_zone2()
               #                 map_monde.fond = monde2_jouer
               #                 map_monde.screen.blit(map_monde.fond,(0,0))
               #                 map_monde.screen.blit(map_monde.hero,(177*map_monde.longueur_ecran/1280,475*map_monde.hauteur_ecran/720))
               #                 pygame.event.clear()
               #                 pygame.display.flip()
               #                 level = 2


               #             #-4-#
               #             if map_monde.zone == 4:
               #                 map_monde.zone = 2
               #                 map_monde.fond = monde4
               #                 map_monde.sprite_zone4_zone3()
               #                 map_monde.sprite_zone3_zone2()
               #                 map_monde.fond = monde2_jouer
               #                 map_monde.screen.blit(map_monde.fond,(0,0))
               #                 map_monde.screen.blit(map_monde.hero,(177*map_monde.longueur_ecran/1280,475*map_monde.hauteur_ecran/720))
               #                 pygame.event.clear()
               #                 pygame.display.flip()
               #                 level = 2


               #             #-5-#
               #             if map_monde.zone == 5:
               #                 map_monde.zone = 2
               #                 map_monde.fond = monde5
               #                 map_monde.sprite_zone5_zone4()
               #                 map_monde.sprite_zone4_zone3()
               #                 map_monde.sprite_zone3_zone2()
               #                 map_monde.fond = monde2_jouer
               #                 map_monde.screen.blit(map_monde.fond,(0,0))
               #                 map_monde.screen.blit(map_monde.hero,(177*map_monde.longueur_ecran/1280,475*map_monde.hauteur_ecran/720))
               #                 pygame.event.clear()
               #                 pygame.display.flip()
               #                 level = 2



            #GO ZONE3#
            
               #     if event.button == 1:
               #         if zone_clickable_4.collidepoint(event.pos):
               #             #-1-#
               #             if map_monde.zone == 1 and niveau_max >= 3:
               #                 map_monde.zone = 3
               #                 map_monde.fond = monde1
               #                 map_monde.sprite_zone1_zone2()
               #                 map_monde.sprite_zone2_zone3()
               #                 map_monde.fond = monde3_jouer
               #                 map_monde.screen.blit(map_monde.fond,(0,0))
               #                 map_monde.screen.blit(map_monde.hero,(558*map_monde.longueur_ecran/1280,260*map_monde.hauteur_ecran/720))
               #                 pygame.event.clear()
               #                 pygame.display.flip()
               #                 level = 3


               #             #-2-#
               #             if map_monde.zone == 2 and niveau_max >= 3:
               #                 map_monde.zone = 3
               #                 map_monde.fond = monde2
               #                 map_monde.sprite_zone2_zone3()
               #                 map_monde.fond = monde3_jouer
               #                 map_monde.screen.blit(map_monde.fond,(0,0))
               #                 map_monde.screen.blit(map_monde.hero,(558*map_monde.longueur_ecran/1280,260*map_monde.hauteur_ecran/720))
               #                 pygame.event.clear()
               #                 pygame.display.flip()
               #                 level = 3


               #             #-4-#
               #             if map_monde.zone == 4:
               #                 map_monde.fond = monde4
               #                 map_monde.zone = 3
               #                 map_monde.sprite_zone4_zone3()
               #                 map_monde.fond = monde3_jouer
               #                 map_monde.screen.blit(map_monde.fond,(0,0))
               #                 map_monde.screen.blit(map_monde.hero,(558*map_monde.longueur_ecran/1280,260*map_monde.hauteur_ecran/720))
               #                 pygame.event.clear()
               #                 pygame.display.flip()
               #                 level = 3


               #             #-5-#
               #             if map_monde.zone == 5:
               #                 map_monde.zone = 3
               #                 map_monde.fond = monde5
               #                 map_monde.sprite_zone5_zone4()
               #                 map_monde.sprite_zone4_zone3()
               #                 map_monde.fond = monde3_jouer
               #                 map_monde.screen.blit(map_monde.fond,(0,0))
               #                 map_monde.screen.blit(map_monde.hero,(558*map_monde.longueur_ecran/1280,260*map_monde.hauteur_ecran/720))
               #                 pygame.event.clear()
               #                 pygame.display.flip()
               #                 level = 3


            #GO ZONE4#

               #     if event.button == 1:
               #         if zone_clickable_5.collidepoint(event.pos):
               #             #-1-#
               #             if map_monde.zone == 1 and niveau_max >= 4:
               #                 map_monde.zone = 4
               #                 map_monde.fond = monde1
               #                 map_monde.sprite_zone1_zone2()
               #                 map_monde.sprite_zone2_zone3()
               #                 map_monde.sprite_zone3_zone4()
               #                 map_monde.fond = monde4_jouer
               #                 map_monde.screen.blit(map_monde.fond,(0,0))
               #                 map_monde.screen.blit(map_monde.hero,(970*map_monde.longueur_ecran/1280,556*map_monde.hauteur_ecran/720))
               #                 pygame.event.clear()
               #                 pygame.display.flip()
               #                 level = 4


               #             #-2-#
               #             if map_monde.zone == 2 and niveau_max >= 4:
               #                 map_monde.zone = 4
               #                 map_monde.fond = monde2
               #                 map_monde.sprite_zone2_zone3()
               #                 map_monde.sprite_zone3_zone4()
               #                 map_monde.fond = monde4_jouer
               #                 map_monde.screen.blit(map_monde.fond,(0,0))
               #                 map_monde.screen.blit(map_monde.hero,(970*map_monde.longueur_ecran/1280,556*map_monde.hauteur_ecran/720))
               #                 pygame.event.clear()
               #                 pygame.display.flip()
               #                 level = 4


               #             #-3-#
               #             if map_monde.zone == 3 and niveau_max >= 4:
               #                 map_monde.zone = 4
               #                 map_monde.fond = monde3
               #                 map_monde.sprite_zone3_zone4()
               #                 map_monde.fond = monde4_jouer
               #                 map_monde.screen.blit(map_monde.fond,(0,0))
               #                 map_monde.screen.blit(map_monde.hero,(970*map_monde.longueur_ecran/1280,556*map_monde.hauteur_ecran/720))
               #                 pygame.event.clear()
               #                 pygame.display.flip()
               #                 level = 4


                            #-5-#
               #             if map_monde.zone == 5:
               #                 map_monde.zone = 4
               #                 map_monde.fond = monde5
               #                 map_monde.sprite_zone5_zone4()
               #                 map_monde.fond = monde4_jouer
               #                 map_monde.screen.blit(map_monde.fond,(0,0))
               #                 map_monde.screen.blit(map_monde.hero,(970*map_monde.longueur_ecran/1280,556*map_monde.hauteur_ecran/720))
               #                 pygame.event.clear()
               #                 pygame.display.flip()
               #                 level = 4


            #GO ZONE5#

               #     if event.button == 1:
               #         if zone_clickable_6.collidepoint(event.pos):
               #             #-1-#
               #             if map_monde.zone == 1 and niveau_max >= 5:
               #                 map_monde.zone = 5
               #                 map_monde.fond = monde1
               #                 map_monde.sprite_zone1_zone2()
               #                 map_monde.sprite_zone2_zone3()
               #                 map_monde.sprite_zone3_zone4()
               #                 map_monde.sprite_zone4_zone5()
               #                 map_monde.fond = monde5_jouer
               #                 map_monde.screen.blit(map_monde.fond,(0,0))
               #                 map_monde.screen.blit(map_monde.hero,(1070*map_monde.longueur_ecran/1280,64*map_monde.hauteur_ecran/720))
               #                 pygame.event.clear()
               #                 pygame.display.flip()
               #                 level = 5

                            #-2-#
               #             if map_monde.zone == 2 and niveau_max >= 5:
               #                 map_monde.zone = 5
               #                 map_monde.fond = monde2
               #                 map_monde.sprite_zone2_zone3()
               #                 map_monde.sprite_zone3_zone4()
               #                 map_monde.sprite_zone4_zone5()
               #                 map_monde.fond = monde5_jouer
               #                 map_monde.screen.blit(map_monde.fond,(0,0))
               #                 map_monde.screen.blit(map_monde.hero,(1070*map_monde.longueur_ecran/1280,64*map_monde.hauteur_ecran/720))
               #                 pygame.event.clear()
               #                 pygame.display.flip()
               #                 level = 5

               #             #-3-#
               #             if map_monde.zone == 3 and niveau_max >= 5:
               #                 map_monde.zone = 5
               #                 map_monde.fond = monde3
               #                 map_monde.sprite_zone3_zone4()
               #                 map_monde.sprite_zone4_zone5()
               #                 map_monde.fond = monde5_jouer
               #                 map_monde.screen.blit(map_monde.fond,(0,0))
               #                 map_monde.screen.blit(map_monde.hero,(1070*map_monde.longueur_ecran/1280,64*map_monde.hauteur_ecran/720))
               #                 pygame.event.clear()
               #                 pygame.display.flip()
               #                 level = 5

                            #-4-#
               #             if map_monde.zone == 4 and niveau_max >= 5:
               #                 map_monde.zone = 5
               #                 map_monde.fond = monde4
               #                 map_monde.sprite_zone4_zone5()
               #                 map_monde.fond = monde5_jouer
               #                 map_monde.screen.blit(map_monde.fond,(0,0))
               #                 map_monde.screen.blit(map_monde.hero,(1070*map_monde.longueur_ecran/1280,64*map_monde.hauteur_ecran/720))
               #                 pygame.event.clear()
               #                 pygame.display.flip()
               #                 level = 5
                    if event.button == 1:
                        if zone_clickable_1.collidepoint(event.pos):
                            largeur,hauteur = map_monde.screen.get_width(),map_monde.screen.get_height()
                            map_monde.fond = pygame.transform.scale(pygame.image.load("menu/fond_menu.jpg"),(largeur,hauteur))
                            map_monde.screen.blit(map_monde.fond,(0,0))
                            map_monde.fond = pygame.transform.scale(pygame.image.load("menu/MenuDemarrage.png"),(largeur,hauteur))
                            map_monde.screen.blit(map_monde.fond,(0,0))
                            pygame.display.update()
                            continuer = False


