from random import *
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

class Algo():
    def __init__(self):
        self.tableau=[]
        self._win = Tk()
        self._win.title("Parametrage")
        self._cote = IntVar()
        self._clock_variable = 0


        text = Label(self._win, text="Nombre de cases par côté du tableau : ")
        text.grid(row=0, column=0)
        scale = Scale( self._win, variable = self._cote , from_ = 1, to = 20 , orient = HORIZONTAL )
        scale.grid(row=1, column=0)
        self._button_start = Button(self._win, text='Start', command=self.start)
        self._button_start.config(bg="light blue", fg="black", font=("Arial", 8, "bold"), padx=10, pady=5, relief=RAISED)
        self._button_start.grid(row=2, column=0)

        self._win.mainloop()

        

    def start(self):
        self.init_tableau(self._cote.get())
        
        self._win.destroy()
        self._dow = Tk()
        self._dow.title("Grilles_tournantes")
        self._dow.geometry('800x800')
        
        self._board = Canvas(self._dow, width=600, height=600, bg='black')
        self._board.grid(row=0, column=0)
        self._button_load = Button(self._dow, text='Load', command=self.load)
        self._button_load.config(bg="light blue", fg="black", font=("Arial", 8, "bold"), padx=10, pady=5, relief=RAISED)
        self._button_load.place(x=675,y=250)
        self._button_random = Button(self._dow, text='Random', command=self.random)
        self._button_random.config(bg="light blue", fg="black", font=("Arial", 8, "bold"), padx=10, pady=5, relief=RAISED)
        self._button_random.place(x=665,y=285)
        self._button_save = Button(self._dow, text='Save', command=self.save)
        self._button_save.config(bg="light blue", fg="black", font=("Arial", 8, "bold"), padx=10, pady=5, relief=RAISED)
        self._button_save.place(x=675,y=320)
        

        self._text_cipher = Label(self._dow, text="Clear")
        self._text_cipher.place(x=30,y=640)
        self._entry_cipher = Text(self._dow, height=2.5, width= 80, bg ="light cyan")
        self._entry_cipher.place(x=75, y=625)

        self._button_cipher = Button(self._dow, text='Cipher', command=self.cipher)
        self._button_cipher.config(bg="light blue", fg="black", font=("Arial", 8, "bold"), padx=10, pady=5, relief=RAISED)
        self._button_cipher.place(x=300,y=688)
        self._button_decipher = Button(self._dow, text='Decipher', command=self.decipher)
        self._button_decipher.config(bg="light blue", fg="black", font=("Arial", 8, "bold"), padx=10, pady=5, relief=RAISED)
        self._button_decipher.place(x=375,y=688)
        self._button_clear = Button(self._dow, text='Clear', command=self.clear)
        self._button_clear.config(bg="light blue", fg="black", font=("Arial", 8, "bold"), padx=10, pady=5, relief=RAISED)
        self._button_clear.place(x=465,y=688)
        
        self._clock_checkbox = Checkbutton(self._dow, text='Clock',command=self.change_clock)
        self._clock_checkbox.place(x=540,y=689)

        self._text_decipher = Label(self._dow,text="Cipher")
        self._text_decipher.place(x=30,y=750)
        self._entry_decipher = Text(self._dow, height=2.5, width= 80, bg ="light pink")
        self._entry_decipher.place(x=80,y=735)

        self.draw()
        self._dow.mainloop()
    
    def change_clock(self):
        self._clock_variable = 1 - self._clock_variable
        
    def random(self):
        self.init_tableau(self._cote.get())
        self.draw()

    def clear(self):
        self._entry_cipher.delete("1.0", END)
        self._entry_decipher.delete("1.0", END)
        
    def save(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        with open(file_path, 'w') as f:
            for ligne in self.tableau:
                f.write(''.join(map(str, ligne)) + '\n')
        
    def load(self):
        compatible = 0
        liste=[]
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        with open(file_path, 'r') as file:
            lines = file.readlines()  
            for line in lines:
                line = list(line)
                liste.append(line[:-1])
        for i in range(len(liste)):
            for j in range(len(liste[i])):
                if len(liste) != len(liste[i]):
                    compatible += 1
                if liste[i][j] != "0" and liste[i][j] != "1" :
                    compatible += 1 
                else :
                    liste[i][j] = int(liste[i][j])
        if compatible == 0 :
            v = len(liste)
            liste_1=liste
            liste_2=liste
            liste_3=liste
            l=[liste_1, liste_2, liste_3]
            for k in range(3):
                for o in range(k+1):
                    tab = [[0] * v for _ in range(v)]
                    for m in range(v):
                        for n in range(v):
                            tab[n][v-1-m] = l[k][m][n]
                    l[k] = tab
            for p in range(len(liste)):
                for q in range(len(liste)):
                    liste[p][q] += l[0][p][q]
                    liste[p][q] += l[1][p][q]
                    liste[p][q] += l[2][p][q]
                    if liste[p][q] == 1 :
                        pass
                    elif liste[p][q] == 0 and len(liste) % 2 == 1 and p==((len(liste)//2)) and q==((len(liste)//2)):
                        pass
                    else :
                        compatible += 1
        if compatible > 0 :
            messagebox.showerror("Error", "Cette clé n'est pas compatible")
        else :
            messagebox.showinfo("Succes", "La clé est importée !")
            self.tableau=l[2]
            self.rotation_droite()
            self.draw()

        

    def draw(self):
        dim = 500//len(self.tableau)
        for i in range(len(self.tableau)):
            for j in range(len(self.tableau)):
                if self.tableau[i][j]==1:
                    self._board.create_rectangle(50+dim*i, 50+dim*j, 50+dim*(i+1), 50+dim*(j+1), fill='white', outline='light blue')
                else:
                    self._board.create_rectangle(50+dim*i, 50+dim*j, 50+dim*(i+1), 50+dim*(j+1), fill= 'grey', outline='light blue')

    
    def rotation_droite(self):
        n = len(self.tableau)
        tab = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                tab[j][n-1-i] = self.tableau[i][j]
        self.tableau = tab
        
    def rotation_gauche(self):
        n = len(self.tableau)
        tab = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                tab[n-1-j][i] = self.tableau[i][j]
        self.tableau = tab

    
    def init_tableau(self, cote):
        self.tableau=[]
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
        
        a = self._entry_cipher.get("1.0", "end-1c")
        a = list(a)
        code = ""
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
                if self._clock_variable == 0 :
                    self.rotation_gauche()
                elif self._clock_variable == 1 :
                    self.rotation_droite()
            for k in range(len(self.tableau)):
                for l in range(len(self.tableau)):
                    if tab[k][l]!=0:
                        code+=tab[k][l]
        self._entry_decipher.delete("1.0", END)
        self._entry_decipher.insert(END, code)
    
    def decipher(self):
        a = self._entry_decipher.get("1.0", "end-1c")
        a = list(a)
        decode = ""
        while len(a) > 0 :
            tab=[]
            for _ in range(len(self.tableau)):
                tab.append([0] * len(self.tableau))
            for i in range(len(self.tableau)):
                for j in range(len(self.tableau)):
                    if len(a) > 0 :
                        tab[i][j]=a[0]
                        a.pop(0)
            for _ in range(4):
                for k in range(len(tab)):
                    for l in range(len(tab)):
                        if self.tableau[k][l] == 1 and tab[k][l] != 0:
                            decode += tab[k][l]
                if self._clock_variable == 0 :
                    self.rotation_gauche()
                elif self._clock_variable == 1 :
                    self.rotation_droite()
        self._entry_cipher.delete("1.0", END)
        self._entry_cipher.insert(END, decode)
            

Algo()