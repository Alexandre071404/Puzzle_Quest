import pygame
from pygame.locals import *
from random import *
from boules import *
import time
import numpy as np
import sys
sys.path.insert(0, "image_carte")
from carte_class import*

#################################################################################################################################
#                                                    effets des boules                                                         #

def degat(vie,attaque,defense,boule):
        vie=vie-(attaque*boule/2+(randint(0,1)*0.5*attaque)-defense)#Formule de dégats en utilise (boule/2) pour modifier les dégats par rapports au nombres de boules pourquoi 2 car a force de test 2 est apparu comme le meilleur chiffre,on utilise en randint pour avoir 50% de chance d'avoir coups critique qui représente 50% des dégats d'attaque
        if vie<0:#Exeptions pour éviter d'avoir un moins de vie
                vie=0
        return(round(vie,1)) 
def protection(defense,boule):
        defense=defense+defense*0.1*(boule/2)#Formule du bonus permanent de défense qui utilise également (boule/2) pour modifier le bonus de défense par rapport au nombres de boules, on utilise le coefficient 0.25 car je trouce que c'est le meilleur coefficient. 
        return(defense)
def soin(vieMax,vie,boule):
        vie=vie+(vieMax/10)*(boule/2)#Formule de soin qui utilise aussi (boule/2) pour augmenter le soin par rapport au nombre de boules utilisé. 
        if vie>vieMax:#Exeptions pour éviter d'avoir un surplus de vie
                vie=vieMax
        if vie<0:#Exeptions pour éviter d'avoir un moins de vie
                vie=0
        return(round(vie,1))
#################################################################################################################################

#################################################################################################################################
def boule(i,j,tailleBoule,x,y,matrice,screen):#fonction qui affiche la boule au coordonée donné*
        image=pygame.transform.scale(pygame.image.load("boules/boule_"+str(matrice[j][i])+".png"),(tailleBoule,tailleBoule))
        screen.blit(image,(i*tailleBoule+x,j*tailleBoule+y))#affiche la boule dans la bonne case de la matrice graphique
#################################################################################################################################

#################################################################################################################################
def horizontal(matrice):#crée une matrice composer de 0 et de 1 avec sachant que 0 signifie qu'il y a des boules aligné en horizontal
        Boule_Testee=matrice[0][0]
        coordonee_Boule_Teste=[0,0]
        liste_effet=[]
        matrice_test=[[1 for i in range (len(matrice[0]))]for j in range (len(matrice))]#crée une matrice pleine de 1
        for i in range(len(matrice)):
                Nb_Boules_Identiques=0
                for j in range(len(matrice[i])):
                        if Boule_Testee==matrice[i][j]:
                                Nb_Boules_Identiques=Nb_Boules_Identiques+1
                                if j==len(matrice[i])-1:#vérifie si malgré le saut de ligne il y a un alignement
                                        if Nb_Boules_Identiques>=3:
                                                liste_effet.append((Boule_Testee,Nb_Boules_Identiques))#ajoute a liste effet Boule_Testee et Nb_Boules_Identiques qui vont permettre de faire des dégats,de soigner,de se protéger.
                                                for k in range(Nb_Boules_Identiques):
                                                        matrice_test[i][j-k]=0
                        else:
                                if Nb_Boules_Identiques>=3:
                                        liste_effet.append((Boule_Testee,Nb_Boules_Identiques))#ajoute a liste effet Boule_Testee et Nb_Boules_Identiques qui vont permettre de faire des dégats,de soigner,de se protéger.
                                        for k in range(Nb_Boules_Identiques):
                                                matrice_test[i][j-k-1]=0
                                Nb_Boules_Identiques=1
                                Boule_Testee=matrice[i][j]
                                coordonee_Boule_Teste=[i,j]
        return(matrice_test,liste_effet)

def vertical(matrice):#crée une matrice composer de 0 et de 1 avec sachant que 0 signifie qu'il y a des boules aligné en vertical
    Boule_Testee=matrice[0][0]
    coordonee_Boule_Teste=[0,0]
    liste_effet=[]
    matrice_test=[[1 for i in range (len(matrice[0]))]for j in range (len(matrice))]
    for i in range(len(matrice[0])):
        Nb_Boules_Identiques=0
        for j in range(len(matrice)):
            if Boule_Testee==matrice[j][i]:
                Nb_Boules_Identiques=Nb_Boules_Identiques+1
                if j==len(matrice)-1:
                        if Nb_Boules_Identiques>=3:
                                liste_effet.append((Boule_Testee,Nb_Boules_Identiques))
                                for k in range(Nb_Boules_Identiques):
                                        matrice_test[j-k][i]=0
            else:
                if Nb_Boules_Identiques>=3:
                    liste_effet.append((Boule_Testee,Nb_Boules_Identiques))#ajoute a liste effet Boule_Testee et Nb_Boules_Identiques qui vont permettre de faire des dégats,de soigner,de se protéger.
                    for k in range(Nb_Boules_Identiques):
                        matrice_test[j-k-1][i]=0
                Nb_Boules_Identiques=1
                Boule_Testee=matrice[j][i]
                coordonee_Boule_Teste=[j,i]
    return(matrice_test,liste_effet)

def combinaison_de_matrice(matrice):#crée une combinaison entre la matrice vertical et horizontal et aussi des liste_effet de chaque fonctions
        matrice_test_horizontal=horizontal(matrice)
        matrice_test_vertical=vertical(matrice)
        liste_effet=matrice_test_horizontal[1]+matrice_test_vertical[1]#crée la liste d'effet compléte
        for i in range(len(matrice)):
                for j in range(len(matrice[i])):
                        matrice[i][j]=matrice[i][j]*matrice_test_horizontal[0][i][j]*matrice_test_vertical[0][i][j]
        return(matrice,liste_effet)
#################################################################################################################################
niveau_monde = carte(1)
#################################################################################################################################
def jeu(hero,enemie,matrice,level):
        global exp
        hero.levelup(1.5,1,1,0.75,10,10,1,hero.experience,hero.experienceMax)
        largeur_matrice=longeur_matrice=8#taille de la matrices
        case_presser,case_relacher=(0,0)#définie des variables vides
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)#récupere l'écran screen de la carte
        longuer_ecran,largeur_ecran=screen.get_width(),screen.get_height()#récupere la taille de l'écran
        tailleBoule=longuer_ecran/(1280/60)
        if hero.niveau>5:
                niveau=5
        else:
                niveau=hero.niveau
        fond = pygame.transform.scale(pygame.image.load("boules/fond_combat_"+str(level)+".jpg"),(longuer_ecran,largeur_ecran))#défini le fond et les différents personnage 
        sprite_1 = pygame.transform.scale(pygame.image.load("sprite_combat/sprite_"+str(level)+"_enemi.png"),(longuer_ecran,largeur_ecran))
        sprite_2 = pygame.transform.scale(pygame.image.load("sprite_combat/sprite_"+str(niveau)+"_hero.png"),(longuer_ecran,largeur_ecran))
        sortir = pygame.transform.scale(pygame.image.load("images/Exit.png"),(longuer_ecran,largeur_ecran))
        sortir = pygame.transform.rotate(sortir, 180)
        
        reset =  pygame.Rect(longuer_ecran*0.02, largeur_ecran*0.84, longuer_ecran*0.105, largeur_ecran*0.085)
        screen.blit(fond,(0,0))#affiche le fond et les différents personnage
        screen.blit(sortir,(0,0))
        screen.blit(sprite_1,(0,0))
        screen.blit(sprite_2,(0,0))
        x=screen.get_width()/2-tailleBoule*longeur_matrice/2#coordonée de l'angle en haut à gauche de la matrice
        y=screen.get_height()/2-(tailleBoule*largeur_matrice/2+1)
        font = pygame.font.Font("font/verdana.ttf", 15)#ajout de la police d'écriture
        pygame.draw.rect(screen,pygame.Color(255, 0, 0),((longuer_ecran-tailleBoule-(0.37*longuer_ecran)+((enemie.vieMax-enemie.vie)*(0.37*longuer_ecran)/enemie.vieMax),tailleBoule),((enemie.vie*(0.37*longuer_ecran))/enemie.vieMax,20)))#barre de vie enemie
        pygame.draw.rect(screen,pygame.Color(255, 255, 255),((longuer_ecran-tailleBoule-(0.37*longuer_ecran),tailleBoule),(0.37*longuer_ecran,20)),2)#contour de la barre de vie enemie
        pygame.draw.rect(screen,pygame.Color(0, 200, 0),((tailleBoule,tailleBoule),((hero.vie*(0.37*longuer_ecran))/hero.vieMax,20)))#barre de vie joueur
        pygame.draw.rect(screen,pygame.Color(255, 255, 255),((tailleBoule,tailleBoule),(0.37*longuer_ecran,20)),2)#contour de barre de vie du joueur
        afficher = font.render(str(round(enemie.vie,1)), 1, (255, 255, 255))
        screen.blit(afficher,((longuer_ecran-tailleBoule-(0.37*longuer_ecran)+2,tailleBoule)))
        afficher = font.render(str(round(hero.vie,1)), 1, (255, 255, 255))
        screen.blit(afficher,(((0.37*longuer_ecran)+tailleBoule-afficher.get_size()[0]-2,tailleBoule)))
        continuer = True
        while continuer:
                for j in range(len(matrice)):
                        for i in range(len(matrice[j])):
                                boule(i,j,tailleBoule,x,y,matrice,screen)#éxécute la fonction boules
                while 0 in np.array(matrice):#boucle tant que il y a des zéros dans la matrice
                        for j in range(len(matrice)):
                                for i in range(len(matrice[j])):
                                        boule(i,j,tailleBoule,x,y,matrice,screen)#éxécute la fonction boules
                                        if matrice[i][j]==0 and i==0:#rédéfinie les boules qui sont sur la prémière ligne
                                                matrice[i][j]=randint(1,5)
                                        elif matrice[i][j]==0:#fait chuter les boules
                                                matrice[i][j]=matrice[i-1][j]
                                                matrice[i-1][j]=0
                                        pygame.display.update()
                liste_effet=combinaison_de_matrice(matrice)[1]#liste des effets a appliquer après chaque mouvement 
                for i in range(len(liste_effet)):#boucle qui appplique la liste effet et qui affiche une boules a côté de la barre de vie pour montrer l'action produite
                        if liste_effet[i][0]==1:
                                enemie.vie=degat(enemie.vie,hero.attaque,enemie.defense,liste_effet[i][1])
                                screen.blit(pygame.transform.scale(pygame.image.load("boules/boule_1.png"),(tailleBoule,tailleBoule)),((((0.37*longuer_ecran)+2+tailleBoule,tailleBoule/1.5))))
                        elif liste_effet[i][0]==2:
                                hero.defense=protection(hero.defense,liste_effet[i][1])
                                screen.blit(pygame.transform.scale(pygame.image.load("boules/boule_2.png"),(tailleBoule,tailleBoule)),((((0.37*longuer_ecran)+2+tailleBoule,tailleBoule/1.5))))
                        elif liste_effet[i][0]==3:
                                enemie.vie=degat(enemie.vie,hero.magie,enemie.defMagie,liste_effet[i][1])
                                screen.blit(pygame.transform.scale(pygame.image.load("boules/boule_3.png"),(tailleBoule,tailleBoule)),((((0.37*longuer_ecran)+2+tailleBoule,tailleBoule/1.5))))
                        elif liste_effet[i][0]==4:
                                hero.defMagie=protection(hero.defMagie,liste_effet[i][1])
                                screen.blit(pygame.transform.scale(pygame.image.load("boules/boule_4.png"),(tailleBoule,tailleBoule)),((((0.37*longuer_ecran)+2+tailleBoule,tailleBoule/1.5))))
                        elif liste_effet[i][0]==5:
                                hero.vie=soin(hero.vieMax,hero.vie,liste_effet[i][1])
                                screen.blit(pygame.transform.scale(pygame.image.load("boules/boule_5.png"),(tailleBoule,tailleBoule)),((((0.37*longuer_ecran)+2+tailleBoule,tailleBoule/1.5))))
                        pygame.draw.rect(screen,pygame.Color(0, 0, 0),((tailleBoule,tailleBoule),((0.37*longuer_ecran),20)))#place en rectangle noir a la place des barres de vie 
                        pygame.draw.rect(screen,pygame.Color(0, 0, 0),((longuer_ecran-tailleBoule-(0.37*longuer_ecran),tailleBoule),(0.37*longuer_ecran,20)))
                        pygame.draw.rect(screen,pygame.Color(255, 0, 0),((longuer_ecran-tailleBoule-(0.37*longuer_ecran)+((enemie.vieMax-enemie.vie)*(0.37*longuer_ecran)/enemie.vieMax),tailleBoule),((enemie.vie*(0.37*longuer_ecran))/enemie.vieMax,20)))#barre de vie enemie
                        pygame.draw.rect(screen,pygame.Color(255, 255, 255),((longuer_ecran-tailleBoule-(0.37*longuer_ecran),tailleBoule),(0.37*longuer_ecran,20)),2)#contour de la barre de vie enemie
                        pygame.draw.rect(screen,pygame.Color(0, 200, 0),((tailleBoule,tailleBoule),((hero.vie*(0.37*longuer_ecran))/hero.vieMax,20)))#barre de vie joueur
                        pygame.draw.rect(screen,pygame.Color(255, 255, 255),((tailleBoule,tailleBoule),(0.37*longuer_ecran,20)),2)#contour de barre de vie du joueur
                        afficher = font.render(str(enemie.vie), 1, (255, 255, 255))
                        screen.blit(afficher,((longuer_ecran-tailleBoule-(0.37*longuer_ecran)+2,tailleBoule)))#affiche le nombre de point de vie en texte
                        afficher = font.render(str(hero.vie), 1, (255, 255, 255))
                        screen.blit(afficher,(((0.37*longuer_ecran)+tailleBoule-afficher.get_size()[0]-2,tailleBoule)))#affiche le nombre de point de vie en texte
                        pygame.display.update()
                if aucuncoup(matrice)==False and not(0 in np.array(matrice)):
                        matrice=consmatrice(len(matrice),len(matrice))#on recreer une grille si aucun déplacement n'est possible sur l'ensemble de la matrice.
                pygame.display.update()
                if (hero.vie<=0):
                        screen.blit(pygame.transform.scale(pygame.image.load("images/defaite.png"),(largeur_ecran,largeur_ecran)),(longuer_ecran/2-largeur_ecran/2,largeur_ecran/2-largeur_ecran/2))#affiche l'images au centre de l'écran
                        pygame.display.update()
                        while continuer:
                                for event in pygame.event.get():
                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                                continuer=False
                elif (enemie.vie<=0):
                        expe = randint(40*(level/2), 80*(level/2))#on utilise c'est variable pour avoir une courbe de progession correcte
                        hero.experience += expe
                        hero.levelup(1.5,1,1,0.75,10,10,1,hero.experience,hero.experienceMax)
                        screen.blit(pygame.transform.scale(pygame.image.load("images/victoire.png"),(largeur_ecran,largeur_ecran)),(longuer_ecran/2-largeur_ecran/2,largeur_ecran/2-largeur_ecran/2))#affiche l'images au centre de l'écran
                        pygame.display.update()
                        while continuer:
                                for event in pygame.event.get():
                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                                continuer=False
                        if hero.carte_max==level:
                                hero.carte_max=hero.carte_max+1#augmente de 1 le niveau maximum que l'on peut atteindre 
                for event in pygame.event.get():
                        pos=pygame.mouse.get_pos(x,y)              
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                if pygame.Rect.collidepoint(reset, pos):
                                        continuer=False
                                case_presser =(int((pygame.mouse.get_pos()[1]-y)//tailleBoule),int((pygame.mouse.get_pos()[0]-x)//tailleBoule))#récupere la parti de la matrice cliquer
                        if event.type == QUIT:
                                continuer = False
                                sys.exit()
                        if event.type == pygame.MOUSEBUTTONUP:
                                case_relacher=(int((pygame.mouse.get_pos()[1]-y)//tailleBoule),int((pygame.mouse.get_pos()[0]-x)//tailleBoule))#récupere la parti de la matrice relacher
                                if abs(case_presser[0]-case_relacher[0])==1 and abs(case_presser[1]-case_relacher[1])==0 or abs(case_presser[0]-case_relacher[0])==0 and abs(case_presser[1]-case_relacher[1])==1:#si l'action est inférieur a 1 dans n'importe direction alors on peut
                                        if case_presser[0]<8 and case_presser[1]<8 and case_relacher[0]<8 and case_relacher[1]<8 and case_presser[0]>-1 and case_presser[1]>-1 and case_relacher[0]>-1 and case_relacher[1]>-1:
                                                matrice_possible=[[matrice[j][i] for i in range(len(matrice))] for j in range(len(matrice[i]))]#creer une matrice identique a la matrice de jeux
                                                ajout=matrice_possible[case_presser[0]][case_presser[1]]
                                                matrice_possible[case_presser[0]][case_presser[1]]=matrice_possible[case_relacher[0]][case_relacher[1]]#fais l'échange sur la matrice possible
                                                matrice_possible[case_relacher[0]][case_relacher[1]]=ajout
                                                if possible(matrice_possible,case_relacher[0],case_relacher[1]) or possible(matrice_possible,case_presser[0],case_presser[1]):#si le mouvement est utile on le fais
                                                        ###
                                                        coup_enemie=randint(0,2)
                                                        if coup_enemie==2 and enemie.vie < (enemie.vieMax*50/100):
                                                                enemie.vie=soin(enemie.vieMax,enemie.vie,3)
                                                                screen.blit(pygame.transform.scale(pygame.image.load("boules/boule_5.png"),(tailleBoule,tailleBoule)),(((longuer_ecran-tailleBoule*2-(0.37*longuer_ecran)-2,tailleBoule/1.5))))
                                                        else:
                                                                coup_enemie=randint(0,1)
                                                        if coup_enemie==0:
                                                                hero.vie=degat(hero.vie,enemie.attaque,hero.defense,3)
                                                                screen.blit(pygame.transform.scale(pygame.image.load("boules/boule_1.png"),(tailleBoule,tailleBoule)),(((longuer_ecran-tailleBoule*2-(0.37*longuer_ecran)-2,tailleBoule/1.5))))
                                                        if coup_enemie==1:
                                                                hero.vie=degat(hero.vie,enemie.magie,hero.defMagie,3)
                                                                screen.blit(pygame.transform.scale(pygame.image.load("boules/boule_3.png"),(tailleBoule,tailleBoule)),(((longuer_ecran-tailleBoule*2-(0.37*longuer_ecran)-2,tailleBoule/1.5))))
                                                        if hero.vie>hero.vieMax:#Exeptions pour éviter d'avoir un surplus de vie
                                                                hero.vie=hero.vieMax
                                                        if hero.vie<0:#Exeptions pour éviter d'avoir un moins de vie
                                                                hero.vie=0
                                                        if enemie.vie>enemie.vieMax:#Exeptions pour éviter d'avoir un surplus de vie
                                                                enemie.vie=enemie.vieMax
                                                        if enemie.vie<0:#Exeptions pour éviter d'avoir un moins de vie
                                                                enemie.vie=0
                                                        ###
                                                        ajout=matrice[case_presser[0]][case_presser[1]]
                                                        matrice[case_presser[0]][case_presser[1]]=matrice[case_relacher[0]][case_relacher[1]]#fais l'échange sur la matrice jeux
                                                        matrice[case_relacher[0]][case_relacher[1]]=ajout
        hero.vie=hero.vieMax
        hero.defense=hero.defMax
        hero.defMagie=hero.defMagieMax
