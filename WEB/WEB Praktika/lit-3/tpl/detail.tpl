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
      <script type="text/javascript" src="/js/detail.js"></script>
   </head>
   <body>
      <h1 id="idSiteHeader" class="clSiteHeader">
         Web-Engineering: Anwendungsbeispiel Lit-3
      </h1>
      <form id="idForm" class="clContent" action="/save" method="POST">
         <h2 id="idContentHeader" class="clContentHeader">
            Literatur- / Quellenverzeichnis / Formular (per Template)
         </h2>
         <div id="idContentArea" class="clContentArea">

         ## man hat hier Zugriff auf das Dictionary "data_o"

         <input type="hidden" value="${data_o['id']}" id="id_s" name="id_s" />
         <div class="clFormRow">
            <label for="name_s">Name <span class="clRequired"></span></label>
            <input type="text" value="${data_o['name']}" id="name_s" name="name_s" autofocus required />
         </div>
         <div class="clFormRow">
            <label for="typ_s">Typ <span class="clRequired"></span></label>
            <input type="text" value="${data_o['typ']}" id="typ_s" name="typ_s" required />
         </div>
         <div class="clFormRow">
            <label for="referenz_s">Referenz</label>
            <input type="url" value="${data_o['referenz']}" id="referenz_s" name="referenz_s" />
         </div>
 
         </div>
         <div id="idButtonArea" class="clButtonArea">
            <a href="/" title="Zurück zur Startseite">Zurück</a>
            <input type="submit" value="Speichern" />
         </div>
      </form>
   </body>
</html>
## EOF