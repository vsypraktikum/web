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
		    <tr>
                <th>Willkommen!</th>
                <div>
					<th>Bitte geben Sie ihr Kennwort ein:</th> 
				</div>
				<form id="idWTForm" action="/login_bk" method="POST">
				<div>
					<label for="benutzername_s">Benutzername</label>
					<input type="string" value="$benutzername_s" id="benutzername_s" name="benutzername_s" required />
				</div>
				<div>
					<label for="kennwort_s">Kennwort</label>
					<input type="text" value="$kennwort_s" id="kennwort_s" name="kennwort_s" required />
				</div>
				 <div>
					<input type="submit" value="Anmeldung"/>
				</div>
            </tr>
    </body>
</html>

