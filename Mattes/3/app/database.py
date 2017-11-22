# coding: utf-8
import os
import os.path
import codecs
import json
import datetime
#----------------------------------------------------------
class Database_cl(object):
#----------------------------------------------------------
# da es hier nur darum geht, die Daten dauerhaft zu speichern,
# wird ein sehr einfacher Ansatz verwendet:
# - es k�nnen Daten zu genau 15 Teams gespeichert werden
# - je Team werden 2 Teilnehmer mit Namen, Vornamen und Matrikelnummer
# ber�cksichtigt
# - die Daten werden als eine JSON-Datei abgelegt
	
	#-------------------------------------------------------
	def __init__(self):
	#-------------------------------------------------------
		self.view = ['student'
		             ,'lehrende'
		             ,'firma'
		             ,'ppangebot'
		             ,'ppangebot']		
		self.data_o = None
		#self.readData_p()
	
	def GetDefault(self, ansicht):
		data_o = ''
		
		if ansicht == 0:
			data_o = {
			        "matrikelnr": '',
			        "name": '', 
			        "vorname": ''
			}
		elif ansicht == 1:
			data_o = {
			        "titel": '', 
			        "name": '', 
			        "vorname": '',
			        "lehrgebiet": ''
			}			
		elif ansicht == 2:
			data_o = {
			        "name": '', 
			        "branche": '', 
			        "schwerpunkt": '',
			        "sitz": '',
			        "mitarbeiteranzahl": ''
			}			
		else:
			data_o = {
			        "pptitel": '', 
			        "beschreibung": '', 
			        "firmaid": '',
			        "voraussetzung": '',
			        "kontakt": '',
			        "lehrendenid": '',
			        "matrikelid": '',
			        "anfangsdatum": '',
			        "enddatum": ''
			}			
		
		return data_o
	
	#-------------------------------------------------------
	def updateRow(self, ansicht, id_s, data_s):
	#-------------------------------------------------------
		del self.data_o[self.view[ansicht]]['list'][id_s]
		self.data_o[self.view[ansicht]]['list'].update({id_s: ''})
		self.data_o[self.view[ansicht]]['list'][id_s] = eval(data_s)
		self.saveData()
		return 	
	
	#-------------------------------------------------------
	def getRow(self, ansicht, id_s):
	#-------------------------------------------------------	
		return self.data_o[self.view[ansicht]]['list'][id_s]

	#-------------------------------------------------------
	def addRow(self, ansicht, data_s):
	#-------------------------------------------------------
		id_s = self.data_o[self.view[ansicht]]['count']
		self.data_o[self.view[ansicht]]['count'] += 1
		
		self.data_o[self.view[ansicht]]['list'].update({id_s: ''})
		self.data_o[self.view[ansicht]]['list'][id_s] = eval(data_s)
					
		self.saveData();
		return 	
	
	#-------------------------------------------------------
	def deleteRow(self, ansicht, id_s):
	#-------------------------------------------------------
		del self.data_o[self.view[ansicht]]['list'][id_s]
		self.saveData()
		return
	#-------------------------------------------------------
	def pushPPA(self, id_s):
	#-------------------------------------------------------	
		data_opl = self.data_o['ppangebot']['list'][id_s]
		del self.data_o['ppangebot']['list'][id_s]

		self.data_o['ppaktuell']['list'].append(data_opl)
		self.saveData()
		return
	
	#-------------------------------------------------------
	def ReadData(self):
	#-------------------------------------------------------
		fp_o = codecs.open(os.path.join('data', 'ppm.json'), 'r', 'utf-8')
		with fp_o:
			self.data_o = json.load(fp_o)
		
		return self.data_o		
	
	#-------------------------------------------------------
	def saveData(self):
	#-------------------------------------------------------
			
		with codecs.open(os.path.join('data', 'ppm.json'), 'w', 'utf-8') as fp_o:
			json.dump(self.data_o, fp_o)
# EOF