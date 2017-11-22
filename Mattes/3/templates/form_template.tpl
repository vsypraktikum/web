<%doc>
	Tempaltes für sämtliche Formulare
</%doc>

% if ansicht==0:
		<br>
		<menu id="menuContainer">
			<button id="save">Speichern</button>
			<button id="back">Abbrechen</button>
		</menu>
		<form id="Form">
			<input type="hidden" value="${id_s}" id="id" name="id" />
		
			<div class="labelBox"><label for="matrikelnr">Matrikel Nr.</label></div>
			<div class="inputBox"><input type="text" value="${data_o['matrikelnr']}" id="matrikelnr" name="matrikelnr" required /></div>
			
			<div class="labelBox"><label for="name">Name</label></div>
			<div class="inputBox"><input type="text" value="${data_o['name']}" id="name" name="name" required /></div>
			
			<div class="labelBox"><label for="vorname">Vorname</label></div>
			<div class="inputBox"><input type="text" value="${data_o['vorname']}" id="vorname" name="vorname" required /></div>
			
		</form>
		
		
% elif ansicht==1:
		<br>
		<menu id="menuContainer">
			<button id="save">Speichern</button>
			<button id="back">Abbrechen</button>
		</menu>
		<form id="Form">
		
			<input type="hidden" value="${id_s}" id="id" name="id" />
			
			<div class="labelBox"><label for="titel">Titel</label></div>
			<div><input type="text" value="${data_o['titel']}" id="titel" name="titel" required /></div>
				
			<div class="labelBox"><label for="name">Name</label></div>
			<div><input type="text" value="${data_o['name']}" id="name" name="name" required /></div>
			
			<div class="labelBox"><label for="vorname">Vorname</label></div>
			<div><input type="text" value="${data_o['vorname']}" id="vorname" name="vorname" required /></div>
			
			<div class="labelBox"><label for="lehrgebiet">Lehrgebiet</label></div>
			<div><input type="text" value="${data_o['lehrgebiet']}" id="lehrgebiet" name="lehrgebiet" required /></div>
		</form>
		
% elif ansicht==2:
		<br>
		<menu id="menuContainer">
			<button id="save">Speichern</button>
			<button id="back">Abbrechen</button>
		</menu>
		<form id="Form">
		
			<input type="hidden" value="${id_s}" id="id" name="id_" />
			
			<div class="labelBox"><label for="name">Name</label></div>
			<div><input type="text" value="${data_o['name']}" id="name" name="name" required /></div>
			
			<div class="labelBox"><label for="branche">Branche</label></div>
			<div><input type="text" value="${data_o['branche']}" id="branche" name="branche" required /></div>
			
			<div class="labelBox"><label for="schwerpunkt">Tätigkeitsschwerpunkt</label></div>
			<div><input type="text" value="${data_o['schwerpunkt']}" id="schwerpunkt" name="schwerpunkt" required /></div>
			
			<div class="labelBox"><label for="sitz">Sitz</label></div>
			<div><input type="text" value="${data_o['sitz']}" id="sitz" name="sitz" required /></div>
			
			<div class="labelBox"><label for="mitarbeiteranzahl">Mitarbeiteranzahl</label></div>
			<div><input type="text" value="${data_o['mitarbeiteranzahl']}" id="mitarbeiteranzahl" name="mitarbeiteranzahl" required /></div>
			
		</form>
		
% elif ansicht==3:
		<br>
		<menu id="menuContainer">
			<button id="save">Speichern</button>
			<button id="back">Abbrechen</button>
		</menu>
		<form id="Form">
			<input type="hidden" value="${id_s}" id="id" name="id" />
			
			<div class="labelBox"><label for="pptitel">pptitel</label></div>
			<div><input type="text" value="${data_o['pptitel']}" id="pptitel" name="pptitel" required /></div>
			
			<div class="labelBox"><label for="beschreibung">Beschreibung</label></div>
			<div><input type="text" value="${data_o['beschreibung']}" id="beschreibung" name="beschreibung" required /></div>

			<div class="labelBox"><label for="firma">Firma-ID</label></div>
			<div><select id="firmaid" name="firmaid" required>
					<option value=""></option>
				% for key_s in option['firma']['list']:
					<option value="${key_s}">${option['firma']['list'][key_s]['name']}</option>
				% endfor
			</select></div>
			
			<div class="labelBox"><label for="voraussetzung">Voraussetzungen</label></div>
			<div><input type="text" value="${data_o['voraussetzung']}" id="voraussetzung" name="voraussetzung" required /></div>
			
			<div class="labelBox"><label for="kontakt">Kontakt</label></div>
			<div><input type="text" value="${data_o['kontakt']}" id="kontakt" name="kontakt" required /></div>
			
			<div><input type="hidden" value="${data_o['lehrendenid']}" id="lehrendenid" name="lehrendenid" required /></div>
			<div><input type="hidden" value="${data_o['matrikelid']}" id="matrikelid" name="matrikelid" required /></div>
			<div><input type="hidden" value="${data_o['anfangsdatum']}" id="anfangsdatum" name="anfangsdatum" required /></div>
			<div><input type="hidden" value="${data_o['enddatum']}" id="enddatum" name="enddatum" required /></div>
			</form>
			
% else:
		<br>
		<menu id="menuContainer">
			<button id="save">Speichern</button>
			<button id="back">Abbrechen</button>
		</menu>
		<form id="Form">
			<input type="hidden" value="${id_s}" id="id" name="id" />
			
			<div class="labelBox"><label for="pptitel">pptitel</label></div>
			<div><input type="text" value="${data_o['pptitel']}" id="pptitel" name="pptitel" required /></div>
			
			<div class="labelBox"><label for="beschreibung">Beschreibung</label></div>
			<div><input type="text" value="${data_o['beschreibung']}" id="beschreibung" name="beschreibung" required /></div>

			<div class="labelBox"><label for="firma">Firma-ID</label></div>
			<div><select id="firmaid" name="firmaid" required>
					<option value=""></option>
				% for key_s in option['firma']['list']:
					<option value="${key_s}">${option['firma']['list'][key_s]['name']}</option>
				% endfor
			</select></div>
			
			<div class="labelBox"><label for="voraussetzung">Voraussetzungen</label></div>
			<div><input type="text" value="${data_o['voraussetzung']}" id="voraussetzung" name="voraussetzung" required /></div>
			
			<div class="labelBox"><label for="kontakt">Kontakt</label></div>
			<div><input type="text" value="${data_o['kontakt']}" id="kontakt" name="kontakt" required /></div>
			
			<div class="labelBox"><label for="lehrendenid">Lehrenden-ID</label></div>
			<div><select id="lehrendenid" name="lehrendenid" required>
				% for key_s in option['lehrende']['list']:
					<option value="${key_s}">${option['lehrende']['list'][key_s]['name']}</option>
				% endfor
			</select></div>
			
			<div class="labelBox"><label for="matrikelid">Matrikelidt</label></div>
			<div><select id="matrikelid" name="matrikelid" required>
					<option value="${data_o['matrikelid']}"></option>
				% for key_s in option['student']['list']:
					<option value="${key_s}">${option['student']['list'][key_s]['name']}</option>
				% endfor
			</select></div>
			
			<div class="labelBox"><label for="anfangsdatum">Anfangsdatum</label></div>
			<div><input type="date" value="${data_o['anfangsdatum']}" id="anfangsdatum" name="anfangsdatum" required /></div>
			
			<div class="labelBox"><label for="enddatum">Enddatum</label></div>
			<div><input type="date" value="${data_o['enddatum']}" id="enddatum" name="enddatum" required /></div>
			</form>
% endif
		<div id="StatusText"></div>