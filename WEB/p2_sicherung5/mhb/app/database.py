# coding: utf-8

import os
import os.path
import codecs

import json

#----------------------------------------------------------
class Database_cl(object):
#----------------------------------------------------------
    #IdVergabe
    id_s = 0    
    # da es hier nur darum geht, die Daten dauerhaft zu speichern,
    # wird ein sehr einfacher Ansatz verwendet:
    # - es können Daten zu genau 15 Teams gespeichert werden
    # - je Team werden 2 Teilnehmer mit Namen, Vornamen und Matrikelnummer
    # berücksichtigt
    # SOWIE ALS Ergänzung: Semesterzahl!
    # - die Daten werden als eine JSON-Datei abgelegt
    
    #-------------------------------------------------------
    def __init__(self):
    #-------------------------------------------------------
        self.data_o = None #Liste für Studiengänge
        self.data_b = None #Liste für Benutzer
        self.data_l = None #Liste für Lehrveranstaltungen
        self.data_m = None #Liste für Module
        self.readData_p()  #Filestream für Data_o --> studiengaenge.json
        self.readData_benutzer_p() #Filestream für Data_b --> benutzer.json
        self.readData_lehrveranstaltungen_p() #Filestream für Data_l --> lehrveranstaltungen.json
        self.readData_module_p() #Filestream für Data_l --> lehrveranstaltungen.json
    #-------------------------------------------------------
    def create_px(self, data_opl):
    #-------------------------------------------------------
        # Überprüfung der Daten müsste ergänzt werden!

        # 'freien' Platz suchen,
        # falls vorhanden: belegen und Nummer des Platzes als Id zurückgeben
        #---Länge der Daten aus der studiengaenge.json ermitteln und zurückgeben   
        id_s = None
        data_o_len = self.data_o.__len__()
        id_s = str(data_o_len)
            
        for i in range(0, data_o_len):
            if str(i) not in self.data_o:
                id_s = str(i)
                break
        
        #for i in range(0, data_o_len):
        #    if data_opl[0] == self.data_o[str(i)][0]:
        #        return "Studiengang bereits vorhanden!"
    
        self.data_o[id_s] = data_opl
        self.saveData_p()        
        
        return id_s

    #-------------------------------------------------------
    def create_module_px(self, data_opl):
    #-------------------------------------------------------
        # Überprüfung der Daten müsste ergänzt werden!

        # 'freien' Platz suchen,
        # falls vorhanden: belegen und Nummer des Platzes als Id zurückgeben
        #---Länge der Daten aus der studiengaenge.json ermitteln und zurückgeben   
        id_s = None
        data_m_len = self.data_m.__len__()
        id_s = str(data_m_len)
            
        for i in range(0, data_m_len):
            if str(i) not in self.data_m:
                id_s = str(i)
                break
        
        #for i in range(0, data_o_len):
        #    if data_opl[0] == self.data_o[str(i)][0]:
        #        return "Studiengang bereits vorhanden!"
    
        self.data_m[id_s] = data_opl
        self.saveData_module_p()        
        
        return id_s
    
    #-------------------------------------------------------
    def create_lehrveranstaltungen_px(self, data_opl):
    #-------------------------------------------------------
        # Überprüfung der Daten müsste ergänzt werden!

        # 'freien' Platz suchen,
        # falls vorhanden: belegen und Nummer des Platzes als Id zurückgeben
        #---Länge der Daten aus der studiengaenge.json ermitteln und zurückgeben   
        id_s = None
        data_l_len = self.data_l.__len__()
        id_s = str(data_l_len)
            
        for i in range(0, data_l_len):
            if str(i) not in self.data_l:
                id_s = str(i)
                break
        
        #for i in range(0, data_o_len):
        #    if data_opl[0] == self.data_o[str(i)][0]:
        #        return "Studiengang bereits vorhanden!"
    
        self.data_l[id_s] = data_opl
        self.saveData_lehrveranstaltungen_p()        
        
        return id_s
    
    #-------------------------------------------------------
    def read_px(self, id_spl = None):
    #-------------------------------------------------------
        # hier zur Vereinfachung:
        # Aufruf ohne id: alle Einträge liefern
        data_o = None
        if id_spl == None:
            data_o = self.data_o
        else:
            if id_spl in self.data_o:
                data_o = self.data_o[id_spl]
        
        return data_o
    
    #-------------------------------------------------------
    def read_benutzer_px(self, id_spl = None):
    #-------------------------------------------------------
        # Read-Funktion für Benutzer
        data_b = None
        if id_spl == None:
            data_b = self.data_b
        else:
            if id_spl in self.data_b:
                data_b = self.data_b[id_spl]
        
        return data_b    
    
    #-------------------------------------------------------
    def read_lehrveranstaltungen_px(self, id_spl = None):
    #-------------------------------------------------------
        # Read-Funktion für Lehrveranstaltungen
        data_l = None
        if id_spl == None:
            data_l = self.data_l
        else:
            if id_spl in self.data_l:
                data_l = self.data_l[id_spl]
            else: #----> hier bearbeitet
                data_l = self.data_l
        
        return data_l

    #-------------------------------------------------------
    def read_module_px(self, id_spl = None):
    #-------------------------------------------------------
        # Read-Funktion für Benutzer
        data_m = None
        if id_spl == None:
            data_m = self.data_m
        else:
            if id_spl in self.data_m:
                data_m = self.data_m[id_spl]
        
        return data_m
    
    #-------------------------------------------------------
    def update_px(self, id_spl, data_opl):
    #-------------------------------------------------------
        # Überprüfung der Daten müsste ergänzt werden!
        status_b = False
        if id_spl in self.data_o:
            self.data_o[id_spl] = data_opl
            self.saveData_p()
            status_b = True

        return status_b

    #-------------------------------------------------------
    def update_module_px(self, id_spl, data_opl):
    #-------------------------------------------------------
        # Überprüfung der Daten müsste ergänzt werden!
        status_b = False
        if id_spl in self.data_m:
            self.data_m[id_spl] = data_opl
            self.saveData_module_p()
            status_b = True

        return status_b
    
    #-------------------------------------------------------
    def update_lehrveranstaltungen_px(self, id_spl, data_opl):
    #-------------------------------------------------------
        # Überprüfung der Daten müsste ergänzt werden!
        status_b = False
        if id_spl in self.data_l:
            self.data_l[id_spl] = data_opl
            self.saveData_lehrveranstaltungen_p()
            status_b = True

        return status_b    
        
    #-------------------------------------------------------
    def delete_px(self, id_spl):
    #-------------------------------------------------------
        #Löschvorgang für Studiengaenge
        status_b = False
        if id_spl in self.data_o:
           # pass
           # hier müssen Sie den Code ergänzen
           # Löschen als Zurücksetzen auf die Default-Werte implementieren
           # Ihre Ergänzung
           # self.data_o[id_spl] = ['', '', '', '']
           # self.saveData_p()
           # status_b = True

            del self.data_o[id_spl]
            self.saveData_p()
            status_b = True 
            
        return status_b
   
    #-------------------------------------------------------
    def delete_m_px(self, id_spl):
    #-------------------------------------------------------
        #Löschvorgang für Studiengaenge
        status_b = False
        if id_spl in self.data_m:
           # pass
           # hier müssen Sie den Code ergänzen
           # Löschen als Zurücksetzen auf die Default-Werte implementieren
           # Ihre Ergänzung
           # self.data_o[id_spl] = ['', '', '', '']
           # self.saveData_p()
           # status_b = True

            del self.data_m[id_spl]
            self.saveData_p()
            status_b = True 
            
        return status_b
    
    #-------------------------------------------------------
    def delete_lv_px(self, id_spl):
    #-------------------------------------------------------
        #Löschvorgang für Studiengaenge
        status_b = False
        if id_spl in self.data_l:
           # pass
           # hier müssen Sie den Code ergänzen
           # Löschen als Zurücksetzen auf die Default-Werte implementieren
           # Ihre Ergänzung
           # self.data_o[id_spl] = ['', '', '', '']
           # self.saveData_p()
           # status_b = True

            del self.data_l[id_spl]
            self.saveData_p()
            status_b = True 
            
        return status_b
        
            
    #-------------------------------------------------------
    def getDefault_px(self):
    #-------------------------------------------------------
        return ['', '', '', '', self.getDefault_lehrveranstaltungen_px] 
    # 4 Felder für Studiengänge
    
    #-------------------------------------------------------
    def getDefault_lehrveranstaltungen_px(self):
    #-------------------------------------------------------
        return ['', '', '', '', ''] 
    # 3 Felder für Lehrveranstaltungen    

    #-------------------------------------------------------
    def getDefault_module_px(self):
    #-------------------------------------------------------
        return ['', '', '', '', '', '', '', '', ''] 
    # 7 Felder für Lehrveranstaltungen
    
    #-------------------------------------------------------
    def readData_p(self):
    #-------------------------------------------------------
        try:
            fp_o = codecs.open(os.path.join('data', 'studiengaenge.json'), 'r', 'utf-8')
        except:
            # Datei neu anlegen
            self.data_o = {}
            self.saveData_p()
        else:
            with fp_o:
                self.data_o = json.load(fp_o)
    #-------------------------------------------------------
    def readData_benutzer_p(self):
    #-------------------------------------------------------
        try:
            fp_o = codecs.open(os.path.join('data', 'benutzer.json'), 'r', 'utf-8')
        except:
            # Datei neu anlegen
            self.data_b = {}
            self.saveData_p()
        else:
            with fp_o:
                self.data_b = json.load(fp_o)

    #-------------------------------------------------------
    def readData_lehrveranstaltungen_p(self):
    #-------------------------------------------------------
        try:
            fp_o = codecs.open(os.path.join('data', 'lehrveranstaltungen.json'), 'r', 'utf-8')
        except:
            # Datei neu anlegen
            self.data_l = {}
            self.saveData_lehrveranstaltungen_p()
        else:
            with fp_o:
                self.data_l = json.load(fp_o)                
    #-------------------------------------------------------
    def readData_module_p(self):
    #-------------------------------------------------------
        try:
            fp_o = codecs.open(os.path.join('data', 'module.json'), 'r', 'utf-8')
        except:
            # Datei neu anlegen
            self.data_m = {}
            self.saveData_module_p()
        else:
            with fp_o:
                self.data_m = json.load(fp_o)    
    
    #-------------------------------------------------------
    def saveData_p(self):
    #-------------------------------------------------------
        with codecs.open(os.path.join('data', 'studiengaenge.json'), 'w', 'utf-8')as fp_o:
            json.dump(self.data_o, fp_o, sort_keys=True)
     
    #-------------------------------------------------------
    def saveData_benutzer_p(self):
    #-------------------------------------------------------
        with codecs.open(os.path.join('data', 'benutzer.json'), 'w', 'utf-8')as fp_b:
            json.dump(self.data_b, fp_b, sort_keys=True)
    
    #-------------------------------------------------------
    def saveData_lehrveranstaltungen_p(self):
    #-------------------------------------------------------
        with codecs.open(os.path.join('data', 'lehrveranstaltungen.json'), 'w', 'utf-8')as fp_l:
            json.dump(self.data_l, fp_l, sort_keys=True)
            
    #-------------------------------------------------------
    def saveData_module_p(self):
    #-------------------------------------------------------
        with codecs.open(os.path.join('data', 'module.json'), 'w', 'utf-8')as fp_m:
            json.dump(self.data_m, fp_m, sort_keys=True)               
# EOF