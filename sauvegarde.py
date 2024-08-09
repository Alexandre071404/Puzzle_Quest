def sauvegarderobj(a):#On écrit les caractéristiques dans un fichier 
	with open("sauvegarde.txt",'w') as file:
		file.write(str(a.attaque)+",")
		file.write(str(a.defMax)+",")
		file.write(str(a.defense)+",")
		file.write(str(a.magie)+",")		
		file.write(str(a.defMagieMax)+",")
		file.write(str(a.defMagie)+",")
		file.write(str(a.vie)+",")
		file.write(str(a.vieMax)+",")
		file.write(str(a.niveau)+",")
		file.write(str(a.experience)+",")
		file.write(str(a.experienceMax)+",")
		file.write(str(a.carte_max))
		file.close()

def sauvegarder(a):#On écrit les caractéristiques dans un fichier 
	with open("sauvegarde.txt",'w') as file:
		file.write(str(a))

def charger(fichier):#On charge le fichier avec l'extraction de toutes les données 
	don=[]
	with open(fichier,'r') as file:
		for i in file:
			don.append([str(d) for d in i.split(",")])
	file.close
	return don
	
	
def chargerhero(h,fichier):#les données chargées sont mises en lien avec les statistiques du héro dans le jeu
	c=charger(fichier)
	for i in c:
		h.attaque=i[0]
		h.defMax=i[1]
		h.defense=i[2]
		h.magie=i[3]
		h.defMagieMax=i[4]
		h.defMagie=i[5]
		h.vie=i[6]
		h.vieMax=i[7]
		h.niveau=i[8]
		h.experience=i[9]
		h.experienceMax=i[10]
		h.carte_max=i[-1]
	return h
	
def recommencer():#réinitialise le fichier sauvegarde.py pour recommencer la partie
	with open("sauvegarde.txt",'w') as file:
		file.write(str(15)+",")
		file.write(str(10)+",")
		file.write(str(10)+",")
		file.write(str(10)+",")		
		file.write(str(7.5)+",")
		file.write(str(7.5)+",")
		file.write(str(100)+",")
		file.write(str(100)+",")
		file.write(str(1)+",")
		file.write(str(0)+",")
		file.write(str(100)+",")
		file.write(str(1))
		file.close()
