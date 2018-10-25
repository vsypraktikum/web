var selected;

function get_tabellenzeile(event_opl){
	if(event_opl.target.tagName.toLowerCase()=='td')
	{
		if (selected != undefined){
			var tmp = document.getElementById(selected.toString())
			tmp.style.textAlign = "left";
		}
		
		selected = event_opl.target.parentNode.id;
		
		var tmp = document.getElementById(selected.toString())
		
		tmp.style.textAlign = "center";
	}// Klick auf Link zum Löschen
}

function delete_eintrag_studiengang() {

	if (confirm("Wollen Sie diesen Eintrag wirklich löschen? " + selected.toString())){
		document.location.href = "/delete_sg/" + selected.toString();
	}

}

function edit_eintrag_studiengang() {
		if (confirm("Wollen Sie diesen Eintrag wirklich bearbeiten? " + selected.toString())){
		document.location.href = "/edit_sg/" + selected.toString();
	}
}

function delete_eintrag_modul() {

	if (confirm("Wollen Sie diesen Eintrag wirklich löschen? " + selected.toString())){
		document.location.href = "/delete_m/" + selected.toString();
	}

}

function edit_eintrag_modul() {
	if (confirm("Wollen Sie diesen Eintrag wirklich bearbeiten? " + selected.toString())){
		document.location.href = "/edit_m/" + selected.toString();
	}
}

function open_modulhandbuch() {
		document.location.href = "/modulhandbuch/" + selected.toString();
}

function form_abschicken(path) {
	var data = new FormData(document.getElementById("idWTForm"));
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			document.getElementById("demo").innerHTML =
			this.responseText;
		}
	};
	xhttp.open("POST", path, true);
	xhttp.send(data);
}

window.onload=function(){
	let list_o = document.getElementById('idList');
	let button_delete = document.getElementById('deleter_studiengang');
	let button_delete_m = document.getElementById('deleter_modul');
	let button_edit = document.getElementById('edit_studiengang');
	let button_edit_m = document.getElementById('edit_modul');
	let button_modulhandbuch = document.getElementById('modulhandbuch');
	
	list_o.addEventListener('click',get_tabellenzeile, false);
	button_delete.addEventListener('click', delete_eintrag_studiengang, false);
	button_delete_m.addEventListener('click', delete_eintrag_modul, false);
	button_edit.addEventListener('click', edit_eintrag_studiengang, false);
	button_edit_m.addEventListener('click', edit_eintrag_modul, false);
	button_modulhandbuch.addEventListener('click', open_modulhandbuch, false);
	button_open_lehrveranstaltungen.addEventListener('click', open_lehrveranstaltungen, false);
}
