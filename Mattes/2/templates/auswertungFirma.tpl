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
				<th>Firma</th>
				<th>Branche</th>
				<th>Schwerpunkt</th>
				<th>Sitz</th>
				<th>Mitarbeiteranzahl</th>
				<th>Projekttitel</th>
				<th>Beschreibung</th>
				<th>Voraussetzungen</th>
				<th>Kontakt</th>
				<th>Lehrenden-ID</th>
				<th>Matrikel-ID</th>
				<th>Anfangsdatum</th>
				<th>Enddatum</th>
			</tr>
			% for key_s in ppangebot_o:
				<tr id="${key_s}">
					<td>${ppangebot_o[key_s]['name']}</td>
					<td>${ppangebot_o[key_s]['branche']}</td>
					<td>${ppangebot_o[key_s]['schwerpunkt']}</td>
					<td>${ppangebot_o[key_s]['sitz']}</td>
					<td>${ppangebot_o[key_s]['mitarbeiteranzahl']}</td>
					<td>${ppangebot_o[key_s]['pptitel']}</td>
					<td>${ppangebot_o[key_s]['beschreibung']}</td>
					<td>${ppangebot_o[key_s]['voraussetzung']}</td>
					<td>${ppangebot_o[key_s]['kontakt']}</td>
					<td>${ppangebot_o[key_s]['lehrendenid']}</td>
					<td>${ppangebot_o[key_s]['matrikelid']}</td>
					<td>${ppangebot_o[key_s]['anfangsdatum']}</td>
					<td>${ppangebot_o[key_s]['enddatum']}</td>
				</tr>
			% endfor
			% for key_s in ppaktuell_o:
				<tr id="" class="PPAktuell">
					<td>${key_s['name']}</td>
					<td>${key_s['branche']}</td>
					<td>${key_s['schwerpunkt']}</td>
					<td>${key_s['sitz']}</td>
					<td>${key_s['mitarbeiteranzahl']}</td>
					<td>${key_s['pptitel']}</td>
					<td>${key_s['beschreibung']}</td>
					<td>${key_s['voraussetzung']}</td>
					<td>${key_s['kontakt']}</td>
					<td>${key_s['lehrendenid']}</td>
					<td>${key_s['matrikelid']}</td>
					<td>${key_s['anfangsdatum']}</td>
					<td>${key_s['enddatum']}</td>
				</tr>
			% endfor
			% for key_s in ppabgeschlossen_o:
				<tr id="" class="PPAbgeschlossen">
					<td>${key_s['name']}</td>
					<td>${key_s['branche']}</td>
					<td>${key_s['schwerpunkt']}</td>
					<td>${key_s['sitz']}</td>
					<td>${key_s['mitarbeiteranzahl']}</td>
					<td>${key_s['pptitel']}</td>
					<td>${key_s['beschreibung']}</td>
					<td>${key_s['voraussetzung']}</td>
					<td>${key_s['kontakt']}</td>
					<td>${key_s['lehrendenid']}</td>
					<td>${key_s['matrikelid']}</td>
					<td>${key_s['anfangsdatum']}</td>
					<td>${key_s['enddatum']}</td>
				</tr>
			% endfor
		</table>
		
	</body>
</html>
