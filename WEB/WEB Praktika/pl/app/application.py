# coding: utf-8

# Demonstrator / keine Fehlerbehandlung

import cherrypy
#neu
import json
import os
import os.path
import codecs
#ende neu 
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
                 
@cherrypy.expose
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
   def DELETE(self, *args, **kwargs):
   #-------------------------------------------------------
   # /pensionaer/id daten eines pensionaers löschen
   # /congratstmpl/id per path identifizierte vorlage löschen 

      if args[0] == "pensionaer":
            id = args[1]
            count = 0
            d = None
            data_tmp = self.db_o.pensionaere
            for data in data_tmp:
                  if str(count) == id:
                        d =  data_tmp.pop(count)
                  count = count + 1
            self.db_o.saveData()
            self.db_o.readData()
      else: 
            if args[0] == "congratstempl":
                  self.VorlageLoeschen(*args, **kwargs)
      
   #-------------------------------------------------------
   def VorlageLoeschen(self, *args, **kwargs):
         #print("in function VorlageLoeschen")
         data_tmp = self.db_o.Congrats
         id = args[1]
         #print("ID: ", id)
         count = 0
         path = None
         filepath = " "
         for data in data_tmp:
               if str(data_tmp[count]["ID"]) == str(id):
                     #print("VORLAGE LOESCHEN")
                     filepath = data_tmp[count]["Path"]
                     #path = os.path.join(cherrypy.Application.currentDir_s, "congratstempl", filepath)
                     #os.remove(path)
                     data_tmp.pop(count)
               count = count + 1

         self.db_o.saveCongrats()
         self.db_o.readCongrats()

   def PUT(self, *args, **kwargs):
   #-------------------------------------------------------
   # /pensionaer/id + daten daten eines pensionaers aktualisieren 
      
      print("ARGS: ", args)
      if args[1] == None:
            return ''
      else:
            data_tmp = self.db_o.pensionaere
            #print(data_tmp)
            
            daten = {
                  "id": args[1],
                  "Anrede":kwargs["Anrede"], 
                  "Name": kwargs["Name"], 
                  "Vorname":kwargs["Vorname"], 
                  "Titel":kwargs["Titel"], 
                  "Geburtsdatum":kwargs["Geburtsdatum"], 
                  "Strasse":kwargs["Strasse"], 
                  "Hausnummer":kwargs["Hausnummer"], 
                  "Adresszusatz":kwargs["Adresszusatz"], 
                  "Postleitzahl":kwargs["Postleitzahl"], 
                  "Ort":kwargs["Ort"]
            }
            #print(daten)
            index = 0
            for data in data_tmp:
                  #print("INDEX: ", index)
                  #print("DATA: ", data)
                  if str(index) == args[1]:
                        #print("DATEN WERDEN EINGESPEICHERT")
                        data_tmp[index] = daten
                        #print("DATA[index]: ", data_tmp[index])
                  index = index + 1     
      
      self.db_o.saveData()
      self.db_o.readData()
      return '{}'
      
   #-------------------------------------------------------
   def POST(self, *args, **kwargs):
   #-------------------------------------------------------
   # /pensionaer/ daten daten eines neuen pensionaers speichern und ID liefern
   # /congratstmpl/path + daten vorlage importieren/neue id liefern
   # /annuallist/ jahresüberblick erzeugen 
   # /significantBirthdays/ + daten abfrage ausführen
   # /congratulation/ + daten gratulationsschreiben erstellen 
      if args[0] == "pensionaer":
            return self.postPensionaer(*args, **kwargs)
      else: 
            if args[0] == "congratstempl":
                  return self.postCongratstempl(*args, **kwargs)
            else: 
                  if args[0] == "annuallist":
                        return self.postAnnuallist(*args, **kwargs)
                  else: 
                        if args[0] == "significantbirthdays":
                              return self.postBirthdays(*args, **kwargs)
                        else: 
                              if args[0] == "congratulation":
                                    return self.postCongrats(*args, **kwargs)


   def postCongratstempl(self, *args, **kwargs):
         # /congratstmpl/path + daten vorlage importieren/neue id liefern
      path = args[0]
      filename = args[2]
      beschreibung = kwargs["Beschreibung"]
      print("PFAD: ", path)
      print("ARGS: ", args)
      print("KWARGS", kwargs)
      
      self.db_o.readCongrats()
      data_tmp = self.db_o.Congrats
      retVal = {
            "ID":"",
            "Beschreibung":"",
            "Path":"" 
      }
      
      count = 0
      maxID = 0
      for data in data_tmp:
            if data_tmp[count]["ID"] > maxID:
                  maxID = data_tmp[count]["ID"] #finde höchste id
            count = count + 1

      maxID = int(maxID) + 1
      retVal["ID"] = str(maxID)
      retVal["Beschreibung"] = beschreibung
      retVal["Path"] = filename
      data_tmp.append(retVal)

      self.db_o.saveCongrats()
      self.db_o.readCongrats()
         

         
   def postAnnuallist(self, *args, **kwargs):
         # /annuallist/ jahresüberblick erzeugen 
         data_tmp = self.db_o.pensionaere
         daten = [
            {
               "Name": "",
               "Vorname":"",
               "Geburtsdatum":"",
               "Alter":""
            }
         ]

         tmp = None
         count = 0
         for data in data_tmp:
               
               tmp = data_tmp[count]["Geburtsdatum"]
               tmp = tmp[6:]
               daten.append({})
               daten[count]["Name"] = data_tmp[count]["Name"]
               daten[count]["Vorname"] = data_tmp[count]["Vorname"]
               daten[count]["Geburtsdatum"] = data_tmp[count]["Geburtsdatum"]
               daten[count]["Alter"] = str(2017-int(tmp))
               
               count = count + 1

         return json.dumps(daten)
         
   def postBirthdays(self, *args, **kwargs):
         # /significantBirthdays/ + daten abfrage ausführen
         uebergabeDatum = kwargs["Datum"]
         uebergabeDauer = kwargs["Dauer"]
         startmonat = int(uebergabeDatum[:2])
         startjahr = int(uebergabeDatum[4:])
         endmonat = int(uebergabeDauer)
         print(startmonat, ".", startjahr, " - ", endmonat)
         data_tmp = self.db_o.pensionaere
         count = 0
         
         daten = [

         ]

         countSignificantBirthdays = 0
         for data in data_tmp:
               jahr = int(data_tmp[count]["Geburtsdatum"][6:])    
               monat = int(data_tmp[count]["Geburtsdatum"][3:5])
               dateFound = 0
               print(count, jahr, monat)
               if monat <= endmonat and monat >= startmonat and dateFound == 0:      #nur berechnen, falls geburtstagsmonat des pensionaers im angegebenen zeitraum liegt 
                  
                  #berechne ob geburtstag "SIGNIFIKANT" ist
                  for jahrIndex in range (0, 35, 5):              #startjahr 5, bis 30, schritt: 5
                        if 2018-jahr == 70 + jahrIndex and dateFound == 0:               # falls alter == 70, 75, 80, 85, 90, 95, 100
                            daten.append({})
                            daten[countSignificantBirthdays]['Name'] = data_tmp[count]["Name"]
                            daten[countSignificantBirthdays]['ID'] = data_tmp[count]["id"]
                            daten[countSignificantBirthdays]['Vorname'] = data_tmp[count]["Vorname"]
                            daten[countSignificantBirthdays]['Geburtstag'] = str(data_tmp[count]["Geburtsdatum"][:2] + "." + str(monat) + ".2018")
                            daten[countSignificantBirthdays]['Alter'] = str(70 + jahrIndex)
                            dateFound = 1
                            countSignificantBirthdays = countSignificantBirthdays + 1
               count = count + 1
         print(daten)
         print(json.dumps(daten))
         return json.dumps(daten)
         #return json.dumps([{"ID":"1"}]) 



   def postCongrats(self, *args, **kwargs):
         # /congratulation/ + daten gratulationsschreiben erstellen 
         print(args, kwargs)
         id = args[1]
         retVal = [
               {
                  "id": self.db_o.pensionaere[int(id)]["id"],
                  "Anrede":self.db_o.pensionaere[int(id)]["Anrede"], 
                  "Name": self.db_o.pensionaere[int(id)]["Name"], 
                  "Vorname":self.db_o.pensionaere[int(id)]["Vorname"], 
                  "Titel":self.db_o.pensionaere[int(id)]["Titel"], 
                  "Geburtsdatum":self.db_o.pensionaere[int(id)]["Geburtsdatum"], 
                  "Strasse":self.db_o.pensionaere[int(id)]["Strasse"], 
                  "Hausnummer":self.db_o.pensionaere[int(id)]["Hausnummer"], 
                  "Adresszusatz":self.db_o.pensionaere[int(id)]["Adresszusatz"], 
                  "Postleitzahl":self.db_o.pensionaere[int(id)]["Postleitzahl"], 
                  "Ort":self.db_o.pensionaere[int(id)]["Ort"],
                  
               },
               {
                  
               }
         ]
         data_tmp = self.db_o.pensionaere
         rentner = data_tmp[int(id)]
         jahr = int(rentner["Geburtsdatum"][6:])  
         name = kwargs["vorlage"]
         path = os.path.join(cherrypy.Application.currentDir_s, 'congratstempl', name)
         datei = open(path, "r")

         
         content = datei.read()
         retVal[1] = content
         
         print(json.dumps(retVal))
         datei.close()
         return json.dumps(retVal)
         #return content  
         
   def postPensionaer(self, *args, **kwargs):
      # /pensionaer/ daten daten eines neuen pensionaers speichern und ID liefern
      data_tmp = self.db_o.pensionaere
      daten = {
            "id": None, #id wird später ermittelt
            "Anrede":kwargs["Anrede"], 
            "Name": kwargs["Name"], 
            "Vorname":kwargs["Vorname"], 
            "Titel":kwargs["Titel"], 
            "Geburtsdatum":kwargs["Geburtsdatum"], 
            "Strasse":kwargs["Strasse"], 
            "Hausnummer":kwargs["Hausnummer"], 
            "Adresszusatz":kwargs["Adresszusatz"], 
            "Postleitzahl":kwargs["Postleitzahl"], 
            "Ort":kwargs["Ort"]
      }

      count = 0
      for data in data_tmp:
            count = count + 1    # zaehle anzahl datensätze 

      count = count + 1
      maxID = 0
      for i in range(0, count-1):
            if data_tmp[i]["id"] > maxID:
                  maxID = data_tmp[i]["id"]     #suche größte id

      print("prev: ", maxID)
      maxID = int(maxID) + 1 
      print ("after: ", maxID)
      daten["id"] = maxID

      data_tmp.append(daten)
      self.db_o.saveData()
      self.db_o.readData()
      return ''

   #-------------------------------------------------------
   def GET(self, *args):
   #-------------------------------------------------------
   # /anzeigen startseite
   # /pensionaer/ daten aller pensionaere als liste ausliefern
   # /pensionaer/id daten eines pensionaers anhand id liefern

   # /congratstmpl/ liste aller vorlagen liefern
   # /congratstmpl/path inhalt pfad zur dateiauswahl für den import liefern
   # /congratstmpl/id beschreibung für und inhalt der per id gewaehlten vorlage gratulationen liefern
   
   # /significantBirthdays/ defaultwerte für ein formular zur abfrage der einstellungen liefern
      
      if args[0] == "pensionaer":
            return self.getPensionaer(*args)
      else:
            if args[0] == "congratstempl":
                  return self.getCongrats(*args)
            else:
                  if args[0] == "significantbirthdays":
                        return self.getBirthdays()
                  else:
                        return ''


   def getBirthdays(self):
      # /significantBirthdays/ defaultwerte für ein formular zur abfrage der einstellungen liefern   
      # abfrage 
      pass

   def getCongrats(self, *args):
      # /congratstmpl/ liste aller vorlagen liefern
      # /congratstmpl/path inhalt pfad zur dateiauswahl für den import liefern
      # /congratstmpl/id beschreibung und inhalt der per id gewaehlten vorlage gratulationen liefern


      #bei erfolgreichem import muss json automatisch erstellt werden client oder server?
      path = args[2]
      id = args[1]
      if path == "-1" and id == "-1":
            return self.CgetList()
      else:
            if path != "-1":
                  return self.CgetPathContent(path)
            else:
                  if id != "-1":
                        return self.CgetTemplateById(id)
            

   def CgetList(self):
      
      # liste aller möglichen vorlagen
      #informationen aus .json dateien in congratstempl
      
      retVal_s = self.db_o.Congrats
      return json.dumps(retVal_s)

   def CgetPathContent(self, path):
      #liste mit allen dateien im pfad die importiert werden können 
      # pfad muss sich in root von server befinden 
      #print("CgetPathContent")
      retVal = [

      ]
      _path = None
      if path == "a":
            _path = "congratstempl"
            files_a = os.listdir(os.path.join(cherrypy.Application.currentDir_s, _path))
      else:
            _path = path
            files_a = os.listdir(_path)
      count = 0
      for FileNames in files_a:
            #print(FileNames)
            #retVal[count]["Dateiname"] = FileNames
            retVal.append(FileNames)
            count = count + 1
            
      return json.dumps(retVal)
      


   def CgetTemplateById(self, id):
      #waehle template anhand von id aus liste aus und liefere speicherort des templates 
      #und beschreibung 
      
      retVal = [
            {
                  "ID":"",
                  "Beschreibung":"",
                  "Path":"",
                  "Text":""
            }
      ]
      self.db_o.readCongrats()
      data_tmp = self.db_o.Congrats
      path = None
      count = 0
      for data in data_tmp:
            
            if str(data_tmp[count]['ID']) == str(id):
                  retVal[0]['ID'] = data_tmp[count]["ID"]
                  retVal[0]['Beschreibung'] = data_tmp[count]["Beschreibung"]
                  retVal[0]['Path'] = data_tmp[count]["Path"]
                  
                  path = data_tmp[count]['Path']

                  file_x = codecs.open(os.path.join("congratstempl", path), 'r', 'utf-8')
                  content = file_x.read()
                  
                  file_x.close()
                  retVal[0]['Text'] = content
                  #print(retVal)
                  return json.dumps(retVal) 
            count = count + 1
   

   def getPensionaer(self, *args):
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
   def getList_p(self):
   #-------------------------------------------------------
      data_a = self.db_o.read_px()
      print(json.dumps(data_a))
      return self.view_o.createList_px(data_a)
   
   #-------------------------------------------------------
   def getDetail_p(self, id_spl):
   #-------------------------------------------------------
      data_o = self.db_o.read_px(id_spl)
      return self.view_o.createDetail_px(data_o)
# EOF