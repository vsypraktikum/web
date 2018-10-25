## coding: utf-8 
<!DOCTYPE html>
<html>
    <head>
        <title>Modulhandbuch</title>
        <meta charset="UTF-8" />
        <style>
            @import "/mhb.css";
        </style>
		<script type="text/javascript" src="/mhb_login.js"></script>
    </head>
    <body id="body">
                <h1>Willkommen beim Modulhandbuch!</h1>
                <div>
				<p><th>Bitte geben Sie ihre Anmeldedaten ein:</th></p> 
				</div>
				<form id="idWTForm">
				<div>
					<label for="benutzername_s">Benutzername</label>
					<input type="string" value="@stud.hn.de" id="benutzername_s" name="benutzername_s" required />
				</div>
				<div>
					<label for="kennwort_s">Kennwort</label>
					<input type="password" value="" id="kennwort_s" name="kennwort_s"/>
				</div>
				<div>
					<button type="button" onclick="form_abschicken('login')">Weiter</button>
				</div>
				</form>
    </body>
	
</html>