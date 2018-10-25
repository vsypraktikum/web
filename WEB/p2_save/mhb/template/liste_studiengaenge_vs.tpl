## coding: utf-8 
<body id="demo">
		<h1>Liste der Studiengänge</h1>
		<table id="idList">
			<tr><th>Bezeichnung</th><th>Kurzbezeichnung</th><th>Beschreibung</th><th>Anzahl Semester</th><th>Lehrveranstaltungen</th>
			## man verwendet hier Zugriff auf das Dictionary "data_o"
			% for id_s in sorted(data_o):
				<tr id="${id_s}">
				<td>${data_o[id_s][0]}</td>
				<td>${data_o[id_s][1]}</td>
				<td>${data_o[id_s][2]}</td>
				<td>${data_o[id_s][3]}</td>
				<td>
					% for id_l in sorted(data_l):
					%	if data_l[id_l][4]==data_o[id_s][1]:	
						${data_l[id_l][0]} /
					%	endif	
					% endfor	
				</td>	
			</tr>
			% endfor
		</table>
		<div>
            <form method = "GET" action ="/add_sg">
			<button type="submit">Erfassen</button>
			</form>
			<button id = "deleter_studiengang" >Loeschen</button>
			<button id = "edit_studiengang" >Bearbeiten</button>
			<button id = "modulhandbuch" >Modulhandbuch</button>
		</div>
		<h1>Liste der Module</h1>
		<table id="idList">
			<tr><th>Bezeichnung</th><th>Beschreibung</th><th>Anzahl Kreditpunkte</th><th>Anzahl SWS - Vorlesung</th><th>Anzahl SWS - Übung</th><th>Anzahl SWS - Praktikum</th><th>Voraussetzungen(andere Module)</th><th>Modulverantwortlicher</th><th>Studiengang Kurzbezeichnung</th>
			## man verwendet hier Zugriff auf das Dictionary "data_m"
			% for id_s in data_m:
				<tr id="${id_s}">
				<td>${data_m[id_s][0]}</td>
				<td>${data_m[id_s][1]}</td>
				<td>${data_m[id_s][2]}</td>
				<td>${data_m[id_s][3]}</td>
				<td>${data_m[id_s][4]}</td>
				<td>${data_m[id_s][5]}</td>
				<td>${data_m[id_s][6]}</td>
				<td>${data_m[id_s][7]}</td>
				<td>${data_m[id_s][8]}</td>
			</tr>
			% endfor
		</table>
		<div>
            <form method = "GET" action ="/add_m">
			<button type="submit">Erfassen</button>
			</form>
			<button id = "deleter_modul" >Loeschen</button>
			<button id = "edit_modul" >Bearbeiten</button>
		</div>
		<input type="reset" value="Logout" onclick="location.href = '/'"/><!-- Logout Button -->
</body>