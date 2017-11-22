# coding: utf-8
import json
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
		self.db_o = Database_cl()
		self.view_o = View_cl()
	@cherrypy.expose
	#-------------------------------------------------------
	def index(self):
	#-------------------------------------------------------
		return self.view_o.createstart_px();
	@cherrypy.expose
	
	#-------------------------------------------------------
	def createPPAuswahlForm(self, id):
	#-------------------------------------------------------
		return self.createPPAuswahlForm_p(id)
	@cherrypy.expose	
	
	#-------------------------------------------------------
	def addStudent(self):
	#-------------------------------------------------------
		return self.createStudentForm_p()
	@cherrypy.expose
	
	#-------------------------------------------------------
	def addLehrer(self):
	#-------------------------------------------------------
		return self.createLehrerForm_p()
	@cherrypy.expose
	
	#-------------------------------------------------------
	def addFirma(self):
	#-------------------------------------------------------
		return self.createFirmenForm_p()
	@cherrypy.expose
	
	#-------------------------------------------------------
	def addPPA(self):
	#-------------------------------------------------------
			return self.createPPAForm_p()
	@cherrypy.expose	
	
	#-------------------------------------------------------
	def editStudent(self, id):
	#-------------------------------------------------------
		return self.createStudentForm_p(id)
	@cherrypy.expose
	
	#-------------------------------------------------------
	def editLehrer(self, id):
	#-------------------------------------------------------
		return self.createLehrerForm_p(id)
	@cherrypy.expose	

	def editFirma(self, id):
	#-------------------------------------------------------
		return self.createFirmenForm_p(id)
	@cherrypy.expose
	
	def editPPA(self, id):
	#-------------------------------------------------------
		return self.createPPAForm_p(id)
	@cherrypy.expose
	
	#-------------------------------------------------------
	def saveStudent(self, **data_opl):
	#-------------------------------------------------------
		id_s = data_opl["id_s"]
		data_a = {
		        "matrikelnr": int(data_opl["matrikelnr"])
		        , "name": data_opl["name"]
		        , "vorname": data_opl["vorname"]
		}
		if id_s != "None":
		# Update-Operation
			self.db_o.updateStudent_px(id_s, data_a)
		else:
		# Create-Operation
			id_s = self.db_o.createStudent_px(data_a)
			
		return self.createStudentList()	
	@cherrypy.expose
	
	#-------------------------------------------------------
	def saveLehrer(self, **data_opl):
	#-------------------------------------------------------
		id_s = data_opl["id_s"]
		data_a = {
		        "titel": data_opl["titel"]
		        , "name": data_opl["name"]
		        , "vorname": data_opl["vorname"]
		        , "lehrgebiet": data_opl["lehrgebiet"]
		}
		if id_s != "None":
		# Update-Operation
			self.db_o.updateLehrer_px(id_s, data_a)
		else:
		# Create-Operation
			id_s = self.db_o.createLehrer_px(data_a)
				
		return self.createLehrerList()	
	@cherrypy.expose
	
	#-------------------------------------------------------
	def saveFirma(self, **data_opl):
	#-------------------------------------------------------
		id_s = data_opl["id_s"]
		data_a = {
			"name": data_opl["name"]
			, "branche": data_opl["branche"]
			, "schwerpunkt": data_opl["schwerpunkt"]
			, "sitz": data_opl["sitz"]		        
		        , "mitarbeiteranzahl": int(data_opl["mitarbeiteranzahl"])
		}
		if id_s != "None":
		# Update-Operation
			self.db_o.updateFirma_px(id_s, data_a)
		else:
		# Create-Operation
			id_s = self.db_o.createFirma_px(data_a)
					
		return self.createFirmenList()	
	@cherrypy.expose
	
	#-------------------------------------------------------
	def savePPA(self, **data_opl):
	#-------------------------------------------------------
		data_o = self.db_o.readData_p()
		if data_opl["firmaid"] not in data_o['firma']['list']:
			return self.view_o.createPPAForm_px(data_opl["id_s"], data_opl, 'Firma nicht gefunden!')
		
		id_s = data_opl["id_s"]
		
		data_a = {
		        "pptitel": data_opl['pptitel'], 
		        "beschreibung": data_opl['beschreibung'], 
		        "firmaid": data_opl['firmaid'],
		        "voraussetzung": data_opl['voraussetzung'],
		        "kontakt": data_opl['kontakt'],
		        "lehrendenid": data_opl['lehrendenid'],
		        "matrikelid": data_opl['matrikelid'],
		        "anfangsdatum": data_opl['anfangsdatum'],
		        "enddatum": data_opl['enddatum']
		}
		
		if id_s != "None":
		# Update-Operation
			self.db_o.updatePPA_px(id_s, data_a)
		else:
		# Create-Operation
			self.db_o.createPPA_px(data_a)
						
		
		
		return self.createPPAList()	
	@cherrypy.expose
	
	#-------------------------------------------------------
	def savePPAktuell(self, **data_opl):
	#-------------------------------------------------------
		self.db_o.readData_p();
		case = self.db_o.savePPaktuell_px(**data_opl)
		
		if case == 1:
			return self.createPPAList()
		elif case == -1:
			return self.createPPAuswahlForm_p(data_opl['id_s'], 'Student nicht gefunden!')
		elif case == -2:
			return self.createPPAuswahlForm_p(data_opl['id_s'], 'Student bereits Eingetragen!')
	@cherrypy.expose	
	
	#-------------------------------------------------------
	def deleteStudent(self, id):
	#-------------------------------------------------------
		# Eintrag l�schen, dann Liste neu anzeigen
		self.db_o.deleteStudent_px(id)
		return self.createStudentList()
	@cherrypy.expose
	
	#-------------------------------------------------------
	def deleteLehrer(self, id):
	#-------------------------------------------------------
		# Eintrag l�schen, dann Liste neu anzeigen
		self.db_o.deleteLehrer_px(id)
		return self.createLehrerList()
	@cherrypy.expose
	
	#-------------------------------------------------------
	def deleteFirma(self, id):
	#-------------------------------------------------------
		# Eintrag l�schen, dann Liste neu anzeigen
		self.db_o.deleteFirma_px(id)
		return self.createFirmenList()
	@cherrypy.expose
	
	#-------------------------------------------------------
	def deletePPA(self, id):
	#-------------------------------------------------------
		# Eintrag l�schen, dann Liste neu anzeigen
		self.db_o.deletePPA_px(id)
		return self.createPPAList()
	@cherrypy.expose	
	
	#-------------------------------------------------------
	def createStudentList(self):
	#-------------------------------------------------------	
		data_o = self.db_o.readData_p()
		
		return self.view_o.createStudentList_px(data_o)
	@cherrypy.expose
	
	#-------------------------------------------------------
	def createLehrerList(self):
	#-------------------------------------------------------	
		data_o = self.db_o.readData_p()
		
		return self.view_o.createLehrerList_px(data_o)
	@cherrypy.expose
	
	def createFirmenList(self):
		#-------------------------------------------------------	
		data_o = self.db_o.readData_p()
			
		return self.view_o.createFirmenList_px(data_o)
	@cherrypy.expose
	
	#-------------------------------------------------------
	def createPPAList(self):
	#-------------------------------------------------------	
		data_o = self.db_o.readData_p()
				
		return self.view_o.createPPAList_px(data_o)
	@cherrypy.expose
	
	#-------------------------------------------------------
	def createAuswertungFirma(self):
	#-------------------------------------------------------	
		data_o = self.db_o.readData_p()
		
				
		return self.view_o.createAuswertungFirma_px(data_o)
	@cherrypy.expose
	
	#-------------------------------------------------------
	def createAuswertungStudent(self):
	#-------------------------------------------------------	
		data_o = self.db_o.readData_p()
			
		return self.view_o.createAuswertungStudent_px(data_o)
	@cherrypy.expose
	
	#-------------------------------------------------------
	def createAuswertungLehrer(self):
	#-------------------------------------------------------	
		data_o = self.db_o.readData_p()
				
		return self.view_o.createAuswertungLehrer_px(data_o)
	@cherrypy.expose	
	
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
	def createStudentForm_p(self, id_spl = None):
	#-------------------------------------------------------
		if id_spl != None:
			data_o = self.db_o.readStudent_px(id_spl)
		else:
			data_o = {
			        "matrikelnr": '', 
			        "name": '', 
			        "vorname": ''
			}
		# mit diesen Daten Markup erzeugen
		return self.view_o.createStudentForm_px(id_spl, data_o)
	
	#-------------------------------------------------------
	def createLehrerForm_p(self, id_spl = None):
	#-------------------------------------------------------
		if id_spl != None:
			data_o = self.db_o.readLehrer_px(id_spl)
		else:
			data_o = {
			        "titel": '', 
			        "name": '', 
			        "vorname": '',
			        "lehrgebiet": ''
			}
		# mit diesen Daten Markup erzeugen
		return self.view_o.createLehrerForm_px(id_spl, data_o)
	
	#-------------------------------------------------------
	def createFirmenForm_p(self, id_spl = None):
	#-------------------------------------------------------
		if id_spl != None:
			data_o = self.db_o.readFirma_px(id_spl)
		else:
			data_o = {
			        "name": '', 
			        "branche": '', 
			        "schwerpunkt": '',
			        "sitz": '',
			        "mitarbeiteranzahl": ''
			}
		# mit diesen Daten Markup erzeugen
		return self.view_o.createFirmenForm_px(id_spl, data_o)
	#-------------------------------------------------------
	def createPPAForm_p(self, id_spl = None):
	#-------------------------------------------------------
		if id_spl != None:
			data_o = self.db_o.readPPA_px(id_spl)
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
		# mit diesen Daten Markup erzeugen
		return self.view_o.createPPAForm_px(id_spl, data_o)
	
	#-------------------------------------------------------
	def createPPAuswahlForm_p(self, id_spl = None, alert = None):
	#-------------------------------------------------------
		data_o = self.db_o.readPPA_px(id_spl)
		
		return self.view_o.createPPAuswahlForm_px(id_spl, data_o, alert)	
# EOF
		
		
		
		
		
