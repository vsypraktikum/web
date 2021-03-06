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
            if (id_spl in self.data_o[i]["id"]) or (id_spl in self.data_o[i]["Bezeichnung"]):
               data_o = self.data_o[i] 
               
      return data_o   
   
   #-------------------------------------------------------
   def readFavorites_px(self, id_spl = None):
   #-------------------------------------------------------
      # hier zur Vereinfachung:
      # Aufruf ohne id: alle Einträge liefern
      data_o = []
      for i in range(len(self.data_o)): 
         if "favorites" in self.data_o[i]["Kategorien"]:
            print(self.data_o[i]["Kategorien"])
            data_o.append(self.data_o[i])            
      print(data_o)
      return data_o   
   
   #-------------------------------------------------------
   def readMissing_px(self, id_spl = None):
   #-------------------------------------------------------
      # hier zur Vereinfachung:
      # Aufruf ohne id: alle Einträge liefern
      data_o = []
      missing = None
      marked = None
      same = 0
      if id_spl == None:
         for i in range(len(self.data_o)):   
            missing = self.data_o[i]["Text"].split()    
            print(missing)
            for missed in missing:
               #if kategorie in kategorien: ---> hier weitermachen
               if "[[" in missed:
                  marked = missed.replace("[[","")
                  marked = marked.replace("]]","")
                  print("das ist ein Thema", missed)
                  for j in range(len(self.data_o)): 
                     if marked in self.data_o[j]["Bezeichnung"]:
                        print("übereinstimmendes thema", marked)
                        same = 1
                  if same == 0:
                     print("nicht übereinstimmend", marked)
                     data_o.append(marked)
                  same = 0   
                     
      print("endergebnis")
      print(data_o)        
      return data_o   
   
   #-------------------------------------------------------
   def readOrphans_px(self, id_spl = None):
   #-------------------------------------------------------
      # hier zur Vereinfachung:
      # Aufruf ohne id: alle Einträge liefern
      data_o = []
      same = 0
      for i in range(len(self.data_o)): 
         linked = "[[" + self.data_o[i]["Bezeichnung"] + "]]"
         for j in range(len(self.data_o)):
            print("linked: ", linked)
            if linked in self.data_o[j]["Text"]:
               print(self.data_o[j]["Bezeichnung"])
               same = 1   
            
         if (same == 0) and (self.data_o[i]["Bezeichnung"] not in data_o):   
            data_o.append(self.data_o[i])
         same = 0   
               
      print(data_o)
      return data_o   
   
   #-------------------------------------------------------
   def readTags_px(self, id_spl = None):
   #-------------------------------------------------------
      # hier zur Vereinfachung:
      # Aufruf ohne id: alle Einträge liefern
      data_o = []
      kategorien = None
      if id_spl == None:
         for i in range(len(self.data_o)): 
            if self.data_o[i]["Kategorien"] != "Kategorien sind noch anzugeben":  
               kategorien = self.data_o[i]["Kategorien"].split()    
               print(kategorien)
               for kategorie in kategorien:
                  print(kategorie)
                  #if kategorie in kategorien: ---> hier weitermachen
                  if kategorie in data_o:
                     print("doppelter eintrag")
                  else:   
                     data_o.append(kategorie)
                     print(data_o)
         print("endergebnis")
         print(data_o)            
      else:
         #id_i = int(id_spl)
         for i in range(len(self.data_o)):
            if id_spl in self.data_o[i]["Kategorien"]:
               print(self.data_o[i]["Kategorien"])
               data_o.append(self.data_o[i])
      print(data_o)         
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