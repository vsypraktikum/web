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
		# spezielle Initialisierung k�nnen hier eingetragen werden
		self.view = ['student'
		             ,'lehrende'
		             ,'firma'
		             ,'ppangebot']		
		self.db_o = Database_cl()
		self.view_o = View_cl()
	@cherrypy.expose
	#-------------------------------------------------------
	def index(self):
	#-------------------------------------------------------
		return self.view_o.CreateIndex_px()
	@cherrypy.expose
	
	#-------------------------------------------------------
	def deleteRow(self, ansicht, id_s):
	#-------------------------------------------------------	
		ansicht = int(ansicht)
		self.db_o.deleteRow(ansicht, id_s)
		
		data_o = self.db_o.ReadData()
		data_o = data_o[self.view[ansicht]]['list']
		return self.view_o.CreateList_px(data_o, ansicht)
	@cherrypy.expose
	
	#-------------------------------------------------------
	def addRow(self, ansicht, data_s):
	#-------------------------------------------------------	
		ansicht = int(ansicht)
		
		self.db_o.addRow(ansicht, data_s)

		return self.CreateList(ansicht)
	@cherrypy.expose
	
	#-------------------------------------------------------
	def updateRow(self, ansicht, id_s, data_s):
	#-------------------------------------------------------
		ansicht = int(ansicht)
		self.db_o.updateRow(ansicht, id_s, data_s)
		
		if ansicht == 4:
			self.db_o.pushPPA(id_s)		
	
		return self.CreateList(ansicht)
	@cherrypy.expose
	
	#-------------------------------------------------------
	def checkID(self, ansicht, id_s):
	#-------------------------------------------------------	
		ansicht = int(ansicht)
		data_o = self.db_o.ReadData()
		
		if ansicht == 0:
			key = 'matrikelid'
		elif ansicht == 1:
			key = 'lehrendenid'
		elif ansicht == 3:
			key = 'firmaid'
		elif ansicht == 4:
			key = 'matrikelid'
		else:
			return "1"
			
		for dct in data_o['ppaktuell']['list']:
			if dct[key] == id_s:
				return "1"

		for dct in data_o['ppabgeschlossen']['list']:
			if dct[key] == id_s:
				return "1"
		
		return "0"
	@cherrypy.expose	
	
	#-------------------------------------------------------
	def CreateList(self, ansicht):
	#-------------------------------------------------------
		ansicht = int(ansicht)
		data_o = self.db_o.ReadData()
				
		
		if ansicht > 3:
			ppangebot = data_o['ppangebot']['list']
			ppaktuell = data_o['ppaktuell']['list']  
			ppabgeschlossen = data_o['ppabgeschlossen']['list']
			ppaktuell.sort(key=lambda x: x['anfangsdatum'])
			ppabgeschlossen.sort(key=lambda x: x['anfangsdatum'])
			
			if ansicht == 4:
				for key in ppangebot:
					ppangebot[key].update(data_o['firma']['list'][ppangebot[key]['firmaid']])
				
				for key in range(0, len(ppaktuell)):
					ppaktuell[key].update(data_o['firma']['list'][ppaktuell[key]['firmaid']])
				   
				for key in range(0, len(ppabgeschlossen)):
					ppabgeschlossen[key].update(data_o['firma']['list'][ppabgeschlossen[key]['firmaid']])        
					    
								
			elif ansicht == 5:
				for key in range(0, len(ppaktuell)):
					ppaktuell[key].update(data_o['student']['list'][ppaktuell[key]['matrikelid']])
					    
				for key in range(0, len(ppabgeschlossen)):
					ppabgeschlossen[key].update(data_o['student']['list'][ppabgeschlossen[key]['matrikelid']]) 			
				
			elif ansicht == 6:
				for key in range(0, len(ppaktuell)):
					ppaktuell[key].update(data_o['lehrende']['list'][ppaktuell[key]['lehrendenid']])
	
				for key in range(0, len(ppabgeschlossen)):
					ppabgeschlossen[key].update(data_o['lehrende']['list'][ppabgeschlossen[key]['lehrendenid']])   			

			data_o['ppangebot']['list'] = ppangebot
			data_o['ppaktuell']['list'] = ppaktuell
			data_o['ppabgeschlossen']['list'] = ppabgeschlossen
		
		else:
			data_o = data_o[self.view[ansicht]]['list']
		
		return self.view_o.CreateList_px(data_o, ansicht)
	
	@cherrypy.expose	
	#-------------------------------------------------------
	def CreateForm(self, ansicht, id_s = ""):
	#-------------------------------------------------------
		data_o = self.db_o.ReadData()
		
		ansicht = int(ansicht)
		if id_s == "":
			data_opl = self.db_o.GetDefault(ansicht)
			id_s = ' '
		else:
			data_opl = self.db_o.getRow(ansicht, id_s)
		
		return self.view_o.CreateForm_px(data_opl, data_o, ansicht, id_s)
# EOF
		
		
		
		
		
