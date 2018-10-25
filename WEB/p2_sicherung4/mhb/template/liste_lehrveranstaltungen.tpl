## coding: utf-8 
		<h1>Liste der Lehrveranstaltungen</h1>
		<table id="idList_lv">
			<tr><th>Bezeichnung</th><th>Kurzbezeichnung</th><th>Lage (Semester)</th><th>Modul</th><th>Studiengang Kurzbezeichnung</th>
			## man verwendet hier Zugriff auf das Dictionary "data_o"
			% for id_s in data_o:
				<tr id="${id_s}">
				<td>${data_o[id_s][0]}</td>
				<td>${data_o[id_s][1]}</td>
				<td>${data_o[id_s][2]}</td>
				<td>${data_o[id_s][3]}</td>
				<td>${data_o[id_s][4]}</td>
			</tr>
			% endfor
		</table>
		<div>
            <form method = "GET" action ="/add_lv/">
			<button type="submit">Erfassen</button>
			</form>
			<button id = "deleter_lv" >Loeschen</button>
			<button id = "edit_lv" >Bearbeiten</button>
		</div>
		</div>
			<input type="reset" value="Zurück" onclick="location.href = '/studiengaenge'"/><!-- Logout Button -->
		</div>