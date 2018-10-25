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

name_s = 'xyz';

console.log(name_s);
