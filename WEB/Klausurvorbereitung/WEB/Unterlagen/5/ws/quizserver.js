/*
   Beispiel Quiz mit Websockets / Server

   rev. 0, 24.01.2016 / Bm
*/

/* Module laden */
var WebSocketServer = require('ws').Server;
var http = require('http');

/* Standard HTTP Server einrichten */
var server_o = http.createServer();
server_o.listen(8080);

/* Socket-Server einrichten */
var wss_o = new WebSocketServer({server: server_o});
console.log('WS-Server auf localhost:8080');

/* die Fragen */
var fragen_a = [
   ["Frage 1", 0],
   ["Frage 2", 1],
   ["Frage 3", 1],
   ["Frage 4", 0],
   ["Frage 5", 0],
   ["Frage 6", 1]
];

var clients_o = {
};

var id_i = 0;

/* Ereignis des WS-Server */
wss_o.on('connection', function(ws_opl) {
   var qnr_i = 0;
   var id_s = "";
   id_i++;
   id_s = id_i.toString();
   clients_o[id_s] = {"ws": ws_opl, "q": [null, null, null, null, null, null]};
   console.log('started client:' + id_s);
   ws_opl.send(JSON.stringify({"id": id_s, "cmd": "question", "question":fragen_a[0][0]}));
   ws_opl.on('close', function() {
      console.log('stopping client');
   });
   ws_opl.on('message', function (msg_spl) {
      var event_o = JSON.parse(msg_spl);
      console.log("client: " + id_s + " / " + msg_spl);
      var result_b = fragen_a[qnr_i][1] == parseInt(event_o.answer);
      clients_o[id_s]["q"][qnr_i] = result_b;
      ws_opl.send(JSON.stringify({"id": id_s, "cmd": "result", "result": result_b, "qnr": qnr_i, }));
      qnr_i++;
      if (qnr_i < 6) {
         ws_opl.send(JSON.stringify({"id": id_s, "cmd": "question", "question":fragen_a[qnr_i][0]}));
      } else {
         ws_opl.send(JSON.stringify({"id": id_s, "cmd": "end"}));
      }
      var data_o = calculateAnswers_p(); 
      var msg_s = JSON.stringify({"cmd": "info", "results": data_o})
      wss_o.broadcast(msg_s);
  });
});

wss_o.broadcast = function broadcast(data) {
   wss_o.clients.forEach(function each(client) {
      client.send(data);
   });
};

function calculateAnswers_p () {
   var result_a = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]];
   for (id_s in clients_o) {
      var q_a = clients_o[id_s]["q"];
      for (var loop_i = 0; loop_i < q_a.length; loop_i++) {
         if (q_a[loop_i] != null) {
            if (q_a[loop_i]) {
               result_a[loop_i][0] += 1;
            } else {
               result_a[loop_i][1] += 1;
            }
         }
      }
   }
   return result_a;
}
// EOF
