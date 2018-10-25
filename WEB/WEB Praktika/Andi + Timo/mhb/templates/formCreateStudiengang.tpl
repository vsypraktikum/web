## -*- coding: utf-8 -*-
<div id="createStudiengang">
		<h1>Create / Edit Studiengang</h1>
		<br>
		<form id="idWTForm" action="/saveStudiengang" method="POST">
			<input type="string" value="$id_s" id="id_s" name="id_s" />
			<div>
				<label for="bezeichnungStudiengang">Bezeichnung</label>
				<input type="string" value="$bezeichnungStudiengang" id="bezeichnungStudiengang" name="bezeichnungStudiengang" required />
			</div>
			<div>
				<label for="kurzbezeichnungStudiengang">Kurzbezeichnung</label>
				<input type="string" value="$kurzbezeichnungStudiengang" id="kurzbezeichnungStudiengang" name="kurzbezeichnungStudiengang" required />
			</div>
			<div>
				<label for="beschreibungStudiengang">Beschreibung</label>
				<input type="text" value="$beschreibungStudiengang" id="beschreibungStudiengang" name="beschreibungStudiengang" required />
			</div>
			<div>
				<label for="semesteranzahlStudiengang">Semesteranzahl</label>
				<input type="number" value="$semesteranzahlStudiengang" id="semesteranzahlStudiengang" name="semesteranzahlStudiengang" required />
			</div>
			<div>
				<input type="submit" value="Speichern"/>
				<input type="reset" value="Go Back" onclick="location.href = '/lehr'"/>
			</div>
		</form>
</div>

