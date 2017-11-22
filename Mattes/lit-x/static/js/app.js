// ----------------------------------------------
// Beispiel lit-x
// app.js
// ----------------------------------------------
// Verwendung von jquery, Single-Page / Ajax, Event-Service
// REST-Interface
// ----------------------------------------------

'use strict'

// ----------------------------------------------
// Namensraum einrichten
// ----------------------------------------------

let APP = {};

// ----------------------------------------------
APP.Application_cl = class {
// ----------------------------------------------
   constructor () {
      this.content_o         = null; // das jeweils aktuelle Objekt im Contentbereich
      this.nav_o             = new APP.Nav_cl();
      this.listSources_o     = new APP.ListView_cl('source', '/source/', 'sourceslist.tpl');
      this.detailSources_o   = new APP.SourceDetailView_cl('source', '/source/', 'sourcedetail.tpl');
      this.listEvaluated_o   = new APP.ListView_cl('evaluated', '/evaluated/', 'evaluatedlist.tpl');
      this.detailEvaluated_o = new APP.DetailView_cl('evaluated', '/evaluated/', 'evaluateddetail.tpl');

      // Registrierungen
      APP.es_o.subscribe_px(this, 'app');
   }
   notify_px (self_opl, message_spl, data_apl) {
      switch (message_spl) {
      case 'app':
         switch (data_apl[0]) {
         case 'init':
            APP.tm_o = new TemplateManager_cl();
            break;
         case 'templates.loaded':
            self_opl.nav_o.render_px();
            // Liste Quellen im Content-Bereich anzeigen
            self_opl.setContent_p(self_opl.listSources_o, data_apl[1]);
            break;
         case 'source':
            // Liste Quellen im Content-Bereich anzeigen
            self_opl.setContent_p(self_opl.listSources_o, data_apl[1]);
            break;
         case 'source.add':
            // (leeres) Detailformular im Content-Bereich anzeigen
            self_opl.setContent_p(self_opl.detailSources_o, data_apl[1]);
            break;
         case 'source.edit':
            // Detailformular im Content-Bereich anzeigen
            self_opl.setContent_p(self_opl.detailSources_o, data_apl[1]);
            break;
         case 'evaluated':
            // Liste Quellen im Content-Bereich anzeigen
            self_opl.setContent_p(self_opl.listEvaluated_o, data_apl[1]);
            break;
         case 'evaluated.add':
            // (leeres) Detailformular im Content-Bereich anzeigen
            self_opl.setContent_p(self_opl.detailEvaluated_o, data_apl[1]);
            break;
         case 'evaluated.edit':
            // Detailformular im Content-Bereich anzeigen
            self_opl.setContent_p(self_opl.detailEvaluated_o, data_apl[1]);
            break;
         default:
            console.warn('[Application_cl] unbekannte app-Notification: '+data_apl[0]);
            break;
         }
         break;
      default:
         console.warn('[Application_cl] unbekannte Notification: '+message_spl);
         break;
      }
   }
   setContent_p (newContent_opl, data_opl) {
      if (this.content_o != null) {
         if (this.content_o === newContent_opl) { // Achtung: Vergleich auf Identität (===) und nicht nur auf Gleichheit (==)
            // wird bereits angezeigt, keine Änderung
         } else {
            if (this.content_o.canClose_px()) {
               this.content_o.close_px();
               this.content_o = newContent_opl;
               this.content_o.render_px(data_opl);
            }
         }
      } else {
         this.content_o = newContent_opl;
         this.content_o.render_px(data_opl);
      }
   }
}

// ----------------------------------------------
$(document).ready(function(){
// ----------------------------------------------
   // wird ausgeführt, wenn das Dokument vollständig geladen wurde
   APP.es_o  = new EventService_cl();
   APP.app_o = new APP.Application_cl();

   APP.es_o.publish_px('app', ['init', null]);

});
// EOF