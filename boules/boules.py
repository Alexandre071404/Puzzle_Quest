from random import * 
import time
def consmatrice(a,b):
	matrice=[]
	for i in range(a):
		ligne=[]
		for k in range(b):
			r=randint(1,5)
			ligne.append(r)
		matrice.append(ligne)	#génération de la matrice de jeu
	e=False 
	while e==False:
		e=True
		z=0
		for val in range(a):
			for val2 in range(1,b-1):
				if matrice[val][val2]==matrice[val][val2-1] and matrice[val][val2]==matrice[val][val2+1]:#on verifie si il n'y a pas 3 boules de la même famille en ligne
					al=matrice[val][val2]
					z+=2
					while al==matrice[val][val2]:
						matrice[val][val2]=randint(1,5)
		for val3 in range(1,a-1):
			for val4 in range(b):#on verifie si il n'y a pas 3 boules de la même famille en collone
				if matrice[val3][val4]==matrice[val3-1][val4] and matrice[val3][val4]==matrice[val3+1][val4]:
					m=matrice[val3][val4]
					z+=2
					while m==matrice[val3][val4]:
						matrice[val3][val4]=randint(1,5)
		if z!=0:
			e=False
	return matrice

def possible(matrice,x,y):
#On teste les diverses manières de positions des boules avec des conditions pour éviter des "out of range"
	a=len(matrice)-2
	b=len(matrice)-1
	
	if x==0:
		if matrice[x][y]==matrice[x+1][y]==matrice[x+2][y]:
			return True
	if y==0:
		if matrice[x][y]==matrice[x][y+1]==matrice[x][y+2]:
			return True

	if x==a:
		if matrice[x][y]==matrice[x-1][y]==matrice[x-2][y] or matrice[x][y]==matrice[x-1][y]==matrice[x+1][y]:
			return True 

	if y==a:
		if matrice[x][y]==matrice[x][y+1]==matrice[x][y-1] or  matrice[x][y]==matrice[x][y-1]==matrice[x][y-2]:
			return True
	if y==b:
		if matrice[x][y]==matrice[x][y-1]==matrice[x][y-2]:
			return True
	if x==b:
		if matrice[x][y]==matrice[x-1][y]==matrice[x-2][y]:
			return True 
	
	if x<a and x!=0:
		if matrice[x][y]==matrice[x-1][y]==matrice[x-2][y] or matrice[x][y]==matrice[x-1][y]==matrice[x+1][y] or matrice[x][y]==matrice[x+1][y]==matrice[x+2][y]:
			return True 			
	if y<a and y!=0:
		if matrice[x][y]==matrice[x][y+1]==matrice[x][y+2] or matrice[x][y]==matrice[x][y+1]==matrice[x][y-1] or matrice[x][y]==matrice[x][y-1]==matrice[x][y-2]: #Permet de verifier les lignes 
			return True
	else:
		return False


#groupes-de-fonction-pour-verifier-que-des-matches-sont-possibles--------------#  

def haut(matrice,i,j):#-------------verifier les different matches possible vers le haut--------------#
	if matrice[i][j]==matrice[i-1][j] and matrice[i][j]==matrice[i-2][j+1] or matrice[i][j]==matrice[i-1][j] and matrice[i][j]==matrice[i-2][j-1] or matrice[i][j]==matrice[i-2][j] and matrice[i][j]==matrice[i-1][j+1] or matrice[i][j]==matrice[i-2][j] and matrice[i][j]==matrice[i-1][j-1] or matrice[i][j]==matrice[i-1][j+1] and matrice[i][j]==matrice[i-2][j+1] or matrice[i][j]==matrice[i-1][j-1] and matrice[i][j]==matrice[i-2][j-1]:
		return True

def bas(matrice,i,j):#-------------verifier les different matches possible vers le bas--------------#
	if matrice[i][j]==matrice[i+1][j] and matrice[i][j]==matrice[i+2][j+1] or matrice[i][j]==matrice[i+1][j] and matrice[i][j]==matrice[i+2][j-1] or matrice[i][j]==matrice[i+2][j] and matrice[i][j]==matrice[i+1][j+1] or matrice[i][j]==matrice[i+2][j] and matrice[i][j]==matrice[i+1][j-1] or matrice[i][j]==matrice[i+1][j+1] and matrice[i][j]==matrice[i+2][j+1] or matrice[i][j]==matrice[i+1][j-1] and matrice[i][j]==matrice[i+2][j-1]:
		return True

def droite(matrice,i,j):#-------------verifier les different matches possible vers la droite--------------#
	if matrice[i][j]==matrice[i][j+1] and matrice[i][j]==matrice[i+1][j+2] or matrice[i][j]==matrice[i][j+1] and matrice[i][j]==matrice[i-1][j+2] or matrice[i][j]==matrice[i][j+2] and matrice[i][j]==matrice[i-1][j+1] or matrice[i][j]==matrice[i][j+2] and matrice[i][j]==matrice[i+1][j+1] or matrice[i][j]==matrice[i+1][j+1] and matrice[i][j]==matrice[i+1][j+2] or matrice[i][j]==matrice[i-1][j+1] and matrice[i][j]==matrice[i-1][j+2]:
		return True

def gauche(matrice,i,j):#-------------verifier les different matches possible vers la gauche--------------#
	if matrice[i][j]==matrice[i][j-1] and matrice[i][j]==matrice[i+1][j-2] or matrice[i][j]==matrice[i][j-1] and matrice[i][j]==matrice[i-1][j-2] or matrice[i][j]==matrice[i][j-2] and matrice[i][j]==matrice[i-1][j-1] or matrice[i][j]==matrice[i][j-2] and matrice[i][j]==matrice[i+1][j-1] or matrice[i][j]==matrice[i+1][j-1] and matrice[i][j]==matrice[i+1][j-2] or matrice[i][j]==matrice[i-1][j-1] and matrice[i][j]==matrice[i-1][j-2]:
		return True
#----------------------------------------------------------------------#
def cornerTL(matrice,i,j):#----------verifier les matches du coin en haut a gauche--------------#
	if matrice[i][j]==matrice[i+1][j+1] and matrice[i][j]==matrice[i+1][j+2] or matrice[i][j]==matrice[i][j+1] and matrice[i][j]==matrice[i+1][j+2] or matrice[i][j]==matrice[i+1][j+1] and matrice[i][j]==matrice[i][j+2] or matrice[i][j]==matrice[i+1][j+1] and matrice[i][j]==matrice[i+2][j] or matrice[i][j]==matrice[i+1][j] and matrice[i][j]==matrice[i+2][j+1] or matrice[i][j]==matrice[i+1][j+1] and matrice[i][j]==matrice[i+2][j+1]:
		return True

def cornerTR(matrice,i,j):#----------verifier les matches du coin en haut a droite--------------#
	if matrice[i][j]==matrice[i][j-1] and matrice[i][j]==matrice[i+1][j-2] or matrice[i][j]==matrice[i+1][j] and matrice[i][j]==matrice[i+2][j-1] or matrice[i][j]==matrice[i+1][j-1] and matrice[i][j]==matrice[i+2][j-1] or matrice[i][j]==matrice[i+1][j-1] and matrice[i][j]==matrice[i+1][j-2] or matrice[i][j]==matrice[i][j-2] and matrice[i][j]==matrice[i+1][j-1] or matrice[i][j]==matrice[i+2][j] and matrice[i][j]==matrice[i+1][j-1]:
		return True

def cornerBL(matrice,i,j):#----------verifier les matches du coin en bas a gauche
	if matrice[i][j]==matrice[i-1][j] and matrice[i][j]==matrice[i-2][j+1] or matrice[i][j]==matrice[i][j+1] and matrice[i][j]==matrice[i-1][j+2] or matrice[i][j]==matrice[i-1][j+1] and matrice[i][j]==matrice[i-2][j] or matrice[i][j]==matrice[i-1][j+1] and matrice[i][j]==matrice[i][j+2] or matrice[i][j]==matrice[i-1][j+1] and matrice[i][j]==matrice[i-1][j+2] or matrice[i][j]==matrice[i-1][j+1] and matrice[i][j]==matrice[i-2][j+1]:
		return True

def cornerBR(matrice,i,j):#----------verifier les matches du coin en bas a droite--------------#
	if matrice[i][j]==matrice[i-1][j-1] and matrice[i][j]==matrice[i-2][j-1] or matrice[i][j]==matrice[i-1][j-1] and matrice[i][j]==matrice[i-1][j-2] or matrice[i][j]==matrice[i-1][j-1] and matrice[i][j]==matrice[i-2][j] or matrice[i][j]==matrice[i-1][j-1] and matrice[i][j]==matrice[i][j-2] or matrice[i][j]==matrice[i-1][j] and matrice[i][j]==matrice[i-2][j-1] or matrice[i][j]==matrice[i][j-1] and matrice[i][j]==matrice[i-1][j-2]:
		return True
#----------------------------------------------------------------------#	
def ligneD(matrice,i,j):#------------verifie le matche de gauche a droite en ligne------------#
	if matrice[i][j]==matrice[i][j+2] and matrice[i][j]==matrice[i][j+3]:
		return True

def ligneG(matrice,i,j):#------------verifie le matche de droite a gauche en ligne------------#
	if matrice[i][j]==matrice[i][j-2] and matrice[i][j]==matrice[i][j-3]:
		return True

def coloneB(matrice,i,j):#------------verifie le matche de haut en bas en ligne------------#
	if matrice[i][j]==matrice[i+2][j] and matrice[i][j]==matrice[i+3][j]:
		return True

def coloneH(matrice,i,j):#------------verifie le matche de bas en haut en ligne------------#
	if matrice[i][j]==matrice[i-2][j] and matrice[i][j]==matrice[i-3][j]:
		return True
#-----------------------------------------------------------------------------------

def aucuncoup(matrice):#si aucun coup n'est possible dans l'ensemble de la matrice alors on va en refaire une.
	for x in range(len(matrice)-1):
		for y in range(len(matrice[0])-1):#matrice[0] permet de prendre une ligne de la matrice 
			
#------------------------------VERIFIER LA HAUTEUR--------------------		
			if y>=1 and y<=len(matrice)-2:
				if x>=0 and x<=len(matrice)-3:
					if bas(matrice,x,y):
						return True
				elif x>=2 and x<=len(matrice)-1:
					if haut(matrice,x,y):
						return True	
			elif x>=0 and x<=len(matrice)-1:
				if y>=0 and y<=len(matrice)-4:
					if ligneD(matrice,x,y):
						return True	
				elif y>=3 and y<=len(matrice)-1:
					if ligneG(matrice,x,y):
						return True
#------------------------------VERIFIER LA LARGEUR--------------------
			elif x>=1 and x<=len(matrice)-2:
				if y>=0 and y<=len(matrice)-3 :
					if droite(matrice,x,y):
						return True
				elif y>=2 and y>len(matrice)-1 :
					if gauche(matrice,x,y):
						return True
						
			elif y>=0 and y<=len(matrice)-1:
				if x>=0 and x<=len(matrice)-4:
					if coloneB(matrice,x,y):
						return True	
				elif x>=3 and x<=len(matrice)-1:
					if coloneH(matrice,x,y):
						return True
#------------------------------VERIFIER LES COINS--------------------
			elif x==0 and y==0:
				if cornerTL(matrice,x,y):
					return True
			elif x==0 and y==len(matrice)-1:
				if cornerTR(matrice,x,y):
					return True
			elif x==len(matrice)-1 and y==0:
				if cornerBL(matrice,x,y):
					return True
			elif x==len(matrice)-1 and y==len(matrice)-1:
				if cornerBR(matrice,x,y):
					return True
	return False
