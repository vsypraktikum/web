Name: Mark Hilsendegen\     
Matrikelnummer: 1121869\     
Gruppe: B\     
Datum: 30.11.2017\     

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

**Beschreibung der Komponenten des Servers:**

Application_cl:     

- stellt die Verbindung zwischen Database_cl und View_cl her     

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
					/liste_studiengaenge_module.tpl <--- Listen

	


**Durchgeführte Ergänzungen:**     

- Dateneingabe für die Daten des 2. Team-Mitglieds im Formular     
- zusätzliches Attribut "Semesteranzahl" (für beide Teammitglieder) in allen Listen und Formularen     
  sowie in der Datenbasis     
- Aktion "Abbrechen" im Formular implementiert     
- Gestaltung mit CSS: CSS-Stilregeln in die Datei webteams.css eingetragen     
- Löschen der Daten eines Teams auf der Serverseite implementiert (siehe Datei database.py)     
- Rückfrage an den Benutzer beim Löschen von Einträgen in der Liste Datei webteams.js      