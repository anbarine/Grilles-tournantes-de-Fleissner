from random import *

class Gui():
    def __init__(self):
        pass
    
    def affichage_grille(self):
        pass
    
    def main_gui(self):
        pass
    

class Algo():
    def __init__(self, cases):
        self.tableau=[]
        self.cases=cases
    
    def init_tableau(self):
        if len(self.tableau) % 2 == 0:
            for i in range(1,(len(self.tableau)**2)/4):
                rand=randint(1,4)
   
                
                



    
    def add_lettre(self):
        pass
    
    def rotation(self):
        pass
    

def main():
    jeu=Algo()
    cote=int(input("Nombre de cases par côté du tableau : "))
    for x in range(cote):
        for y in range(cote):
            jeu.tableau[x][y]=0
    