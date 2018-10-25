# coding: utf-8

import cherrypy
from .database import Database_cl
from .view import View_cl

#----------------------------------------------------------
class Application_cl(object):
#----------------------------------------------------------
    
    benutzer = ""
    rolle = ""
    
    #-------------------------------------------------------
    def __init__(self):
    #-------------------------------------------------------
        # spezielle Initialisierung können hier eingetragen werden
        self.view_o = View_cl()
        self.db_o = Database_cl()
    @cherrypy.expose
    
    #-------------------------------------------------------
    def index(self):
    #-------------------------------------------------------
        return self.anmeldung()

    @cherrypy.expose
    
    #-------------------------------------------------------
    def test(self):
    #-------------------------------------------------------
        return str(self.db_o.getNewID_p)

    @cherrypy.expose
    #-------------------------------------------------------
    def anmeldung(self):
    #-------------------------------------------------------
        return self.createForm_login_b_p()
    
    @cherrypy.expose
    
    #-------------------------------------------------------
    def studiengaenge(self):
    #-------------------------------------------------------  
        global rolle
        
        if rolle == "vs":
            return self.createList_studiengaenge_module_p()
        elif rolle == "vm":
            return self.createList_studiengaenge_lv_module_p()
        elif rolle == "student":
            return self.createList_studiengaenge_student_p()
    
    @cherrypy.expose     
    
    #-------------------------------------------------------
    def studiengaenge_vs(self):
    #-------------------------------------------------------
        return self.createList_studiengaenge_module_p()
    
    @cherrypy.expose 

    #-------------------------------------------------------
    def studiengaenge_vm(self):
    #-------------------------------------------------------
        return self.createList_studiengaenge_lv_module_p()
    
    @cherrypy.expose
    
    #-------------------------------------------------------
    def delete_sg(self, id):
    #-------------------------------------------------------
        self.db_o.delete_px(id)
        return self.studiengaenge()
    
    @cherrypy.expose    
    
    #-------------------------------------------------------
    def delete_lv(self, id):
    #-------------------------------------------------------
        self.db_o.delete_lv_px(id)
        return self.studiengaenge()
    
    @cherrypy.expose       
    
    #-------------------------------------------------------
    def delete_m(self, id):
    #-------------------------------------------------------
        self.db_o.delete_m_px(id)
        return self.studiengaenge()
    
    @cherrypy.expose          
    
    #-------------------------------------------------------
    def add_sg(self):
    #-------------------------------------------------------
        return self.createForm_studiengaenge_p()
    
    @cherrypy.expose

    #-------------------------------------------------------
    def add_lv(self):
    #-------------------------------------------------------
        return self.createForm_lehrveranstaltungen_p()
    @cherrypy.expose
    
    #-------------------------------------------------------
    def add_m(self):
    #-------------------------------------------------------
        return self.createForm_module_p()
    
    @cherrypy.expose    
        
    #-------------------------------------------------------
    def edit_sg(self, id):
    #-------------------------------------------------------
        return self.createForm_studiengaenge_p(id)
    
    @cherrypy.expose  
    
    #-------------------------------------------------------
    def edit_lv(self, id):
    #-------------------------------------------------------
        return self.createForm_lehrveranstaltungen_p(id)
    
    @cherrypy.expose      
    
    #-------------------------------------------------------
    def edit_m(self, id):
    #-------------------------------------------------------
        return self.createForm_module_p(id)
    
    @cherrypy.expose        

    #-------------------------------------------------------
    def save_sg(self, **data_opl):
    #-------------------------------------------------------
        # Sichern der Daten: aufgrund der Formularbearbeitung muss
        # eine vollständige HTML-Seite zurückgeliefert werden!
        
        # data_opl: Dictionary mit den gelieferten key-value-Paaren
        
        # hier müsste man prüfen, ob die Daten korrekt vorliegen!
        
        # HIER müssen Sie die Semesterzahl(en) ergänzen
        
        id_s = data_opl["id_s"]
        data_a = [ data_opl["bezeichnung_s"]
        ,   data_opl["kurzbezeichnung_s"]
        ,   data_opl["beschreibung_s"]
        ,   data_opl["semesteranzahl_s"] # Semesterzahl ergänzt
        ,   []
        ]
        
        if id_s != "None":
            # Update-Operation
            self.db_o.update_px(id_s, data_a)
        else:
            # Create-Operation
            id_s = self.db_o.create_px(data_a)

        return self.createForm_studiengaenge_p(id_s)
        
    @cherrypy.expose        

    #-------------------------------------------------------
    def save_m(self, **data_opl):
    #-------------------------------------------------------
        # Sichern der Daten: aufgrund der Formularbearbeitung muss
        # eine vollständige HTML-Seite zurückgeliefert werden!
        
        # data_opl: Dictionary mit den gelieferten key-value-Paaren
        
        # hier müsste man prüfen, ob die Daten korrekt vorliegen!
        
        # HIER müssen Sie die Semesterzahl(en) ergänzen
        
        id_s = data_opl["id_s"]
        data_z = [ data_opl["bezeichnung_s"]
        ,   data_opl["beschreibung_s"]
        ,   data_opl["anzahl_kreditpunkte_s"]
        ,   data_opl["anzahl_sws_vorlesung_s"]
        ,   data_opl["anzahl_sws_uebung_s"]
        ,   data_opl["anzahl_sws_praktikum_s"]
        ,   data_opl["voraussetzungen_s"]
        ,   data_opl["modulverantwortlicher_s"]
        ,   data_opl["stg_kurzbezeichnung_s"]
        ]
        
        if id_s != "None":
            # Update-Operation
            self.db_o.update_module_px(id_s, data_z)
        else:
            # Create-Operation
            id_s = self.db_o.create_module_px(data_z)

        return self.createForm_module_p(id_s)
        
    @cherrypy.expose        
    
    #-------------------------------------------------------
    def save_lv(self, **data_opl):
    #-------------------------------------------------------
        # Sichern der Daten: aufgrund der Formularbearbeitung muss
        # eine vollständige HTML-Seite zurückgeliefert werden!
        
        # data_opl: Dictionary mit den gelieferten key-value-Paaren
        
        # hier müsste man prüfen, ob die Daten korrekt vorliegen!
        
        # HIER müssen Sie die Semesterzahl(en) ergänzen
        
        id_s = data_opl["id_s"]
        data_z = [ data_opl["bezeichnung_s"]
        ,   data_opl["kurzbezeichnung_s"]
        ,   data_opl["lage_semester_s"]
        ,   data_opl["modul_s"]
        ,   data_opl["stg_kurzbezeichnung_s"]
        ]
        
        if id_s != "None":
            # Update-Operation
            self.db_o.update_lehrveranstaltungen_px(id_s, data_z)
        else:
            # Create-Operation
            id_s = self.db_o.create_lehrveranstaltungen_px(data_z)

        return self.createForm_lehrveranstaltungen_p(id_s)
        
    @cherrypy.expose    
        
    #-------------------------------------------------------
    def login(self, **data_opl):
    #-------------------------------------------------------
        # Hier soll der Benutzername überprüft werden
        #return data_opl["benutzername_s"]
        
        data_b = self.db_o.read_benutzer_px()
        
        global benutzer
        global rolle
        
        benutzer = data_opl["benutzername_s"]
        kennwort = data_opl["kennwort_s"]
        
        if "@stud.hn.de" in benutzer:    
            rolle = "student"
            return self.studiengaenge()
        #else: 
        for i in range(0, len(data_b)):
            #Wenn Benutzer in der benutzer.json dann geh in login_bk
            if (benutzer == data_b[str(i)][0]) and (kennwort == data_b[str(i)][1]): 
                #return data_b[str(i)][0]
                #return "Benutzer ist kein Student!"
                #return self.view_o.createForm_login_bk_px(data_opl) 
                #---------> hier weitermachen für kennwort
                rolle = data_b[str(i)][2]
                return self.studiengaenge()
                #if (rolle=="vm"):
                    #return "Hier ist Verantwortlicher Module" 
                #    return self.createList_studiengaenge_lv_module_p()
                #elif (rolle=="vs"):
                    #return "Hier ist Verantwortlicher Studiengang"
                #    return self.createList_studiengaenge_module_p()
            elif (benutzer == data_b[str(i)][0]) and (kennwort != data_b[str(i)][1]): 
                #"Kennwort ist falsch!"
                return self.error()
    @cherrypy.expose
    
    #-------------------------------------------------------
    def beziehung_sg_lv(self, id):
    #-------------------------------------------------------
    #---> hier weitermachen 
        if id_spl != None:
            data_sg_lv = self.db_o.read_module_px(id_spl)
        else:
            data_m = self.db_o.getDefault_module_px()
    @cherrypy.expose    
    
    #-------------------------------------------------------
    def error(self):
    #-------------------------------------------------------
        data_o = {}
        return self.view_o.createList_error_px(data_o)
    @cherrypy.expose    
    
    #-------------------------------------------------------
    def modulhandbuch(self, id):
    #-------------------------------------------------------
        #data_o = {}
        data_o = self.db_o.read_px()
        data_l = self.db_o.read_lehrveranstaltungen_px()
        data_m = self.db_o.read_module_px()        
        return self.view_o.createList_modulhandbuch_px(id, data_o, data_l, data_m)
    @cherrypy.expose

    #-------------------------------------------------------
    def lehrveranstaltungen(self, id):
    #-------------------------------------------------------
        return self.createList_lehrveranstaltungen_p(id)
    @cherrypy.expose
    
    #-------------------------------------------------------
    #def login_bk(self, benutzer, rolle):
    #-------------------------------------------------------
    #    return benutzer + rolle
    #@cherrypy.expose    
    
    #-------------------------------------------------------
    def createList_studiengaenge_student_p(self):
    #-------------------------------------------------------
        # mit diesen Daten Markup erzeugen
        data_o = self.db_o.read_px()
        data_l = self.db_o.read_lehrveranstaltungen_px()
        return self.view_o.createList_studiengaenge_student_px(data_o, data_l)    
    
    #-------------------------------------------------------
    def createList_studiengaenge_module_p(self):
    #-------------------------------------------------------
        # mit diesen Daten Markup erzeugen
        data_o = self.db_o.read_px()
        #data_l = self.db_o.read_lehrveranstaltungen_px()
        data_m = self.db_o.read_module_px()
        data_l = self.db_o.read_lehrveranstaltungen_px()
        return self.view_o.createList_studiengaenge_module_px(data_o, data_m, data_l)

    #-------------------------------------------------------
    def createList_studiengaenge_lv_module_p(self):
    #-------------------------------------------------------
        # mit diesen Daten Markup erzeugen
        global benutzer
        data_o = self.db_o.read_px()
        data_l = self.db_o.read_lehrveranstaltungen_px()
        data_m = self.db_o.read_module_px()
        return self.view_o.createList_studiengaenge_lv_module_px(data_o, data_m, data_l, benutzer)

    
    #-------------------------------------------------------
    def createList_lehrveranstaltungen_p(self, id):
    #-------------------------------------------------------
        # mit diesen Daten Markup erzeugen
        data_l = self.db_o.read_lehrveranstaltungen_px(id)
        return self.view_o.createList_lehrveranstaltungen_px(data_l)    
    
    #-------------------------------------------------------
    def createForm_studiengaenge_p(self, id_spl = None):
    #-------------------------------------------------------
    #Erstellung des Forms für die Studiengänge
        data_l = self.db_o.read_lehrveranstaltungen_px()
        if id_spl != None:
            data_o = self.db_o.read_px(id_spl)
        else:
            data_o = self.db_o.getDefault_px()
        # mit diesen Daten Markup erzeugen
        return self.view_o.createForm_studiengaenge_px(id_spl, data_o, data_l)     

    #-------------------------------------------------------
    def createForm_module_p(self, id_spl = None):
    #-------------------------------------------------------
    #Erstellung des Forms für die Module
        if id_spl != None:
            data_m = self.db_o.read_module_px(id_spl)
        else:
            data_m = self.db_o.getDefault_module_px()
        # mit diesen Daten Markup erzeugen
        return self.view_o.createForm_module_px(id_spl, data_m)     
    
    #-------------------------------------------------------
    def createForm_lehrveranstaltungen_p(self, id_spl = None):
    #-------------------------------------------------------
    #Erstellung des Forms für die Module
        if id_spl != None:
            data_l = self.db_o.read_lehrveranstaltungen_px(id_spl)
        else:
            data_l = self.db_o.getDefault_lehrveranstaltungen_px()
        # mit diesen Daten Markup erzeugen
        return self.view_o.createForm_lehrveranstaltungen_px(id_spl, data_l)       

    #-------------------------------------------------------
    #def default(self, *arguments, **kwargs):
    #-------------------------------------------------------
     #   msg_s = "unbekannte Anforderung: " + \
      #          str(arguments) + \
       #         ' ' + \
        #        str(kwargs)
        #raise cherrypy.HTTPError(404, msg_s)
    #default.exposed= True    

    #-------------------------------------------------------
    def createForm_login_b_p(self):
    #-------------------------------------------------------
        # mit diesen Daten Markup erzeugen
        data_b = self.db_o.read_px()
        return self.view_o.createForm_login_b_px(data_b)     
    
    #-------------------------------------------------------
    #def createForm_login_bk_p(self):
    #-------------------------------------------------------
        # mit diesen Daten Markup erzeugen
        #data_b = self.db_o.read_px()
        #return self.view_o.createForm_login_bk_px(data_b)      
    
# EOF