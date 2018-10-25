# coding: utf-8

# sehr einfache Erzeugung des Markups für vollständige Seiten
# jeweils 3 Abschnitte:
# - begin
# - content
# - end

# bei der Liste wird der content-Abschnitt wiederholt
# beim Formular nicht

import codecs
import os.path
import string

#----------------------------------------------------------
class View_cl(object):
#----------------------------------------------------------

	#-------------------------------------------------------
	def __init__(self):
	#-------------------------------------------------------
		pass

	#-------------------------------------------------------
	def createList_px(self, data_opl):
	#-------------------------------------------------------
		# hier müsste noch eine Fehlerbehandlung ergänzt werden !
		markup_s = ''
		markup_s += self.readFile_p('list0.tpl')

		markupV_s = self.readFile_p('list1.tpl')
		lineT_o = string.Template(markupV_s)
		# mehrfach nutzen, um die einzelnen Zeilen der Tabelle zu erzeugen
		for loop_i in range(0,15):
			data_a = data_opl[str(loop_i)]
			markup_s += lineT_o.safe_substitute (name1_s=data_a[0] # HIER müssen Sie eine Ergänzung vornehmen
			, vorname1_s=data_a[1]
			, matrnr1_s=data_a[2]
			, name2_s=data_a[3]
			, vorname2_s=data_a[4]
			, matrnr2_s=data_a[5]
			, id_s=str(loop_i)
			)

		markup_s += self.readFile_p('list2.tpl')

		return markup_s
		
	#-------------------------------------------------------
	def createForm_px(self, id_spl, data_opl):
	#-------------------------------------------------------

		# hier müsste noch eine Fehlerbehandlung ergänzt werden !
		markup_s = ''
		markup_s += self.readFile_p('form0.tpl')

		markupV_s = self.readFile_p('form1.tpl')
		lineT_o = string.Template(markupV_s)
		markup_s += lineT_o.safe_substitute (name1_s=data_opl[0] # HIER müssen Sie eine Ergänzung vornehmen
		, vorname1_s=data_opl[1]
		, matrnr1_s=data_opl[2]
		, name2_s=data_opl[3]
		, vorname2_s=data_opl[4]
		, matrnr2_s=data_opl[5]
		, id_s=id_spl
		)

		markup_s += self.readFile_p('form2.tpl')
		
		return markup_s
		
	#-------------------------------------------------------
	def readFile_p(self, fileName_spl):
	#-------------------------------------------------------
		content_s = ''
		with codecs.open(os.path.join('content', fileName_spl), 'r', 'utf-8') as fp_o:
			content_s = fp_o.read()
			
		return content_s
# EOF