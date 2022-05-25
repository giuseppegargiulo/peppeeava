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
            
            dd.append(o)
            print (dd)

listaparole("cia")