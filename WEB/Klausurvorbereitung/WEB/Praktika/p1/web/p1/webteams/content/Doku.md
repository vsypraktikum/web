<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="generator" content="pandoc">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
  <title></title>
  <style type="text/css">code{white-space: pre;}</style>
  <!--[if lt IE 9]>
    <script src="//cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.3/html5shiv-printshiv.min.js"></script>
  <![endif]-->
</head>
<body>
<h2 id="webpraktikum">Webpraktikum</h2>
<p><strong>Gruppe C: Jan Hamacher, Christian Abel</strong>:</p>
<p><strong>Aufbau Der Webanwendung</strong>: Die Webanwendug besteht aus zwei Seiten: -Startseite:Auflistung der Daten von Teammitgliedern (max.15). -Formular:Erfassung neuer Daten oder Bearbeitung vorhandener Daten.</p>
<p><em>mögliche Aktionen sind</em>:</p>
<p>-erfassen: führt in den Zustand &quot;Detail-neu&quot; -bearbeiten: führt in den Zustand &quot;Detail-alt&quot; -löschen: Daten eines Web-Teams entfernen und Liste wieder aneigen; d.h. der Zustand wird nicht verlassen</p>
<p><em>Zustand&quot;Detail-neu&quot;</em>: -es wird ein leeres Formular angezeigt <em>mögliche Aktionen sind</em>:<br> -abbrechen<br> -speichern</p>
<p><em>Zustand&quot;Detail-neu&quot;</em>: -das Formular zeigt die Daten des ausgewählten Teams an <em>mögliche Aktionen sind</em>:<br> -abbrechen<br>-speichern</p>
<p><strong>Duchgeführte Ergänzugen</strong>: -Überprüfung der Übergabewerte auf Inhalt<br> -Dateneingabe für die Daten des zweiten Teammitglieds hinzugefügt<br> -Aktion Abbrechen im Formular Implementiert<br> -CSS Stilregeln in die Datei webteams.css eingetragen<br> -Löschen der Daten eines Teams auf der Serverseite Implementiert<br> -Rückfrage an den Benutzer beim Löschen von Einträgen in der Liste vervollständigt</p>
<p><strong>Beschreibung des HTTP-Datenverkehrs</strong>:</p>
<p><em>Beim start der Anwendung</em>:</p>
<br><img src="vorher.png" alt="vorher">
<p><em>Beim Speichern von Formulardaten</em>:</p>
<br><img src="nachher.png" alt="nachher">
</body>
</html>
