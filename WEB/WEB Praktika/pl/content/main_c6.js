//------------------------------------------------------------------------------
//Demonstrator es/te/tm - Variante mit ES6-Classes
//------------------------------------------------------------------------------
// hier zur Vereinfachung (!) die Klassen in einer Datei

'use strict'

class Significantbirthdays_cl {
    constructor (el_spl, template_spl) {
        this.el_s = el_spl;
        this.template_s = template_spl;
    }
    render_px (id_spl) {
        this.doRender_p();
     }
     doRender_p (data_opl=null) {
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
        if (event_opl.target.id == "significantbutton") {
            event_opl.preventDefault();
           APPETT.es_o.publish_px("app.cmd", ["significantbutton", null]);
        }
     }}

class Significantbirthdays2_cl {
        constructor (el_spl, template_spl) {
            this.el_s = el_spl;
            this.template_s = template_spl;
            this.configHandleEvent_p();
        }
        render_px () {
            // Daten anfordern
            var path3 = "/app/significantbirthdays/";
            var form3 = document.getElementById("daten");
            var data3 = new FormData(form3);
            
            APPETT.xhr_o.request_px(path3, 
                function (responseText_spl) {
                    let data_o = JSON.parse(responseText_spl);
                     this.doRender_p(data_o);
                }.bind(this),
                 function (responseText_spl) {
                     alert("List - render failed");
               }
            , "POST", data3);
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
            if (event_opl.target.tagName.toUpperCase() == "TD") {
                let elx_o = document.querySelector(".clSelected");
                if (elx_o != null) {
                   elx_o.classList.remove("clSelected");
                }
                event_opl.target.parentNode.classList.add("clSelected");
                event_opl.preventDefault();
             } else if (event_opl.target.id == "erstellung") {
                let elx_o = document.querySelector(".clSelected");
                if (elx_o == null) {
                   alert("Bitte zuerst einen Eintrag auswählen!");
                } else {
                    event_opl.preventDefault();
                    APPETT.es_o.publish_px("app.cmd", ["TheEnd", elx_o.id]);  
            }
        }
    }
}
    
    


class Congratstempl_cl {
    constructor (el_spl, template_spl) {
        this.el_s = el_spl;
        this.template_s = template_spl;
        this.configHandleEvent_p();
    }
    render_px (id_spl) {
        // Daten anfordern
        let path_s = "/app/congratstempl/-1/-1/";
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
        }
    }
    configHandleEvent_p () {
        let el_o = document.querySelector(this.el_s);
        if (el_o != null) {
           el_o.addEventListener("click", this.handleEvent_p);
        }
     }
     handleEvent_p (event_opl) {
        if (event_opl.target.tagName.toUpperCase() == "TD") {
            let elx_o = document.querySelector(".clSelected");
            if (elx_o != null) {
               elx_o.classList.remove("clSelected");
            }
            event_opl.target.parentNode.classList.add("clSelected");
            event_opl.preventDefault();
         } else if (event_opl.target.id == "idShowListEntryC") {
            let elx_o = document.querySelector(".clSelected");
            if (elx_o == null) {
               alert("Bitte zuerst einen Eintrag auswählen!");
            } else {
               APPETT.es_o.publish_px("app.cmd", ["congratstempdetails", elx_o.id] );
            }   
            event_opl.preventDefault();

         } else if (event_opl.target.id == "DeleteC") {
                let elx_o = document.querySelector(".clSelected");
                if (elx_o == null) {
                   alert("Bitte zuerst einen Eintrag auswählen!");
                } else {
                   APPETT.es_o.publish_px("app.cmd", ["deleteC", elx_o.id] );
                }   
                event_opl.preventDefault();
        } else if (event_opl.target.id == "ImportPath") {
            APPETT.es_o.publish_px("app.cmd", ["ImportPath", document.getElementById("Path").value]);
            event_opl.preventDefault();           
         }       
    }}





class Congratstempimport_cl {
    constructor (el_spl, template_spl) {
        this.el_s = el_spl;
        this.template_s = template_spl;
        this.configHandleEvent_p();
    }
    render_px (id_spl) {
        // Daten anfordern
        let path_s = "/app/congratstempl/-1/"+ id_spl;
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
        }
    }
    configHandleEvent_p () {
        let el_o = document.querySelector(this.el_s);
        if (el_o != null) {
           el_o.addEventListener("click", this.handleEvent_p);
        }
     }
     handleEvent_p (event_opl) {
        if (event_opl.target.tagName.toUpperCase() == "TD") {
            let elx_o = document.querySelector(".clSelected");
            if (elx_o != null) {
               elx_o.classList.remove("clSelected");
            }
            event_opl.target.parentNode.classList.add("clSelected");
            event_opl.preventDefault();
         } else if (event_opl.target.id == "importEntry") {
            let elx_o = document.querySelector(".clSelected");
            if (elx_o == null) {
               alert("Bitte zuerst einen Eintrag auswählen!");
            } else {
               APPETT.es_o.publish_px("app.cmd", ["congratstempimportierung", elx_o.id] );
            }   
            event_opl.preventDefault();   
        }   
 }}


class Congratstempdetails_cl {
    constructor (el_spl, template_spl) {
        this.el_s = el_spl;
        this.template_s = template_spl;
    }
    render_px (id_spl) {
        // Daten anfordern
        let path_s = "/app/congratstempl/"+id_spl+"/-1/";
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
        }
    }
 }

class Annuallist_cl {
    constructor (el_spl, template_spl) {
        this.el_s = el_spl;
        this.template_s = template_spl;
    }
    render_px (id_spl) {
        // Daten anfordern
        let path_s = "/app/annuallist";
        APPETT.xhr_o.request_px(path_s, 
           function (responseText_spl) {
              let data_o = JSON.parse(responseText_spl);
              this.doRender_p(data_o);
           }.bind(this),
           function (responseText_spl) {
              alert("Detail - render failed"); 
              }
        ,"POST");
     }
     doRender_p (data_opl) {
        let markup_s = APPETT.tm_o.execute_px(this.template_s, data_opl);
        let el_o = document.querySelector(this.el_s);
        if (el_o != null) {
           el_o.innerHTML = markup_s;
        }
    }
}

class DetailView_cl {

   constructor (el_spl, template_spl) {
      this.el_s = el_spl;
      this.template_s = template_spl;
      this.rentner_id=null
      
   }
   render_px (id_spl) {
      // Daten anfordern
      if(id_spl!=null){
        this.rentner_id=id_spl;
        let path_s = "/app/pensionaer/" + id_spl;
        APPETT.xhr_o.request_px(path_s, 
            function (responseText_spl) {
                let data_o = JSON.parse(responseText_spl);
                this.doRender_p(data_o);
            }.bind(this),
           function (responseText_spl) {
                alert("Detail - render failed");
            },
        );
        }
        else
        {
            this.rentner_id=10000;
            this.doRender_p(null);
        }
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
         el_o.rentner_id=this.rentner_id;
      }
   }
   handleEvent_p (event_opl) {
      if (event_opl.target.id == "idBack") {
         APPETT.es_o.publish_px("app.cmd", ["idBack", null]);
         event_opl.preventDefault();
      } else if(event_opl.target.id == "pensionaerspeichern"){
          event_opl.preventDefault();
          APPETT.es_o.publish_px("app.cmd", ["pensionaerspeichern", this.rentner_id]);
          
      }
   }}

class ListView_cl {

   constructor (el_spl, template_spl) {
      this.el_s = el_spl;
      this.template_s = template_spl;
      this.configHandleEvent_p();
   }
   render_px () {
      // Daten anfordern
      let path_s = "/app/pensionaer/";
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
      if (event_opl.target.tagName.toUpperCase() == "TD") {
         let elx_o = document.querySelector(".clSelected");
         if (elx_o != null) {
            elx_o.classList.remove("clSelected");
         }
         event_opl.target.parentNode.classList.add("clSelected");
         event_opl.preventDefault();
      } else if (event_opl.target.id == "idShowListEntry") {
         let elx_o = document.querySelector(".clSelected");
         if (elx_o == null) {
            alert("Bitte zuerst einen Eintrag auswählen!");
         } else {
            APPETT.es_o.publish_px("app.cmd", ["detail", elx_o.id] );
         }   
         event_opl.preventDefault();
      } else if(event_opl.target.id == "idDeleteListEntry") {
        let elx_o = document.querySelector(".clSelected");
        if (elx_o == null) {
           alert("Bitte zuerst einen Eintrag auswählen!");
        } else {
            APPETT.es_o.publish_px("app.cmd", ["pensionaerloeschen", elx_o.id] );
        } 
        event_opl.preventDefault();    
      } else if (event_opl.target.id == "idNewListEntry") {
           APPETT.es_o.publish_px("app.cmd", ["detail", null] );
        }   
        event_opl.preventDefault();
   }}

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
   }}

class Application_cl {

   constructor () {
      // Registrieren zum Empfang von Nachrichten
      APPETT.es_o.subscribe_px(this, "templates.loaded");
      APPETT.es_o.subscribe_px(this, "templates.failed");
      APPETT.es_o.subscribe_px(this, "app.cmd");
      this.sideBar_o = new SideBar_cl("aside", "sidebar.tpl.html");
      this.listView_o = new ListView_cl("main", "list.tpl.html");
      this.detailView_o = new DetailView_cl("main", "pensionaer.tpl.html");
      this.significantbirthdays_o=new Significantbirthdays_cl("main", "significantbirthdays.tpl.html");
      this.significantbirthdays2_o=new Significantbirthdays2_cl("main", "significantbirthdays2.tpl.html");
      this.annuallist_o=new Annuallist_cl("main", "annuallist.tpl.html");
      this.congratstempl_o=new Congratstempl_cl("main", "congratstemplist.tpl.html");
      this.congratstempdetails_o=new Congratstempdetails_cl("main", "congratstemp.tpl.html");
      this.congratstempimport_o=new Congratstempimport_cl("main", "congratstempimport.tpl.html");

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
            ["home", "Startseite"],
            ["list", "Liste der Pensionäre"],
            ["congratstempl", "Vorlagen"],
            ["significantbirthdays", "Signifikante Geburtstage"],
            ["annuallist", "Jahresübersicht Geburtstage"],
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
         case "detail":
            this.detailView_o.render_px(data_opl[1]);
            break;
         case "significantbirthdays":
            this.significantbirthdays_o.render_px();
            break;
         case "annuallist":
            this.annuallist_o.render_px(data_opl[1]);
            break;
         case "congratstempl":
            this.congratstempl_o.render_px(data_opl[1]);
            break;
         case "idBack":
            APPETT.es_o.publish_px("app.cmd", ["list", null]);
            break;
         case "pensionaerspeichern":
            let versandmethode;
            let path_s;
            if(data_opl[1]==10000)
                {versandmethode="POST"
                path_s= "/app/pensionaer/";}
            else
                {versandmethode="PUT";
                path_s = "/app/pensionaer/"+data_opl[1];}
            
            var form = document.getElementById("pensidata");
            var data = new FormData(form);
            
            APPETT.xhr_o.request_px(path_s, 
                function (responseText_spl) {
                   let data_o = JSON.parse(responseText_spl);
                   this.doRender_p(data_o);
                }.bind(this),
                function (responseText_spl) {
                   alert("List - render failed");
                }
             , versandmethode, data);
            APPETT.es_o.publish_px("app.cmd", ["list", null]);
            break;
         case "pensionaerloeschen":
            let path_s2 = "/app/pensionaer/"+data_opl[1];
            APPETT.xhr_o.request_px(path_s2, 
                function (responseText_spl) {
                    let data_o2 = JSON.parse(responseText_spl);
                    this.doRender_p(data_o2);
                }.bind(this),
                function (responseText_spl) {
                     alert("List - render failed");
                 }
            , "DELETE");
            APPETT.es_o.publish_px("app.cmd", ["list", null]);
            break;

         case "ImportPath":
            this.congratstempimport_o.render_px(data_opl[1]);
            break;
         case "congratstempdetails":
            this.congratstempdetails_o.render_px(data_opl[1]);
            break;
         case "savecongratstempl":
            APPETT.es_o.publish_px("app.cmd", ["list", null]);
            break;
         case "deleteC":
            let path_s3 = "/app/congratstempl/"+data_opl[1];
            APPETT.xhr_o.request_px(path_s3, 
                function (responseText_spl) {
                    let data_o2 = JSON.parse(responseText_spl);
                    this.doRender_p(data_o3);
                 }.bind(this),
                function (responseText_spl) {
                     alert("List - render failed");
                }
            , "DELETE");
             APPETT.es_o.publish_px("app.cmd", ["congratstempl", null]);
            break;
         case "congratstempimportierung":  
            var path = "/app/congratstempl/-1/"+data_opl[1];
            var form2 = document.getElementById("beschreibungsdaten");
            var data2 = new FormData(form2);
            APPETT.xhr_o.request_px(path, 
                function (responseText_spl) {
                    let data_o = JSON.parse(responseText_spl);
                    this.doRender_p(data_o4);
                }.bind(this),
                function (responseText_spl) {
                    alert("List - render failed");
                 }
            , "POST", data2);
            APPETT.es_o.publish_px("app.cmd", ["congratstempl", null]);
            break;    
         case "significantbutton":
            this.significantbirthdays2_o.render_px();
            break;
         case "TheEnd":
                var form4 = document.getElementById("vorlagenid");
                var data4 = new FormData(form4);
                APPETT.xhr_o.request_px("/app/congratulation/"+data_opl[1], 
                    function (responseText_spl) {
                        let data_o = JSON.parse(responseText_spl);
                        //----------------------------------------------------------
                            var myWindow = window.open("", "MsgWindow", "width=600,height=600");
                            //console.log(data_o[1], data_o[0]);
                            //this.tm_o.templates_o = data_o[0];
                            APPETT.tm_o.templates_o["vorlage.txt"] = data_o[1]
                            let markup_s = APPETT.tm_o.execute_px("vorlage.txt", data_o[0]);
                            console.log(markup_s);
                            //let el_o = document.querySelector(this.el_s);
                            //if (el_o != null) {
                            myWindow.document.write(markup_s);
                                
                            //}
                        }.bind(this),
                        function (responseText_spl) {
                        alert("List - render failed");
                    }
                , "POST", data4);
              
             
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