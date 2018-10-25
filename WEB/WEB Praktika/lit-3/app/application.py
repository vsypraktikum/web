# coding: utf-8

import cherrypy

from .database import Database_cl
from .view import View_cl

#----------------------------------------------------------
class Application_cl(object):
#----------------------------------------------------------

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      # spezielle Initialisierung können hier eingetragen werden
      self.db_o = Database_cl()
      self.view_o = View_cl(cherrypy.Application.currentDir_s)

   #-------------------------------------------------------
   def index(self):
   #-------------------------------------------------------
      return self.createList_p()
      
   index.exposed = True
      
   #-------------------------------------------------------
   def add(self):
   #-------------------------------------------------------
      return self.createForm_p()
      
   add.exposed = True

   #-------------------------------------------------------
   def edit(self, id):
   #-------------------------------------------------------
      return self.createForm_p(id)
      
   edit.exposed = True

   #-------------------------------------------------------
   def save(self, **data_opl):
   #-------------------------------------------------------
      # Sichern der Daten: aufgrund der Formularbearbeitung muss
      # eine vollständige HTML-Seite zurückgeliefert werden!

      # data_opl: Dictionary mit den gelieferten key-value-Paaren

      # hier müsste man prüfen, ob die Daten korrekt vorliegen!

      id_s = data_opl["id_s"]
      data_o = {
         'name': data_opl["name_s"],
         'typ': data_opl["typ_s"],
         'referenz': data_opl["referenz_s"]
      }
      if id_s != "None":
         # Update-Operation
         self.db_o.update_px(id_s, data_o)
      else:
         # Create-Operation
         id_s = self.db_o.create_px(data_o)
         
      return self.view_o.createForm_px(id_s, data_o)

   save.exposed = True
      
   #-------------------------------------------------------
   def delete(self, id):
   #-------------------------------------------------------
      # Eintrag löschen, dann Liste neu anzeigen

      self.db_o.delete_px(id)
      return self.createList_p()

   delete.exposed = True
      
   #-------------------------------------------------------
   def default(self, *arguments, **kwargs):
   #-------------------------------------------------------
      msg_s = "unbekannte Anforderung: " + \
              str(arguments) + \
              ' ' + \
              str(kwargs)
      raise cherrypy.HTTPError(404, msg_s) 
   default.exposed= True

   #-------------------------------------------------------
   def createList_p(self):
   #-------------------------------------------------------
      data_o = self.db_o.read_px()
      # mit diesen Daten Markup erzeugen
      return self.view_o.createList_px(data_o)
   
   #-------------------------------------------------------
   def createForm_p(self, id_spl = None):
   #-------------------------------------------------------
      if id_spl != None:
         data_o = self.db_o.read_px(id_spl)
      else:
         data_o = self.db_o.getDefault_px()
      # mit diesen Daten Markup erzeugen
      return self.view_o.createForm_px(id_spl, data_o)
   
# EOF