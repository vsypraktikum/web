'''
Created on 17.11.2017

@author: johannes
'''
import os 
import os.path 
import codecs
import json
import string
import cherrypy

from .database import Database_cl 
from .view import View_cl
from enum import Enum

from __main__ import name
class Mitarbeiter(object):
    name = ' '
    vorname = ' '
    akadem = ' '
    taetigkeit = ' '
    
    def MA(self):
        pass

class Weiterbildung(object):
    bezeichnung = ' '
    von = ' '
    bis = ' '
    beschreibung = ' '              #txt = string?
    maximale = ' '                  #int = string?
    minimale = ' '                  #int = string?
    
    def WB(self):
        pass
    
class Teilnahme(Enum):
    angemeldet = 1
    nimmtteil = 2
    storniert = 3
    angebrochen = 4
    nichterfolgreich = 5
    erfolgreich = 6
    
    def TN(self):
        pass
    
class Zertifikat(object):
    bezeichnung = ' '
    beschreibung = ' '              #txt = string?
    berechtigung = ' '
    
    def ZF(self):
        pass

class Qualifikation(object):
    bezeichnung = ' '
    beschreibung = ' '              #txt = string?
    
    def QA(self):
        pass
    
    
#Dateioperation, von python in json
#irgendwas stimmt mit eclipse noch nicht 
    
   
    
    
    
