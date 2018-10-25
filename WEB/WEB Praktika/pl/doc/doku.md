# WEB Praktikum 2 Gruppe C

## Joey Laschet und Lukas van Gemmeren 

## 1. Aufbau der Webanwendung

### Framework

Verwendetes Framework: CherryPi - ein einfaches Web Framework um Webanwendungen objektorientiert in der Sprache Python zu erstellen.

### server.py

Startet den CherryPi Server, dient außerdem zur Konfiguration des Servers. Static Konfiguration für einige Elemente und das Mounten von 3 Klassen. (Siehe Konfiguration)

### application.py

Stellt die Basis der Anwendung, von hier aus gelangt man in die Besucher und Sachbearbeiterklasse.

### Besucher.py

Stellt die Methoden für einen Besucher bereit, wie etwa das Anzeigen, Buchen und Stornieren von Veranstaltungen. Ruft hauptsächlich Bview.py-Methoden und die der Datenbank auf.

### Sachbearbeiter.py

Stellt alle Funktionen für den Sachbearbeiter bereit. Neben dem Hinzufügen/Löschen/Bearbeiten von Veranstaltungen gibt es die Möglichkeit einzelne Teilobjekte, aus denen Veranstaltungen bestehen zu bearbeiten, wie etwa Kategorien, Orte und Künstler. Ruft Hauptsächlich Sview.py-Methoden und die der Datenbank auf.

### Sview.py 

Stellt die Methoden bereit, um aus den Templates für den Sachbearbeiter fertigen Code zu erzeugen. Benutzt Template Engine Mako.

### Bview.py

Stellt die Methoden bereit, um aus den Templates für den Besucher fertigen Code zu erzeugen. Benutzt Template Engine Mako.

### database.py

Verwaltung der Datenbank im Server. Diese Funktionen stellt die Schnittstelle zwischen dem Webserver und den zu verarbeitenden Daten dar. In diesem Fall werden die Daten sortiert nach Kategorien in .json abgelegt und zur Laufzeit in Dictionairies gehalten.

### templates und content Ordner

In diesem Ordner befinden sich alle Template Dateien, für jede mögliche Website eine. Weiterhin befinden sich eine JavaScript Datei für eine interaktive Benutzeroberfläche und eine CSS-Datei zum Formatieren der Webseite.

## Datenablage

### .json Dateien

In diesen vom Server angelegten Dateien werden die Eingabedaten abgespeichert und auf Anfrage
ausgelesen und in die Formulare/Templates eingebettet. Jede Datei stellt dabei eine Kategorie dar, wie etwa Veranstaltungen, Orte, Künstler und Besucher. In den Dictionairies befinden sich Arrays um alle Bestandteile der Daten zu trennen.

## Konfiguration

### Static

Statisch abgelegt wird die Allgemeingültige CSS Datei und die Javascript Datei die eine Sicherheitsabfrage vor dem Löschen bereitstellt.

### Gemountete Module

Die Wurzel / wird durch die Application.py  dargestellt, welche nur die oberste Startseite bereitstellt. Sie hat keine Funktion außer die Sachbearbeiter und Besucher Klassen zu initialisieren. 
Sachbearbeiter und Besucher stellen die eigentliche Anwendung bereit, aufgeteilt in 2 Bereiche für 2 Benutzer.