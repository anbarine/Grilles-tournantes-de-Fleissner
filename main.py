from random import *

class Gui():
    def __init__(self):
        pass
    
    def affichage_grille(self):
        pass
    
    def main_gui(self):
        pass
    

class Algo():
    def __init__(self):
        self.tableau=[]
    
    def rotation(self):
        tab = self.tableau
        for i in range(len(self.tableau)):
            for j in range(len(self.tableau)):
                tab[5-j][i], self.tableau[i][j] = self.tableau[i][j], tab[5-j][i]
        self.tableau = tab
    
    def init_tableau(self, cote):
        if len(self.tableau) % 2 == 0:
            for _ in range(cote):
                self.tableau.append([0] * cote)
            for i in range((len(self.tableau))//2):
                for j in range((len(self.tableau))//2):
                    self.tableau[i][j]=1
                    rand=randint(1,4)
                    for _ in range(rand):
                        self.rotation()
                    
    def add_lettre(self):
        pass
    
    

def main():
    cote=int(input("Nombre de cases par côté du tableau : "))
    jeu=Algo()
    jeu.init_tableau(cote)
    for i in range(len(jeu.tableau)):
        print(jeu.tableau[i])
    
main()