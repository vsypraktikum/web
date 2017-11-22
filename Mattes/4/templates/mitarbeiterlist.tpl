<!-- Template -->
<div id="idListContent" class="clContent">
   <h2 id="idContentHeader" class="clContentHeader">
        Mitarbeiter-Liste
   </h2>
   <div id="idContentArea" class="clContentArea">
      <table id="idList">
         <tr class="listheader"><th>Vorname</th><th>Nachname</th>
      @var rows_o = context['data'];@
      @for var key_s in rows_o@
         <tr id='#key_s#'>
         @var row_o = rows_o[key_s];@
            <td>#row_o['vorname']#</td><td>#row_o['nachname']#</td>
         </tr>
      @endfor@
      </table>
   </div>
   <div id="idButtonArea" class="clButtonArea">
      <button data-action="add" class="clButton">Hinzufügen</button>
      <button data-action="edit" class="clButton">Bearbeiten</button>
      <button data-action="delete" class="clButton">Löschen</button>
   </div>
</div>

<!-- EOF -->