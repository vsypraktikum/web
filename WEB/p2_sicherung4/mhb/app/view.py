# coding: utf-8
import os.path
import codecs
import string

from mako.template import Template
from mako.lookup import TemplateLookup

#----------------------------------------------------------
class View_cl(object):
#----------------------------------------------------------

    #-------------------------------------------------------
    def __init__(self):
    #-------------------------------------------------------
        # Pfad hier zur Vereinfachung fest vorgeben
        self.path_s = "C:\\Users\\Mark\\Python_Projects\\web\\p2\\mhb\\template"
        self.lookup_o = TemplateLookup(directories=self.path_s)
    
    # ... weitere Methoden

    #-------------------------------------------------------
    def createList_error_px(self, data_opl):
    #-------------------------------------------------------
        #Generierung des Loginforms für die Anmeldung mit dem Benutzernamen
        return self.createTemplate_p('error_login.tpl', data_opl)     
    
    #-------------------------------------------------------
    def createList_modulhandbuch_px(self, id_spl, data_opl, data_opl2, data_opl3):
    #-------------------------------------------------------
        #Generierung des Loginforms für die Anmeldung mit dem Benutzernamen
        return self.createTemplate_mhb_p('liste_modulhandbuch.tpl', id_spl, data_opl, data_opl2, data_opl3)    
    
    #-------------------------------------------------------
    def createTemplate_p(self, template_spl, data_opl):
    #-------------------------------------------------------
        # Auswertung mit templates
        template_o = self.lookup_o.get_template(template_spl)
        # mit der Methode render wird das zuvor 'übersetzte' Template ausgeführt
        # data_o sind die im Template angegebenen Daten
        # data_opl die übergebenen Daten
        
        markup_s = template_o.render(data_o = data_opl)
        return markup_s
    
    #-------------------------------------------------------
    def createTemplate_mit_kbez_p(self, template_spl, kbez, data_opl):
    #-------------------------------------------------------
        # Auswertung mit templates
        template_o = self.lookup_o.get_template(template_spl)
        # mit der Methode render wird das zuvor 'übersetzte' Template ausgeführt
        # data_o sind die im Template angegebenen Daten
        # data_opl die übergebenen Daten
        
        markup_s = template_o.render(stg_kbez = kbez, data_o = data_opl)
        return markup_s    

    #-------------------------------------------------------
    def createTemplate2_p(self, template_spl, data_opl, data_opl2):
    #-------------------------------------------------------
        # Auswertung mit templates
        template_o = self.lookup_o.get_template(template_spl)
        # mit der Methode render wird das zuvor 'übersetzte' Template ausgeführt
        # data_o sind die im Template angegebenen Daten
        # data_opl die übergebenen Daten
        
        markup_s = template_o.render(data_o = data_opl, data_m = data_opl2)
        return markup_s

    #-------------------------------------------------------
    def createTemplate_modul_p(self, template_spl, data_opl, data_opl2, benutzer):
    #-------------------------------------------------------
        # Auswertung mit templates
        template_o = self.lookup_o.get_template(template_spl)
        # mit der Methode render wird das zuvor 'übersetzte' Template ausgeführt
        # data_o sind die im Template angegebenen Daten
        # data_opl die übergebenen Daten
        
        markup_s = template_o.render(data_o = data_opl, data_m = data_opl2, modulv = benutzer)
        return markup_s
    
    #-------------------------------------------------------
    def createTemplate_mhb_p(self, template_spl, id_spl, data_opl, data_opl2, data_opl3):
    #-------------------------------------------------------
        # Auswertung mit templates
        template_o = self.lookup_o.get_template(template_spl)
        # mit der Methode render wird das zuvor 'übersetzte' Template ausgeführt
        # data_o sind die im Template angegebenen Daten
        # data_opl die übergebenen Daten
        
        markup_s = template_o.render(id_stg = id_spl, data_o = data_opl, data_l = data_opl2, data_m = data_opl3)
        return markup_s    
    
    #-------------------------------------------------------
    def createForm_login_b_px(self, data_opl):
    #-------------------------------------------------------
        #Generierung des Loginforms für die Anmeldung mit dem Benutzernamen
        return self.createTemplate_p('form_anmeldung_benutzername.tpl', data_opl) 

    #-------------------------------------------------------
    #def createForm_login_bk_px(self, data_opl):
    #-------------------------------------------------------
        #Generierung des Loginforms für die Anmeldung mit Benutzername + Kennwort
        #return self.createTemplate_p('form_anmeldung_kennwort.tpl', data_opl)
    #-------------------------------------------------------
    def createList_studiengaenge_student_px(self, data_opl):
    #-------------------------------------------------------
        return self.createTemplate_p('liste_studiengaenge_student.tpl', data_opl)

    #-------------------------------------------------------
    def createList_lehrveranstaltungen_px(self, data_opl):
    #-------------------------------------------------------
        return self.createTemplate_p('liste_lehrveranstaltungen.tpl', data_opl)

    #-------------------------------------------------------
    def createList_studiengaenge_module_px(self, data_opl, data_opl2):
    #-------------------------------------------------------
        return self.createTemplate2_p('liste_studiengaenge_vs.tpl', data_opl, data_opl2)
  
    #-------------------------------------------------------
    def createList_studiengaenge_lv_module_px(self, data_opl, data_opl2, benutzer):
    #-------------------------------------------------------
        return self.createTemplate_modul_p('liste_studiengaenge_vm.tpl', data_opl, data_opl2, benutzer)

    #-------------------------------------------------------
    def createForm_studiengaenge_px(self, id_spl, data_opl, data_opl2):
    #-------------------------------------------------------
    #Generierung des Speichern/Bearbeitungsforms für die Studiengänge
        # hier müsste noch eine Fehlerbehandlung ergänzt werden !
        markup_s =''
        markup_s += self.readFile_p('form_studiengaenge_0.tpl')

        markupV_s = self.readFile_p('form_studiengaenge_1.tpl')
        lineT_o = string.Template(markupV_s)
        markup_s += lineT_o.safe_substitute (bezeichnung_s=data_opl[0]
                ,   kurzbezeichnung_s=data_opl[1]
                ,   beschreibung_s=data_opl[2]
                ,   semesteranzahl_s=data_opl[3]
                ,   id_s=id_spl
                )

        markup_s += self.readFile_p('form_studiengaenge_2.tpl')
        #markup_s += self.createTemplate_p('liste_lehrveranstaltungen.tpl', data_opl[4])
        markup_s += self.createTemplate_mit_kbez_p('liste_lehrveranstaltungen.tpl', data_opl[1], data_opl2)
        markup_s += self.readFile_p('form_studiengaenge_3.tpl')
        
        return markup_s
    
    #-------------------------------------------------------
    def createForm_module_px(self, id_spl, data_opl):
    #-------------------------------------------------------
    #Generierung des Speichern/Bearbeitungsforms für die Studiengänge

        # hier müsste noch eine Fehlerbehandlung ergänzt werden !
        markup_s =''
        markup_s += self.readFile_p('form_module_0.tpl')

        markupV_s = self.readFile_p('form_module_1.tpl')
        lineT_o = string.Template(markupV_s)
        markup_s += lineT_o.safe_substitute (bezeichnung_s=data_opl[0]
                ,   beschreibung_s=data_opl[1]
                ,   anzahl_kreditpunkte_s=data_opl[2]
                ,   anzahl_sws_vorlesung_s=data_opl[3]
                ,   anzahl_sws_uebung_s=data_opl[4]
                ,   anzahl_sws_praktikum_s=data_opl[5]
                ,   voraussetzungen_s=data_opl[6]
                ,   modulverantwortlicher_s=data_opl[7]
                ,   stg_kurzbezeichnung_s=data_opl[8]
                ,   id_s=id_spl
                )

        markup_s += self.readFile_p('form_module_2.tpl')

        return markup_s    
    
    #-------------------------------------------------------
    def createForm_lehrveranstaltungen_px(self, id_spl, data_opl):
    #-------------------------------------------------------
    #Generierung des Speichern/Bearbeitungsforms für die Studiengänge

        # hier müsste noch eine Fehlerbehandlung ergänzt werden !
        markup_s =''
        markup_s += self.readFile_p('form_lehrveranstaltungen_0.tpl')

        markupV_s = self.readFile_p('form_lehrveranstaltungen_1.tpl')
        lineT_o = string.Template(markupV_s)
        markup_s += lineT_o.safe_substitute (bezeichnung_s=data_opl[0]
                ,   kurzbezeichnung_s=data_opl[1]
                ,   lage_semester_s=data_opl[2]
                ,   modul_s=data_opl[3]
                ,   stg_kurzbezeichnung_s=data_opl[4]
                ,   id_s=id_spl
                )

        markup_s += self.readFile_p('form_lehrveranstaltungen_2.tpl')

        return markup_s        
    #-------------------------------------------------------
    def readFile_p(self, fileName_spl):
    #-------------------------------------------------------
        content_s =''
        with codecs.open(os.path.join('template', fileName_spl),'r','utf-8')as fp_o:
            content_s = fp_o.read()

        return content_s    
# EOF        