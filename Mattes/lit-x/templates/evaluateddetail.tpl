<!-- Template -->
<form id="idForm" class="clContent">
   <h2 id="idContentHeader" class="clContentHeader">
      Literaturauswertung / Formular
   </h2>
   <div id="idContentArea" class="clContentArea">

   <input type="hidden" value="#context.data.id#" id="id_s" name="id_s" />
   <div class="clFormRow">
      <label for="title_s">Titel <span class="clRequired"></span></label>
      <input type="text" value="#context.data.title#" id="title_s" name="title_s" autofocus required />
   </div>
   <div class="clFormRow">
      <label for="author_s">Autor <span class="clRequired"></span></label>
      <input type="text" value="#context.data.author#" id="author_s" name="author_s" required />
   </div>
   <div class="clFormRow">
      <label for="evalyear_s">Jahr de Auswertung</label>
      <input type="url" value="#context.data.evalyear#" id="evalyear_s" name="evalyear_s" />
   </div>

   </div>
   <div id="idButtonArea" class="clButtonArea">
      <button data-action="back" class="clButton">Zurück</button>
      <button data-action="save" class="clButton">Speichern</button>
   </div>
</form>
<!-- EOF -->