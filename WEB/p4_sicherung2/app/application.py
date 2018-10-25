# coding: utf-8

# Demonstrator / keine Fehlerbehandlung

import cherrypy
import json
import os
import os.path
import codecs
from .database import Database_cl
from .view import View_cl

# Method-Dispatching!

# Übersicht Anforderungen / Methoden

"""

Anforderung       GET    
-------------------------
/                 Liste  
                  liefern

/{id}             Detail  
                  mit {id}
                  liefern
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
      if args[0] == "topics":
         return self.getTopics(*args)
      else:
         return ''
   
   #-------------------------------------------------------   
   def getTopics(self, *args):
   #-------------------------------------------------------
   # /pensionaer/ daten aller pensionaere als liste ausliefern
   # /pensionaer/id daten eines pensionaers anhand id liefern
      retVal_s = ''
      if len(args)==1:
     
         retVal_s = self.getList_p()
      else:
         id = args[1]
    
         retVal_s = self.getDetail_p(id)

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
      #die ID eines topics ist die Bezeichnung 
      data_tmp = self.db_o.data_o
      daten = {
         "id": None,
         #"id": kwargs["Bezeichnung"],
         "Bezeichnung": kwargs["Bezeichnung"],
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
   def PUT(self, data_opl):
   #-------------------------------------------------------
      # Sichern der Daten: jetzt wird keine vollständige Seite
      # zurückgeliefert, sondern nur noch die Information, ob das
      # Speichern erfolgreich war

      print("ARGS: ", args)
      if args[1] == None:
         return ''
      else:
         data_tmp = self.db_o.data_o
         #print(data_tmp)

         daten = {
            "id": args[1], 
            "Bezeichnung": kwargs["Bezeichnung"],
            "Titel": kwargs["Titel"],
            "Text": kwargs["Text"],
            "Kategorien": kwargs["Kategorien"]
         }
         #print(daten)
         index = 0
         for data in data_tmp:
            print("INDEX: ", index)
            print("DATA: ", data)
            if str(index) == args[1]:
               #print("DATEN WERDEN EINGESPEICHERT")
               data_tmp[index] = daten
               #print("DATA[index]: ", data_tmp[index])
            index = index + 1     

      self.db_o.saveData()
      self.db_o.readData()
      return '{}'

   #-------------------------------------------------------
   def DELETE(self, id):
   #-------------------------------------------------------
      # Eintrag löschen, nur noch Rückmeldung liefern
      retVal_s = {
         'id': id
      }

      if self.db_o.delete_px(id):
         pass
      else:
         retVal_s['id'] = None

      return retVal_s   
      
   #-------------------------------------------------------
   def getList_p(self):
   #-------------------------------------------------------
      data_a = self.db_o.read_px()
      # default-Werte entfernen
      # ndata_a = data_a[1:]
      return self.view_o.createList_px(data_a)
   
   #-------------------------------------------------------
   def getDetail_p(self, id_spl):
   #-------------------------------------------------------
      data_o = self.db_o.read_px(id_spl)
      return self.view_o.createDetail_px(data_o)
# EOF