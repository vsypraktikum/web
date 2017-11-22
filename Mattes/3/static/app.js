//Globale Variablen
var Ansicht;//Indikator für die aktuell geladene Liste
var Auswahl;//Indikator für die Gewählte Reihe
var Modus;
var statusText = '';
var callBack;

//-----------------------------------------------------------------------
//Funktionalität für das Kommunizieren mit de Server
//----------------------------------------------------------------------

function SetContent(view){
	var request_o = new XMLHttpRequest();
	request_o.open("Get", view);
	
	request_o.onload = function () {
		if(this.status == 200){
			
			let content_o = document.getElementById("contentContainer");
			content_o.innerHTML = this.responseText;
			if(callBack){
				callBack();
			}
		}else{
		}
	}
	request_o.send();
}

function SetStatus(view){
	var request_o = new XMLHttpRequest();
	request_o.open("Get", view);
	
	request_o.onload = function () {
		if(this.status == 200){

			statusText = this.responseText;
			if(callBack){
				callBack();
			}
		}else{
		}
	}
	request_o.send();
}

//-----------------------------------------------------------------------
//Funktionalität für das Formular-Menü
function GetFormData(){
	StatusText = '';
	let formElements = document.getElementById('Form').elements;
	let data_s = '{';

	for (let i = 1; i < formElements.length; i++){
		if(formElements[i].value != "" || formElements[i].type == "hidden"){
			data_s += '"' + formElements[i].name + '": "' + formElements[i].value + '",';
		}else{
			StatusText = "Bitte Feld:'"+formElements[i].name+"' Ausfüllen!";
			return 0;
		}
	}
	
	data_s = data_s.substr(0, data_s.length-1);
	data_s += '}'
	return data_s;
}

function addRow(){
	let id = document.getElementById('id').value;
	let data_s = GetFormData();
	
	if(data_s){
		
		SetContent('/addRow/' + Ansicht + '/' + data_s);
	}else{
		document.getElementById('StatusText').innerHTML = StatusText;
	}
	
}
//-----------------------------------------------------------------------


//-----------------------------------------------------------------------
//Funktionalität für das Listen-Menü
//-----------------------------------------------------------------------
function markRow(event_opl){

	var row = event_opl.target.parentNode;
		
	if(Auswahl){
		Auswahl.className = "noMark";
	}
	if(Auswahl != row){
		Auswahl = row;
		row.className = "Mark";
	}else{
		Auswahl = undefined;
		row.className = "noMark";	
	}
}

//Löschen von Zeilen
function deleteRow(){
	if(Auswahl){
		callBack = function () {
			if(statusText == "0"){
				if(confirm("Are you sure?")){
					alert("deleted")
					SetContent('/deleteRow/'+Ansicht+'/'+Auswahl.id);
				}
			}else{
				alert("Löschen nicht möglich")
			}
			
			statusText = '';
			callBack = undefined;
		}
		SetStatus('/checkID/'+Ansicht+'/'+Auswahl.id);
	}else{
		alert("Keine Auswahl getroffen!");
	}
}

//Bearbeiten von Zeilen
function updateRow(){
	let id = document.getElementById('id').value;
	let data_s = GetFormData()
	if(data_s){
		if(Ansicht == 4){
			
			let matrikelid = document.getElementById("matrikelid").value;
			
			callBack = function () {
				if(statusText == "0"){
					SetContent('/updateRow/' +Ansicht+'/'+ id + '/' + data_s);
				}else{
					document.getElementById('StatusText').innerHTML = "Student bereits Eingeschrieben!";
				}
				statusText = '';
				callBack = undefined;
				
			}
			SetStatus('/checkID/' + Ansicht+'/' + matrikelid);
		}else{
			SetContent('/updateRow/' +Ansicht+'/'+ id + '/' + data_s);
		}
	}else{
		document.getElementById('StatusText').innerHTML = StatusText;
	}
}

//Einschreiben in PPA
function Einschreiben(){
	if(Auswahl){
		Ansicht = 4;
		CreateForm(Auswahl.id);
	}else{
		alert("Keine Auswahl getroffen!");
	}
}

//Hinzufügen von Zeilen
function CreateForm(id_s){
	if (id_s || id_s == "0"){
		Modus = "UPDATE";
		SetContent('/CreateForm/' + Ansicht + '/' + id_s);
	}else{
		Modus = "ADD";
		SetContent('/CreateForm/' + Ansicht);
	}
}
//-----------------------------------------------------------------------
//Funktionalität für die Navigation

function CreateList(event_opl){
	Ansicht = event_opl.target.id;
	SetContent('/CreateList/' + event_opl.target.id);
}


//-----------------------------------------------------------------------
//EventHandler für Click im Content-Bereich
//-----------------------------------------------------------------------
function ClickContent(event_opl){
	
	if(event_opl.target.tagName == 'TD'){
		markRow(event_opl);
	}else if (event_opl.target.tagName == 'BUTTON'){
		if(event_opl.target.id == 'add'){
			CreateForm();
		}else if(event_opl.target.id == 'edit'){
			CreateForm(Auswahl.id);
		}else if(event_opl.target.id == 'delete'){
			deleteRow();
		}else if(event_opl.target.id == 'einschreiben'){
			Einschreiben(event_opl);
		}else if(event_opl.target.id == 'save'){
			if(Modus == "ADD"){
				addRow();
			}else{
				updateRow();
			}
		}else if(event_opl.target.id == 'einschreiben'){
			Einschreiben()
		}else if(event_opl.target.id == 'back'){
			SetContent('/CreateList/' + Ansicht);
		}
	}
}
//-----------------------------------------------------------------------
//Programm Initalisierung
window.onload = function () {
	document.getElementById('navContainer').addEventListener('click', CreateList);
	document.getElementById('contentContainer').addEventListener('click', ClickContent);
}
