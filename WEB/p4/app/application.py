# coding: utf-8

# Demonstrator / keine Fehlerbehandlung

import cherrypy
import json
import os
import os.path
import codecs
import time
from .database import Database_cl
from .view import View_cl

# Method-Dispatching!

# Übersicht Anforderungen / Methoden

"""

Anforderung       GET               POST              PUT               DELETE
------------------------------------------------------------------------------
/                 Liste             neue                                    /  
                  liefern           Daten                /                  /
                                    eintragen                             /

/{id}             Detail                              bestehenden      datensatz mit
                  mit {id}              /              Datensatz        id loeschen
                  liefern                             bearbeiten/
                                                      ergaenzen


"""

#----------------------------------------------------------
class Application_cl(object):
#----------------------------------------------------------

   exposed = True # gilt für alle Methoden

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      # spezielle Initialisierung können hier eingetragen werden
      self.db_o = Database_cl()
      self.view_o = View_cl()

   #-------------------------------------------------------
   def GET(self, *args):
   #-------------------------------------------------------
      print(args[0])
      if args[0] == "topics":
         return self.getTopics(*args)
      elif args[0] == "tags":
         return self.getTags(*args)
      elif args[0] == "favorites":
         return self.getFavorites(*args)
      elif args[0] == "missing":
         return self.getMissing(*args)
      elif args[0] == "orphans":
         return self.getOrphans(*args)      
      else:
         return ''
   
   #-------------------------------------------------------   
   def getTopics(self, *args):
   #-------------------------------------------------------
   # /topics/ daten aller themen als liste ausliefern
   # /topics/id daten eines themas anhand id liefern
      retVal_s = ''
      if len(args)==1:          
         retVal_s = self.getList_p()
      else:
         id = args[1]

         retVal_s = self.getDetail_p(id)

      return retVal_s

   #-------------------------------------------------------   
   def getMissing(self, *args):
   #-------------------------------------------------------
      retVal_s = ''
      if len(args)==1:          
         retVal_s = self.getMissingList_p()
      else:
         id = args[1]
         retVal_s = self.getDetail_p(id)

      return retVal_s
   
   #-------------------------------------------------------   
   def getFavorites(self, *args):
   #-------------------------------------------------------
      retVal_s = ''
      if len(args)==1:          
         retVal_s = self.getFavoritesList_p()
      else:
         id = args[1]

         retVal_s = self.getDetail_p(id)

      return retVal_s
   
   #-------------------------------------------------------   
   def getOrphans(self, *args):
   #-------------------------------------------------------
      retVal_s = ''
      if len(args)==1:          
         retVal_s = self.getOrphansList_p()
      else:
         id = args[1]

         retVal_s = self.getDetail_p(id)

      return retVal_s   
   
   #-------------------------------------------------------   
   def getTags(self, *args):
   #-------------------------------------------------------
   # /tags/ daten aller kategorien als liste ausliefern
   # /tags/id daten eines kategorien anhand id liefern
      retVal_s = ''
      if len(args)==1:          
         retVal_s = self.getListTags_p()
      else:
         id = args[1]
    
         retVal_s = self.getDetailTags_p(id)

      return retVal_s
   
   
   #-------------------------------------------------------
   def POST(self, *args, **kwargs):
   #-------------------------------------------------------
      if args[0] == "topics":
         return self.postTopics(*args, **kwargs)      
      else:
         return ''
   #-------------------------------------------------------
   def postTopics(self, *args, **kwargs):
   #-------------------------------------------------------
      #print current date and time
      print(time.strftime("%d.%m.%Y %H:%M:%S"))
      print(kwargs)
      print("args bei post", args)
      data_tmp = self.db_o.data_o
      
      if args[0] == None:
         daten = {
         "id": None,
         #"id": kwargs["Bezeichnung"],
         "Bezeichnung": args[1],
         "Datum_Erstellung": time.strftime("%d.%m.%Y %H:%M:%S"),
         "Datum_Aenderung" : time.strftime("%d.%m.%Y %H:%M:%S"),
         "Titel": "Titel ist noch anzugeben",
         "Text": "Text ist noch anzugeben",
         "Kategorien": "Kategorien sind noch anzugeben"              
         }
      else:
         daten = {
         "id": None,
         #"id": kwargs["Bezeichnung"],
         "Bezeichnung": kwargs["Bezeichnung"],
         "Datum_Erstellung": time.strftime("%d.%m.%Y %H:%M:%S"),
         "Datum_Aenderung" : time.strftime("%d.%m.%Y %H:%M:%S"),
         "Titel": "Titel ist noch anzugeben",
         "Text": "Text ist noch anzugeben",
         "Kategorien": "Kategorien sind noch anzugeben"              
      }
      #Erstellung einer ID die bei jedem Post hochgezählt wird
      # Create-Operation
      #id_s = self.db_o.create_px(data_o)
      self.db_o.getNewID_p()
      id_s = str(self.db_o.dataID_o)      
      daten["id"] = id_s
      print(daten)
      data_tmp.append(daten)
      self.db_o.saveData_p()
      self.db_o.readData_p()
         
      return ''      
   #-------------------------------------------------------
   def PUT(self, *args, **kwargs):
   #-------------------------------------------------------
      # Sichern der Daten: jetzt wird keine vollständige Seite
      # zurückgeliefert, sondern nur noch die Information, ob das
      # Speichern erfolgreich war

      print("ARGS: ", args)
      print("kwargs: ", kwargs)
      if args[1] == None:
         return ''
      else:
         data_tmp = self.db_o.data_o
         #print(data_tmp)
         daten = {
            "id": args[1], 
            "Bezeichnung": kwargs["Bezeichnung"],
            "Datum_Erstellung": kwargs["Datum_Erstellung"],
            "Datum_Aenderung" : time.strftime("%d.%m.%Y %H:%M:%S"),            
            "Titel": kwargs["Titel"],
            "Text": kwargs["Text"],
            "Kategorien": kwargs["Kategorien"]
         }
         #print(daten)
         index = 0
         for data in data_tmp:
            #print("INDEX: ", index)
            print("DATA: ", data)
            if data['id'] == args[1]:
               data_tmp[index] = daten
            index = index + 1     

      self.db_o.saveData_p()
      self.db_o.readData_p()
      return '{}'

   #-------------------------------------------------------
   def DELETE(self, *args, **kwargs):
   #-------------------------------------------------------
      # Eintrag löschen, nur noch Rückmeldung liefern
      
      if args[0] == "topics":
         id = args[1]
         count = 0
         data_tmp = self.db_o.data_o
         for data in data_tmp:
            if data['id'] == id:
               data_tmp.pop(count)
            count = count + 1
         self.db_o.saveData_p()
         self.db_o.readData_p() 
      
   #-------------------------------------------------------
   def getList_p(self):
   #-------------------------------------------------------
      data_a = self.db_o.read_px()
      # default-Werte entfernen
      # ndata_a = data_a[1:]
      return self.view_o.createList_px(data_a)

   #-------------------------------------------------------
   def getFavoritesList_p(self):
   #-------------------------------------------------------
      data_a = self.db_o.readFavorites_px()
      # default-Werte entfernen
      # ndata_a = data_a[1:]
      return self.view_o.createList_px(data_a)
   
   #-------------------------------------------------------
   def getMissingList_p(self):
   #-------------------------------------------------------
      data_a = self.db_o.readMissing_px()
      # default-Werte entfernen
      # ndata_a = data_a[1:]
      return self.view_o.createList_px(data_a)   
   
   #-------------------------------------------------------
   def getOrphansList_p(self):
   #-------------------------------------------------------
      data_a = self.db_o.readOrphans_px()
      # default-Werte entfernen
      # ndata_a = data_a[1:]
      return self.view_o.createList_px(data_a)   
   
   #-------------------------------------------------------
   def getDetail_p(self, id_spl):
   #-------------------------------------------------------
      data_o = self.db_o.read_px(id_spl)
      if (data_o == None) and (id_spl != "null"):
         self.postTopics(None, id_spl)
         data_o = self.db_o.read_px(id_spl)   
      return self.view_o.createDetail_px(data_o)

   #-------------------------------------------------------
   def getListTags_p(self):
   #-------------------------------------------------------
      data_a = self.db_o.readTags_px()
      # default-Werte entfernen
      # ndata_a = data_a[1:]
      return self.view_o.createList_px(data_a)
   
   #-------------------------------------------------------
   def getDetailTags_p(self, id_spl):
   #-------------------------------------------------------
      data_o = self.db_o.readTags_px(id_spl)
      return self.view_o.createDetail_px(data_o)
# EOF