import pygame
from pygame.locals import*
from carte import*
import sys
from sauvegarde import *
from reset import *
import os
from subprocess import call

#sys.path.insert(0, "boules")
#from boules import*
#from stats import*
#from jeux import*

pygame.init()
os.system('gpg -o sauvegarde.txt -d sauvegarde.txt.gpg')
os.system('o')
#call(["gpg", "-o", "sauvegarde.txt", "-d", "sauvegarde.txt.gpg"])
#call(["o"])
