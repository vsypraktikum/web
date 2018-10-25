// hier wird nur zur Vereinfachung der Demonstration direkt Markup in js verwendet
// NICHT nachahmen!

function ShowDom()
{
   var DOMText  = "<table>" +
                  "<tr><th>Level</th>" + 
                  "<th>Type</th>" +
                  "<th>Name</th>" +
                  "<th>Value</th>" +
                  "<th>Attributes</th></tr>";
   var Iterator = new DOMIterator(document);
   var Node     = Iterator.First();
   while (Node != null) {
      DOMText += "<tr><td>"  + Iterator.Level.toString() + 
                 "</td><td>" + Node.nodeType +
                 "</td><td>" + Node.nodeName +
                 "</td><td>" + Node.nodeValue +
                 "</td><td>" + ListAttributes(Node) +
                 "</td></tr>";
      Node = Iterator.Next();
   }
   DOMText += "</table>";

   document.getElementById("ShowDomTree").innerHTML = DOMText;
}

function ShowDomAsList()
{
   var space_s = " ".repeat(20);
   var DOMText  = "<pre>" +  
                  "Level" + space_s.substr(0, 15) + " // Type // Name // Value // Attributes\n\n";
   var Iterator = new DOMIterator(document);
   var Node     = Iterator.First();
   while (Node != null) {
      DOMText += space_s.substr(0, 3*Iterator.Level) +
                 Iterator.Level.toString() + 
                 space_s.substr(0, 20 - 3*Iterator.Level - 1) +
                 " // " + Node.nodeType +
                 " // " + Node.nodeName;
      if (Node.nodeName == "#text") {
         DOMText += " // [[" + Node.nodeValue + "]]";
      } else {
         DOMText += " // " + Node.nodeValue;
      }
      DOMText += " // " + ListAttributes(Node) +
                 "\n";
      Node = Iterator.Next();
   }
   DOMText += "</pre>";

   document.getElementById("ShowDomTree").innerHTML = DOMText;
}

function ListAttributes(Node_opl)
{
   //debugger
   var Content_s = "null";
   if (Node_opl.attributes != null) {
      Content_s = "";
      for (var loop_i = 0; 
           loop_i < Node_opl.attributes.length;
           loop_i++) {
         // hier Attribute mit Wert null ausblenden, 
         // um die Anzeige zu vereinfachen
         if (Node_opl.attributes[loop_i].nodeValue != null) {
            Content_s += Node_opl.attributes[loop_i].nodeName + " : " + 
                         Node_opl.attributes[loop_i].nodeValue + " / ";
         }
      }
   }
   return Content_s;
}
