## -*- coding: utf-8 -*-
<%inherit file="layout.tpl"/>
<%block name="header">
	<body>
		<h1>Create / Edit Studiengang</h1>
		<br>
		<form id="idWTForm" action="/saveLehrveranstaltung" method="POST">
			<input type="string" value="$id_s" id="id_s" name="id_s" />
			<div>
				<label for="bezeichnungLehrveranstaltung">Bezeichnung</label>
				<input type="string" value="$bezeichnungLehrveranstaltung" id="bezeichnungLehrveranstaltung" name="bezeichnungLehrveranstaltung" required />
			</div>
			<div>
				<label for="beschreibungLehrveranstaltung">Beschreibung</label>
				<input type="string" value="$beschreibungLehrveranstaltung" id="beschreibungLehrveranstaltung" name="beschreibungLehrveranstaltung" required />
			</div>
			<div>
				<label for="lageLehrveranstaltung">Lage (Semester)</label>
				<input type="number" value="$lageLehrveranstaltung" id="lageLehrveranstaltung" name="lageLehrveranstaltung" required />
			</div>
			<div>
				<label for="modulLehrveranstaltung">Modul</label>
				<input type="text" value="$modulLehrveranstaltung" id="modulLehrveranstaltung" name="modulLehrveranstaltung" required />
			</div>
			<div>
				<label for="studiengangKurzbezeichnung">Studiengang Kurzbezeichnung</label>
				<input type="text" value="$studiengangKurzbezeichnung" id="studiengangKurzbezeichnung" name="studiengangKurzbezeichnung" required />
			</div>
			<div>
				<input type="submit" value="Speichern"/>
				<input type="reset" value="Go Back" onclick="location.href = '/lehr'"/><!-- Abbrechen Button -->
			</div>
		</form>
	</body>
</%block>
