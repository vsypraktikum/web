/*
   Beispiel Quiz mit Websockets

   rev. 0, 24.01.2016 / Bm
*/

function disable_p () {
   document.getElementById('idYes').disabled = true;
   document.getElementById('idNo').disabled = true;
}
function enable_p () {
   document.getElementById('idYes').disabled = false;
   document.getElementById('idNo').disabled = false;
}

function showInfo_p (data_apl) {
   var result_s = "<p>Ergebnisse aller Teilnehmer</p><table><tr><th>Frage</th><th>richtig</th><th>falsch</th>";
   for (var loop_i = 0; loop_i < data_apl.length; loop_i++) {
      result_s += "<tr><td>" + loop_i.toString() + "</td>";
      result_s += "<td>" + data_apl[loop_i][0].toString() + "</td>";
      result_s += "<td>" + data_apl[loop_i][1].toString() + "</td></tr>";
   }
   result_s += "</table>";
   return result_s;
}

window.onload = function () {
   disable_p();
   /* EventHandler einrichten */
   document.getElementById('idYes').onclick = function (event_opl) {
      ws_o.send(JSON.stringify({"answer":"1"}));
     disable_p();
   }
   document.getElementById('idNo').onclick = function (event_opl) {
      var msg_s = JSON.stringify({"answer":"0"});
      ws_o.send(msg_s);
      disable_p();
   }

   /* Websocket-Verbindung einrichten */
   var ws_o = new WebSocket('ws://localhost:8080');
   /* EventHandler für das Websocket-Objekt einrichten */
   ws_o.onopen = function (event_opl) {
      document.getElementById('idStatus').innerHTML = "Verbindung hergestellt";
   };
   ws_o.onmessage = function (event_opl) {
      var data_o = JSON.parse(event_opl.data);
      console.log(data_o.cmd);
      switch (data_o.cmd) {
      case 'result':
         var text_s = "Die Antwort zur Frage " + (data_o.qnr+1).toString() + " ist ";
         if (data_o.result) {
            text_s += "richtig!";
         } else {
            text_s += "falsch!";
         }
         document.getElementById('idAnswer').innerHTML = text_s;
         break;
      case 'question':
         document.getElementById('idQuestion').innerHTML = data_o.question;
         enable_p();
         break;
      case 'info':
         document.getElementById('idInfo').innerHTML = showInfo_p(data_o.results);
         break;
      case 'end':
         document.getElementById('idQuestion').innerHTML = "Keine weiteren Fragen!";
         break;
      }
   };
   ws_o.onclose = function (event_opl) {
      document.getElementById('idStatus').innerHTML = "Verbindung gelöst";
   };
}
// EOF
