import os, sys
import subprocess as psh
from tkinter import *


class Cisco (Frame) :
    Repertoire = os.path.dirname(os.path.abspath(__file__))
    
    __fichier = ""
    
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        # self.controller = controller
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.create_widgets()
        
    def __restart__(self) :
        USER = os.getlogin()
        self.__programme = os.path.abspath(__file__)
        psh.Popen(
            [ f"C:/Users/{USER}/AppData/Local/Microsoft/WindowsApps/python3.13.exe",
             f"{self.__programme}"
             ]
        )
        sys.exit()
        
    def menuChoix(self) :
        couleur = "brown"
        self.MenuUP = LabelFrame(bg=couleur)
        self.MenuUP.grid(row=0, column=0, columnspan=50, sticky="new")
        for i in range(5) :
            self.MenuUP.columnconfigure(i, weight=1)

        
        self.Option0 = Button(self.MenuUP,text="🧭NewFile", command=self.fenetreNom, bd=0, bg=couleur, fg="white")
        self.Option0.grid(row=0, column=0, sticky=NW)

        self.Option1 = Button(self.MenuUP,text="Enregistrer", command=self.fenetreNom, bd=0, bg=couleur, fg="white")
        self.Option1.grid(row=0, column=1, sticky=NW)

        self.Option2 = Button(self.MenuUP,text="♻️Redemarrer", command=self.__restart__, bd=0, bg=couleur, fg="white")
        self.Option2.grid(row=0, column=2, sticky=NW)
        
        self.Option2 = Button(self.MenuUP,text="♻️Quitter", command=self.quit, bd=0, bg=couleur, fg="white")
        self.Option2.grid(row=0, column=3, sticky=NW)

    def create_widgets(self) :
        self.menuChoix()
        
        self.options = LabelFrame(width=500, height=500, bg="grey", bd=0)
        self.options.grid(row=2, column=0, rowspan=15, padx=10, sticky="nsw")
        ligne = 2; padligne = 6
        liste_fichiers = os.listdir(self.Repertoire)  
        liste_fichiers = [f for f in liste_fichiers if os.path.isfile(os.path.join(self.Repertoire, f))]     
        for i, titre in enumerate(liste_fichiers) :
            self.option_button(text=f"{titre}", bg="darkred", width=10, command=lambda val=f"{self.Repertoire}/{titre}": self.LireFile(val), row=ligne+i, col=1, sticky="nw",
                        textop="open", bcg="#C19A6B", widths=3, commands=lambda val=f"{self.Repertoire}/{titre}": self.OuvrirFile(val), rows=ligne+i, cols=2, padxs=10, padys=padligne)
        
        # --------------------------------------------------------------------------------------
        self.terminal = LabelFrame(width=500, height=500, bd=0)
        self.terminal.grid(row=2, column=8, padx=10, rowspan=8, sticky="ne")
        # insert sert au curseur, # insertbackground sert a la couleur du curseur, insertontime sert a l'intervalle d'affichage du curseur, # insertofftime sert a l'intervalle d'affichage du curseur
        self.aff1 = Text(self.terminal, bg="black", fg="white", cursor="xterm", insertbackground="white", insertwidth=2, insertontime=600, insertofftime=300)
        self.aff1.focus_set()
        self.aff1.grid(row=2, column=8, rowspan=8, sticky="ne")
        # --------------------------------------------------------------------------------------
        self.terminal2 = LabelFrame(width=500, height=500, bd=0)
        self.terminal2.grid(row=2, column=8, padx=10, pady=400, rowspan=8, sticky="se")
        
        self.aff2 = Text(self.terminal2, bg="black", fg="white", cursor="xterm", insertbackground="white", insertwidth=2, insertontime=600, insertofftime=300)
        self.aff2.grid(row=18, column=8, rowspan=8, sticky="se")
        
        self.aff1.bind("<Button-3>", lambda event: self.afficher_menu_contextuel(objet=self.aff1, event=event))
        self.aff2.bind("<Button-3>", lambda event: self.afficher_menu_contextuel(objet=self.aff2, event=event))


    def option_button(self, text="", bg="black", fg="white", width=1, height=1, command="", row=0, col=0, rowspan=1, 
                      columnspan=1, sticky="", padx=0, pady=0, textop="", bcg="black", fcg="white",
                      widths=1, heights=1, commands="", rows=0, cols=0, padxs=0, padys=0) :
        self.label1 = Button(self.options, text=text, bg=bg, width=width, fg=fg, command=command)
        self.label1.grid(row=row, column=col, rowspan=rowspan, pady=pady, sticky=sticky)
        self.label1_open = Button(self.options, text=textop, bg=bcg, width=widths, fg=fcg, command=commands)
        self.label1_open.grid(row=rows, column=cols, padx=padxs, pady=padys)
    
    def fenetreNom(self):
        self.askNom = Toplevel(background="blue", bd=0)
        self.askNom.geometry("300x100")
        self.askNom.title("Creation de fichiers")
        self.askNom.columnconfigure(0, weight=1)
        self.label_nom = Label(self.askNom, text="Entrez le nom du fichier", bg="blue", fg="white")
        self.label_nom.grid(row=0, column=0, padx=10, pady=2, sticky="nsew", columnspan=2)
        self.entry_nom = Entry(self.askNom, bg="black", fg="white", width=50, cursor="xterm", insertbackground="white", insertwidth=2, insertontime=600, insertofftime=300)
        self.entry_nom.grid(row=1, column=0, padx=10, pady=2, sticky="nsew", columnspan=2)
        
        self.bouton_valider = Button(self.askNom, text="Valider", command=self.get_exec, width=10, bg="green", fg="white")
        self.bouton_valider.grid(row=2, column=0, pady=10)
        self.bouton_clear = Button(self.askNom, text="Effacer", command=lambda: self.effacer_entree(self.entry_nom))
        self.bouton_clear.grid(row=2, column=1, padx=20, pady=10)
        
    def get_exec(self) :
        fichierNom = self.entry_nom.get()
        print(f"{self.Repertoire}\\{fichierNom}"); print(fichierNom)
        self.creerFile(f"{self.Repertoire}\\{fichierNom}")
        if fichierNom != "" and os.path.exists(f"{self.Repertoire}\\{fichierNom}") :
            self.OuvrirFile(f"{self.Repertoire}\\{fichierNom}")

    def copier_selection(self, objet, event=None):
        try: 
            # copie la sélection dans le presse-papier
            self.clipboard_clear()
            if objet.selection_get() != "":
                # si la sélection n'est pas vide
                self.clipboard_append(objet.selection_get())
        except TclError:
            pass # rien sélectionné
        
    def couper_selection(self, objet, event=None):
        try: 
            # couper la sélection dans le presse-papier
            self.clipboard_clear()
            if objet.selection_get() != "":
                # si la sélection n'est pas vide
                self.clipboard_append(objet.selection_get())
                objet.delete("sel.first", "sel.last")
        except TclError:
            pass # rien sélectionné
        
    def coller_selection(self, objet, event=None):
        try: 
            # copie la sélection dans le presse-papier
            recup = self.clipboard_get()
            objet.insert(INSERT, recup)
        except TclError:
            pass # rien sélectionné
        
    def all_selection(self, objet, event=None):
        try: 
            # copie la sélection dans le presse-papier
            objet.tag_add(SEL, "1.0", END)
        except TclError:
            pass # rien sélectionné
    def tout_effacer(self, objet, event=None):
        try: 
            # copie la sélection dans le presse-papier
            objet.delete("1.0", END)
        except TclError:
            pass
    
    def effacer_entree(self, objet):
        objet.delete(0, END)
        objet.insert(0, "")
        objet.focus_set()        

    def afficher_menu_contextuel(self, objet, event):
        menu_clic_droit = Menu(self, tearoff=0)
        menu_clic_droit.add_command(label="Couper", command=lambda: self.couper_selection(objet=objet))
        menu_clic_droit.add_command(label="Copier", command=lambda: self.copier_selection(objet=objet))
        menu_clic_droit.add_command(label="Coller", command=lambda: self.coller_selection(objet=objet))
        menu_clic_droit.add_command(label="Sélectionner tout", command=lambda: self.all_selection(objet=objet))
        menu_clic_droit.add_command(label="Tout effacer", command=lambda: self.tout_effacer(objet=objet))
        menu_clic_droit.add_command(label="Nouveau", command=self.fenetreNom)
        menu_clic_droit.add_command(label="Rajouter", command=self.enregistrerFile)
        menu_clic_droit.add_command(label="Réécrire", command=self.reecrireFile)
        menu_clic_droit.tk_popup(event.x_root, event.y_root)
        
    def LireFile(self, fichier) :
        with open(fichier, 'r') as read :
            print(f"{fichier} en cours de lecture")
            info = read.read()
            print(info)
            print("-" * 20)
            self.aff2.delete("1.0", END)
            self.aff2.insert("1.0", info)
        self.set_fichier(fichier)

    def creerFile(self, fichier) :
        try :
            if not os.path.exists(fichier):
                with open(fichier, 'w') as write :
                    print(f"{fichier} a été créé")
                    content = f"\n{self.aff1.get("1.0", END)}"
                    write.write(content)
            else :
                with open(fichier, 'a') as edit :
                    content = f"\n{self.aff1.get("1.0", END)}"
                    edit.write(content)
                self.label_nom = Label(self.askNom, text="Existe deja ! Sauvegarde...", bg="blue", fg="Green")
                self.label_nom.grid(row=0, column=0, padx=10, pady=2, sticky="nsew", columnspan=2)
        except Exception as e:
            print(f"Erreur lors de l'ouverture de {fichier} : {e}")
            self.label_nom = Label(self.askNom, text=f"{e} !", bg="blue", fg="red")
            self.label_nom.grid(row=0, column=0, padx=10, pady=2, sticky="nsew", columnspan=2)
    
    def enregistrerFile(self) :
        if os.path.exists(self.get_fichier()):
            with open(self.get_fichier(), 'a') as edit:
                content = f"\n{self.aff2.get("1.0", END)}"
                edit.write(content)
                print(f"{self.get_fichier()} a été enregistré")
                
    def reecrireFile(self) :
        if os.path.exists(self.get_fichier()):
            with open(self.get_fichier(), 'w') as edit:
                content = f"\n{self.aff2.get("1.0", END)}"
                edit.write(content)
                print(f"{self.get_fichier()} a été réécrit")

    def supprimerFile(self, fichier) :
        if os.path.exists(fichier) :
            os.remove(fichier)
            print(f"{fichier} a été supprimé")
        else :
            print(f"{fichier} n'existe pas")
    
    def renommerFile(self, fichier, nouveau_nom) :
        if os.path.exists(fichier) :
            os.rename(fichier, nouveau_nom)
            print(f"{fichier} a été renommé en {nouveau_nom}")
        else :
            print(f"{fichier} n'existe pas")
            
    def OuvrirFile(self, fichier) :
        try :
            os.startfile(fichier)
        except Exception as e:
            print(f"Erreur lors de l'ouverture de {fichier} : {e}")
            self.label_nom = Label(self.askNom, text="Fichier introuvable !", bg="blue", fg="red")
            self.label_nom.grid(row=0, column=0, padx=10, pady=2, sticky="nsew", columnspan=2)

    def get_fichier(self):
        # Cette méthode pourrait être utilisée pour obtenir le nom du fichier actuellement ouvert
        return self.__fichier
    def set_fichier(self, fichier):
        # Cette méthode pourrait être utilisée pour définir le nom du fichier actuellement ouvert
        self.__fichier = fichier
        # Vous pourriez également mettre à jour l'interface utilisateur ici, par exemple :
        # self.label_fichier.config(text=f"Fichier ouvert : {self.__fichier}")

# command=lambda val=True: self.(val)

root = Tk()
root.config(bg="grey")
root.geometry("800x850")
root.title("Cisco")
app = Cisco(root)
app.mainloop()
