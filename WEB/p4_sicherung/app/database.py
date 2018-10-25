# coding: utf-8

import os
import os.path
import codecs

import json

#----------------------------------------------------------
class Database_cl(object):
#----------------------------------------------------------

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      #self.type_s = type_spl
      #self.path_s = os.path.join('data', type_spl)     
      self.data_o = None #Liste
      self.dataID_o = None
      self.readData_p()  #Filestream für Data_o --> .json
      self.readDataID_p()
   
   #-------------------------------------------------------
   def create_px(self, data_opl):
   #-------------------------------------------------------

      self.getNewID_p()
      id_s = str(self.dataID_o)

      self.data_o[id_s] = data_opl
      self.saveData_p()        

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
         #id_i = int(id_spl)
         for i in range(len(self.data_o)):
            if id_spl in self.data_o[i]["id"]:
               data_o = self.data_o[i]
               
      return data_o   
   
   #-------------------------------------------------------
   def readData_p(self):
   #-------------------------------------------------------
      try:
         fp_o = codecs.open(os.path.join('data', 'topics.json'), 'r', 'utf-8')
      except:
         # Datei neu anlegen
         self.data_o = []
         self.saveData_p()
         pass
      else:
         with fp_o:
            self.data_o = json.load(fp_o)    
   
   #-------------------------------------------------------
   def readDataID_p(self):
   #-------------------------------------------------------
      try:
         fp_id = codecs.open(os.path.join('data', 'ID.json'), 'r', 'utf-8')
      except:
         # Datei neu anlegen
         self.dataID_o = 0
         self.saveDataID_p()
      else:
         with fp_id:
            self.dataID_o = json.load(fp_id)   
   
   #-------------------------------------------------------
   def saveData_p(self):
   #-------------------------------------------------------
      with codecs.open(os.path.join('data', 'topics.json'), 'w', 'utf-8')as fp_o:
         json.dump(self.data_o, fp_o, sort_keys=True)   
   
   #-------------------------------------------------------
   def saveDataID_p(self):
   #-------------------------------------------------------
      with codecs.open(os.path.join('data', 'ID.json'), 'w', 'utf-8') as fp_id:
         json.dump(self.dataID_o, fp_id)       
   
   #-------------------------------------------------------
   def getDefault_px(self):
   #-------------------------------------------------------
      return {
         'bezeichnung': ''
      }
   
   #-------------------------------------------------------
   def getNewID_p(self):
   #-------------------------------------------------------
      tmpID = None
      self.tmpID = self.dataID_o
      self.dataID_o = self.tmpID + 1
      self.saveDataID_p()
   
   
# EOF