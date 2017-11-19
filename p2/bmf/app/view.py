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

from .Erstellen import Mitarbeiter
from mako.template import Template
from mako.lookup import TemplateLookup

#--------------------------------------------------------
class View_cl(object): 
#---------------------------------------------------------

    #------------------------------------------------------
    def __init__(self, path_spl): 
        #------------------------------------------------------
        self.path_s = os.path.join(path_spl, "template")
        self.lookup_o = TemplateLookup(directories=self.path_s)
    
    #------------------------------------------------------
    def create_p(self, template_spl, data_opl):
        
        template_o = self.lookup_o.get_template(template_spl)
        markup_s = template_o.render(data_o = data_opl)
        
        return markup_s
        
    
    def createMitarbeiter_E(self, data_opl):
        markup_s = '' 
        markup_s += self.readFile_p('list0.tpl')
        
        markupV_s = self.readFile_p('list1.tpl') 
        lineT_o = string.Template(markupV_s) 
        # mehrfach nutzen, um die einzelnen Zeilen der Tabelle zu erzeugen 
        for id_s in data_opl: 
            data_a = data_opl[str(id_s)] 
            markup_s += lineT_o.safe_substitute (name=data_a[0] # HIER müssen Sie eine Ergänzung vornehmen - erl
            ,   vorname=data_a[1] 
            ,   akagra=data_a[2]
            ,   taetigkeit=data_a[3] 
            )
        markup_s += self.readFile_p('list2.tpl')
        
        return self.create_p('liste.tpl', data_opl) #markup_s 
    
    
       
    def createList_px(self, data_opl): #createMitarbeiter_e
    #------------------------------------------------------
        # hier müsste noch eine Fehlerbehandlung ergänzt werden ! 
        markup_s = '' 
        markup_s += self.readFile_p('list0.tpl')
        
        markupV_s = self.readFile_p('list1.tpl') 
        lineT_o = string.Template(markupV_s) 
        # mehrfach nutzen, um die einzelnen Zeilen der Tabelle zu erzeugen 
        for id_s in data_opl: 
            data_a = data_opl[str(id_s)] 
            markup_s += lineT_o.safe_substitute (name_s=data_a[0] # HIER müssen Sie eine Ergänzung vornehmen - erl
            ,   vorname_s=data_a[1] 
            ,   akadem_s=data_a[2]
            ,   taetigkeit_s=data_a[3] 
            )
        markup_s += self.readFile_p('list2.tpl')
        
        return self.create_p('liste.tpl', data_opl) #markup_s
    #------------------------------------------------------
    def createForm_px(self, id_spl, data_opl): 
    #------------------------------------------------------
    # hier müsste noch eine Fehlerbehandlung ergänzt werden ! 
        markup_s = '' 
        markup_s += self.readFile_p('form0.tpl')
        markupV_s = self.readFile_p('form1.tpl') 
        lineT_o = string.Template(markupV_s) 
        markup_s += lineT_o.safe_substitute (name1_s=data_opl[0] # HIER müssen Sie eine Ergänzung vornehmen - erl
        ,   vorname1_s=data_opl[1] 
        ,   matrnr1_s=data_opl[2]
        ,   sem1_s=data_opl[3] 
        ,   name2_s=data_opl[4] 
        ,   vorname2_s=data_opl[5] 
        ,   matrnr2_s=data_opl[6]
        ,   sem2_s=data_opl[7] 
        ,   id_s=id_spl
        )


        markup_s += self.readFile_p('form2.tpl')
        return markup_s
    
    #------------------------------------------------------
    def readFile_p(self, fileName_spl): 
        #------------------------------------------------------
        content_s = '' 
        with codecs.open(os.path.join('content', fileName_spl), 'r', 'utf-8') as fp_o: 
            content_s = fp_o.read()
        return content_s
# EOF
