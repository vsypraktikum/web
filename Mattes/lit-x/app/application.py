# coding: utf-8

import json

import cherrypy

from .database import SourceDatabase_cl, EvaluatedDatabase_cl

# Method-Dispatching!

# Übersicht Anforderungen / Methoden

"""

Anforderung       GET          POST         PUT           DELETE
----------------------------------------------------------------
/                 Liste        -            -             -
                  Literatur
                  liefern

/source           Liste        -            -             -
                  Literatur
                  liefern

/evaluated        Liste        -            -             -
                  Auswertungen
                  liefern

/source/0         Dokument     Dokument     -             -
                  mit id=0     anlegen      
                  liefern
                  (Vorgabe-Werte)

/evaluated/0      Dokument     Dokument     -             -
                  mit id=0     anlegen      
                  liefern
                  (Vorgabe-Werte)

/source/{id}      Dokument     -            Dokument      Dokument
                  mit {id}                  ändern        löschen
                  liefern
                  (Literatur)

/evaluated/{id}   Dokument     -            Dokument      Dokument
                  mit {id}                  ändern        löschen
                  liefern
                  (Auswertungen)

id > 0 ! 

"""

#-------------------------------------------------------
def adjustId_p(id_spl, data_opl):
#-------------------------------------------------------

   if id_spl == None:
      data_opl['id'] = ''
   elif id_spl == '':
      data_opl['id'] = ''
   elif id_spl == '0':
      data_opl['id'] = ''
   else:
      data_opl['id'] = id_spl
   return data_opl


#----------------------------------------------------------
class Source_cl(object):
#----------------------------------------------------------

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.db_o = SourceDatabase_cl()

   #-------------------------------------------------------
   def GET(self, id):
   #-------------------------------------------------------
      retVal_o = {
         'data': None
      }
      if id == None:
         # Anforderung der Liste
         retVal_o['data'] = self.db_o.read_px()
      else:
         # Anforderung eines Dokuments
         data_o = self.db_o.read_px(id)
         if data_o != None:
            retVal_o['data'] = adjustId_p(id, data_o)

      return retVal_o
      
   #-------------------------------------------------------
   def POST(self, data_opl):
   #-------------------------------------------------------
      retVal_o = {
         'id': None
      }

      # data_opl: Dictionary mit den gelieferten key-value-Paaren

      data_o = {
         'name': data_opl["name_s"],
         'typ': data_opl["typ_s"],
         'referenz': data_opl["referenz_s"]
      }
      # Create-Operation
      id_s = self.db_o.create_px(data_o)
      retVal_o['id'] = id_s
         
      return retVal_o
      
   #-------------------------------------------------------
   def PUT(self, data_opl):
   #-------------------------------------------------------
      # Sichern der Daten: jetzt wird keine vollständige Seite
      # zurückgeliefert, sondern nur noch die Information, ob das
      # Speichern erfolgreich war

      retVal_o = {
         'id': None
      }

      # data_opl: Dictionary mit den gelieferten key-value-Paaren

      id_s = data_opl["id_s"]
      data_o = {
         'name': data_opl["name_s"],
         'typ': data_opl["typ_s"],
         'referenz': data_opl["referenz_s"]
      }
      # Update-Operation
      retVal_o['id'] = id_s
      if self.db_o.update_px(id_s, data_o):
         pass
      else:
         retVal_o['id'] = None

      return retVal_o

   #-------------------------------------------------------
   def DELETE(self, id):
   #-------------------------------------------------------
      # Eintrag löschen, nur noch Rückmeldung liefern
      retVal_o = {
         'id': id
      }

      if self.db_o.delete_px(id):
         pass
      else:
         retVal_o['id'] = None

      return retVal_o


#----------------------------------------------------------
class Evaluated_cl(object):
#----------------------------------------------------------

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.db_o = EvaluatedDatabase_cl()

   #-------------------------------------------------------
   def GET(self, id):
   #-------------------------------------------------------
      retVal_o = {
         'data': None
      }
      if id == None:
         # Anforderung der Liste
         retVal_o['data'] = self.db_o.read_px()
      else:
         # Anforderung eines Dokuments
         data_o = self.db_o.read_px(id)
         if data_o != None:
            retVal_o['data'] = adjustId_p(id, data_o)

      return retVal_o
      
   #-------------------------------------------------------
   def POST(self, data_opl):
   #-------------------------------------------------------
      retVal_o = {
         'id': None
      }

      # data_opl: Dictionary mit den gelieferten key-value-Paaren

      # hier müsste man prüfen, ob die Daten korrekt vorliegen!

      data_o = {
         'title': data_opl["title_s"],
         'author': data_opl["author_s"],
         'evalyear': data_opl["evalyear_s"]
      }
      # Create-Operation
      id_s = self.db_o.create_px(data_o)
      retVal_o['id'] = id_s

      return retVal_o
      
   #-------------------------------------------------------
   def PUT(self, data_opl):
   #-------------------------------------------------------
      # Sichern der Daten: jetzt wird keine vollständige Seite
      # zurückgeliefert, sondern nur noch die Information, ob das
      # Speichern erfolgreich war

      retVal_o = {
         'id': None
      }

      # data_opl: Dictionary mit den gelieferten key-value-Paaren
      # hier müsste man prüfen, ob die Daten korrekt vorliegen!

      id_s = data_opl["id_s"]
      data_o = {
         'title': data_opl["title_s"],
         'author': data_opl["author_s"],
         'evalyear': data_opl["evalyear_s"]
      }
      # Update-Operation
      retVal_o['id'] = id_s
      if self.db_o.update_px(id_s, data_o):
         pass
      else:
         retVal_o['id'] = None

      return retVal_o

   #-------------------------------------------------------
   def DELETE(self, id):
   #-------------------------------------------------------
      # Eintrag löschen, nur noch Rückmeldung liefern
      retVal_o = {
         'id': id
      }

      if self.db_o.delete_px(id):
         pass
      else:
         retVal_o['id'] = None

      return retVal_o

#----------------------------------------------------------
class Application_cl(object):
#----------------------------------------------------------

   exposed = True # gilt für alle Methoden

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.handler_o = {
         'source': Source_cl(),
         'evaluated': Evaluated_cl()
      }

   # es wird keine index-Methode vorgesehen, weil stattdessen
   # die Webseite index.html ausgeliefert wird (siehe Konfiguration)

   #-------------------------------------------------------
   def GET(self, path_spl = 'source', id=None):
   #-------------------------------------------------------
      retVal_o = {
         'data': None
      }

      if path_spl in self.handler_o:
         retVal_o = self.handler_o[path_spl].GET(id)

      if retVal_o['data'] == None:
         cherrypy.response.status = 404

      return json.dumps(retVal_o)
      
   #-------------------------------------------------------
   def POST(self, path_spl = 'source', **data_opl):
   #-------------------------------------------------------
      retVal_o = {
         'id': None
      }

      # data_opl: Dictionary mit den gelieferten key-value-Paaren

      # hier müsste man prüfen, ob die Daten korrekt vorliegen!

      if path_spl in self.handler_o:
         retVal_o = self.handler_o[path_spl].POST(data_opl)

      if retVal_o['id'] == None:
         cherrypy.response.status = 409
         
      return json.dumps(retVal_o)
      
   #-------------------------------------------------------
   def PUT(self, path_spl = 'source', **data_opl):
   #-------------------------------------------------------
      # Sichern der Daten: jetzt wird keine vollständige Seite
      # zurückgeliefert, sondern nur noch die Information, ob das
      # Speichern erfolgreich war

      retVal_o = {
         'id': None
      }

      # data_opl: Dictionary mit den gelieferten key-value-Paaren
      # hier müsste man prüfen, ob die Daten korrekt vorliegen!

      if path_spl in self.handler_o:
         retVal_o = self.handler_o[path_spl].PUT(data_opl)

      if retVal_o['id'] == None:
         cherrypy.response.status = 404

      return json.dumps(retVal_o)

   #-------------------------------------------------------
   def DELETE(self, path_spl = 'source', id=None):
   #-------------------------------------------------------
      # Eintrag löschen, nur noch Rückmeldung liefern
      retVal_o = {
         'id': id
      }

      if path_spl in self.handler_o:
         retVal_o = self.handler_o[path_spl].DELETE(id)

      if retVal_o['id'] == None:
         cherrypy.response.status = 404

      return json.dumps(retVal_o)

   #-------------------------------------------------------
   def default(self, *arguments, **kwargs):
   #-------------------------------------------------------
      msg_s = "unbekannte Anforderung: " + \
              str(arguments) + \
              ' ' + \
              str(kwargs)
      raise cherrypy.HTTPError(404, msg_s) 

# EOF