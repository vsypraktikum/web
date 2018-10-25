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


function delete_eintrag_lv() {

	if (confirm("Wollen Sie diesen Eintrag wirklich löschen? " + selected.toString())){
		document.location.href = "/delete_lv/" + selected.toString();
	}

}

function edit_eintrag_lv() {
		if (confirm("Wollen Sie diesen Eintrag wirklich bearbeiten? " + selected.toString())){
		document.location.href = "/edit_lv/" + selected.toString();
	}
}

window.onload=function(){
	let list_lv_o = document.getElementById('idList_lv');
	let button_create = document.getElementById('erfassen_lv');
	let button_o = document.getElementById('deleter_lv');
	let button_edit = document.getElementById('edit_lv');
	
	
	list_lv_o.addEventListener('click',get_tabellenzeile,false);
	button_o.addEventListener('click', delete_eintrag_lv, false);
	button_edit.addEventListener('click', edit_eintrag_lv, false);
}
