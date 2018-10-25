# coding: UTF-8

import os
import os.path
import codecs

import json

import datetime

from cherrypy import log

#----------------------------------------------------------
class Database_cl(object):
#----------------------------------------------------------
    def __init__(self):
        #Datenmodell instanziieren
        self.data_o = None
        self.readData_p()


    def delete_px(self, id):
        for value in self.data_o:
            if int(id) == int(value['id']):        
                self.data_o.remove(value)
                
        self.saveData_p()
                
        return str(id)

    # Datensatz nach dem letzten Element hinzufügen
    def update_px(self, id, data_opl):
        # format for curl
        if type(data_opl['tag'] is str):
            data_opl['tag'] = data_opl['tag'].replace('[', '')
            data_opl['tag'] = data_opl['tag'].replace(']', '')
            data_opl['tag'] = data_opl['tag'].replace('\'', '')
            data_opl['tag'] = data_opl['tag'].split(', ')        
        
        #datum
        now = datetime.datetime.now()
        currentDate = now.strftime("%d.%m.%Y")        
        
        
        for value in self.data_o:
            if int(id) == int(value['id']):
                value['title'] = data_opl['title']
                value['chdat'] = currentDate
                value['change'] = int(value['change']) + 1
                value['tag'] = data_opl['tag']
        
        self.saveData_p()
        
        return str(data_opl['id'])



    # Datensatz nach dem letzten Element hinzufügen
    def create_px(self, data_opl):
        # format for curl
        if type(data_opl['tag'] is str):
            data_opl['tag'] = data_opl['tag'].replace('[', '')
            data_opl['tag'] = data_opl['tag'].replace(']', '')
            data_opl['tag'] = data_opl['tag'].replace('\'', '')
            data_opl['tag'] = data_opl['tag'].split(',')
        
        id_s = len(self.data_o)
        
        #datum
        now = datetime.datetime.now()
        currentDate = now.strftime("%d.%m.%Y")
        
        data_add = {}
        
        data_add['id'] = id_s
        data_add['title'] = data_opl['title']
        data_add['crdat'] = currentDate
        data_add['chdat'] = currentDate
        data_add['change'] = 0
        data_add['tag'] = data_opl['tag']        
        
        self.data_o.append(data_add)
        
        self.saveData_p()
        
        return str(id_s)
       
    #-------------------------------------------------------
    def read_px(self, id_spl = None):
    #-------------------------------------------------------
        self.readData_p()
        
        if id_spl == None:
            return self.data_o
        else:
            # else: return article with id
            for value in self.data_o:
                if int(id_spl) == int(value['id']):
                    return value
            
            return -1
    
    def readData_p(self):
        try:
            fp_o = codecs.open(os.path.join('data', 'artikel.json'), 'r', 'utf-8')
        except:
            # Bei Exception Datei neu anlegen
            self.data_o = {}
            self.data_o[0] = ['', '', '']
            self.saveData_p()
        else:
            with fp_o:
                self.data_o = json.load(fp_o)
    
        return
    def saveData_p(self):
        with codecs.open(os.path.join('data', 'artikel.json'), 'w', 'utf-8') as fp_o:
            json.dump(self.data_o, fp_o)
# EOF
