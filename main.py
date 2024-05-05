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
    
    def rotation_droite(self):
        n = len(self.tableau)
        tab = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                tab[j][n-1-i] = self.tableau[i][j]
        self.tableau = tab

    
    def init_tableau(self, cote):
        for _ in range(cote):
                self.tableau.append([0] * cote)
        if len(self.tableau) % 2 == 0:
            for i in range((len(self.tableau))//2):
                for j in range((len(self.tableau))//2):
                    rand=randint(1,4)
                    self.tableau[i][j]=1
                    for _ in range(rand):
                        self.rotation_droite()
        else :
            for i in range(((len(self.tableau))//2)+1):
                for j in range((len(self.tableau))//2):
                    rand=randint(1,4)
                    self.tableau[i][j]=1
                    for _ in range(rand):
                        self.rotation_droite()
                    
    def cipher(self):
        a="salutcommentcavapersocavaniquelettoi"
        a = list(a)
        code=""
        while len(a) > 0:
            tab=[]
            for _ in range(len(self.tableau)):
                tab.append([0] * len(self.tableau))
            for _ in range(4):
                for i in range(len(self.tableau)):
                    for j in range(len(self.tableau)):
                        if self.tableau[i][j]==1 and len(a) > 0 :
                            tab[i][j]=a[0]
                            a.pop(0)
                self.rotation_droite()
            for k in range(len(self.tableau)):
                for l in range(len(self.tableau)):
                    if tab[k][l]!=0:
                        code+=tab[k][l]
        return code
            
                

def main():
    cote=int(input("Nombre de cases par côté du tableau : "))
    jeu=Algo()
    jeu.init_tableau(cote)
    for i in range(len(jeu.tableau)):
        print(jeu.tableau[i])
    code = jeu.cipher()
    print(code)
    
main()