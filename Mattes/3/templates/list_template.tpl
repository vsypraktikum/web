<%doc>
	Tempaltes für samtliche Templates
</%doc>

% if ansicht==0:
		<menu id="menuContainer">
			<button id="add">Hinzufügen</button>
			<button id="edit">Bearbeiten</button>
			<button id="delete">Löschen</button>
		</menu>
		<table id="table">
			<tr>
				<th>Matr.-Nr.</th><th>Name</th><th>Vorname</th>
			</tr>
			% for key_s in data_o:
				<tr id="${key_s}" class="noMark">
					<td >${data_o[key_s]['matrikelnr']}</td>
					<td>${data_o[key_s]['name']}</td>
					<td>${data_o[key_s]['vorname']}</td>

				</tr>
			% endfor
		</table>
		
		
% elif ansicht==1:
		<menu id="menuContainer">
			<button id="add">Hinzufügen</button>
			<button id="edit">Bearbeiten</button>
			<button id="delete">Löschen</button>
		</menu>
		<table id="table">
			<tr>
				<th>Titel</th><th>Name</th><th>Vorname</th><th>Lehrgebiet</th>
			</tr>
			
			% for key_s in data_o:
				<tr id="${key_s}" class="noMark">
					<td>${data_o[key_s]['titel']}</td>
					<td>${data_o[key_s]['name']}</td>
					<td>${data_o[key_s]['vorname']}</td>
					<td>${data_o[key_s]['lehrgebiet']}</td>
				</tr>
			% endfor
		
		</table>
		

% elif ansicht==2:
		<menu id="menuContainer">
			<button id="add">Hinzufügen</button>
			<button id="edit">Bearbeiten</button>
			<button id="delete">Löschen</button>
		</menu>
		<table id="table"> 
		
			<tr>
				<th>Name.</th><th>Branche</th><th>Taetigkeitsschwerpunkt</th><th>Sitz</th><th>Anzahl Mitarbeiter</th>
			</tr>
			
			% for key_s in data_o:
				<tr id="${key_s}" class="noMark">
					<td>${data_o[key_s]['name']}</td>
					<td>${data_o[key_s]['branche']}</td>
					<td>${data_o[key_s]['schwerpunkt']}</td>
					<td>${data_o[key_s]['sitz']}</td>
					<td>${data_o[key_s]['mitarbeiteranzahl']}</td>
				</tr>
			% endfor
		</table>

% elif ansicht==3:
		<menu id="menuContainer">
			<button id="add">Hinzufügen</button>
			<button id="edit">Bearbeiten</button>
			<button id="einschreiben">Einschreiben</button>
			<button id="delete">Löschen</button>
		</menu>
		<table id="table">
			<tr>
				<th>Titel</th>
				<th>Beschreibung</th>
				<th>Firma-ID</th>
				<th>Voraussetzungen</th>
				<th>Kontakt</th>
				<!--<th>Lehrenden-ID</th>
				<th>Matrikel-ID</th>
				<th>Anfangsdatum</th>
				<th>Enddatum</th>-->
			</tr>
			<div id="table">
			% for key_s in data_o:
				<tr id="${key_s}" class="noMark">
					<td>${data_o[key_s]['pptitel']}</td>
					<td>${data_o[key_s]['beschreibung']}</td>
					<td>${data_o[key_s]['firmaid']}</td>
					<td>${data_o[key_s]['voraussetzung']}</td>
					<td>${data_o[key_s]['kontakt']}</td>
					<!--<td>${data_o[key_s]['lehrendenid']}</td>
					<td>${data_o[key_s]['matrikelid']}</td>
					<td>${data_o[key_s]['anfangsdatum']}</td>
					<td>${data_o[key_s]['enddatum']}</td>-->
				</tr>
			% endfor
			
		</table>
		
% elif ansicht==4:

		<table id="table">
			<tr>
				<th>Firma</th>
				<th>Branche</th>
				<th>Schwerpunkt</th>
				<th>Sitz</th>
				<th>Mitarbeiteranzahl</th>
				<th>Projekttitel</th>
				<th>Beschreibung</th>
				<th>Voraussetzungen</th>
				<th>Kontakt</th>
				<th>Lehrenden-ID</th>
				<th>Matrikel-ID</th>
				<th>Anfangsdatum</th>
				<th>Enddatum</th>
			</tr>
			
			% for key_s in data_o['ppangebot']['list']:
				<tr id="${key_s}">
					<td>${data_o['ppangebot']['list'][key_s]['name']}</td>
					<td>${data_o['ppangebot']['list'][key_s]['branche']}</td>
					<td>${data_o['ppangebot']['list'][key_s]['schwerpunkt']}</td>
					<td>${data_o['ppangebot']['list'][key_s]['sitz']}</td>
					<td>${data_o['ppangebot']['list'][key_s]['mitarbeiteranzahl']}</td>
					<td>${data_o['ppangebot']['list'][key_s]['pptitel']}</td>
					<td>${data_o['ppangebot']['list'][key_s]['beschreibung']}</td>
					<td>${data_o['ppangebot']['list'][key_s]['voraussetzung']}</td>
					<td>${data_o['ppangebot']['list'][key_s]['kontakt']}</td>
					<td>${data_o['ppangebot']['list'][key_s]['lehrendenid']}</td>
					<td>${data_o['ppangebot']['list'][key_s]['matrikelid']}</td>
					<td>${data_o['ppangebot']['list'][key_s]['anfangsdatum']}</td>
					<td>${data_o['ppangebot']['list'][key_s]['enddatum']}</td>
				</tr>
			% endfor
			
			% for key_s in data_o['ppaktuell']['list']:
				<tr id="" class="PPAktuell">
					<td>${key_s['name']}</td>
					<td>${key_s['branche']}</td>
					<td>${key_s['schwerpunkt']}</td>
					<td>${key_s['sitz']}</td>
					<td>${key_s['mitarbeiteranzahl']}</td>
					<td>${key_s['pptitel']}</td>
					<td>${key_s['beschreibung']}</td>
					<td>${key_s['voraussetzung']}</td>
					<td>${key_s['kontakt']}</td>
					<td>${key_s['lehrendenid']}</td>
					<td>${key_s['matrikelid']}</td>
					<td>${key_s['anfangsdatum']}</td>
					<td>${key_s['enddatum']}</td>
				</tr>
			% endfor
			
			% for key_s in data_o['ppabgeschlossen']['list']:
				<tr id="" class="PPAbgeschlossen">
					<td>${key_s['name']}</td>
					<td>${key_s['branche']}</td>
					<td>${key_s['schwerpunkt']}</td>
					<td>${key_s['sitz']}</td>
					<td>${key_s['mitarbeiteranzahl']}</td>
					<td>${key_s['pptitel']}</td>
					<td>${key_s['beschreibung']}</td>
					<td>${key_s['voraussetzung']}</td>
					<td>${key_s['kontakt']}</td>
					<td>${key_s['lehrendenid']}</td>
					<td>${key_s['matrikelid']}</td>
					<td>${key_s['anfangsdatum']}</td>
					<td>${key_s['enddatum']}</td>
				</tr>
			% endfor
		</table>

% elif ansicht==5:

		<table id="table">
			<tr>
				<th>Matrikelnummer</th>
				<th>Vorname</th>
				<th>Name</th>
				<th>Projekttitel</th>
				<th>Beschreibung</th>
				<th>Firma</th>
				<th>Voraussetzungen</th>
				<th>Kontakt</th>
				<th>Lehrenden-ID</th>
				<th>Anfangsdatum</th>
				<th>Enddatum</th>
			</tr>
			% for key_s in data_o['ppaktuell']['list']:
				<tr id="${key_s}" class="PPAktuell">
					<td>${key_s['matrikelnr']}</td>
					<td>${key_s['vorname']}</td>
					<td>${key_s['name']}</td>
					<td>${key_s['pptitel']}</td>
					<td>${key_s['beschreibung']}</td>
					<td>${key_s['firmaid']}</td>
					<td>${key_s['voraussetzung']}</td>
					<td>${key_s['kontakt']}</td>
					<td>${key_s['lehrendenid']}</td>
					<td>${key_s['anfangsdatum']}</td>
					<td>${key_s['enddatum']}</td>
				</tr>
			% endfor
			
			% for key_s in data_o['ppabgeschlossen']['list']:
				<tr id="${key_s}" class="PPAbgeschlossen">
					<td>${key_s['matrikelnr']}</td>
					<td>${key_s['vorname']}</td>
					<td>${key_s['name']}</td>
					<td>${key_s['pptitel']}</td>
					<td>${key_s['beschreibung']}</td>
					<td>${key_s['firmaid']}</td>
					<td>${key_s['voraussetzung']}</td>
					<td>${key_s['kontakt']}</td>
					<td>${key_s['lehrendenid']}</td>
					<td>${key_s['anfangsdatum']}</td>
					<td>${key_s['enddatum']}</td>
				</tr>
			% endfor
		</table>

% elif ansicht==6:

		<table id="table">
			<tr>
				<th>Titel</th>
				<th>Vorname</th>
				<th>Name</th>
				<th>Lehrgebiet</th>
				<th>Titel</th>
				<th>Beschreibung</th>
				<th>Firmen-ID</th>
				<th>Voraussetzungen</th>
				<th>Kontakt</th>
				<th>Matrikel-ID</th>
				<th>Anfangsdatum</th>
				<th>Enddatum</th>
			</tr>
			% for key_s in data_o['ppaktuell']['list']:
				<tr id="${key_s}" class="PPAktuell">
					<td>${key_s['titel']}</td>
					<td>${key_s['vorname']}</td>
					<td>${key_s['name']}</td>
					<td>${key_s['lehrgebiet']}</td>
					<td>${key_s['pptitel']}</td>
					<td>${key_s['beschreibung']}</td>
					<td>${key_s['firmaid']}</td>
					<td>${key_s['voraussetzung']}</td>
					<td>${key_s['kontakt']}</td>
					<td>${key_s['matrikelid']}</td>
					<td>${key_s['anfangsdatum']}</td>
					<td>${key_s['enddatum']}</td>
				</tr>
			% endfor
			
			% for key_s in data_o['ppabgeschlossen']['list']:
				<tr id="${key_s}" class="PPAbgeschlossen">
					<td>${key_s['titel']}</td>
					<td>${key_s['vorname']}</td>
					<td>${key_s['name']}</td>
					<td>${key_s['lehrgebiet']}</td>
					<td>${key_s['pptitel']}</td>
					<td>${key_s['beschreibung']}</td>
					<td>${key_s['firmaid']}</td>
					<td>${key_s['voraussetzung']}</td>
					<td>${key_s['kontakt']}</td>
					<td>${key_s['matrikelid']}</td>
					<td>${key_s['anfangsdatum']}</td>
					<td>${key_s['enddatum']}</td>
				</tr>
			% endfor
		</table>

% endif