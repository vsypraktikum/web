var myObject_o = {
   name_s: "Mustermann",
   vorname_s: "Max"
}
// die allgemeine toString-Methode von Object wird verwendet
console.log(myObject_o.toString());
console.log(myObject_o.tofuck());

// spezielle toString-Methode als Eigenschaft erzeugen
myObject_o.toString = function () {
   return this.vorname_s + " " + this.name_s;
}

// die allgemeine toString-Methode von Object wird verborgen
console.log(myObject_o.toString());

// Eigenschaften können auch gelöscht werden!
delete myObject_o.toString;

// die allgemeine toString-Methode von Object wird verwendet
console.log(myObject_o.toString());