<!-- Template -->
<!-- Projekt -->

      <table id="idList" class = "clTable">
         <tr class="listheader" class = "clTable">
             <th>Fehlerursache</th><th>Kategorie</th><th>Komponente</th><th>Beschreibung</th><th>Mitarbeiter</th><th>Status</th></tr>
      @var rows_o = context['data'];@
      @var rows_fehler = context['data_fehler'];@
      @for var key_s in rows_fehler@
         <tr id='#key_s#'>
         @var row_fehler = rows_fehler[key_s];@
            <td>#rows_o['fehlerursache']#</td><td>#rows_o['fehlerbeschreibung']#</td><td>#row_fehler['komponente']#</td><td>#row_fehler['beschreibung']#</td><td>#row_fehler['mitarbeiter']#</td><td>#row_fehler['fehlerstatus']#</td>
         </tr>
      @endfor@
      </table>
<!-- EOF -->