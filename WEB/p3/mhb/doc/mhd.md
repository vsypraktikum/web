Name: Mark Hilsendegen\     
Matrikelnummer: 1121869\     
Gruppe: B\     
Datum: 09.01.2018\     

**Allgemeine Beschreibung der Lösung:**     

Aufgabe der Anwendung:     

Mit der Webanwendung werden die Beschreibungen der Studiengänge und Module abgerufen bzw. gepﬂegt.    

Übersicht der fachlichen Funktionen:    
    
Mit der Anwendung soll es möglich sein, neben der Datenpﬂege ein Modulhandbuch zu erstellen:    
     
• das Modulhandbuch zu einem Studiengang enthält     
◦ die Zusammenstellung der Angaben zum Studiengang     
◦ eine Übersicht mit allen Lehrveranstaltungen, alphabetisch sortiert     
▪ auch die Modulverantwortlichen werden aufgeführt     
     
einen detaillierten Semesterplan:     

▪ vom 1. bis zum letzten Semester des Studiengangs werden die Lehrveranstaltungen mit allen Daten ausgewiesen     
▪ die je Semester erzielbaren Kreditpunkte werden ausgewiesen     
▪ die insgesamt erzielbaren Kreditpunkte werden ausgewiesen     
• es werden drei Rollen vorgesehen:     
     
Rolle "Studierender":     

▪ kann alle Studiengänge einsehen     
▪ kann zu jedem Studiengang das Modulhandbuch abrufen     
     
Rolle "Verantwortlicher Modul":     

▪ kann die Daten der ihm zugewiesenen Module bearbeiten (aber keine Module erstellen oder löschen!)     
▪ kann alle Studiengänge einsehen     
▪ kann zu jedem Studiengang das Modulhandbuch abrufen     
     
Rolle "Verantwortlicher Studiengang":     

▪ erstellt und pﬂegt die Studiengänge     
▪ erstellt die Module (gibt dabei nur Bezeichnung an - Pﬂege der weiteren Inhalte siehe andere Rolle)     
▪ legt die Zuordnung der Benutzer der Rolle "Verantwortlicher Modul" zu Modulen fest     
▪ kann Module löschen     
▪ legt die Struktur eines Studiengangs anhand der Lehrveranstaltungen in den einzelnen Semestern fest     
▪ legt die Zuordnung der Module zu Lehrveranstaltungen fest     
▪ legt die Modulabhängigkeiten (Voraussetzungen) fest     

**Aufgabenstellung Praktikum 3**

Änderung zu der Aufgabenstellung zu Praktikum 3 ist die Aufbereitung der Webanwendung als Single-Page-Application    
Über Javascript wird nun der Aufruf der HTML-Seiten gesteuert.
Die URI im Browser verändert sich dabei nicht.
Es werden nur einzelne Teile der HTML-Seite neugeladen.

**Beschreibung der Komponenten des Servers:**

Application_cl:     

- stellt die Verbindung zwischen Database_cl und View_cl her     
- stellt die Funktionen der Anwendung bereit (save, edit, delete, login, modulhandbuch, etc.)     

Database_cl:     

- liest, bearbeitet, erstellt Einträge in den zugehörigen .json Dateien     

View_cl:      

- liest die erstellten Templates ein und gibt die Sicht der zugehörigen Anwendung aus     

**Datenablage:**      

	 web     
		/p2     
			/mhd     
				/app     
					/_init_.py <-- Initialisierung     
					/application.py <-- Anwendung     
					/database.py <-- Datenbasis     
					/view.py <-- Sicht     
				/content     
					/mhb.css     
					/mhb.js     
				/data     
					/benutzer.json <-- Daten     
					/studiengaenge.json     
					/module.json     
					/lehrveranstaltungen.json     
				/doc     
				/template     
					/form_anmeldung_benutzername.tpl <-- Formulare     
					/form_module_1.tpl     
					/form_module_2.tpl     
					/form_module_3.tpl     
					/form_studiengaenge_1.tpl     
					/form_studiengaenge_2.tpl     
					/form_studiengaenge_3.tpl     
					/form_lehrveranstaltungen_1.tpl     
					/form_lehrveranstaltungen_2.tpl     
					/form_lehrveranstaltungen_3.tpl     
					/liste_studiengaenge_vs.tpl <--- Listen
					/liste_studiengaenge_vm.tpl     
					/liste_lehrveranstaltungen.tpl     

**Konfiguration:**      

#coding: utf-8     
import os     
import cherrypy    
from app import application     

#--------------------------------------     
def main():     
#--------------------------------------     
    # Get current directory     
    try:     
        current_dir = os.path.dirname(os.path.abspath(__file__))      
    except:     
        current_dir = os.path.dirname(os.path.abspath(sys.executable))     
    # disable autoreload and timeout_monitor     
    cherrypy.engine.autoreload.unsubscribe()     
    cherrypy.engine.timeout_monitor.unsubscribe()     
    # Static content config     
    staticConfig_o = {     
        '/': {     
            'tools.staticdir.root': current_dir,     
            'tools.staticdir.on': True,     
            'tools.staticdir.dir': './content',     
        }     
    }     
    cherrypy.config.update({     
        'tools.log_headers.on':  True,     
        'tools.sessions.on':     False,      
        'tools.encode.on':       True,    
        'tools.encode.encoding': 'utf-8',     
        'server.socket_port':    8080,    
        'server.socket_timeout': 60,     
        'server.thread_pool':    10,      
        'server.environment':    'production',     
        'log.screen':            True#,     
        #'request.show_tracebacks': False     
    })     

    # Request-Handler definieren      
    cherrypy.tree.mount(application.Application_cl(), '/', staticConfig_o)     

    # Start server     
    cherrypy.engine.start()     
    cherrypy.engine.block()     

#--------------------------------------     
if __name__ == '__main__':      
#--------------------------------------     
    main()     
# EOF      
