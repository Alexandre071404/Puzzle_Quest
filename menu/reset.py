import pygame
from pygame.locals import*
from carte import*
import sys
from sauvegarde import *

def options():
    opt = True
    x=0
    y=0
    while opt:
        pos=pygame.mouse.get_pos(x,y)
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        largeur,hauteur = screen.get_width(),screen.get_height()
        fond = pygame.transform.scale(pygame.image.load("menu/fond_menu.jpg"),(largeur,hauteur))
        exit = pygame.transform.scale(pygame.image.load("images/Exit.png"),(largeur,hauteur))
        res = pygame.transform.scale(pygame.image.load("images/reset.png"),(largeur/2,hauteur))
        #pygame.draw.rect(exit, (255,255,255,), pygame.Rect(largeur-largeur/8,hauteur/13,largeur/12+largeur/44,hauteur/12))
        screen.blit(fond,(0,0))
        screen.blit(exit,(0,0))
        screen.blit(res,(largeur/4,0))
        pygame.display.flip()
        reset = pygame.Rect(37*largeur/128, 6*hauteur/32, 13*largeur/32, 45*hauteur/128)
        quiter = pygame.Rect(7*largeur/8,hauteur/13,4.7*largeur/44,hauteur/12)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect.collidepoint(reset, pos):
                    recommencer()
                if pygame.Rect.collidepoint(quiter, pos):
                    screen.blit(fond,(0,0))
                    menu = pygame.transform.scale(pygame.image.load("menu/MenuDemarrage.png"),(largeur,hauteur))
                    screen.blit(menu,(0,0))
                    opt = False
                    
                    
            
