<!DOCTYPE html>
<html>
	<head>
		<title>Studentliste</title>
		<meta charset="UTF-8" />
		<link rel="stylesheet" type="text/css" href="/style.css">
		<style>
			@import "/style.css";

		</style>
	</head>
	<body>
	<div class="kopf"></div>
		<div><a href="/">Zurück</a></div>
		<table>
			<tr>
				<th>Titel</th>
				<th>Vorname</th>
				<th>Name</th>
				<th>Lehrgebiet</th>
				<th>Titel</th>
				<th>Beschreibung</th>
				<th>Firmen-ID</th>
				<th>Voraussetzungen</th>
				<th>Kontakt</th>
				<th>Matrikel-ID</th>
				<th>Anfangsdatum</th>
				<th>Enddatum</th>
			</tr>
			% for key_s in ppaktuell_o:
				<tr id="${key_s}" class="PPAktuell">
					<td>${key_s['titel']}</td>
					<td>${key_s['vorname']}</td>
					<td>${key_s['name']}</td>
					<td>${key_s['lehrgebiet']}</td>
					<td>${key_s['pptitel']}</td>
					<td>${key_s['beschreibung']}</td>
					<td>${key_s['firmaid']}</td>
					<td>${key_s['voraussetzung']}</td>
					<td>${key_s['kontakt']}</td>
					<td>${key_s['matrikelid']}</td>
					<td>${key_s['anfangsdatum']}</td>
					<td>${key_s['enddatum']}</td>
				</tr>
			% endfor
			
			% for key_s in ppabgeschlossen_o:
				<tr id="${key_s}" class="PPAbgeschlossen">
					<td>${key_s['titel']}</td>
					<td>${key_s['vorname']}</td>
					<td>${key_s['name']}</td>
					<td>${key_s['lehrgebiet']}</td>
					<td>${key_s['pptitel']}</td>
					<td>${key_s['beschreibung']}</td>
					<td>${key_s['firmaid']}</td>
					<td>${key_s['voraussetzung']}</td>
					<td>${key_s['kontakt']}</td>
					<td>${key_s['matrikelid']}</td>
					<td>${key_s['anfangsdatum']}</td>
					<td>${key_s['enddatum']}</td>
				</tr>
			% endfor
		</table>
		
	</body>
</html>
