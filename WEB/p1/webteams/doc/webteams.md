Name: Mark Hilsendegen\     
Matrikelnummer: 1121869\     
Gruppe: B\     
Datum: 23.10.2017\     

**Aufbau der Webanwendung:**     

Eine Liste mit der Daten von Studenten erfasst, bearbeitet und gelöscht werden können.     

Aufbau der Liste:
    
1. Name,      
1. Vorname,      
1. Matrikelnummer,      
1. Semesteranzahl,      
2. Name,      
2. Vorname,      
2. Matrikelnummer,      
2. Semesteranzahl     

**Verzeichnisstruktur:**      

	 web	
		/p1     
			/webteams     
				/app     
					/_init_.py <-- Initialisierung     
					/application.py <-- Anwendung     
					/database.py <-- Datenbasis     
					/view.py <-- Sicht     
				/content     
					/form0.tpl <-- Formulare     
					/form1.tpl     
					/form2.tpl     
					/list0.tpl <-- Liste     
					/list1.tpl     
					/list2.tpl     
					/webteams.css     
					/webteams.js     		
				/data     
					/webteams.json <-- Daten     
				/doc     
	


**Durchgeführte Ergänzungen:**     

- Dateneingabe für die Daten des 2. Team-Mitglieds im Formular     
- zusätzliches Attribut "Semesteranzahl" (für beide Teammitglieder) in allen Listen und Formularen     
  sowie in der Datenbasis     
- Aktion "Abbrechen" im Formular implementiert     
- Gestaltung mit CSS: CSS-Stilregeln in die Datei webteams.css eingetragen     
- Löschen der Daten eines Teams auf der Serverseite implementiert (siehe Datei database.py)     
- Rückfrage an den Benutzer beim Löschen von Einträgen in der Liste Datei webteams.js      



**Beschreibung des Datenverkehrs:**     

Start der Anwendung:     

Es werden drei Anfragen an die Adresse http://localhost:8080/ geschickt:  
   
127.0.0.1 - - [23/Oct/2017:22:40:56] "GET / HTTP/1.1" 200 5198 "" "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0"     
127.0.0.1 - - [23/Oct/2017:22:40:56] "GET /webteams.js HTTP/1.1" 304 - "http://localhost:8080/" "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0"     
127.0.0.1 - - [23/Oct/2017:22:40:56] "GET /webteams.css HTTP/1.1" 304 - "http://localhost:8080/" "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0"     
Die GET-Befehle laden die HTML-Seite, das Javaskript und die CSS-Daten.     



Beim Speichern von Formulardaten:    
 
Die Formulardaten werden mit dem POST Befehl abgeschickt:     

127.0.0.1 - - [23/Oct/2017:22:42:58] "POST /save HTTP/1.1" 200 2307 "http://localhost:8080/add" "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0"     
