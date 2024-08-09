import pygame
from pygame.locals import*
from carte import*
import sys
from sauvegarde import *
from reset import *
import os 

#sys.path.insert(0, "boules")
#from boules import*
#from stats import*
#from jeux import*

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
largeur,hauteur = screen.get_width(),screen.get_height()
fond = pygame.transform.scale(pygame.image.load("menu/fond_menu.jpg"),(largeur,hauteur))
menu = pygame.transform.scale(pygame.image.load("menu/MenuDemarrage.png"),(largeur,hauteur))
screen.blit(fond,(0,0))
screen.blit(menu,(0,0))
pygame.display.flip()
pygame.display.set_caption("The adventure of horned pigeon-man")
pygame.mouse.set_cursor(pygame.cursors.tri_left)
perso1 = hero()
#a=os.system('gpg -d sauvegarde.txt.gpg')
#sauvegarder(a)
perso=chargerhero(perso1,'sauvegarde.txt')
perso.attaque=float(perso.attaque)
perso.defMax=float(perso.defMax)
perso.defense=float(perso.defense)
perso.magie=float(perso.magie)
perso.defMagieMax=float(perso.defMagieMax)
perso.defMagie=float(perso.defMagie)
perso.vie=float(perso.vie)
perso.vieMax=int(perso.vieMax)
perso.niveau=int(perso.niveau)
perso.experience=float(perso.experience)
perso.experienceMax=float(perso.experienceMax)
perso.carte_max=int(perso.carte_max)
menu = True
x=0
y=0

while menu:
    pos=pygame.mouse.get_pos(x,y)
    jeux = pygame.Rect(largeur/3-largeur/47,hauteur/2+hauteur/15,largeur/4-largeur/60,hauteur/5-hauteur/42)
    option = pygame.Rect(largeur/2+largeur/12,hauteur/2+hauteur/4,largeur/9-largeur/256,hauteur/6-hauteur/128)
    quiter = pygame.Rect(largeur-largeur/8,hauteur/13,largeur/12+largeur/44,hauteur/12)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.Rect.collidepoint(quiter, pos):
                menu = False
            if pygame.Rect.collidepoint(jeux, pos):
                carte_monde(perso)
            if pygame.Rect.collidepoint(option, pos):
                options()
