## coding: utf-8
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
		</div>
			<button id = "modulhandbuch">Modulhandbuch</button>
			<input type="reset" value="Logout" onclick="location.href = '/'"/><!-- Logout Button -->
		</div>