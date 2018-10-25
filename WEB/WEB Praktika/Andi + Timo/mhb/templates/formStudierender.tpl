<body>
	<h1>Form Studierender</h1>
	<br>		
		<select id="studiengang" name="studiengang">
			<option value="0">Wählen Sie Ihren Studiengang:</option>
			%for a in data_o.values():
				<option value="${a[1]}">${a[0]}</option>
			%endfor
		</select>
		<button id = "buttonstud">Studienganginfos und Modulhandbuch anzeigen</button>
		<form action="/" method="POST">
			<button type="submit">Logout</button><br>
		</form>
		<script src="mhb_student.js"></script>
</body>
