from random import *
from tkinter import *

class Algo():
    def __init__(self):
        self.tableau=[]
        self._win = Tk()
        self._win.title("Parametrage")
        self._cote = IntVar()


        text = Label(self._win, text="Nombre de cases par côté du tableau : " )
        text.grid(row=0, column=0)
        scale = Scale( self._win, variable = self._cote , from_ = 1, to = 100 , orient = HORIZONTAL )
        scale.grid(row=1, column=0)
        self._button_start = Button(self._win, text='Start', command=self.start)
        self._button_start.grid(row=2, column=0)

        self._win.mainloop()

        

    def start(self):
        self._cote.get()
        
        self._win.destroy()
        self._dow = Tk()
        self._dow.title("Grilles_tournantes")
        self._dow.geometry('700x700')
        
        self._board = Canvas(self._dow, width=600, height=600, bg='black')
        self._board.grid(row=0, column=0)

        self._dow.mainloop()

    def draw(self, cote):
        dim = 500//len(self.tableau)
        for i in range(len(self.tableau)):
            for j in range((len(self.tableau))//2):
                if self.tableau[i][j]==1:
                    self._board.create_rectangle(50+dim*i, 50+dim*j, 50+dim*(i+1), 50+dim*(j+1), fill='grey')
                else:
                    self._board.create_rectangle(50+dim*i, 50+dim*j, 50+dim*(i+1), 50+dim*(j+1), fill= 'white')

    
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
    jeu=Algo()
    for i in range(len(jeu.tableau)):
        print(jeu.tableau[i])
    
main()