# coding: utf-8
import cherrypy
from .database import Database_cl
from .view import View_cl
#----------------------------------------------------------
class Application_cl(object):
#----------------------------------------------------------

	userrole = ""
	#-------------------------------------------------------
	def __init__(self):
	#-------------------------------------------------------
		# spezielle Initialisierung können hier eingetragen werden
		self.db_o = Database_cl()
		self.view_o = View_cl()
	@cherrypy.expose
	#-------------------------------------------------------
	def index(self):
	#-------------------------------------------------------
		return self.view_o.loginfunc("loginStudierende.tpl")
	#-------------------------------------------------------
	@cherrypy.expose
	#-------------------------------------------------------
	def login(self, **data_opl):
	#-------------------------------------------------------
		dat = data_opl["username"]
		if(dat.find("@stud.hn.de") == -1):
			return self.view_o.loginfuncLehrender("loginLehrende.tpl")
		else:
			return self.student()	
	#-------------------------------------------------------
	@cherrypy.expose
	#-------------------------------------------------------
	def studiengang(self, id):
	#-------------------------------------------------------
		data_o = self.db_o.readData_Studiengang()
		data_mod = self.db_o.readData_Modul()
		data_lehr = self.db_o.readData_Lehrveranstaltung()
		for i in data_o.values():
			if(i[1] == id):
				return self.view_o.showStudiengang(id, data_o, data_mod, data_lehr, "formStudiengang.tpl")
		return self.error()
	#-------------------------------------------------------
	@cherrypy.expose
	#-------------------------------------------------------
	def editStudiengang(self, id):
	#-------------------------------------------------------
		return self.createStudiengang(id)
	#-------------------------------------------------------
	@cherrypy.expose
	#-------------------------------------------------------
	def editModul(self, id):
	#-------------------------------------------------------
		return self.createModul(id)
	#-------------------------------------------------------
	@cherrypy.expose
	#-------------------------------------------------------
	def editLehrveranstaltung(self, id):
	#-------------------------------------------------------
		return self.createLehrveranstaltung(id)
	#-------------------------------------------------------
	@cherrypy.expose
	#-------------------------------------------------------
	def deleteStudiengang(self, id):
	#-------------------------------------------------------
		self.db_o.delete_Studiengang(id)
		return self.lehr()
	#-------------------------------------------------------
	@cherrypy.expose
	#-------------------------------------------------------
	def deleteModul(self, id):
	#-------------------------------------------------------
		self.db_o.delete_Modul(id)
		return self.lehr()
	#-------------------------------------------------------
	@cherrypy.expose
	#-------------------------------------------------------
	def deleteLehrveranstaltung(self, id):
	#-------------------------------------------------------
		self.db_o.delete_Lehrveranstaltung(id)
		return self.lehr()
	#-------------------------------------------------------
	@cherrypy.expose
	#-------------------------------------------------------
	def error(self):
	#-------------------------------------------------------
		return self.view_o.error("formError.tpl")
	#-------------------------------------------------------
	@cherrypy.expose
	#-------------------------------------------------------
	def loginL(self, **data_opl):
	#-------------------------------------------------------	
		global userrole
		name = data_opl["username"]	
		pw = data_opl["password"]
		user = self.db_o.read_rolle(name)
		if(name == user[0] and pw == user[1]):
			if(user[2] == "mod"):
				userrole = "Bernd"
				return self.modul()
			else:
				return self.lehr()
		else:
			return self.view_o.loginfunc("loginStudierende.tpl")
	#-------------------------------------------------------
	@cherrypy.expose
	#-------------------------------------------------------
	def student(self, **data_opl):
	#-------------------------------------------------------
	#	self.db_o.readData_p("studiengang.json")
		dat = self.db_o.data_o
		return self.view_o.rolleStudent("formStudierender.tpl", dat)
	#-------------------------------------------------------
	@cherrypy.expose
	#-------------------------------------------------------
	def lehr(self, **data_opl):
	#-------------------------------------------------------
	#	self.db_o.readData_p('studiengang.json')
		dat = self.db_o.data_o
	#	self.db_o.readData_p('modul.json')
		mod = self.db_o.data_m
		lehr = self.db_o.data_l
		return self.view_o.rolleStudiengang("formVerantwortlicherStudiengang.tpl", dat, mod, lehr)
	#-------------------------------------------------------
	@cherrypy.expose
	#-------------------------------------------------------
	def modul(self, **data_opl):
	#-------------------------------------------------------
	#	self.db_o.readData_p('studiengang.json')
		dat = self.db_o.data_o
	#	self.db_o.readData_p('modul.json')
		modul = self.db_o.data_m
		return self.view_o.rolleModul("formVerantwortlicherModul.tpl", dat, modul)
	#-------------------------------------------------------
	@cherrypy.expose
	#-------------------------------------------------------
	def createModul(self, id_spl = None):
	#-------------------------------------------------------
		if id_spl != None:
			dat_m = self.db_o.readData_Modul_single(id_spl)
		else:
			dat_m = self.db_o.getEmptyModul()
		return self.view_o.createModul(id_spl, dat_m, "formCreateModul.tpl")  
	@cherrypy.expose
	#-------------------------------------------------------
	def createStudiengang(self, id_spl = None):
	#-------------------------------------------------------
		if id_spl != None:
			data_o = self.db_o.readData_Studiengang_single(id_spl)
		else:
			data_o = self.db_o.getEmptyStudiengang()
		return self.view_o.createStudiengang(id_spl, data_o, "formCreateStudiengang.tpl")   
	@cherrypy.expose 
	#-------------------------------------------------------
	def createLehrveranstaltung(self, id_spl = None):
	#-------------------------------------------------------
		if id_spl != None:
			data_l = self.db_o.readData_Lehrveranstaltung_single(id_spl)
		else:
			data_l = self.db_o.getEmptyLehrveranstaltung()
		return self.view_o.createLehrveranstaltung(id_spl, data_l, "formCreateLehrveranstaltung.tpl")   
	#-------------------------------------------------------
	@cherrypy.expose 
	#-------------------------------------------------------
	def saveStudiengang(self, **data_opl):
	#-------------------------------------------------------      
		id_s = data_opl["id_s"]
		data_a = [ data_opl["bezeichnungStudiengang"]
		,	data_opl["kurzbezeichnungStudiengang"]
		,	data_opl["beschreibungStudiengang"]
		,	data_opl["semesteranzahlStudiengang"]
		,	[]
		]   
		if id_s != "None":
			self.db_o.update_Studiengang(id_s, data_a)
		else:
			id_s = self.db_o.create_Studiengang(data_a)
		return self.createStudiengang(id_s)
	#-------------------------------------------------------
	@cherrypy.expose 
	#-------------------------------------------------------
	def saveLehrveranstaltung(self, **data_opl):
	#-------------------------------------------------------        
		id_s = data_opl["id_s"]
		data_l = [ data_opl["bezeichnungLehrveranstaltung"]
		,	data_opl["beschreibungLehrveranstaltung"]
		,	data_opl["lageLehrveranstaltung"]
		,	data_opl["modulLehrveranstaltung"]
		,	data_opl["studiengangKurzbezeichnung"]
		,	[]
		]   
		if id_s != "None":
			self.db_o.update_Lehrveranstaltung(id_s, data_l)
		else:
			id_s = self.db_o.create_Lehrveranstaltung(data_l)
		return self.createLehrveranstaltung(id_s)
	#-------------------------------------------------------
	@cherrypy.expose
	#-------------------------------------------------------
	def saveModul(self, **data_opl):
	#-------------------------------------------------------
		id_s = data_opl["studiengangID"]
		data_z = [ data_opl["bezeichnungModul"]
		,	data_opl["beschreibungModul"]
		,	data_opl["anzahlCredits"]
		,	data_opl["anzahlVorlesung"]
		,	data_opl["anzahlUebung"]
		,	data_opl["anzahlPraktika"]
		,	data_opl["voraussetzungen"]
		,	data_opl["modulVerantwortlicher"]
		,	data_opl["studiengangKurzbezeichnung"]
        ]
        
		if id_s != "None":
			self.db_o.update_Modul(id_s, data_z)
		else:
			id_s = self.db_o.create_Modul(data_z)
		return self.createModul(id_s)
# EOF
