## -*- coding: utf-8 -*-
<%inherit file="layout.tpl"/>
<%block name="header">
    <body>
		<h1>Create / Edit Modul</h1>
		<br>
		<form id="idWTForm" action="/saveModul" method="POST">
			<input type="string" value="$studiengangID" id="studiengangID" name="studiengangID" />
			<div>
				<label for="bezeichnungModul">Modul Bezeichnung</label>
				<input type="string" value="$bezeichnungModul" id="bezeichnungModul" name="bezeichnungModul" required />
			</div>
			<div>
				<label for="beschreibungModul">Beschreibung</label>
				<input type="text" value="$beschreibungModul" id="beschreibungModul" name="beschreibungModul" required />
			</div>
			<div>
				<label for="anzahlCredits">Anzahl Kreditpunkte</label>
				<input type="number" value="$anzahlCredits" id="anzahlCredits" name="anzahlCredits" required />
			</div>
			<div>
				<label for="anzahlVorlesung">Anzahl SWS-Vorlesung</label>
				<input type="number" value="$anzahlVorlesung" id="anzahlVorlesung" name="anzahlVorlesung" required />
			</div>
			<div>
				<label for="anzahlUebung">Anzahl SWS-Übung</label>
				<input type="number" value="$anzahlUebung" id="anzahlUebung" name="anzahlUebung" required />
			</div>
			<div>
				<label for="anzahlPraktika">Anzahl SWS-Praktikum</label>
				<input type="number" value="$anzahlPraktika" id="anzahlPraktika" name="anzahlPraktika" required />
			</div>
			<div>
				<label for="voraussetzungen">Voraussetzungen</label>
				<input type="text" value="$voraussetzungen" id="voraussetzungen" name="voraussetzungen"/>
			</div>
			<div>
				<label for="modulVerantwortlicher">Modulverantwortlicher</label>
				<input type="string" value="$modulVerantwortlicher" id="modulVerantwortlicher" name="modulVerantwortlicher"/>
			</div>
			<div>
				<label for="studiengangKurzbezeichnung">Studiengang Kurzbezeichnung</label>
				<input type="string" value="$studiengangKurzbezeichnung" id="studiengangKurzbezeichnung" name="studiengangKurzbezeichnung"/>
			</div>
			<div>
				<input type="submit" value="Speichern"/>
				<input type="reset" value="Go Back" onclick="location.href = '/lehr'"/><!-- Abbrechen Button -->
			</div>
		</form>
	</body>
</%block>
