# coding: utf-8

# Demonstrator!
import os
import os.path
import codecs
import json
import cherrypy

#----------------------------------------------------------
class Database_cl(object):
#----------------------------------------------------------

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------

      self.pensionaere = [
            {
                  "id":"0",
                  "Anrede": "-0",
                  "Name":"Mustermann",
                  "Vorname":"Max",
                  "Titel": " - ",
                  "Geburtsdatum": "31.08.1918",
                  "Strasse":"Teststrasse",
                  "Hausnummer":"1234",
                  "Adresszusatz":" - ",
                  "Postleitzahl": "47804",
                  "Ort":"Krefeld"
            },
            {
                  "id":"1",
                  "Anrede": "-1",
                  "Name":"Mustermann1",
                  "Vorname":"Max1",
                  "Titel": " -1 ",
                  "Geburtsdatum": "31.08.1828",
                  "Strasse":"Teststrasse 1",
                  "Hausnummer":"1234 1",
                  "Adresszusatz":" - 1",
                  "Postleitzahl": "47804 1",
                  "Ort":"Krefeld 1"
            },
            {
                  "id":"2",
                  "Anrede": "-2",
                  "Name":"Mustermann2",
                  "Vorname":"Max2",
                  "Titel": " -2 ",
                  "Geburtsdatum": "22.03.1938",
                  "Strasse":"Teststrasse 2",
                  "Hausnummer":"1234 2",
                  "Adresszusatz":" - 2",
                  "Postleitzahl": "47804 2",
                  "Ort":"Krefeld 2"
            },
            {
                  "id":"3",
                  "Anrede": "-3",
                  "Name":"Mustermann3",
                  "Vorname":"Max3",
                  "Titel": " -3 ",
                  "Geburtsdatum": "01.07.1908",
                  "Strasse":"Teststrasse 3",
                  "Hausnummer":"1234 3",
                  "Adresszusatz":" - 3",
                  "Postleitzahl": "47804 3",
                  "Ort":"Krefeld 3"
            }
      ]
      self.Congrats = [
            {
                  "ID":"0",
                  "Beschreibung":"WatWeissIch",
                  "Path":"DaVorne"
            },
            {
                  "ID":"1",
                  "Beschreibung":"WatWeissIch1",
                  "Path":"DaVorne1"
            },
            {
                  "ID":"2",
                  "Beschreibung":"WatWeissIch2",
                  "Path":"DaVorne2"
            }
      ]
      
      self.readData()
      self.readCongrats()
      
   def saveCongrats(self):
      with codecs.open(os.path.join('congratstempl', 'congrats.json'), 'w', 'utf-8') as file_x:
            json.dump(self.Congrats, file_x) 

   def readCongrats(self):
      try:
            file_x = codecs.open(os.path.join('congratstempl', 'congrats.json'), 'r', 'utf-8')
      except: #falls datei nicht vorhanden ist: datei anlegen durch speichern der werte 
            #speichere daten in josn datein
            self.saveCongrats()
      else:
            with file_x:
                  self.Congrats = json.load(file_x)
      self.saveCongrats()
#-------------------------------------------------------------------------

   def saveData(self):
      with codecs.open(os.path.join('data', 'daten.json'), 'w', 'utf-8') as file_x:
            json.dump(self.pensionaere, file_x) 

   def readData(self):
      try:
            file_x = codecs.open(os.path.join('data', 'daten.json'), 'r', 'utf-8')
      except: #falls datei nicht vorhanden ist: datei anlegen durch speichern der werte 
            #speichere daten in josn datein
            self.saveData()
      else:
            with file_x:
                  self.pensionaere = json.load(file_x)
      self.saveData()

   #-------------------------------------------------------
   def read_px(self, id_spl = None):
   #-------------------------------------------------------
      data_o = None
      if id_spl == None:
         data_o = self.pensionaere
      else:
         id_i = int(id_spl)
         if id_i > 0 and  id_i < len(self.pensionaere):
            data_o = self.pensionaere[id_i]
         else:
            data_o = self.pensionaere[0]

      return data_o

# EOF