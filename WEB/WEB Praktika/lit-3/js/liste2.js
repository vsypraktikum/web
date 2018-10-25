// Beispiel lit-3
// liste.js -> Variante mit querySelector

// wird ausgeführt, wenn das Dokument vollständig geladen wurde

window.onload = function () {

   var element_o;
   
   // Ereignisverarbeitung für die Tabelle einrichten
   document.getElementById("idList").onclick = function (event_opl) {
      if (event_opl.target.tagName.toLowerCase() == 'td') {

         element_o = document.querySelector(".clSelected");
         if (element_o != null) {
            element_o.className = "";
         }
         element_o = event_opl.target.parentNode;
         element_o.className = "clSelected";
      }
   }

   // Ereignisverarbeitung für die Schalter einrichten

   document.getElementById("idButtonArea").onclick = function (event_opl) {
      var element_o;
      if (event_opl.target.tagName.toLowerCase() == 'a') {
         var path_s = event_opl.target.href;
         var do_b = false;
         if (event_opl.target.href.indexOf('/add') > 0) {
            do_b = true;
         } else if (event_opl.target.href.indexOf('/edit') > 0) {
            // Id der selektierten Tabellenzeile anhängen
            element_o = document.querySelector(".clSelected");
            if (element_o != null) {
               path_s += "/" + element_o.id.substr(1); 
               do_b = true;
            } else {
               alert("Wählen Sie bitte einen Eintrag in der Tabelle aus!");
            }
         } else if (event_opl.target.href.indexOf('/delete') > 0) {
            element_o = document.querySelector(".clSelected");
            if (element_o != null) {
               if (confirm("Soll der Datensatz gelöscht werden?")) {
                  // Id der selektierten Tabellenzeile anhängen
                  path_s += "/" + element_o.id.substr(1); 
                  do_b = true;
               }
            } else {
               alert("Wählen Sie bitte einen Eintrag in der Tabelle aus!");
            }
         }
         if (do_b) {
            // Anforderung einer neuen Seite und damit Request an den Server senden
            console.log("Wechsel von: "+window.location.href+" zu: "+path_s);
            window.location.href = path_s;
         }
         // Weiterleitung und Standardbearbeitung unterbinden
         event_opl.stopPropagation();
         event_opl.preventDefault();
      }
   }
}
// EOF