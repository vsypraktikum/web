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

from enum import Enum

def __init__(self): 
    
    pass

class Mitarbeiter(object):
    
    
    def createMitarbeiter_E(self, data_opl):
        markup_s = '' 
        markup_s += self.readFile_p('list0.tpl')
        
        markupV_s = self.readFile_p('list1.tpl') 
        lineT_o = string.Template(markupV_s) 
        # mehrfach nutzen, um die einzelnen Zeilen der Tabelle zu erzeugen 
        for id_s in data_opl: 
            data_a = data_opl[str(id_s)] 
            markup_s += lineT_o.safe_substitute (name=data_a[0] # HIER müssen Sie eine Ergänzung vornehmen - erl
            ,   vorname=data_a[1] 
            ,   akagra=data_a[2]
            ,   taetigkeit=data_a[3] 
            )
        markup_s += self.readFile_p('list2.tpl')
        
        return self.create_p('liste.tpl', data_opl) #markup_s 
        
class Weiterbildung(object):
    bz_w = ' '
    von = ' '
    bis = ' '
    bs_w = ' '                      #txt = string?
    max = ' '                  #int = string?
    min = ' '                  #int = string?
    
    def WB(self):
        pass
    
class Teilnahme(Enum):
    angemeldet = 1
    nimmtteil = 2
    storniert = 3
    abgebrochen = 4
    nichterfolgreich = 5
    erfolgreich = 6
    
    def TN(self):
        pass
    
class Zertifikat(object):
    bz_z = ' '
    bs_z= ' '              #txt = string?
    berechtigung = ' '
    
    def ZF(self):
        pass

class Qualifikation(object):
    bz_q = ' '
    bs_q = ' '              #txt = string?
    
    def QA(self):
        pass
    
#EoF
    
    

    
   
    
    
    
