function studiengangAnzeige() {
	var get = document.getElementById("studiengang");
	var selected = get.options[get.selectedIndex].value;
	if(selected == '0'){
		alert("Bitte geben Sie einen Studiengang an");
	}
	else document.location.href = "/studiengang/" + selected.toString();
}

function studiengangEdit() {
	var get = document.getElementById("studiengang");
	var selected = get.options[get.selectedIndex].value;
	if(selected == '0'){
		alert("Bitte geben Sie einen Studiengang an");
	}
	else document.location.href = "/editStudiengang/" + selected.toString();
}

function modulEdit() {
	var get = document.getElementById("modul");
	var selected = get.options[get.selectedIndex].value;
		if(selected == '0'){
		alert("Bitte geben Sie ein Modul an");
	}
	else document.location.href = "/editModul/" + selected.toString();
}

function lehrEdit() {
	var get = document.getElementById("lehr");
	var selected = get.options[get.selectedIndex].value;
		if(selected == '0'){
		alert("Bitte geben Sie eine Lehrveranstaltung an");
	}
	else document.location.href = "/editLehrveranstaltung/" + selected.toString();
}

function modulDelete() {
	var get = document.getElementById("modul");
	var selected = get.options[get.selectedIndex].value;
		if(selected == '0'){
		alert("Bitte geben Sie ein Modul an");
	}
	else document.location.href = "/deleteModul/" + selected.toString();
}

function lehrDelete() {
	var get = document.getElementById("lehr");
	var selected = get.options[get.selectedIndex].value;
		if(selected == '0'){
		alert("Bitte geben Sie eine Lehrveranstaltung an");
	}
	else document.location.href = "/deleteLehrveranstaltung/" + selected.toString();
}

function studDelete() {
	var get = document.getElementById("studiengang");
	var selected = get.options[get.selectedIndex].value;
		if(selected == '0'){
		alert("Bitte geben Sie einen Studiengang an");
	}
	else document.location.href = "/deleteStudiengang/" + selected.toString();
}

window.onload=function(){
	let studbutton = document.getElementById('buttonstud');
	studbutton.addEventListener('click', studiengangAnzeige, false);
	
	let studbuttonedit = document.getElementById('buttonstudedit');
	studbuttonedit.addEventListener('click', studiengangEdit, false);

	let studbuttondelete = document.getElementById('buttonstuddelete');
	studbuttondelete.addEventListener('click', studDelete, false);

	let modulbuttonedit = document.getElementById('buttonmoduledit');
	modulbuttonedit.addEventListener('click', modulEdit, false);

	let modulbuttondelete = document.getElementById('buttonmoduldelete');
	modulbuttondelete.addEventListener('click', modulDelete, false);

	let lehrbuttondelete = document.getElementById('buttonlehrdelete');
	lehrbuttondelete.addEventListener('click', lehrDelete, false);

	let lehrbuttonedit = document.getElementById('buttonlehredit');
	lehrbuttonedit.addEventListener('click', lehrEdit, false);
}

