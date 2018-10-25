var referenzwert = 1;
var referenzTyp1 = referenzwert;
console.log(referenzTyp1);
var referenzTyp2 = referenzTyp1;
console.log(referenzTyp2);
referenzTyp1 = null;
console.log(referenzTyp1);
console.log(referenzTyp2);
var actDate_o = new Date();
console.log(actDate_o);
//Objekt mit Object.create erstellen
var newObject_o = Object.create(Object.prototype);
newObject_o.eigenschaft_s = 'Wert';
console.log(newObject_o.eigenschaft_s);
//Objekt mit new erstellen
function Person_cl(){
	this.eigenschaft_s = 'Wert';
}
var newPerson_o = new Person_cl();
console.log(newPerson_o.eigenschaft_s);

// Erzeugung
var x = new Function ("v", "return v;");
// Aufruf
var y = x("abcde"); // welchen Wert erhält y?
console.log(y);

g = 'globalix';
function f() {
console.log(g);
console.log(this.g);
}

f();

function Person_cl (name_spl) {
// Eigenschaften anlegen
this.name_s = name_spl;
}
// normale Verwendung als Konstruktor
var person1_o = new Person_cl("Mustermann1");
// name_s ist wie erwartet die Eigenschaft des erzeugten Objekts
console.log(person1_o.name_s);
// versehentliche Verwendung ohne den new-Operator
var person2_o = Person_cl("Mustermann2");
// name_s ist KEINE Eigenschaft des erzeugten Objekts
// person2_o erhält return-Wert der Funktion, diese liefert aber
// keinen return-Wert zurück, d.h. person2_o erhält
// den Wert undefined
try {
console.log(person2_o.name_s);
}
catch (error_o) {
console.warn("Zugriff nicht möglich!");
}
// Was gibt es stattdessen: eine Eigenschaft im global-Object!
console.log(name_s);

console.log("ab hier ist ein anderer test");

//probeklausur

function backgroundchange(event_opl){
	if ((event_opl.target.tagName.toLowerCase() == 'a') && (event_opl.target.className == "link")){
		//document.getElementById('link1').style.background = "green";
		event_opl.target.style.background = "green";
		alert("juhu");
	}
}
window.onload = function () {
    let a_o = document.querySelectorAll('nav')[0];
    a_o.addEventListener('click', backgroundchange , false);
}