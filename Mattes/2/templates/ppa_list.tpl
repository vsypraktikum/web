<!DOCTYPE html>
<html>
	<head>
		<title>Studentliste</title>
		<meta charset="UTF-8" />
		<link rel="stylesheet" href="/style.css">
		<style>
			@import "/style.css";

		</style>
		<script type="text/javascript" src="/ppm.js"></script>
	</head>
	<body onload="PPAngebot_INIT()">
	<div class="kopf"></div>
		<div><a href="/">Zurück</a></div>
		<div><a href="/addPPA">Neu</a></div></div>
		<table>
			<tr>
				<th>Titel</th>
				<th>Beschreibung</th>
				<th>Firma-ID</th>
				<th>Voraussetzungen</th>
				<th>Kontakt</th>
				<th>Lehrenden-ID</th>
				<th>Matrikel-ID</th>
				<th>Anfangsdatum</th>
				<th>Enddatum</th>
			</tr>
			<div id="table">
			% for key_s in data_o:
				<tr id="${key_s}" class="noMark" onClick="markRow(${key_s});">
					<td>${data_o[key_s]['pptitel']}</td>
					<td>${data_o[key_s]['beschreibung']}</td>
					<td>${data_o[key_s]['firmaid']}</td>
					<td>${data_o[key_s]['voraussetzung']}</td>
					<td>${data_o[key_s]['kontakt']}</td>
					<td>${data_o[key_s]['lehrendenid']}</td>
					<td>${data_o[key_s]['matrikelid']}</td>
					<td>${data_o[key_s]['anfangsdatum']}</td>
					<td>${data_o[key_s]['enddatum']}</td>
				</tr>
			% endfor
			
		</table>
		<div id="/createPPAuswahlForm/" class="likeabutton">Eintragen</div>
		<div id="/deletePPA/" class="likeabutton">Löschen</div>
		<div id="/editPPA/" class="likeabutton">Bearbeiten</div>
	</body>
</html>