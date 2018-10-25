<!-- Template -->
<!-- Projekt -->
<div id="idListContent" class="clContent">
   <h2 id="idContentHeader" class="clContentHeader">
      Kategorieverzeichnis
   </h2>
   <div id="idContentArea" class="clContentArea">
   </div>

   <div id="idButtonArea" class="clButtonArea">
      <button data-action="auswerten_kategorie" class="clButton">Auswählen:</button>
      <select id = "kategorie_auswertung_name" name>
         @var rows_proj = context['data'];@
         @console.log(rows_proj);@
         @for var key_p in rows_proj@
            <option value="#key_p#">#rows_proj[key_p]['fehlerbeschreibung']#</option>
         @endfor@
      </select>
   </div>

</div>

<!-- EOF -->