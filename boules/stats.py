class hero:
    def __init__(self):
        self.attaque=15
        self.defMax=10
        self.defense=self.defMax
        self.magie=10
        self.defMagieMax=7.5
        self.defMagie=self.defMagieMax
        self.vie=100
        self.vieMax=100
        self.niveau=1
        self.experience=0
        self.experienceMax=100
        self.carte_max= 1
    def levelup(self,attaque,defense,magie,defMagie,vie,vieMax,niveau,experience,experienceMax):
        if experience >= experienceMax:
            self.experience = experience-experienceMax
            self.niveau+=niveau
            self.attaque+=attaque
            self.defMax+=defense
            self.magie+=magie
            self.defMagieMax+=defMagie
            self.vie+=vie
            self.vieMax+=vieMax
            self.experienceMax+=(experienceMax/2)

class enemie:
    def __init__(self,vieMax,vie,attaque,defense,magie,defMagie):
        self.attaque=attaque
        self.defense=defense
        self.magie=magie
        self.defMagie=defMagie
        self.vie=vie
        self.vieMax=vieMax
