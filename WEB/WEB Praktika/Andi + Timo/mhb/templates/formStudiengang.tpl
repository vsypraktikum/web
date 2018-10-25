## -*- coding: utf-8 -*-
<%inherit file="layout.tpl"/>
<%block name="header">
	<body>		
		<h1><u>Informationen zum Studiengang:</u> ${id_s}</h1>
		<table id="studInfos">
			<tr>
				<th>Bezeichnung des Studiengangs</th>
				<th>Kurzbezeichnung des Studiengangs</th>
				<th>Beschreibung des Studiengangs</th>
				<th>Anzahl der Semester des Studiengangs</th>
				<tr>
						%for a in data_o.values():
							%if a[1] == id_s:
								<td>${a[0]}</td>
								<td>${a[1]}</td>
								<td>${a[2]}</td>
								<td>${a[3]}</td>
								</tr>
							%endif
						%endfor
			</tr>
		</table>
		<h1><u>Modulhandbuch:</u> ${id_s}</h1>
		<table id="modInfos">
			<tr>
				<th>Bezeichnung</th>
				<th>Beschreibung</th>
				<th>Kreditpunkte</th>
				<th>Anzahl Vorlesung</th>
				<th>Anzahl Übung</th>
				<th>Anzahl Praktikum</th>
				<th>Voraussetzungen</th>
				<th>Modulverantwortlicher</th>
				<tr>
					%for b in data_mod.values():
						%if b[8] == id_s:
							<td>${b[0]}</td>
							<td>${b[1]}</td>
							<td>${b[2]}</td>
							<td>${b[3]}</td>
							<td>${b[4]}</td>
							<td>${b[5]}</td>
							<td>${b[6]}</td>
							<td>${b[7]}</td>
							</tr>
						%endif
					%endfor
			</tr>
		</table>
		<h1><u>Lehrveranstaltungen:</u> ${id_s}</h1>
		<table id="modInfos">
			<tr>
				<th>Bezeichnung</th>
				<th>Kurzbezeichnung</th>
				<th>Lage (Semester)</th>
				<th>Modul</th>
				<tr>
					%for c in data_lehr.values():
						%if c[4] == id_s:
							<td>${c[0]}</td>
							<td>${c[1]}</td>
							<td>${c[2]}</td>
							<td>${c[3]}</td>
							</tr>
						%endif
					%endfor
			</tr>
		</table>
		<div>
			<p />
			<input type="reset" value="Logout" onclick="location.href = '/'"/><p />
			<button onclick="goBack()">Go Back</button>
		</div>
		<script>
		function goBack() {
			window.history.back();
		}
		</script>
	</body>
</%block>
