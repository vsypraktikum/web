## -*- coding: utf-8 -*-
<div id="formVerantwortlicherStudiengang">
	<table style="text-align:center;">
	<h1>Form Lehrender Studiengang</h1>
	<br>
		<select id="studiengang" name="studiengang">
			<option value="0">Wählen Sie Ihren Studiengang:</option>
			%for a in data_o.values():
				<option value="${a[1]}">${a[0]}</option>
			%endfor
		</select>
		<button id="buttonstud">Studienganginfos und Modulhandbuch anzeigen</button>
		<p />
		<form id="createStudiengang" action="" method="POST">
			<button onclick="loadDoccreateStudiengang()">Studiengang Erfassen</button>
		</form> 
		<form id="editStudiengang" action="" method="POST">
			<button onclick="loadDocstudiengangEdit()">Studiengang Bearbeiten</button>
		</form> 
		<button id="buttonstuddelete">Studiengang Löschen</button><br>
		<p />
		<select id="lehr" name="lehr">
			<option value="0">Wählen Sie Ihre Lehrveranstaltung aus:</option>
			%for b in data_lehr.values():
				<option value="${b[0]}">${b[0]}</option>
			%endfor
		</select>
		<p />
		<form action="/createLehrveranstaltung" method="POST">
			<button type="submit">Lehrveranstaltung Erfassen</button><br>
		</form> 
		<button id="buttonlehredit">Lehrveranstaltung Bearbeiten</button><br>
		<button id="buttonlehrdelete">Lehrveranstaltung Löschen</button><br>
		<p />
		<select id="modul" name="modul">
			<option value="0">Wählen Sie Ihr Modul aus:</option>
			%for c in data_mod.values():
				<option value="${c[0]}">${c[0]}</option>
			%endfor
		</select>
		<p />
		<form action="/createModul" method="POST">
			<button type="submit">Modul Erfassen</button><br>
		</form>
		<button id="buttonmoduledit">Modul Bearbeiten</button><br>
		<button id="buttonmoduldelete">Modul Löschen</button>
		<br>
		<p />
		<form action="/" method="POST">
			<button type="submit">Logout</button><br>
		</form> 
		<script src="mhb_studiengang.js"></script>
</div>
