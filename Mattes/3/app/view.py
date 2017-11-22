# coding: utf-8
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
		self.view = ['student'
		              ,'lehrende'
		              ,'firma'
		              ,'ppangebot'
		              ,'ppaktuell'
		              ,'ppabgeschlossen']	
		
		pass
	#-------------------------------------------------------
	def CreateIndex_px(self):
	#-------------------------------------------------------
		return self.readFile_p('hauptseite.html')
	
	#-------------------------------------------------------
	def CreateList_px(self, data_o, ansicht):
	#-------------------------------------------------------
		ListTemplate = ''
		with codecs.open(os.path.join('templates', 'list_template.tpl'), 'r', 'utf-8') as fp_o:
			ListTemplate = fp_o.read()
		
		template_o = template.Template(ListTemplate)
		markup = ""
	
		markup = template_o.render(data_o = data_o, ansicht = ansicht)

		return markup
	
	#-------------------------------------------------------
	def CreateForm_px(self, data_o, option, ansicht, id_s):
	#-------------------------------------------------------
		FormTemplate = ''
		with codecs.open(os.path.join('templates', 'form_template.tpl'), 'r', 'utf-8') as fp_o:
			FormTemplate = fp_o.read()

		template_o = template.Template(FormTemplate)
		markup = template_o.render(data_o = data_o, option = option, ansicht = ansicht, id_s = id_s)

		return markup
    
	# -------------------------------------------------------
	def readFile_p(self, fileName_spl):
	# -------------------------------------------------------   
		content_s = ''

		with codecs.open(os.path.join('static', fileName_spl), 'r', 'utf-8') as fp_o:
			content_s = fp_o.read()
            
		return content_s

# EOF
