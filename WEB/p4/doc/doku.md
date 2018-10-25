Name: Mark Hilsendegen\     
Matrikelnummer: 1121869\     
Gruppe: B\     
Datum: 05.02.2018\     

**Allgemeine Beschreibung der Lösung:**     

Aufgabe der Anwendung:     

Mit der Webanwendung wird ein Wiki bereitgestellt mit dem man Themen erstellen und pflegen kann.
Mit einem Klick auf die Links wird eine Detailbeschreibung des Themas geöffnet.
Kategorien können einem Thema zugeordnet werden.    

Übersicht der fachlichen Funktionen:    
    
Mit der Anwendung soll es möglich sein, neben der Datenpﬂege auch verwaiste und fehlende Themen zu finden:    
     
• fehlende Themen sind Themen auf die verwiesen wurde aber noch nicht in der Datenbank enthalten sind     
◦ verwaiste Themen sind Themen die in der Datenbank enthalten sind, aber auf die nicht verwiesen wurde        
     
ein detailliertes Thema:     

▪ zeigt die Bezeichnung des Themas an     
▪ dem Thema kann ein Titel und ein Text gegeben werden     
▪ Kategorien können dem Thema zugewiesen werden      

Favoriten:

▪ zeigt die Themen an die die Kategorie "favorite" enthalten          

**Beschreibung der Komponenten des Servers:**

Application_cl:     

- stellt die Verbindung zwischen Database_cl und View_cl her     
- stellt alle Methoden für das Method-Dispatching bereit
- die Methoden GET, PUT, POST und DELETE sind implementiert

GET:
- holt sich die Daten auf der Datenbank "topics.json""

POST:
- fügt ein neues Thema der Datenbank hinzu

PUT:
- ändert ein bestehendes Thema

DELETE:
- löscht ein einzelnes Thema

Database_cl:     

- liest, bearbeitet, erstellt Einträge in den zugehörigen .json Dateien     

View_cl:      

- gibt die Daten der GET-Anfragen aus     

**Datenablage:**      

	 web     
		/p4          
				/app     
					/_init_.py <-- Initialisierung     
					/application.py <-- Anwendung     
					/database.py <-- Datenbasis     
					/view.py <-- Sicht     
				/static     
					/es_to_c6.js
					/main.css     
					/main.thml
					/main_c6.js
					/te_c6.js
					/tm_c6.css
					/xhr_c6.js					
				/data     
					/topics.json <-- Daten     
					/ID.json          
				/doc     
					/doku.md
					/doku.html     
				/template     
					/detail_create.tpl.html     
					/detail_edit.tpl.html     
					/detail_show.tpl.html     
					/detailTags.tpl.html     
					/favorites.tpl.html     
					/footer.tpl.html     
					/header.tpl.html     
					/home.tpl.html     
					/missing.tpl.html     
					/orphans.tpl.html     
					/sidebar.tpl.html   
					/tags.tpl.html     
					/topics.tpl.html     

**Beschreibung der Komponenten des Servers:**

- Der Server stellt jediglich die Daten bereit die in der Datenbank gespeichert wurden
- Die Methoden POST, GET, PUT, DELETE greifen auf die Datenbank zu und bearbeiten oder geben diese aus
      
**Beschreibung der Komponenten des Clients:**

main_c6.js    

ist für die Verarbeitung auf dem Client zuständig. Der Event-Handler fängt die Anfragen vom Client ab und gibt die entsprechende angefragte Seite aus.
Die einzelnen Komponenten der HTML-Seite werden hier geladen.

