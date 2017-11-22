# coding: utf-8
# sehr einfache Erzeugung des Markups f�r vollst�ndige Seiten
# jeweils 3 Abschnitte:
# - begin
# - content
# - end
# bei der Liste wird der content-Abschnitt wiederholt
# beim Formular nicht

import codecs
import os.path
import string
from mako import template
from mako.lookup import TemplateLookup

# ----------------------------------------------------------
class View_cl(object):
# ----------------------------------------------------------
    
    # -------------------------------------------------------
    def __init__(self):
    # -------------------------------------------------------
	self.ListTemplate_o = ''

        with codecs.open(os.path.join('template', 'list_template.tpl'), 'r', 'utf-8') as fp_o:
            self.ListTemplate_o = fp_o.read()
	
        pass
    #-------------------------------------------------------
    def CreateIndexMarkup(self):
    #-------------------------------------------------------
	return self.readFile_p('hauptseite.html')
	
    #-------------------------------------------------------
    def CreateList_px(self, data_o, option):
    #-------------------------------------------------------
	template = template.Template(self.ListTemplate)
	markup = ""
	
	#Studentenliste
	if option == 0:
	    markup = template.render(data_o = data_o['student']['list'], option = option)
	
	#Lehrendenliste
	elif option == 1:
	    markup = template.render(data_o = data_o['student']['lehrende']
	                             , option = option)
	
	#Firmaliste    
	elif option == 2:
	    markup = template.render(data_o = data_o['student']['firma']
	                             , option = option)
	
	#PPAngebotListe    
	elif option == 3:
	    markup = template.render(data_o = data_o['student']['ppangebot']
	                             , option = option)
	
	#Auswertung Firma    
	elif option == 4:
	    markup = template.render(data_o = data_o['student']['list']
	                             , option = option)
	
	#Auswertung Student
	elif option == 5:
	    markup = template.render(data_o = data_o['student']['list']
	                             , option = option)
	
	#Auswertung Lehrenden    
	elif option == 6:
	    markup = template.render(data_o = data_o['student']['list']
	                             , option = option)
	    
	
	return markup
    
    
    # -------------------------------------------------------
    def readFile_p(self, fileName_spl):
    # -------------------------------------------------------   
        content_s = ''

        with codecs.open(os.path.join('static', fileName_spl), 'r', 'utf-8') as fp_o:
            content_s = fp_o.read()
            
        return content_s

# EOF
