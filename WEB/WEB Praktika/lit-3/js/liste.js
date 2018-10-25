// Beispiel lit-3
// liste.js

var g_rowId_s = "";

// wird ausgeführt, wenn das Dokument vollständig geladen wurde

window.onload = function () {

   // Ereignisverarbeitung für die Tabelle einrichten
   document.getElementById("idList").onclick = function (event_opl) {
      if (event_opl.target.tagName.toLowerCase() == 'td') {
         if (g_rowId_s != "") {
            document.getElementById(g_rowId_s).className = "";
         }
         g_rowId_s = event_opl.target.parentNode.id;
         document.getElementById(g_rowId_s).className = "clSelected";
      }
   }

   // Ereignisverarbeitung für die Schalter einrichten

   document.getElementById("idButtonArea").onclick = function (event_opl) {
      if (event_opl.target.tagName.toLowerCase() == 'a') {
         var path_s = event_opl.target.href;
         var do_b = false;
         if (event_opl.target.href.indexOf('/add') > 0) {
            do_b = true;
         } else if (event_opl.target.href.indexOf('/edit') > 0) {
            // Id der selektierten Tabellenzeile anhängen
            if (g_rowId_s != "") {
               path_s += "/" + g_rowId_s.substr(1); 
               do_b = true;
            } else {
               alert("Wählen Sie bitte einen Eintrag in der Tabelle aus!");
            }
         } else if (event_opl.target.href.indexOf('/delete') > 0) {
            if (g_rowId_s != "") {
               if (confirm("Soll der Datensatz gelöscht werden?")) {
                  // Id der selektierten Tabellenzeile anhängen
                  path_s += "/" + g_rowId_s.substr(1); 
                  do_b = true;
               }
            } else {
               alert("Wählen Sie bitte einen Eintrag in der Tabelle aus!");
            }
         }
         if (do_b) {
            // Anforderung einer neuen Seite und damit Request an den Server senden
            window.location.href = path_s;
         }
         // Weiterleitung und Standardbearbeitung unterbinden
         event_opl.stopPropagation();
         event_opl.preventDefault();
      }
   }
}
// EOF