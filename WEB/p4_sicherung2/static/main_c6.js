//------------------------------------------------------------------------------
//Demonstrator es/te/tm - Variante mit ES6-Classes
//------------------------------------------------------------------------------
// hier zur Vereinfachung (!) die Klassen in einer Datei

'use strict'

class DetailView_cl {

   constructor (el_spl, template_spl) {
      this.el_s = el_spl;
      this.template_s = template_spl;
   }
   render_px (id_spl) {
	  //console.log(id_spl);
      alert("Die ID ist " + id_spl);
	  // Daten anfordern
      let path_s = "/app/topics/" + id_spl;
      APPETT.xhr_o.request_px(path_s, 
         function (responseText_spl) {
            let data_o = JSON.parse(responseText_spl);
            this.doRender_p(data_o);
         }.bind(this),
         function (responseText_spl) {
            alert("Detail - render failed");
         }
      );
   }
   doRender_p (data_opl) {
      let markup_s = APPETT.tm_o.execute_px(this.template_s, data_opl);
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.innerHTML = markup_s;
         this.configHandleEvent_p();
      }
   }
   configHandleEvent_p () {
      let el_o = document.querySelector("form");
      if (el_o != null) {
         el_o.addEventListener("click", this.handleEvent_p);
      }
   }
   handleEvent_p (event_opl) {
      if (event_opl.target.id == "idBack") {
         APPETT.es_o.publish_px("app.cmd", ["idBack", null]);
         event_opl.preventDefault();
      } else if(event_opl.target.id == "topicspeichern"){
          event_opl.preventDefault();
          APPETT.es_o.publish_px("app.cmd", ["topicspeichern", this.topic_id]);
		}
		else if(event_opl.target.id == "topicbearbeiten"){
          event_opl.preventDefault();
          APPETT.es_o.publish_px("app.cmd", ["detail_edit", this.topic_id]);
		}
   }
}

class ListView_cl {

   constructor (el_spl, template_spl) {
      this.el_s = el_spl;
      this.template_s = template_spl;
      this.configHandleEvent_p();
   }
   render_px () {
      // Daten anfordern
      let path_s = "/app/topics/";
      APPETT.xhr_o.request_px(path_s, 
         function (responseText_spl) {
            let data_o = JSON.parse(responseText_spl);
            this.doRender_p(data_o);
         }.bind(this),
         function (responseText_spl) {
            alert("List - render failed");
         }
      );
   }
   doRender_p (data_opl) {
      let markup_s = APPETT.tm_o.execute_px(this.template_s, data_opl);
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.innerHTML = markup_s;
      }
   }
   configHandleEvent_p () {
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.addEventListener("click", this.handleEvent_p);
      }
   }
   
   handleEvent_p (event_opl) {
      if (event_opl.target.tagName.toUpperCase() == "A") {
		 var topic_id = event_opl.target.id;
		 //let elx_o = document.querySelector(".clSelected");
         //if (elx_o != null) {
         //   elx_o.classList.remove("clSelected");
         //}
         //event_opl.target.parentNode.classList.add("clSelected");
		 //editiert
		 APPETT.es_o.publish_px("app.cmd", ["detail_show", topic_id] );
         //event_opl.preventDefault();
      } else if (event_opl.target.id == "idNewListEntry") {
           APPETT.es_o.publish_px("app.cmd", ["detail_create", null] );
        }
		event_opl.preventDefault();
	  /*else if (event_opl.target.id == "idShowListEntry") {
         let elx_o = document.querySelector(".clSelected");
         if (elx_o == null) {
            alert("Bitte zuerst einen Eintrag auswählen!");
         } else {
            APPETT.es_o.publish_px("app.cmd", ["detail", elx_o.id] );
         }   
         event_opl.preventDefault();
      }*/
   }
}

class SideBar_cl {

   constructor (el_spl, template_spl) {
      this.el_s = el_spl;
      this.template_s = template_spl;
      this.configHandleEvent_p();
   }
   render_px (data_opl) {
      let markup_s = APPETT.tm_o.execute_px(this.template_s, data_opl);
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.innerHTML = markup_s;
      }
   }
   configHandleEvent_p () {
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.addEventListener("click", this.handleEvent_p);
      }
   }
   handleEvent_p (event_opl) {
      let cmd_s = event_opl.target.dataset.action;
      APPETT.es_o.publish_px("app.cmd", [cmd_s, null]);
   }
}

class Application_cl {

   constructor () {
      // Registrieren zum Empfang von Nachrichten
      APPETT.es_o.subscribe_px(this, "templates.loaded");
      APPETT.es_o.subscribe_px(this, "templates.failed");
      APPETT.es_o.subscribe_px(this, "app.cmd");
      this.sideBar_o = new SideBar_cl("aside", "sidebar.tpl.html");
      this.listView_o = new ListView_cl("main", "list.tpl.html");
	  this.favoritesView_o = new ListView_cl("main", "favorites.tpl.html");
	  this.topicsView_o = new ListView_cl("main", "topics.tpl.html");
      this.tagsView_o = new ListView_cl("main", "tags.tpl.html");
	  this.missingView_o = new ListView_cl("main", "missing.tpl.html");
	  this.orphanthemesView_o = new ListView_cl("main", "orphans.tpl.html");
      this.detail_createView_o = new DetailView_cl("main", "detail_create.tpl.html");
	  this.detail_showView_o = new DetailView_cl("main", "detail_show.tpl.html");
	  this.detail_editView_o = new DetailView_cl("main", "detail_edit.tpl.html");
   }
   notify_px (self, message_spl, data_opl) {
      switch (message_spl) {
      case "templates.failed":
         alert("Vorlagen konnten nicht geladen werden.");
         break;
      case "templates.loaded":
         // Templates stehen zur Verfügung, Bereiche mit Inhalten füllen
         // hier zur Vereinfachung direkt
         let markup_s;
         let el_o;
         markup_s = APPETT.tm_o.execute_px("header.tpl.html", null);
         el_o = document.querySelector("header");
         if (el_o != null) {
            el_o.innerHTML = markup_s;
         }
         markup_s = APPETT.tm_o.execute_px("footer.tpl.html", null);
         el_o = document.querySelector("footer");
         if (el_o != null) {
            el_o.innerHTML = markup_s;
         }
         let nav_a = [
            ["home", "[Home]"],
            ["favorites", "[Favoriten]"],
			["topics", "[Alle Themen]"],
            ["tags", "[Alle Kategorien]"],
            ["missing", "[Fehlende Themen]"],
			["orphans", "[Verwaiste Themen]"]
		 ];
         self.sideBar_o.render_px(nav_a);
         markup_s = APPETT.tm_o.execute_px("home.tpl.html", null);
         el_o = document.querySelector("main");
         if (el_o != null) {
            el_o.innerHTML = markup_s;
         }
         break;
      
      case "app.cmd":
         // hier müsste man überprüfen, ob der Inhalt gewechselt werden darf
         switch (data_opl[0]) {
         case "home":
            let markup_s = APPETT.tm_o.execute_px("home.tpl.html", null);
            let el_o = document.querySelector("main");
            if (el_o != null) {
               el_o.innerHTML = markup_s;
            }
            break;
         case "list":
            // Daten anfordern und darstellen
            this.listView_o.render_px();
            break;
         case "detail_create":
            this.detail_createView_o.render_px(data_opl[1]);
            break;
		 case "detail_show":
            this.detail_showView_o.render_px(data_opl[1]);
            break;
		 case "detail_edit":
            this.detail_editView_o.render_px(data_opl[1]);
            break;
		 case "favorites":
			this.favoritesView_o.render_px();
            break;	
		 case "topics":
			this.topicsView_o.render_px();
            break;
		 case "tags":
			this.tagsView_o.render_px();
            break;
		 case "missing":
			this.missingView_o.render_px();
            break;
		 case "orphans":
			this.orphansView_o.render_px();
            break;
         case "idBack":
            APPETT.es_o.publish_px("app.cmd", ["topics", null]);
            break;		
         case "topicspeichern":
			let method;
			let path_s;
			
			if(data_opl[1]==null){
				method = "POST";
				path_s = "/app/topics/";
			}
			else{
				method = "PUT";
				path_s = "/app/topics/"+data_opl[1];
			}
			
			var form = document.getElementById("topicsData");
			var data = new FormData(form);
			
			APPETT.xhr_o.request_px(path_s, 
                function (responseText_spl) {
                   let data_o = JSON.parse(responseText_spl);
                   this.doRender_p(data_o);
                }.bind(this),
                function (responseText_spl) {
                   alert("List - render failed");
                }
             , method, data);
		
            APPETT.es_o.publish_px("app.cmd", ["topics", null]);
            break;			
         }
         break;
      }
   }
}

window.onload = function () {
   APPETT.xhr_o = new APPETT.XHR_cl();
   APPETT.es_o = new APPETT.EventService_cl();
   var app_o = new Application_cl();
   APPETT.tm_o = new APPETT.TemplateManager_cl();
}