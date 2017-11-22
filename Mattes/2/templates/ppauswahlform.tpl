<!DOCTYPE html>
<html>
	<head>
		<title>Praktikum2</title>
		<meta charset="UTF-8" />

		<style>

		</style>
		<script type="text/javascript" src="/sit.js"></script><!--<script type="text/javascript" src="sorttable.js"></script>-->

	</head>
	<body>
		<div><p>${alert}</p></div>
		<form id="idWTForm" action="/savePPAktuell" method="POST">
			<input type="hidden" value="${key_s}" id="id_s" name="id_s" />
			<div><label for="pptitel">Titel</label></div>
			<div><input type="text" value="${data_o['pptitel']}" id="pptitel" name="pptitel" required /></div>
			<div>
				<label for="beschreibung">Beschreibung</label>
				<input type="text" value="${data_o['beschreibung']}" id="beschreibung" name="beschreibung" required />
			</div>
			<div>
				<label for="firmaid">Firma-ID</label>
				<input type="text" value="${data_o['firmaid']}" id="firma" name="firmaid" required />
			</div>
			<div>
				<label for="voraussetzung">Voraussetzungen</label>
				<input type="text" value="${data_o['voraussetzung']}" id="voraussetzung" name="voraussetzung" required />
			</div>
			<div>
				<label for="kontakt">Kontakt</label>
				<input type="text" value="${data_o['kontakt']}" id="kontakt" name="kontakt" required />
			</div>
			<div>
				<label for="lehrendenid">Lehrenden-ID</label>
				<input type="text" value="${data_o['lehrendenid']}" id="lehrendenid" name="lehrendenid" required />
			</div>
			<div>
				<label for="matrikelid">Matrikelnummer</label>
				<input type="Text" value="${data_o['matrikelid']}" id="matrikelid" name="matrikelid" required />
			</div>
			<div>
				<label for="anfangsdatum">Anfangsdatum</label>
				<input type="text" value="${data_o['anfangsdatum']}" id="anfangsdatum" name="anfangsdatum" required />
			</div>
			<div>
				<label for="enddatum">Enddatum</label>
				<input type="text" value="${data_o['enddatum']}" id="enddatum" name="enddatum" required />
			</div>
			
			
			<div>
				<input type="submit" id="saveButton"  value="Speichern" />
				<a href="/"><input type="submit" value="Abbrechen"  /></a>

			</div>
			</form>
	</body>
</html>
