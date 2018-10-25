function studiengangAnzeige() {
	var get = document.getElementById("studiengang");
	var selected = get.options[get.selectedIndex].value;
	if(selected == '0'){
		alert("Bitte geben Sie einen Studiengang an");
	}
	else document.location.href = "/studiengang/" + selected.toString();
}

function modulEdit() {
	var get = document.getElementById("modul");
	var selected = get.options[get.selectedIndex].value;
		if(selected == '0'){
		alert("Bitte geben Sie ein Modul an");
	}
	else document.location.href = "/editModul/" + selected.toString();
}

window.onload=function(){
	let studbutton = document.getElementById('buttonstud');
	studbutton.addEventListener('click', studiengangAnzeige, false);

	let modulbuttonedit = document.getElementById('buttonmoduledit');
	modulbuttonedit.addEventListener('click', modulEdit, false);
}

