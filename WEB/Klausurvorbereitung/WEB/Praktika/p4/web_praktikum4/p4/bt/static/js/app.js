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
      this.content_o                     = null; // das jeweils aktuelle Objekt im Contentbereich
      this.nav_o                         = new APP.Nav_cl();
      this.listProjekt_o                 = new APP.ListView_cl('projekt', '/projekt/', 'projektlist.tpl');
      this.detailProjekt_o               = new APP.SourceDetailView_cl('projekt', '/projekt/', 'projektdetail.tpl');
      this.listFehler_o                  = new APP.ListView_cl('fehler', '/fehler/', 'fehlerlist.tpl');
      this.detailFehler_o                = new APP.DetailView_cl('fehler', '/fehler/', 'fehlerdetail.tpl');
      this.listKomponenten_o             = new APP.ListView_cl('komponente', '/komponente/', 'komponentelist.tpl');
      this.detailKomponenten_o           = new APP.DetailView_cl('komponente', '/komponente/', 'komponentedetail.tpl');
      this.listMitarbeiter_o             = new APP.ListView_cl('mitarbeiter', '/mitarbeiter/', 'mitarbeiterlist.tpl');
      this.detailMitarbeiter_o           = new APP.DetailView_cl('mitarbeiter', '/mitarbeiter/', 'mitarbeiterdetail.tpl');
      this.listKategorie_o               = new APP.ListView_cl('kategorie', '/kategorie/', 'kategorielist.tpl');
      this.detailKategorie_o             = new APP.DetailView_cl('kategorie', '/kategorie/', 'kategoriedetail.tpl');
      this.prolist_o                     = new APP.ListView_cl('prolist', '/prolist/', 'AuswertungProjektelist.tpl');
      this.katlist_o                     = new APP.ListView_cl('katlist', '/katlist/', 'AuswertungKategorielist.tpl');
      //this.listProjektkomponente_o       = new APP.ListView_cl('Projektkomponente', '/Projektkomponente/', 'Projektkomponentelist.tpl');
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
            // Liste Projekte im Content-Bereich anzeigen
            self_opl.setContent_p(self_opl.listProjekt_o, data_apl[1]);
            break;
         case 'projekt':
            // Liste Projekte im Content-Bereich anzeigen
            self_opl.setContent_p(self_opl.listProjekt_o, data_apl[1]);
            break;
         case 'projekt.add':
            // (leeres) Detailformular im Content-Bereich anzeigen
            self_opl.setContent_p(self_opl.detailProjekt_o, data_apl[1]);
            break;
         case 'projekt.edit':
            // Detailformular im Content-Bereich anzeigen
            self_opl.setContent_p(self_opl.detailProjekt_o, data_apl[1]);
            break;
         case 'fehler':
            // Liste Quellen im Content-Bereich anzeigen
            self_opl.setContent_p(self_opl.listFehler_o, data_apl[1]);
            break;
         case 'fehler.add':
            // (leeres) Detailformular im Content-Bereich anzeigen
            self_opl.setContent_p(self_opl.detailFehler_o, data_apl[1]);
            break;
         case 'fehler.edit':
            // Detailformular im Content-Bereich anzeigen
            self_opl.setContent_p(self_opl.detailFehler_o, data_apl[1]);
            break;
         case 'komponente':
            // Liste Quellen im Content-Bereich anzeigen
            self_opl.setContent_p(self_opl.listKomponenten_o, data_apl[1]);
            break;
         case 'komponente.add':
            // (leeres) Detailformular im Content-Bereich anzeigen
            self_opl.setContent_p(self_opl.detailKomponenten_o, data_apl[1]);
            break;
         case 'komponente.edit':
            // Detailformular im Content-Bereich anzeigen
            self_opl.setContent_p(self_opl.detailKomponenten_o, data_apl[1]);
            break;

         case 'mitarbeiter':
            // Liste Quellen im Content-Bereich anzeigen
            self_opl.setContent_p(self_opl.listMitarbeiter_o, data_apl[1]);
            break;
         case 'mitarbeiter.add':
            // (leeres) Detailformular im Content-Bereich anzeigen
            self_opl.setContent_p(self_opl.detailMitarbeiter_o, data_apl[1]);
            break;
         case 'mitarbeiter.edit':
            // Detailformular im Content-Bereich anzeigen
            self_opl.setContent_p(self_opl.detailMitarbeiter_o, data_apl[1]);
            break;
         case 'kategorie':
            // Liste Quellen im Content-Bereich anzeigen
            self_opl.setContent_p(self_opl.listKategorie_o, data_apl[1]);
            break;
         case 'kategorie.add':
            // (leeres) Detailformular im Content-Bereich anzeigen
            self_opl.setContent_p(self_opl.detailKategorie_o, data_apl[1]);
            break;
         case 'kategorie.edit':
            // Detailformular im Content-Bereich anzeigen
            self_opl.setContent_p(self_opl.detailKategorie_o, data_apl[1]);
            break;
         case 'prolist':
            // Liste Quellen im Content-Bereich anzeigen
            self_opl.setContent_p(self_opl.prolist_o, data_apl[1]);
            break;
         case 'katlist':
            // Liste Quellen im Content-Bereich anzeigen
            self_opl.setContent_p(self_opl.katlist_o, data_apl[1]);
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
   APP.my_bool = false;
   APP.es_o.publish_px('app', ['init', null]);

});
// EOF
