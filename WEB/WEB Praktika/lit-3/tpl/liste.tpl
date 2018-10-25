## coding: utf-8
<!DOCTYPE html>
<html>
   <head>
      <title>
          Web Engineering 2013/2014 / Beispiel lit-3
      </title>
      <meta charset="UTF-8" />
      <style type="text/css">
         @import url("/css/normalize.css");
         @import url("/css/main.css");
      </style>
      <script type="text/javascript" src="/js/liste2.js"></script>
   </head>
   <body>
      <h1 id="idSiteHeader" class="clSiteHeader">
         Web-Engineering: Anwendungsbeispiel Lit-3
      </h1>
      <div id="idContent" class="clContent">
         <h2 id="idContentHeader" class="clContentHeader">
            Literatur- / Quellenverzeichnis
         </h2>
         <div id="idContentArea" class="clContentArea">
            <table id="idList">
               <tr><th>Name</th><th>Typ</th><th>Referenz</th></tr>

               ## man hat hier Zugriff auf das Dictionary "data_o"

               % for key_s in data_o:
               <tr id="r${key_s}"><td>${data_o[key_s]['name']}</td><td>${data_o[key_s]['typ']}</td><td>${data_o[key_s]['referenz']}</td></tr>  
               % endfor
            </table>
         </div>
         <div id="idButtonArea" class="clButtonArea">
            <a href="/add" class="clButton">Hinzufügen</a>
            <a href="/edit" class="clButton">Bearbeiten</a>
            <a href="/delete" class="clButton">Löschen</a>
         </div>
      </div>
   </body>
</html>
## EOF