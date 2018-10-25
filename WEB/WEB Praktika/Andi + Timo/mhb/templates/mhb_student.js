function studiengangAnzeige() {
	var get = document.getElementById("studiengang");
	var selected = get.options[get.selectedIndex].value;
	if(selected == '0'){
		alert("Bitte geben Sie einen Studiengang an");
	}
	else document.location.href = "/studiengang/" + selected.toString();
}

window.onload=function(){
	let e = document.getElementById('buttonstud');
	e.addEventListener('click', studiengangAnzeige, false);
}

