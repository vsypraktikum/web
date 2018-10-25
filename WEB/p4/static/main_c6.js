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
      //alert("Die ID ist " + id_spl);
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
	  if(this.template_s=="detail_show.tpl.html"){
         var zaehler = 0;
		 while (zaehler <= 5){
		 //markup_s = markup_s.replace(/[[/g,"<a href='#' class='link'>").replace(/]]/g,"</a>");
		 markup_s = markup_s.replace("[[","<a href='#' class='link'>").replace("]]","</a>");		 
		 zaehler++;
		 }
	  } 
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
		//var check = confirm('Wenn Sie die Seite verlassen, können Daten verloren gehen. Seite verlassen?'); 
		//if (check == false) {
		//	event_opl.preventDefault()
		//} else{
			APPETT.es_o.publish_px("app.cmd", ["idBack", null]);
			event_opl.preventDefault();
		//  }
      } else if((event_opl.target.tagName.toUpperCase() == "A") && (event_opl.target.className == "link")){
		  var bezeichnung = event_opl.target.innerText;
		  //alert(bezeichnung)
		  event_opl.preventDefault();
          APPETT.es_o.publish_px("app.cmd", ["detail_show", bezeichnung]);
		}
		else if(event_opl.target.id == "topicerstellen"){
          event_opl.preventDefault();
          APPETT.es_o.publish_px("app.cmd", ["topicerstellen", this.topic_id]);
		}
		else if(event_opl.target.id == "topicspeichern"){
          var topic_id = event_opl.target.dataset.id;
		  event_opl.preventDefault();
          APPETT.es_o.publish_px("app.cmd", ["topicspeichern", topic_id]);
		}
		else if(event_opl.target.id == "topicloeschen"){	
          var topic_id = event_opl.target.dataset.id;
		  if(topic_id == "0"){
			  alert("Der Datensatz kann nicht gelöscht werden!")
			  event_opl.preventDefault()
		  }else{
				var check = confirm('Wollen Sie den Datensatz wirklich löschen?'); 
				if (check == false) {
					event_opl.preventDefault()
				}else{
					APPETT.es_o.publish_px("app.cmd", ["topicloeschen", topic_id]);
				 }  
			}
		}
		else if(event_opl.target.id == "topicbearbeiten"){
		  var topic_id = event_opl.target.dataset.id;
          //alert("das ist die bearbeiten topic"+topic_id)
		  event_opl.preventDefault();
          APPETT.es_o.publish_px("app.cmd", ["detail_edit", topic_id]);
		}
   }
}

class DetailTagsView_cl {

   constructor (el_spl, template_spl) {
      this.el_s = el_spl;
      this.template_s = template_spl;
   }
   render_px (id_spl) {
	  // Daten anfordern
      let path_s = "/app/tags/" + id_spl;
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
	  //alert(el_o);
      if (el_o != null) {
         el_o.addEventListener("click", this.handleEvent_p);
      }
   }
   handleEvent_p (event_opl) {
      if (event_opl.target.id == "idBack") {
         APPETT.es_o.publish_px("app.cmd", ["idBack", null]);
         event_opl.preventDefault();
      } else if ((event_opl.target.tagName.toUpperCase() == "A") && (event_opl.target.className == "tagtopics")){
		 var topic_id = event_opl.target.id;
		 alert("das ist tagtopic "+ topic_id);
		 APPETT.es_o.publish_px("app.cmd", ["detail_show", topic_id] );
		 event_opl.preventDefault();
		}
		event_opl.preventDefault();
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
      if (event_opl.target.tagName.toUpperCase() == "A" && (event_opl.target.className == "topics")) {
		 var topic_id = event_opl.target.id;
		 APPETT.es_o.publish_px("app.cmd", ["detail_show", topic_id] );
         event_opl.preventDefault();
      } else if (event_opl.target.id == "idNewListEntry") {
           APPETT.es_o.publish_px("app.cmd", ["detail_create", null] );
		   event_opl.preventDefault();
        }
		event_opl.preventDefault();
   }
}

class ListTagsView_cl {

   constructor (el_spl, template_spl) {
      this.el_s = el_spl;
      this.template_s = template_spl;
      this.configHandleEvent_p();
   }
   render_px () {
      // Daten anfordern
      let path_s = "/app/tags/";
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
      if (event_opl.target.tagName.toUpperCase() == "A" && (event_opl.target.className == "tags")) {
		 var tag_id = event_opl.target.id;
		 APPETT.es_o.publish_px("app.cmd", ["detail_tags", tag_id] );
         event_opl.preventDefault();
      } 
		event_opl.preventDefault();
   }
}

class ListFavoritesView_cl {

   constructor (el_spl, template_spl) {
      this.el_s = el_spl;
      this.template_s = template_spl;
      this.configHandleEvent_p();
   }
   render_px () {
      // Daten anfordern
      let path_s = "/app/favorites/";
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
      if (event_opl.target.tagName.toUpperCase() == "A" && (event_opl.target.className == "favorites")) {
		 var topic_id = event_opl.target.id;
		 APPETT.es_o.publish_px("app.cmd", ["detail_show", topic_id] );
         event_opl.preventDefault();
      } 
		event_opl.preventDefault();
   }
}

class ListMissingView_cl {

   constructor (el_spl, template_spl) {
      this.el_s = el_spl;
      this.template_s = template_spl;
      this.configHandleEvent_p();
   }
   render_px () {
      // Daten anfordern
      let path_s = "/app/missing/";
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
      if (event_opl.target.tagName.toUpperCase() == "A" && (event_opl.target.className == "missing")) {
		 var topic_id = event_opl.target.id;
		 APPETT.es_o.publish_px("app.cmd", ["detail_show", topic_id] );
         event_opl.preventDefault();
      } 
		event_opl.preventDefault();
   }
}

class ListOrphansView_cl {

   constructor (el_spl, template_spl) {
      this.el_s = el_spl;
      this.template_s = template_spl;
      this.configHandleEvent_p();
   }
   render_px () {
      // Daten anfordern
      let path_s = "/app/orphans/";
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
      if (event_opl.target.tagName.toUpperCase() == "A" && (event_opl.target.className == "orphans")) {
		 var topic_id = event_opl.target.id;
		 APPETT.es_o.publish_px("app.cmd", ["detail_show", topic_id] );
         event_opl.preventDefault();
      } 
		event_opl.preventDefault();
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
	  this.favoritesView_o = new ListFavoritesView_cl("main", "favorites.tpl.html");
	  this.topicsView_o = new ListView_cl("main", "topics.tpl.html");
      this.tagsView_o = new ListTagsView_cl("main", "tags.tpl.html");
	  this.missingView_o = new ListMissingView_cl("main", "missing.tpl.html");
	  this.orphansView_o = new ListOrphansView_cl("main", "orphans.tpl.html");
      this.detail_createView_o = new DetailView_cl("main", "detail_create.tpl.html");
	  this.detail_showView_o = new DetailView_cl("main", "detail_show.tpl.html");
	  this.detail_editView_o = new DetailView_cl("main", "detail_edit.tpl.html");
	  this.detail_TagsView_o = new DetailTagsView_cl("main", "detailTags.tpl.html");
	  this.homeView_o = new DetailView_cl("main", "home.tpl.html");
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
         //markup_s = APPETT.tm_o.execute_px("home.tpl.html", null);
         //el_o = document.querySelector("main");
         //if (el_o != null) {
         //   el_o.innerHTML = markup_s;
         //}
		 this.homeView_o.render_px("0");
         break;
      
      case "app.cmd":
         // hier müsste man überprüfen, ob der Inhalt gewechselt werden darf
         let method = null;
		 let path_s = null;
		 switch (data_opl[0]) {
         case "home":
            //let markup_s = APPETT.tm_o.execute_px("home.tpl.html", null);
            //let el_o = document.querySelector("main");
            //if (el_o != null) {
            //   el_o.innerHTML = markup_s;
            //}
			this.homeView_o.render_px("0");
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
		 case "detail_tags":
            this.detail_TagsView_o.render_px(data_opl[1]);
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
         case "topicerstellen":
			method = "POST";
			path_s = "/app/topics/";
			
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
		 case "topicspeichern":
			method = "PUT";
			//alert(data_opl[1])
			path_s = "/app/topics/"+data_opl[1];
			
			var form = document.getElementById("topicsData");
			var data = new FormData(form);
			
			APPETT.xhr_o.request_px(path_s, 
                function (responseText_spl) {
                   let data_o2 = JSON.parse(responseText_spl);
                   this.doRender_p(data_o2);
                }.bind(this),
                function (responseText_spl) {
                   alert("List - render failed");
                }
             , method, data);
		
            APPETT.es_o.publish_px("app.cmd", ["detail_show", data_opl[1]]);
            break;
         case "topicloeschen":
            method = "DELETE"
			path_s = "/app/topics/"+data_opl[1];
            APPETT.xhr_o.request_px(path_s, 
                function (responseText_spl) {
                    let data_o3 = JSON.parse(responseText_spl);
                    this.doRender_p(data_o3);
                }.bind(this),
                function (responseText_spl) {
                     alert("List - render failed");
                 }
            , method);
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