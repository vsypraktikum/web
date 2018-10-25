// Beispiel lit-3
// detail.js

var g_FormContentOrg_o = {
   'id_s': '',
   'name_s': '',
   'typ_s': '',
   'referenz_s': ''
};

function storeFormContent_p() {
   g_FormContentOrg_o['id_s'] = document.getElementById("id_s").value;
   g_FormContentOrg_o['name_s'] = document.getElementById("name_s").value;
   g_FormContentOrg_o['typ_s'] = document.getElementById("typ_s").value;
   g_FormContentOrg_o['referenz_s'] = document.getElementById("referenz_s").value;
}

function isModified_p() {
   // Prüfen, ob Formularinhalt verändert wurde
   var mod_b = 
      g_FormContentOrg_o['id_s'] != document.getElementById("id_s").value ||
      g_FormContentOrg_o['name_s'] != document.getElementById("name_s").value ||
      g_FormContentOrg_o['typ_s'] != document.getElementById("typ_s").value ||
      g_FormContentOrg_o['referenz_s'] != document.getElementById("referenz_s").value;

   return mod_b;
}

function checkContent_p () {
   // hier nur zur Demonstration Prüfung des Typs gegen eine Werteliste
   // (das realisiert man besser mit einer Liste)
   var status_b = true;
   var typ_s = document.getElementById("typ_s").value;
   if ((typ_s != "Typ1") && (typ_s != "Typ2")) {
      status_b = false;
   }
   return status_b;
}

// wird ausgeführt, wenn das Dokument vollständig geladen wurde

window.onload = function () {

   // aktuellen Formularinhalt speichern
   storeFormContent_p();

   // Ereignisverarbeitung für das Formular einrichten

   document.getElementById("idForm").onsubmit = function (event_opl) {
      // Formularinhalt prüfen
      if (isModified_p()) {
         if (checkContent_p()) {
            document.getElementById("idForm").submit();
         } else {
            alert("Bitte prüfen Sie die Eingaben in den Formularfeldern!")
         }
      }
      event_opl.stopPropagation();
      event_opl.preventDefault();
   }

   document.getElementById("idForm").onclick = function (event_opl) {
      if (event_opl.target.tagName.toLowerCase() == 'a') {
         // Formularinhalt prüfen
         if (isModified_p()) {
            if (confirm("Es gibt nicht gespeicherte Änderungen - trotzdem zurück?")) {
               // Anforderung einer neuen Seite und damit Request an den Server senden
               window.location.href = event_opl.target.href;
            }
         } else {
            // Anforderung einer neuen Seite und damit Request an den Server senden
            window.location.href = event_opl.target.href;
         }
         // Weiterleitung und Standardbearbeitung unterbinden
         event_opl.stopPropagation();
         event_opl.preventDefault();
      }
   }

}
// EOF