# coding: utf-8

import os
import os.path
import codecs

import json

#----------------------------------------------------------
class Database_cl(object):
#----------------------------------------------------------

   # Daten in dieser Variante dauerhaft (persistent) speichern
   # dazu jedes Element in einer Datei, die entsprechend der id benannt ist, speichern
   # alle Elemente werden zur Laufzeit des Servers zur Vereinfachung auch im
   # Hauptspeicher abgelegt

   # die nächste zu vergebende Id wird ebenfalls dauerhaft gespeichert

   # zur Vereinfachung wird hier fest vorgegebenen, dass sich die Daten
   # im Unterverzeichnis "data" befinden

   # es wird ferner angenommen, dass die Datei "data/maxid.dat" bereits existiert
   # und als einzigen Eintrag den aktuellen Wert der maximalen Id enthält

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.data_o = {}
      self.readData_p()

   #-------------------------------------------------------
   def create_px(self, data_opl):
   #-------------------------------------------------------
      # Überprüfung der Daten müsste ergänzt werden!
      id_s = self.nextId_p()
      # Datei erzeugen
      file_o = codecs.open(os.path.join('data', id_s+'.dat'), 'w', 'utf-8')
      file_o.write(json.dumps(data_opl, indent=3, ensure_ascii=True))
      file_o.close()

      self.data_o[id_s] = data_opl

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
         if id_spl in self.data_o:
            data_o = self.data_o[id_spl]

      return data_o

   #-------------------------------------------------------
   def update_px(self, id_spl, data_opl):
   #-------------------------------------------------------
      # Überprüfung der Daten müsste ergänzt werden!
      status_b = False
      if id_spl in self.data_o:
         # Datei aktualisieren
         file_o = codecs.open(os.path.join('data', id_spl+'.dat'), 'w', 'utf-8')
         file_o.write(json.dumps(data_opl, indent=3, ensure_ascii=True))
         file_o.close()

         self.data_o[id_spl] = data_opl
         status_b = True
      
      return status_b

   #-------------------------------------------------------
   def delete_px(self, id_spl):
   #-------------------------------------------------------
      status_b = False
      if id_spl in self.data_o:
         # Datei entfernen
         os.remove(os.path.join('data', id_spl+'.dat'))

         del self.data_o[id_spl]
         status_b = True
      
      return status_b
         
   #-------------------------------------------------------
   def getDefault_px(self):
   #-------------------------------------------------------

      return {
         'name': '',
         'typ': '',
         'referenz': ''
      }

   #-------------------------------------------------------
   def readData_p(self):
   #-------------------------------------------------------

      files_a = os.listdir('data')
      for fileName_s in files_a:
         if fileName_s.endswith('.dat') and fileName_s != 'maxid.dat':
            file_o = codecs.open(os.path.join('data', fileName_s), 'rU', 'utf-8')
            content_s = file_o.read()
            id_s = fileName_s[:-4]
            self.data_o[id_s] = json.loads(content_s)

   #-------------------------------------------------------
   def nextId_p(self):
   #-------------------------------------------------------
      file_o = open(os.path.join('data', 'maxid.dat'), 'r+')
      maxId_s = file_o.read()
      maxId_s = str(int(maxId_s)+1)
      file_o.seek(0)
      file_o.write(maxId_s)
      file_o.close()

      return maxId_s
# EOF