## coding: utf-8 
<!DOCTYPE html>
<html>
    <head>
        <title>Modulhandbuch</title>
        <meta charset="UTF-8" />
        <style>
            @import "/mhb.css";
        </style>
        <script type="text/javascript" src="/mhb.js"></script>
    </head>
    <body>
		<h1>Liste der Studiengänge</h1>
		<table id="idList_s">
			<tr><th>Bezeichnung</th><th>Kurzbezeichnung</th><th>Beschreibung</th><th>Anzahl Semester</th>
			## man verwendet hier Zugriff auf das Dictionary "data_o"
			% for id_s in data_o:
				<tr id="${id_s}">
				<td>${data_o[id_s][0]}</td>
				<td>${data_o[id_s][1]}</td>
				<td>${data_o[id_s][2]}</td>
				<td>${data_o[id_s][3]}</td>
			</tr>
			% endfor
		</table>
		</div>
			<button id = "modulhandbuch">Modulhandbuch</button>
			<input type="reset" value="Logout" onclick="location.href = '/'"/><!-- Logout Button -->
		</div>
    </body>
	
</html>