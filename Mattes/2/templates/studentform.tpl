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
	
		<form id="idWTForm" action="/saveStudent" method="POST">
		
			<input type="hidden" value="${key_s}" id="id_s" name="id_s" />
			<div>
				<label for="matrikelnr">Matrikel Nr.</label></div>
				<input type="text" value="${data_o['matrikelnr']}" id="matrikelnr" name="matrikelnr" required />
			</div>
			<div>
				<label for="name">Name</label>
				<input type="text" value="${data_o['name']}" id="name" name="name" required />
			</div>
			<div>
				<label for="vorname">Vorname</label>
				<input type="text" value="${data_o['vorname']}" id="vorname" name="vorname" required />
			</div>
			<div>
				<input type="submit" id="saveButton"  value="Speichern" />
				<a href="/"><input type="submit" value="Abbrechen"  /></a>
			</div>
		</form>
	</body>
</html>
