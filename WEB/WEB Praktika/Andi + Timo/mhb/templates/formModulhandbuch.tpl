## -*- coding: utf-8 -*-
<%inherit file="layout.tpl"/>
<%block name="header">
	<body>
		<h1><u>Modulhandbuch zum Studiengang:</u> ${id_s}</h1>
		<div>
			%for a in data_mod.values():
				%if a[8] == id_s:
					<u>Bezeichnung des Moduls:</u> <p /> ${a[0]} <p />
					<u>Beschreibung des Moduls:</u> <p /> ${a[1]} <p />
					<u>Anzahl Kreditpunkte:</u> <p /> ${a[2]} <p />
					<u>Anzahl Vorlesung:</u> <p /> ${a[3]} <p />
					<u>Anzahl Übung:</u> <p /> ${a[4]} <p />
					<u>Anzahl Praktikum:</u> <p /> ${a[5]} <p />
					<u>Voraussetzungen:</u> <p /> ${a[6]} <p />
					<u>Modulverantwortlicher</u> <p /> ${a[7]} <p />
				%endif
			%endfor
		</div>
	</body>
</%block>
