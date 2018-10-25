# coding: utf-8
import os
import os.path
import codecs
import json
#----------------------------------------------------------
class Database_cl(object):
#----------------------------------------------------------
	def __init__(self):
	#-------------------------------------------------------
		self.dataID_o = None
		self.data_o = None #Liste für Studiengänge
		self.data_l = None #Liste für Lehrveranstaltungen
		self.data_m = None #Liste für Module
		self.data_u = None #Liste für Benutzer
		self.data_temp = None #Liste für Temporäres
		self.readDataID() #Filestream für ID --> ID.json
		self.readData_Studiengang()  #Filestream für Data_o --> studiengang.json
		self.readData_User() #Filestream für Data_u --> user.json
		self.readData_Lehrveranstaltung() #Filestream für Data_l --> lehrveranstaltung.json
		self.readData_Modul() #Filestream für Data_l --> modul.json
	#-------------------------------------------------------
	def create_Studiengang(self, data_opl):
	#-------------------------------------------------------
		self.getNewID()
		id_s = str(self.dataID_o)
		self.data_o[id_s] = data_opl
		self.saveData_Studiengang()        
		return 
	#-------------------------------------------------------
	def create_Modul(self, data_opl):
	#-------------------------------------------------------
		self.getNewID()
		id_s = str(self.dataID_o)
		self.data_m[id_s] = data_opl
		self.saveData_Modul()        
		return 
	#-------------------------------------------------------
	def create_Lehrveranstaltung(self, data_opl):
	#-------------------------------------------------------
		self.getNewID()
		id_s = str(self.dataID_o)
		self.data_l[id_s] = data_opl
		self.saveData_Lehrveranstaltung()        
		return 
	#-------------------------------------------------------
	def delete_Studiengang(self, id_spl):
	#-------------------------------------------------------
	#Löschvorgang für Studiengaenge
		status_b = False
		for key in self.data_o:
			if self.data_o[key][1] == id_spl:
				del self.data_o[key]
				self.saveData_Studiengang()
				status_b = True
				return status_b	   
		return status_b		
	#-------------------------------------------------------
	def delete_Modul(self, id_spl):
	#-------------------------------------------------------
	#Löschvorgang für Modul
		status_b = False
		for key in self.data_m:
			if self.data_m[key][0] == id_spl:
				del self.data_m[key]
				self.saveData_Modul()
				status_b = True
				return status_b	   
		return status_b		
	#-------------------------------------------------------
	def delete_Lehrveranstaltung(self, id_spl):
	#-------------------------------------------------------
	#Löschvorgang für Lehrveranstaltung
		status_b = False
		for key in self.data_l:
			if self.data_l[key][0] == id_spl:
				del self.data_l[key]
				self.saveData_Lehrveranstaltung()
				status_b = True
				return status_b	   
		return status_b
	#-------------------------------------------------------
	def update_Studiengang(self, id_spl, data_opl):
	#-------------------------------------------------------
		status_b = False
		for key in self.data_o:
			if self.data_o[key][1] == id_spl:
				self.data_o[key] = data_opl
				self.saveData_Studiengang()
				status_b = True
				return self.data_o[key]   
		return status_b		
	#-------------------------------------------------------
	def update_Modul(self, id_spl, data_opl):
	#-------------------------------------------------------
		status_b = False
		for key in self.data_m:
			if self.data_m[key][0] == id_spl:
				self.data_m[key] = data_opl
				self.saveData_Modul()
				status_b = True
				return self.data_m[key]	   
		return status_b			
	#-------------------------------------------------------
	def update_Lehrveranstaltung(self, id_spl, data_opl):
	#-------------------------------------------------------
		status_b = False
		for key in self.data_l:
			if self.data_l[key][0] == id_spl:
				self.data_l[key] = data_opl
				self.saveData_Lehrveranstaltung()
				status_b = True
				return self.data_l[key]   
		return status_b	
	#-------------------------------------------------------
	def getNewID(self):
	#-------------------------------------------------------
		tmpID = None
		self.tmpID = self.dataID_o
		self.dataID_o = self.tmpID + 1
		self.saveDataID()
	#-------------------------------------------------------
	def getEmptyModul(self):
    #-------------------------------------------------------
		return ['', '', '', '', '', '', '', '', ''] 
	#-------------------------------------------------------
	def getEmptyStudiengang(self):
    #-------------------------------------------------------
		return ['', '', '', '', '', '', '', '', ''] 
	#-------------------------------------------------------
	def getEmptyLehrveranstaltung(self):
    #-------------------------------------------------------
		return ['', '', '', '', '', '', '', '', ''] 
	#-------------------------------------------------------
	def read_px(self, id_spl = None):
	#-------------------------------------------------------
		data_o = self.readData_Studiengang()
		if id_spl == None:
			data_o = self.data_o
		else:
			if id_spl in self.data_o:
				data_o = self.data_o[id_spl]
		return data_o
	#-------------------------------------------------------
	def read_modul_px(self, id_spl = None):
	#-------------------------------------------------------
		data_m = self.readData_Modul()
		if id_spl == None:
			data_m = self.data_m
		else:
			if id_spl in self.data_m:
				data_m = self.data_m[id_spl]
		return data_m
	#-------------------------------------------------------
	def read_lehrveranstaltung_px(self, id_spl = None):
	#-------------------------------------------------------
		data_l = self.readData_Lehrveranstaltung()
		if id_spl == None:
			data_l = self.data_l
		else:
			if id_spl in self.data_l:
				data_l = self.data_l[id_spl]
		return data_l
	#-------------------------------------------------------
	def readDataID(self):
	#-------------------------------------------------------
		try:
			fp_id = codecs.open(os.path.join('data', 'ID.json'), 'r', 'utf-8')
		except:
			# Datei neu anlegen
			self.dataID_o = 0
			self.saveDataID()
		else:
			with fp_id:
				self.dataID_o = json.load(fp_id)
		return self.dataID_o
	#-------------------------------------------------------
	def readData_p(self, dat):
	#-------------------------------------------------------
		try:
			fp_o = codecs.open(os.path.join('data', dat), 'r', 'utf-8')
		except:
			pass
		else:
			with fp_o:
				self.data_temp = json.load(fp_o)
		return self.data_temp
	#-------------------------------------------------------
	def readData_Studiengang(self):
	#-------------------------------------------------------
		try:
			fp_s = codecs.open(os.path.join('data', 'studiengang.json'), 'r', 'utf-8')
		except:
			# Datei neu anlegen
			self.data_o = {}
			self.saveData_Studiengang()
		else:
			with fp_s:
				self.data_o = json.load(fp_s)
		return self.data_o
	#-------------------------------------------------------
	def readData_User(self):
	#-------------------------------------------------------
		try:
			fp_u = codecs.open(os.path.join('data', 'user.json'), 'r', 'utf-8')
		except:
			# Datei neu anlegen
			self.data_u = {}
			self.saveData_User()
		else:
			with fp_u:
				self.data_u = json.load(fp_u)
		return self.data_u
	#-------------------------------------------------------
	def readData_Lehrveranstaltung(self):
	#-------------------------------------------------------
		try:
			fp_l = codecs.open(os.path.join('data', 'lehrveranstaltung.json'), 'r', 'utf-8')
		except:
			# Datei neu anlegen
			self.data_l = {}
			self.saveData_Lehrveranstaltung()
		else:
			with fp_l:
				self.data_l = json.load(fp_l)   
		return self.data_l
	#-------------------------------------------------------
	def readData_Modul(self):
	#-------------------------------------------------------
		try:
			fp_m = codecs.open(os.path.join('data', 'modul.json'), 'r', 'utf-8')
		except:
			# Datei neu anlegen
			self.data_m = {}
			self.saveData_Modul()
		else:
			with fp_m:
				self.data_m = json.load(fp_m)		
		return self.data_m
	#-------------------------------------------------------
	def readData_Modul_single(self, id_spl):
	#-------------------------------------------------------		
		status_b = False
		for key in self.data_m:
			if self.data_m[key][0] == id_spl:
				status_b = True
				return self.data_m[key]	   
		return status_b	
	#-------------------------------------------------------
	def readData_Studiengang_single(self, id_spl):
	#-------------------------------------------------------		
		status_b = False
		for key in self.data_o:
			if self.data_o[key][1] == id_spl:
				status_b = True
				return self.data_o[key]	   
		return status_b	
	#-------------------------------------------------------
	def readData_Lehrveranstaltung_single(self, id_spl):
	#-------------------------------------------------------		
		status_b = False
		for key in self.data_l:
			if self.data_l[key][0] == id_spl:
				status_b = True
				return self.data_l[key]	   
		return status_b	
	#-------------------------------------------------------	
	def read_rolle(self, id_name = None):
	#-------------------------------------------------------
		self.readData_User()
		data_u = None
		if id_name in self.data_u:
			data_u = self.data_u[id_name]
		return data_u
	#-------------------------------------------------------
	def saveData_p(self, dat):
	#-------------------------------------------------------
		with codecs.open(os.path.join('data', dat), 'w', 'utf-8') as fp_t:
			json.dump(self.data_temp, fp_t)
	#-------------------------------------------------------
	def saveDataID(self):
	#-------------------------------------------------------
		with codecs.open(os.path.join('data', 'ID.json'), 'w', 'utf-8') as fp_id:
			json.dump(self.dataID_o, fp_id)    
	#-------------------------------------------------------
	def saveData_Studiengang(self):
	#-------------------------------------------------------
		with codecs.open(os.path.join('data', 'studiengang.json'), 'w', 'utf-8')as fp_o:
			json.dump(self.data_o, fp_o, sort_keys=True)   
	#-------------------------------------------------------
	def saveData_User(self):
	#-------------------------------------------------------
		with codecs.open(os.path.join('data', 'user.json'), 'w', 'utf-8')as fp_b:
			json.dump(self.data_u, fp_b, sort_keys=True)  
	#-------------------------------------------------------
	def saveData_Lehrveranstaltung(self):
	#-------------------------------------------------------
		with codecs.open(os.path.join('data', 'lehrveranstaltung.json'), 'w', 'utf-8')as fp_l:
			json.dump(self.data_l, fp_l, sort_keys=True)          
	#-------------------------------------------------------
	def saveData_Modul(self):
	#-------------------------------------------------------
		with codecs.open(os.path.join('data', 'modul.json'), 'w', 'utf-8')as fp_m:
			json.dump(self.data_m, fp_m, sort_keys=True) 
# EOF
