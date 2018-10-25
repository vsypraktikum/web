## -*- coding: utf-8 -*-
<%inherit file="layout.tpl"/>
<%block name="header">
	<body>
		<fieldset>
			<form action="/bearbeiten/save" method="POST">
				Studiengang:
				<input type="text" value="${data_o['Studiengang']}"name="Studiengang"><br>
				Modul:
				<input type="text" value="${data_o['Modul']}"name="Modul"><br>
				<button type="submit">Speichern</button><br>
			</form>
			<button onclick="goBack()">Go Back 2 Pages</button>
			<script>
			function goBack() {
			    window.history.go(-1);
			}
			</script>
		</fieldset>
	</body>
</%block>
