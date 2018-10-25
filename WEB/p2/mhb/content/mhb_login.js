var selected;

function event_handler(event_opl){
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
	
	//Modulhandbuch Events
	
	if(event_opl.target.id == "modulhandbuch"){
		seite_anfragen("/modulhandbuch/" + selected.toString());
	}
	
	if(event_opl.target.id == "modulhandbuch_zurück"){
		seite_anfragen("/studiengaenge/");
	}
	
	//Studiengang Events
	
	if(event_opl.target.id == "create_studiengang"){
		seite_anfragen("/add_sg/");
	}
	
	if(event_opl.target.id == "edit_studiengang"){
		seite_anfragen("/edit_sg/" + selected.toString());
	}
	
	if(event_opl.target.id == "studiengang_speichern"){
		form_abschicken("/save_sg/");
	}
	
	if(event_opl.target.id == "deleter_studiengang"){
		seite_anfragen("/delete_sg/" + selected.toString());
	}
	
	//Module Events
	
	if(event_opl.target.id == "create_modul"){
		seite_anfragen("/add_m/");
	}
	
	if(event_opl.target.id == "edit_modul"){
		seite_anfragen("/edit_m/" + selected.toString());
	}
	
	if(event_opl.target.id == "modul_speichern"){
		form_abschicken("/save_m/");
	}
	
	if(event_opl.target.id == "deleter_modul"){
		seite_anfragen("/delete_m/" + selected.toString());
	}
	
	//Lehrveranstaltungen Events
	
	if(event_opl.target.id == "create_lv"){
		seite_anfragen("/add_lv/");
	}
	
	if(event_opl.target.id == "edit_lv"){
		seite_anfragen("/edit_lv/" + selected.toString());
	}
	
	if(event_opl.target.id == "lv_speichern"){
		form_abschicken("/save_lv/");
	}
	
	if(event_opl.target.id == "deleter_lv"){
		seite_anfragen("/delete_lv/" + selected.toString());
	}
}

function form_abschicken(path) {
	var data = new FormData(document.getElementById("idWTForm"));
	console.log(data)
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			document.getElementById("body").innerHTML =
			this.responseText;
		}
	};
	xhttp.open("POST", path, true);
	xhttp.send(data);
}

function seite_anfragen(path) {
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			document.getElementById("body").innerHTML =
			this.responseText;
		}
	};
	xhttp.open("GET", path, true);
	xhttp.send();
}

window.onload=function(){
	
	let body_o = document.getElementById('body');
	//let list_o = document.getElementById('idList');
	//let button_modulhandbuch = document.getElementById('modulhandbuch');
	
	body_o.addEventListener('click', event_handler, false)
	//list_o.addEventListener('click',get_tabellenzeile,false);
	//button_modulhandbuch.addEventListener('click', open_modulhandbuch, false);
}