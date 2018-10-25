## coding: utf-8 
<!DOCTYPE html>
<html>
    <head>
        <title>Web-Teams</title>
        <meta charset="UTF-8" />
        <style>
            @import "/webteams.css";
        </style>
        <script type="text/javascript" src="/webteams.js"></script>
    </head>
    <body>
		<table id="idList">
            <tr>
                <th>Name (1)</th><th>Vorname (1)</th><th>Matr.-Nr. (1)</th><th>Semesteranzahl (1)</th>
                <th>Name (2)</th><th>Vorname (2)</th><th>Matr.-Nr. (2)</th><th>Semesteranzahl (2)</th>
                <th>Aktion</th>
			</tr>
			
			## man verwendet hier Zugriff auf das Dictionary "data_o"
			
			% for key_s in data_o:
			<tr id="r${key_s}">
				  <td>${data_o[key_s][0]}</td><td>${data_o[key_s][1]}
			##    <td>${data_o[key_s]['name1_s']}</td><td>${data_o[key_s]['vorname1_s']}</td><td>${data_o[key_s]['matrnr1_s']}</td><td>${data_o[key_s]['semesteranzahl1_s']}</td>
            ##    <td>${data_o[key_s]['name2_s']}</td><td>${data_o[key_s]['vorname2_s']}</td><td>${data_o[key_s]['matrnr2_s']}</td><td>${data_o[key_s]['semesteranzahl2_s']}</td>
            ##    <td><a href="/edit/$id_s">bearbeiten</a>&nbsp;<a href="/delete/$id_s" class="clDelete">löschen</a></td>
            </tr>
			% endfor
		</table>	
## Mako-Kommentare verwenden zwei #-Zeichen
        <div>
            <a href="/add">erfassen</a>
        </div>
    </body>
</html>
