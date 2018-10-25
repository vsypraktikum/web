# coding: utf-8

import cherrypy

from .database import Database_cl
from .view import View_cl

# GET          /article/:id

# POST         /article/ + Daten       neuen Artikel mit den angegebenen Daten erstellen und id vergeben
# PUT          /article/:id + Daten    bestehenden Artikel aktualisieren
# DELETE       /article/:id            bestehenden Artikel löschen

#----------------------------------------------------------
class Article_cl(object):
#----------------------------------------------------------

   exposed = True

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.db_o = Database_cl()
      self.view_o = View_cl()

   #-------------------------------------------------------
   def GET(self, id):
   #-------------------------------------------------------
      data_o = self.db_o.read_px(id)
      
      return self.view_o.createList_px(data_o)
      
   #-------------------------------------------------------
   def POST(self, **data_opl):
   #-------------------------------------------------------
      if data_opl is None:
         return "-1"
      else:
         return self.db_o.create_px(data_opl)

   #-------------------------------------------------------
   def PUT(self, **data_opl):
   #-------------------------------------------------------
      if data_opl is None:
         return "-1"
      else:
         return self.db_o.update_px(data_opl['id'], data_opl)
      
   #-------------------------------------------------------
   def DELETE(self, id):
   #-------------------------------------------------------
      if id is None:
         return "-1"
      else:
         return self.db_o.delete_px(id)
      
# EOF