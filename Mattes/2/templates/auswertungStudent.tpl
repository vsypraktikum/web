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
				<th>Matrikelnummer</th>
				<th>Vorname</th>
				<th>Name</th>
				<th>Projekttitel</th>
				<th>Beschreibung</th>
				<th>Firma</th>
				<th>Voraussetzungen</th>
				<th>Kontakt</th>
				<th>Lehrenden-ID</th>
				<th>Anfangsdatum</th>
				<th>Enddatum</th>
			</tr>
			% for key_s in ppaktuell_o:
				<tr id="${key_s}" class="PPAktuell">
					<td>${key_s['matrikelnr']}</td>
					<td>${key_s['vorname']}</td>
					<td>${key_s['name']}</td>
					<td>${key_s['pptitel']}</td>
					<td>${key_s['beschreibung']}</td>
					<td>${key_s['firmaid']}</td>
					<td>${key_s['voraussetzung']}</td>
					<td>${key_s['kontakt']}</td>
					<td>${key_s['lehrendenid']}</td>
					<td>${key_s['anfangsdatum']}</td>
					<td>${key_s['enddatum']}</td>
				</tr>
			% endfor
			
			% for key_s in ppabgeschlossen_o:
				<tr id="${key_s}" class="PPAbgeschlossen">
					<td>${key_s['matrikelnr']}</td>
					<td>${key_s['vorname']}</td>
					<td>${key_s['name']}</td>
					<td>${key_s['pptitel']}</td>
					<td>${key_s['beschreibung']}</td>
					<td>${key_s['firmaid']}</td>
					<td>${key_s['voraussetzung']}</td>
					<td>${key_s['kontakt']}</td>
					<td>${key_s['lehrendenid']}</td>
					<td>${key_s['anfangsdatum']}</td>
					<td>${key_s['enddatum']}</td>
				</tr>
			% endfor
		</table>
		
	</body>
</html>
