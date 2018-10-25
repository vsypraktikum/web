var object0_o = Object.create(Object.prototype);

var object1_o = Object.create(object0_o);
object1_o.name_s = "Mustermann1";

var object2_o = Object.create(object1_o);
object2_o.name_s = "Mustermann2";
object2_o.vorname_s = "Max";

function showName_p (object_opl) {
   var result_s = "Ergebnis:";
   if (object_opl.name_s != undefined) {
      result_s += " " + object_opl.name_s;
   }
   if (object_opl.vorname_s != undefined) {
      result_s += " " + object_opl.vorname_s;
   }
   return result_s;
}
console.log(showName_p(object0_o));
console.log(showName_p(object1_o));
console.log(showName_p(object2_o));

console.log(object0_o.toString());
console.log(object1_o.toString());
console.log(object2_o.toString());

object0_o.tofuck = function () {
   return showName_p(this);
}

console.log(object0_o.tofuck());
console.log(object1_o.tofuck());
console.log(object2_o.tofuck());
