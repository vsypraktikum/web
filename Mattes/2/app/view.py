# coding: utf-8
# sehr einfache Erzeugung des Markups f�r vollst�ndige Seiten
# jeweils 3 Abschnitte:
# - begin
# - content
# - end
# bei der Liste wird der content-Abschnitt wiederholt
# beim Formular nicht

import mako
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
        pass
    
    # -------------------------------------------------------
    def createstart_px(self):
    # -------------------------------------------------------
        return self.readFile_p('index.html')
    
    # -------------------------------------------------------
    def createStudentList_px(self, data_opl):
    # -------------------------------------------------------
        data_opl = data_opl['student']['list']
        template_o = template.Template(self.readTemplate_p('student_list.tpl'))
        return template_o.render(data_o=data_opl)           
    
    
    # -------------------------------------------------------
    def createLehrerList_px(self, data_opl):
    # -------------------------------------------------------
        data_opl = data_opl['lehrer']['list']
        template_o = template.Template(self.readTemplate_p('lehrer_list.tpl'))
        return template_o.render(data_o = data_opl)  
    
    # -------------------------------------------------------
    def createFirmenList_px(self, data_opl):
    # -------------------------------------------------------
        data_opl = data_opl['firma']['list']
        template_o = template.Template(self.readTemplate_p('firma_list.tpl'))
        return template_o.render(data_o=data_opl)  
    
    # -------------------------------------------------------
    def createPPAList_px(self, data_opl):
    # -------------------------------------------------------
        data_opl = data_opl['ppangebot']['list']
        template_o = template.Template(self.readTemplate_p('ppa_list.tpl'))
        return template_o.render(data_o=data_opl) 
    
    # -------------------------------------------------------
    def createAuswertungFirma_px(self, data_opl):
    # -------------------------------------------------------
        ppangebot = data_opl['ppangebot']['list']
        ppaktuell = data_opl['ppaktuell']['list']  
        ppabgeschlossen = data_opl['ppabgeschlossen']['list']

        for key in ppangebot:
            ppangebot[key].update(data_opl['firma']['list'][ppangebot[key]['firmaid']])

        for key in range(0, len(ppaktuell)):
            ppaktuell[key].update(data_opl['firma']['list'][ppaktuell[key]['firmaid']])
   
        ppaktuell.sort(key=lambda x: x['anfangsdatum'])
            
        for key in range(0, len(ppabgeschlossen)):
            ppabgeschlossen[key].update(data_opl['firma']['list'][ppabgeschlossen[key]['firmaid']])        
            
        ppabgeschlossen.sort(key=lambda x: x['anfangsdatum'])
        
        template_o = template.Template(self.readTemplate_p('auswertungFirma.tpl'))
        return template_o.render(ppangebot_o = ppangebot, ppaktuell_o = ppaktuell, ppabgeschlossen_o = ppabgeschlossen)
    
    # -------------------------------------------------------
    def createAuswertungStudent_px(self, data_opl):
    # -------------------------------------------------------
        ppaktuell = data_opl['ppaktuell']['list']  
        ppabgeschlossen = data_opl['ppabgeschlossen']['list']

        for key in range(0, len(ppaktuell)):
            ppaktuell[key].update(data_opl['student']['list'][ppaktuell[key]['matrikelid']])
   
        ppaktuell.sort(key=lambda x: x['vorname'])
            
        for key in range(0, len(ppabgeschlossen)):
            ppabgeschlossen[key].update(data_opl['student']['list'][ppabgeschlossen[key]['matrikelid']])        
            
        ppabgeschlossen.sort(key=lambda x: x['vorname'])
        
        template_o = template.Template(self.readTemplate_p('auswertungStudent.tpl'))
        return template_o.render(ppaktuell_o = ppaktuell, ppabgeschlossen_o = ppabgeschlossen)
    
    # -------------------------------------------------------
    def createAuswertungLehrer_px(self, data_opl):
    # -------------------------------------------------------
        ppaktuell = data_opl['ppaktuell']['list']  
        ppabgeschlossen = data_opl['ppabgeschlossen']['list']
    
        for key in range(0, len(ppaktuell)):
            ppaktuell[key].update(data_opl['lehrer']['list'][ppaktuell[key]['lehrendenid']])
       
        ppaktuell.sort(key=lambda x: x['vorname'])
                
        for key in range(0, len(ppabgeschlossen)):
            ppabgeschlossen[key].update(data_opl['lehrer']['list'][ppabgeschlossen[key]['lehrendenid']])        
                
        ppabgeschlossen.sort(key=lambda x: x['vorname'])
            
        template_o = template.Template(self.readTemplate_p('auswertungLehrer.tpl'))
        return template_o.render(ppaktuell_o = ppaktuell, ppabgeschlossen_o = ppabgeschlossen)     

    # -------------------------------------------------------
    def createStudentForm_px(self, id_spl, data_opl):
    # -------------------------------------------------------
        # hier m�sste noch eine Fehlerbehandlung erg�nzt werden !
        template_o = template.Template(self.readTemplate_p('studentform.tpl'))
        return template_o.render(data_o=data_opl, key_s = id_spl) 


    # -------------------------------------------------------
    def createLehrerForm_px(self, id_spl, data_opl):
    # -------------------------------------------------------
        # hier m�sste noch eine Fehlerbehandlung erg�nzt werden !
        template_o = template.Template(self.readTemplate_p('lehrerform.tpl'))
        return template_o.render(data_o=data_opl, key_s = id_spl)     
    
    # -------------------------------------------------------
    def createFirmenForm_px(self, id_spl, data_opl):
    # -------------------------------------------------------
        # hier m�sste noch eine Fehlerbehandlung erg�nzt werden !
        template_o = template.Template(self.readTemplate_p('firmaform.tpl'))
        return template_o.render(data_o=data_opl, key_s = id_spl)
    
    # -------------------------------------------------------
    def createPPAForm_px(self, id_spl, data_opl, alert = ''):
    # -------------------------------------------------------
        # hier m�sste noch eine Fehlerbehandlung erg�nzt werden !
        template_o = template.Template(self.readTemplate_p('ppaform.tpl'))
        return template_o.render(data_o=data_opl, key_s = id_spl, alert = alert)
    # -------------------------------------------------------
    def createPPAuswahlForm_px(self, id_spl, data_opl, alert_s):
    # -------------------------------------------------------
        template_o = template.Template(self.readTemplate_p('ppauswahlform.tpl'))
        return template_o.render(data_o=data_opl, key_s = id_spl, alert = alert_s)

    # -------------------------------------------------------
    def readFile_p(self, fileName_spl):
    # -------------------------------------------------------   
        content_s = ''

        with codecs.open(os.path.join('static', fileName_spl), 'r', 'utf-8') as fp_o:
            content_s = fp_o.read()
            
        return content_s
    
    # -------------------------------------------------------
    def readTemplate_p(self, fileName_spl):
    # -------------------------------------------------------   
        content_s = ''
    
        with codecs.open(os.path.join('templates', fileName_spl), 'r', 'utf-8') as fp_o:
            content_s = fp_o.read()
                
        return content_s
    
        
# EOF
