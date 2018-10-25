function book_cl (title_spl, publisher_spl) {   // constructor-function (CF)
   this.title = title_spl;
   this.publisher = publisher_spl;
}            
console.log("- 01 - ", "prototype"  in book_cl);                 // in: wertet prototype-chain aus
console.log("- 02 - ", "constructor"  in book_cl);
console.log("- 03 - ", book_cl.hasOwnProperty("prototype"));     // hasOwnProperty: untersucht nur das
console.log("- 04 - ", book_cl.hasOwnProperty("constructor"));   //                 einzelne Objekt

book_cl.prototype.toString = function() { 
   return this.title + " / " + this.publisher; 
}

function DoIt() {
   var book = {                                 // Objekt-Initialisierer, d.h.
      title: "Titel",                           // es wird intern nur new Object ausgeführt
      publisher: "MySelf"                       // und nicht die CF "book_cl" !
   };
   console.log("- 05 - ", book.toString());
   console.log("- 06 - ", book.hasOwnProperty("publisher"));
   console.log("- 07 - ", book.hasOwnProperty("toString"));
   console.log("- 08 - ", book.hasOwnProperty("__proto__"));
   console.log("- 09 - ", book.hasOwnProperty("prototype"));
   console.log("- 09 - ", "publisher"  in book);
   console.log("- 10 - ", "toString"   in book);
   console.log("- 11 - ", "__proto__"  in book);
   
   console.log("- 12 - ", "mit Konstruktor-Funktion");
   
   book = new book_cl("t", "p");
   console.log("- 13 - ", book.toString());
   console.log("- 14 - ", book.hasOwnProperty("prototype"));
   console.log("- 15 - ", "prototype"  in book);
   console.log("- 16 - ", "prototype"  in book_cl);
   
   // Erweiterungen der vordefinierten (built-in) Javascript-Objekte

   Function.prototype.test = function () { console.log("- 17 - ", "Function-test"); }
   Object.prototype.otest = function () { console.log("- 18 - ", "Object-test"); }
   
   book_cl.test();
   
   book_cl.prototype.otest();
   
   book_cl.prototype.constructor.test();
   
   book.__proto__.constructor.test();
   try {
      book.test(); // klappt nicht! Warum? Machen Sie sich den Unterschied 
                   // zwischen book_cl und book klar!
   }
   catch(e) {
      console.log("- 19 - ", "klappt nicht!");
   }
 
   book.otest();
   
   book_cl.prototype.test = function () { console.log("- 20 - ", "book_cl.prototype.test!"); }
 
   book_cl.test();
 
   book.test(); // Jetzt geht's! Warum? Was wird angezeigt?
}                     

DoIt();