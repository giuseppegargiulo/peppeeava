<<<<<<< HEAD
from itertools import count
=======
from math import perm
>>>>>>> e5aa32a38e3fc836c9189b16a594c8e0a7027c49
from multiprocessing.connection import wait
from guizero import *
from tkinter import *
import random
import string
from setuptools import Command
from utils import *
from logzero import logger, logfile
from datetime import datetime, timedelta
from itertools import permutations
#INIZIALIZZAZIONE

n = 10 
lettere = string.ascii_lowercase
stringa = ''.join((random.choice(lettere) for x in range(n)))

anagrammi = 0

def crea_lista():
    it = 'words.italian.txt'
    f = open(it, 'r')
    line = f.readline()
    valore_stringa = False

    for line in f:

        if anagrammi == line[:-1]:
            
            valore_stringa = True
    

tempo = 0


#APPLICAZIONE
app = App(title = "Ruzz Lightyear", width=1920, height=1080)

bg = PhotoImage(file='peppeeava/bg.png')
label = Label(app.tk, image=bg)
label.place(x=0, y=0)
app.full_screen = True


#INTERFACCE
locale_schermata = Window(app, title= 'Locale', width=1920, height=1080, visible= False)

label_locale = Label(locale_schermata.tk, image=bg)
label_locale.place(x=0, y=0)

locale_schermata.full_screen = True

classifica_schermata = Window(app, title = 'Classifica', width = 1920, height = 1080, visible = False)
label_classifica = Label(classifica_schermata.tk, image=bg)
label_classifica.place(x = 0, y = 0)

classifica_schermata.full_screen = True

campagna_schermata = Window(app, title='Campagna', width=1920, height=1080, visible= False)
label_campagna = Label(campagna_schermata.tk, image=bg)
label_campagna.place(x=0, y=0)

campagna_schermata.full_screen = True

gioca_schermata = Window(app, title="Gioca", width=1920, height=1080, visible = False)
label_gioca = Label(gioca_schermata.tk, image=bg)
parola_gioca = Label(text= "GIOVANNI")
label_gioca.place(x=0, y=0)

gioco_finito = Window(app, title="Gioco finito", width=1920, height=1080, visible= False)
label_finito = Label(gioco_finito.tk, image=bg)
label_finito.place(x=0, y=0)
gioco_finito.full_screen = True




#PULSANTI
def classifica_function():
    classifica_schermata.show()
    

def esci_function():
    app.destroy()

def locale_function():
    locale_schermata.show()
    

def campagna_function():
    #campagna_schermata.show()
    app.warn("Modalità in sviluppo...", "Questa modalità di gioco è ancora in modalità di sviluppo. Torna presto per provarla!")

def chiudi_locale():
    locale_schermata.visible = False
    

def chiudi_campagna():
    campagna_schermata.visible = False
    

def chiudi_classifica():
    classifica_schermata.visible = False

<<<<<<< HEAD

def gioca_chiudi():
    gioca_schermata.visible = False


def timer(count):
    gioca_schermata.show()
=======
def timer():
    gioca_schermata.show()
    start_time = datetime.time(0, 0, 0)
    now_time = datetime.time(0, 0, 0)
    while (now_time < start_time + timedelta(seconds=120)):
>>>>>>> e5aa32a38e3fc836c9189b16a594c8e0a7027c49
    
    label['text']= count

    if count > 0:
       gioca_schermata.after(1000, timer, count-1)
        
label = Label(gioca_schermata.tk, font=('Helvetica', 48), fg= 'white')
label.place(x= 1600, y=1000)


locale = PushButton(app, image='peppeeava/locale.png', command=locale_function)
campagna = PushButton(app, image='peppeeava/campagna.png', command=campagna_function)
classifica = PushButton(app, image = 'peppeeava/classifica.png', command = classifica_function)
esci = PushButton(app, image='peppeeava/esci.png', command=esci_function)

locale_esci = PushButton(locale_schermata, command = chiudi_locale, image='peppeeava/esci.png')

#campagna_esci = PushButton(campagna_schermata, command = chiudi_campagna, image='peppeeava/esci.png')

gioca_locale = PushButton(locale_schermata, image='peppeeava/gioca.png', command =timer(120))

<<<<<<< HEAD
gioca_esci = PushButton(gioca_schermata, image = 'peppeeava/esci.png', command = gioca_chiudi)

classifica_esci = PushButton(classifica_schermata, command = chiudi_classifica, image='peppeeava/esci.png', pady = 0)
=======
classifica_esci = PushButton(classifica_schermata, command = chiudi_classifica, image='peppeeava/esci.png')
>>>>>>> e5aa32a38e3fc836c9189b16a594c8e0a7027c49

################################### parte funzionale
def listaparole(parola):
    ls=list(parola)
    k=len(parola)
    r=[]
    dd=[]
    for i in ls:
        a= permutations(ls,k)
        r.append(a)
        k-=1
        for z in r:
            for o in z:
                for c in o:
                    dd.append(c)

app.display()