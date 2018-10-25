<form id="idForm" class="clContent">
   <h2 id="idContentHeader" class="clContentHeader">
      Bearbeitung Fehlerdaten / Formular
   </h2>
   <div id="idContentArea" class="clContentArea">

      <input type="hidden" value="#context.data.id#" id="id_s" name="id_s" />
       <div class="clFormRow">
         <label for="komponente_s">Komponente<span class="clRequired"></span></label>
         <input type="text" value="#context.data.komponente#" id="komponente_s" name="komponente_s" autofocus required />
      </div>
      <div class="clFormRow">
         <label for="beschreibung_s">Beschreibung <span class="clRequired"></span></label>
         <input type="text" value="#context.data.beschreibung#" id="beschreibung_s" name="beschreibung_s" autofocus required />
      </div>
      <div class="clFormRow" id="selecter">
         <label for="mitarbeiter_s">Mitarbeiter <span class="clRequired"></span></label>
         @var rows_mitarbeiter = context['data_mitarbeiter'];@
         @console.log(context['abteilung']);@
         <select id="mitarbeiter_s" name="mitarbeiter_s">
            @for var key_mit in rows_mitarbeiter@
                  @var row_mitarbeiter = rows_mitarbeiter[key_mit];@
                  @if (row_mitarbeiter['abteilung'] == context['abteilung'])@
                     <option value="#row_mitarbeiter['name']#">#row_mitarbeiter['name']# </option>
                  @endif@
            @endfor@
         </select>
      </div>
      <div class="clFormRow">
         <label for="datum_s">Datum</label>
         <input type="text" value="#context.data.datum#" id="datum_s" name="datum_s" />
      </div>
      <div class="clFormRow">
         <label for="kategorie_s">Kategorie</label>
         <input type="text" value="#context.data.kategorie#" id="kategorie_s" name="kategorie_s" />
      </div>
      <div class="clFormRow">
         <input type="hidden" value="#context.data.fehlerstatus#" id="fehlerstatus_s" name="fehlerstatus_s" />
      </div>

   </div>
   <div id="idButtonArea" class="clButtonArea">
      <button data-action="back" class="clButton">Zurück</button>
      <button data-action="save" class="clButton" id ="ButtonContinue">Speichern</button>
   </div>
</form>