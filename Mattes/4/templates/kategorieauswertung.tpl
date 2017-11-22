<!-- Template -->
<!-- evaluated -->
<div id="idListContent" class="clContent">
   <h2 id="idContentHeader" class="clContentHeader">
      Auswertung nach Kategorie
   </h2>
   <div id="idContentArea" class="clContentArea">
      <table id="idList">
         <tr class="listheader"><th>Kategorie-Ursache</th><th>Kategorie-Lösung</th><th>Fehler</th><th>Status</th>
      @var rows_o = context['data'];@
      @for var key_s in rows_o@
         <tr id='#key_s#'>
         @var row_o = rows_o[key_s];@
            <td>#row_o['bug']['katid']['title']#</td>
            <td>#row_o['fix']['katid']['title']#</td>
            <td>#row_o['bug']['beschreibung']#</td>
            <td>#row_o['status']#</td>
         </tr>
      @endfor@
      </table>
   </div>
   <div id="idButtonArea" class="clButtonArea">
   </div>
</div>

<!-- EOF -->