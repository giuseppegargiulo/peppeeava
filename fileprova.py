from ast import Pass
from math import perm
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
import redis
from random import *

def listaparole(parola_gioca):
    ls=list(parola_gioca)
    k=len(parola_gioca)
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

def assegnazionescore(parola_utente):
    prl= parola_utente
    lgprl=len(prl)
    if lgprl == 1:
        pass
    if lgprl == 2:
        pass
    if lgprl == 3:
        pass
    if lgprl == 4:
        pass
    if lgprl == 5:
        pass
    if lgprl == 6:
        pass


    

##parte di redis


r = redis.StrictRedis(host='localhost', port=6379, db=0)

# inizializzo la lista delle chiavi del DB
r.keys()

# carichiamo tutte le parole all'interno del DB.

it = "words.italian.txt"
f = open(it, 'r')
line = f.readline()


'''
 La struttura dati che ottimizza la gestione di un insieme di valore è
 il SET, un insieme non ordinato di elementi che non possono essere ripetuti.
'''

# r.scard(it) restituisce la dimensione dell'insieme 'it'
# r.smembers(it) restituisce gli elementi dell'inskeme 'it'
# r.sismember(it,'parola') restituisce 1 se 'parola' è presente nell'insieme IT altrimenti 0

def insCanc():
    
    if(r.scard(it)>0):
        for i in range(r.scard(it)):  # per ogni riga del file vengono eseguite le righe di codice che seguono
                r.spop(it)
                print(r.scard(it))

    else:
        for line in f:  # per ogni riga del file vengono eseguite le righe di codice che seguono
            r.sadd(it, line[:-1])
            print(line[:-1])
            print(r.scard(it))

        
def cerca():
    str = listaparole("cia")
    risultato = r.sismember(it,str)
    print(it)

    if (risultato):
        print("trovato!")
    else: print("non trovato!")



if __name__ == '__main__': 
    
    avanti = True

    while(avanti):
        op = int(input("\n\ncosa vuoi fare?\n 1) inserisci/cancella\n 2) cerca\n 3) chiudi\n"))

        if (op==1):
            insCanc()
            
        elif(op==2):
            cerca()

        elif(op==3):
            avanti = False

    print("\n\nciao!")