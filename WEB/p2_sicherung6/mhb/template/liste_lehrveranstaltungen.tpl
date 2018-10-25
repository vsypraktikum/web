## coding: utf-8 
		<h1>Liste der Lehrveranstaltungen</h1>
		<table id="idList_s">
			<tr><th>Bezeichnung</th><th>Kurzbezeichnung</th><th>Lage (Semester)</th>
			## man verwendet hier Zugriff auf das Dictionary "data_l"
			##% for id_s in data_l:
			##	<tr id="${id_s}">
			##	<td>${data_l[id_s][0]}</td>
			##	<td>${data_l[id_s][1]}</td>
			##	<td>${data_l[id_s][2]}</td>
			</tr>
			##% endfor
			
		</table>
		<div>
            <form method = "GET" action ="/add_lv">
			<button type="submit">Erfassen</button>
			</form>
			<button id = "deleter_studiengang" >Loeschen</button>
			<button id = "edit_studiengang" >Bearbeiten</button>
			<button id = "modulhandbuch" >Modulhandbuch</button>
		</div>
		</div>
			<input type="reset" value="Zurück" onclick="location.href = '/studiengaenge_vs'"/><!-- Logout Button -->
		</div>