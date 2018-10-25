# coding: utf-8
import codecs
import os.path
import string

from mako.template import Template
from mako.lookup import TemplateLookup
#----------------------------------------------------------
class View_cl(object):
#----------------------------------------------------------
	#-------------------------------------------------------
	def __init__(self):
	#-------------------------------------------------------
		self.path_s = os.path.join(os.getcwd(), "templates")
		self.lookup_o = TemplateLookup(directories=self.path_s, module_directory=self.path_s)
	#-------------------------------------------------------
	def loginfunc(self, template_spl):
	#-------------------------------------------------------
		template_o = self.lookup_o.get_template(template_spl)
		markup_s = template_o.render() 
		return markup_s
		#-------------------------------------------------------
	def error(self, template_spl):
	#-------------------------------------------------------
		template_o = self.lookup_o.get_template(template_spl)
		markup_s = template_o.render() 
		return markup_s
	#-------------------------------------------------------
	def loginfuncLehrender(self, template_spl):
	#-------------------------------------------------------
		template_o = self.lookup_o.get_template(template_spl)
		markup_s = template_o.render()
		return markup_s
	#-------------------------------------------------------
	def rolleStudent(self, template_spl, data_opl):
	#-------------------------------------------------------
		template_o = self.lookup_o.get_template(template_spl)
		markup_s = template_o.render(data_o = data_opl)
		return markup_s
	#-------------------------------------------------------
	def rolleModul(self, template_spl, dat, modul):
	#-------------------------------------------------------
		template_o = self.lookup_o.get_template(template_spl)
		markup_s = template_o.render(data_o = dat, data_modul = modul)
		return markup_s
	#-------------------------------------------------------
	def rolleStudiengang(self, template_spl, dat, mod, lehr):
	#-------------------------------------------------------
		template_o = self.lookup_o.get_template(template_spl)
		markup_s = template_o.render(data_o = dat, data_mod = mod, data_lehr = lehr)
		return markup_s
    #-------------------------------------------------------
	def createModul(self, id_spl, data_opl, template_spl):
    #-------------------------------------------------------
		markup_s =''
		template_o = self.lookup_o.get_template(template_spl)
		markupV_s = template_o.render()
		lineT_o = string.Template(markupV_s)
		markup_s += lineT_o.safe_substitute (bezeichnungModul=data_opl[0]
			,   beschreibungModul=data_opl[1]
			,   anzahlCredits=data_opl[2]
			,   anzahlVorlesung=data_opl[3]
			,   anzahlUebung=data_opl[4]
			,   anzahlPraktika=data_opl[5]
			,   voraussetzungen=data_opl[6]
			,   modulVerantwortlicher=data_opl[7]
			,   studiengangKurzbezeichnung=data_opl[8]
			,   studiengangID=id_spl
			)
		return markup_s 
	#-------------------------------------------------------
	def createStudiengang(self, id_spl, data_opl, template_spl):
    #-------------------------------------------------------
		markup_s =''
		template_o = self.lookup_o.get_template(template_spl)
		markupV_s = template_o.render()
		lineT_o = string.Template(markupV_s)
		markup_s += lineT_o.safe_substitute (bezeichnungStudiengang=data_opl[0]
				,	kurzbezeichnungStudiengang=data_opl[1]
				,	beschreibungStudiengang=data_opl[2]
				,	semesteranzahlStudiengang=data_opl[3]
				,   id_s=id_spl
				)
		return markup_s
	#-------------------------------------------------------
	def showStudiengang(self, id_spl, data_opl, data_opl2, data_opl3, template_spl):
    #-------------------------------------------------------
		template_o = self.lookup_o.get_template(template_spl)
		markup_s = template_o.render(id_s = id_spl, data_o = data_opl, data_mod = data_opl2, data_lehr = data_opl3)
		return markup_s
	#-------------------------------------------------------
	def createLehrveranstaltung(self, id_spl, data_opl, template_spl):
    #-------------------------------------------------------
		markup_s =''
		template_o = self.lookup_o.get_template(template_spl)
		markupV_s = template_o.render()
		lineT_o = string.Template(markupV_s)
		markup_s += lineT_o.safe_substitute (bezeichnungLehrveranstaltung=data_opl[0]
				,	beschreibungLehrveranstaltung=data_opl[1]
				,	lageLehrveranstaltung=data_opl[2]
				,	modulLehrveranstaltung=data_opl[3]
				,	studiengangKurzbezeichnung=data_opl[4]
				,   id_s=id_spl
				)
		return markup_s
	#-------------------------------------------------------
	def createModulhandbuch(self, id_spl, data_opl, data_opl2, data_opl3, template_spl):
	#-------------------------------------------------------
		template_o = self.lookup_o.get_template(template_spl)
		markup_s = template_o.render(id_stg = id_spl, data_o = data_opl, data_l = data_opl2, data_m = data_opl3)
		return markup_s
	#-------------------------------------------------------
	def showModulhandbuch(self, id_spl, data_opl, data_opl2, template_spl):
    #-------------------------------------------------------
		template_o = self.lookup_o.get_template(template_spl)
		markup_s = template_o.render(id_s = id_spl, data_o = data_opl, data_mod = data_opl2)
		return markup_s
	#-------------------------------------------------------
	def readFile_p(self, fileName_spl):
	#-------------------------------------------------------
		content_s = ''
		with codecs.open(os.path.join('templates', fileName_spl), 'r', 'utf-8') as fp_o:
			content_s = fp_o.read()
		return content_s
# EOF
