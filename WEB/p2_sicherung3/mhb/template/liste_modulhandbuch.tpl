## coding: utf-8 
<!DOCTYPE html>
<html>
    <head>
        <title>Modulhandbuch</title>
        <meta charset="UTF-8" />
        <style>
            @import "/mhb.css";
        </style>
        <script type="text/javascript" src="/mhb_vm.js"></script>
    </head>
    <body>
		<h1>Modulhandbuch für Studiengang:</h1>
		<table id="idList_m">
			<tr><th>Bezeichnung</th><th>Kurzbezeichnung</th><th>Beschreibung</th><th>Anzahl Semester</th>
			## man verwendet hier Zugriff auf das Dictionary "data_o"
			##% for id_s in data_o:
				<tr id="m${id_stg}">
				<td>${data_o[id_stg][0]}</td>
				<td>${data_o[id_stg][1]}</td>
				<td>${data_o[id_stg][2]}</td>
				<td>${data_o[id_stg][3]}</td>
			</tr>
			##% endfor
		</table>
		<h1>Liste der Module</h1>
		<table id="idList_s">
			<tr><th>Bezeichnung</th><th>Beschreibung</th><th>Anzahl Kreditpunkte</th><th>Anzahl SWS - Vorlesung</th><th>Anzahl SWS - Übung</th><th>Anzahl SWS - Praktikum</th><th>Voraussetzungen(andere Module)</th>
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
			</tr>
			% endfor
		</table>
		<h1>Liste der Lehrveranstaltungen</h1>
		<table id="idList_lv">
			<tr><th>Bezeichnung</th><th>Kurzbezeichnung</th><th>Lage (Semester)</th>
			## man verwendet hier Zugriff auf das Dictionary "data_l"
			% for id_s in data_l:
			% 	if data_l[id_s][3]==data_o[id_stg][1]:
				<tr id="${id_s}">
				<td>${data_l[id_s][0]}</td>
				<td>${data_l[id_s][1]}</td>
				<td>${data_l[id_s][2]}</td>
				</tr>
			%	endif
			% endfor
		</table>
		<input type="reset" value="Logout" onclick="location.href = '/'"/><!-- Logout Button -->
		<input type="reset" value="Zurück" onclick="location.href = '/studiengaenge'"/>
    </body>
</html>