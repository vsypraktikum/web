## -*- coding: utf-8 -*-
<%inherit file="layout.tpl"/>
<%block name="header">
	<body>
		<table style="text-align:center;">
		<h1>Form Lehrender Modul</h1>
		<br>
			<select id="studiengang" name="studiengang">
				<option value="0">Wählen Sie Ihren Studiengang:</option>
				%for a in data_o.values():
					<option value="${a[1]}">${a[0]}</option>
				%endfor
			</select>
			<button id = "buttonstud">Studienganginfos und Modulhandbuch anzeigen</button>
			<p />
			<select id="modul" name="modul">
				<option value="0">Wählen Sie Ihr Modul aus:</option>
				%for b in data_modul.values():
					<option value="${b[0]}">${b[0]}</option>
				%endfor
			</select><br>
			<button id="buttonmoduledit">Modul Bearbeiten</button><br>
			<p />
			<form action="/" method="POST">
				<button type="submit">Logout</button><br>
			</form>
			<script src="mhb_modul.js"></script>
	</body>
</%block>
