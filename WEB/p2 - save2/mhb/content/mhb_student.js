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

function open_modulhandbuch() {
		document.location.href = "/modulhandbuch/" + selected.toString();
}

window.onload=function(){
	
	let body_o = document.getElementById('body');
	//let list_o = document.getElementById('idList');
	let button_modulhandbuch = document.getElementById('modulhandbuch');
	
	body_o.addEventListener('click', get_tabellenzeile, false)
	//list_o.addEventListener('click',get_tabellenzeile,false);
	button_modulhandbuch.addEventListener('click', open_modulhandbuch, false);
}
