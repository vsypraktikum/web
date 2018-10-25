# coding: utf-8

import cherrypy

from .database import Database_cl
from .view import View_cl

#---------------------------------------------------------
class Application_cl(object): 
#---------------------------------------------------------
    #------------------------------------------------------
    def __init__(self): 
    #------------------------------------------------------
        # spezielle Initialisierung k?nnen hier eingetragen werden 
        self.db_o = Database_cl() 
        self.view_o = View_cl()

    @cherrypy.expose 
    #------------------------------------------------------
    def index(self): 
    #------------------------------------------------------
        return self.createList_p()

    @cherrypy.expose
    #------------------------------------------------------
    def add(self):
    #------------------------------------------------------
        return self.createForm_p()

    @cherrypy.expose 
    #------------------------------------------------------
    def edit(self, id): 
    #------------------------------------------------------
        return self.createForm_p(id)

    @cherrypy.expose
    #------------------------------------------------------
    def save(self, **data_opl):
    #------------------------------------------------------
        # Sichern der Daten: aufgrund der Formularbearbeitung muss 
        # eine vollst?ndige HTML-Seite zur?ckgeliefert werden!

        # data_opl: Dictionary mit den gelieferten key-value-Paaren

        
        if data_opl != "None":
			# hier m?sste man pr?fen, ob die Daten korrekt vorliegen!
            id_s = data_opl["id_s"]
            data_a = [ data_opl["name1_s"] 
			,   data_opl["vorname1_s"] 
			,   data_opl["matrnr1_s"] 
			,   data_opl["name2_s"] 
			,   data_opl["vorname2_s"] 
			,   data_opl["matrnr2_s"] 
			]
            if id_s != "None":
                # Update-Operation 
                self.db_o.update_px(id_s, data_a)
            else: 
                # Create-Operation 
                id_s = self.db_o.create_px(data_a)

        return self.createList_p()

    @cherrypy.expose
    #------------------------------------------------------
    def delete(self, id): 
    #------------------------------------------------------
        # Eintrag l?schen, dann Liste neu anzeigen
        self.db_o.delete_px(id) 
        return self.createList_p()

    @cherrypy.expose 
    #------------------------------------------------------
    def default(self, *arguments, **kwargs): 
    #------------------------------------------------------
        msg_s = "unbekannte Anforderung: " + \
            str(arguments) + \
            ' ' + \
            str(kwargs) 
        raise cherrypy.HTTPError(404, msg_s) 
    default.exposed= True

    #------------------------------------------------------
    def createList_p(self): 
    #------------------------------------------------------
        data_o = self.db_o.read_px() 
        # mit diesen Daten Markup erzeugen 
        return self.view_o.createList_px(data_o)

    #------------------------------------------------------
    def createForm_p(self, id_spl = None):
    #------------------------------------------------------
        if id_spl != None: 
            data_o = self.db_o.read_px(id_spl) 
        else:
            data_o = self.db_o.getDefault_px()
        # mit diesen Daten Markup erzeugen 
        return self.view_o.createForm_px(id_spl, data_o)
		

# EOF