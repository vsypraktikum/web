//------------------------------------------------------------------------------
//Demonstrator es/te/tm - Variante mit ES6-Classes
//------------------------------------------------------------------------------
// hier zur Vereinfachung (!) die Klassen in einer Datei

class mainscreen_cl
{
   constructor (el_spl) {
      this.el_s = el_spl;
      
      this.configHandleEvent_p();
      
   }
   render_px () {
      let path_s = "/months/";
      APPETT.xhr_o.request_px(path_s, 
         function (responseText_spl) {
            let data_o = JSON.parse(responseText_spl);
           setTimeout(function(){this.doRender_p(data_o)}.bind(this),5000);
         }.bind(this),
         function (responseText_spl) {
            alert("List - render failed");
         }
      );
      }
      doRender_p (data_opl) {
       
       var i;
   var monat = [];
   
      for (i=0;i<data_opl.length;i++){
      if(data_opl[i][0]=="0"){
      
      if(data_opl[i][1]=="1"){
      monat.push("Januar");
      }
      if(data_opl[i][1]=="2"){
            monat.push("Februar");
      }
      if(data_opl[i][1]=="3"){
            monat.push("Marz");
      }
      if(data_opl[i][1]=="4"){
            monat.push("April");
      }
      if(data_opl[i][1]=="5"){
            monat.push("Mai");
      }
      if(data_opl[i][1]=="6"){
            monat.push("Juni");
      }
      if(data_opl[i][1]=="7"){
            monat.push("Juli");
      }
      if(data_opl[i][1]=="8"){
            monat.push("August");
      }
      if(data_opl[i][1]=="9"){
            monat.push("September");
      }
      
      }else if(data_opl[i][0]=="1"){
            if(data_opl[i][1]=="0"){
                  monat.push("Oktober");
            }
            if(data_opl[i][1]=="1"){
                  monat.push("November");
            }
            if(data_opl[i][1]=="2"){
                  monat.push("Dezember");
            }     
      }
   }
      var data_s =[];
      data_s[0]=[];
      data_s[1]=[];
      setTimeout( function(){
      let path_s = "/articles/month/" + data_opl[0];
      APPETT.xhr_o.request_px(path_s, 
         function (responseText_spl) {
              data_s[0].push(JSON.parse(responseText_spl));
             
             //data_temp = data_o[0];
            
            //data_o[0].push(data_temp);
         }.bind(this),
         function (responseText_spl) {
            alert("Detail - render failed");
         }
      );
      }.bind(this),200);
      
      data_s[1] =monat;
      setTimeout(function(){
      let markup_s = APPETT.tm_o.execute_px("month.tpl.html", data_s);
      //let el_o = document.querySelector(this.el_s);
      let el_o = document.getElementById("idContent");
      if (el_o != null) {
         el_o.innerHTML = markup_s;
      }}.bind(this),300);
         
      }
   
   
   configHandleEvent_p () {
      //this.sideView_o.configHandleEvent_p();
      }
   handleEvent_p (event_opl) {
      //this.sideView_o.handleEvent_p(event_opl);
   }
}





'use strict'
class tags_cl{
constructor (el_spl, template_spl) {
      this.el_s = el_spl;
      this.template_s = template_spl;
      this.configHandleEvent_p();
   }
   render_px () {
      // Daten anfordern
      let path_s = "/tags/";
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
      //let el_o = document.querySelector(this.el_s);
      let el_o = document.getElementById("tags");
      if (el_o != null) {
         el_o.innerHTML = markup_s;
      }
   }
   configHandleEvent_p () {
      //let el_o = document.querySelector(this.el_s);
      let el_o = document.getElementById("tags");
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
      }
   }

}

class monthauswahl_cl{
constructor (el_spl, template_spl) {
      this.el_s = el_spl;
      this.template_s = template_spl;
      this.configHandleEvent_p();
      this.listView_o = new ListView_cl("div", "listside.tpl.html");
   }
   render_px () {
     let path_s = "/months/";
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
   var i;
   var monat = [];
   
      for (i=0;i<data_opl.length;i++){
      if(data_opl[i][0]=="0"){
      
      if(data_opl[i][1]=="1"){
      monat.push("Januar");
      }
      if(data_opl[i][1]=="2"){
            monat.push("Februar");
      }
      if(data_opl[i][1]=="3"){
            monat.push("Marz");
      }
      if(data_opl[i][1]=="4"){
            monat.push("April");
      }
      if(data_opl[i][1]=="5"){
            monat.push("Mai");
      }
      if(data_opl[i][1]=="6"){
            monat.push("Juni");
      }
      if(data_opl[i][1]=="7"){
            monat.push("Juli");
      }
      if(data_opl[i][1]=="8"){
            monat.push("August");
      }
      if(data_opl[i][1]=="9"){
            monat.push("September");
      }
      
      }else if(data_opl[i][0]=="1"){
            if(data_opl[i][1]=="0"){
                  monat.push("Oktober");
            }
            if(data_opl[i][1]=="1"){
                  monat.push("November");
            }
            if(data_opl[i][1]=="2"){
                  monat.push("Dezember");
            }     
      }
   }
      var data_s =[];
      data_s[0]=[];
      data_s[1]=[];
      temp=[]
      var j=0;
      for (j=0; j< data_opl.length;j++){
      var temp=[];
      temp[j]=j;
      setTimeout( function(){
      let path_s = "/articles/month/" + data_opl[j];
      APPETT.xhr_o.request_px(path_s, 
         function (responseText_spl) {
              data_s[0].push(JSON.parse(responseText_spl));
             
             //data_temp = data_o[0];
            
            //data_o[0].push(data_temp);
         }.bind(this),
         function (responseText_spl) {
            alert("Detail - render failed");
         }
      );
      }.bind(this),3000*j);
      
      }
      data_s[1] =monat;
      setTimeout(function(){
      let markup_s = APPETT.tm_o.execute_px(this.template_s, data_s);
      //let el_o = document.querySelector(this.el_s);
      let el_o = document.getElementById("hist");
      if (el_o != null) {
         el_o.innerHTML = markup_s;
      }}.bind(this),30000);
   }
   
   configHandleEvent_p () {
      //let el_o = document.querySelector(this.el_s);
      let el_o = document.getElementById("hist");
      if (el_o != null) {
         el_o.addEventListener("click", this.handleEvent_p);
      }
   }
   handleEvent_p (event_opl) {
     var value = event_opl.target.id;
      
      


}}



class DetailView_cl {

   constructor (el_spl, template_spl) {
      this.el_s = el_spl;
      this.template_s = template_spl;
   }
   render_px (id_spl) {
      // Daten anfordern
      let path_s = "/app/" + id_spl;
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
                 let path_s = "/articles/";
        APPETT.xhr_o.request_px(path_s,
            function (responseText_spl) {
                let data_o = JSON.parse(responseText_spl);
            }.bind(this),
            function (responseText_spl) {
                alert("ListCon - render failed");
            },
            'POST',
            
        );
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
      //month ausgabe
      let path_s = "/articles/all";
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
      
      let el_o = document.getElementById("hist");
      if(this.el_s == "main"){
            el_o = document.querySelector(this.el_s);
      }
      if (el_o != null) {
         el_o.innerHTML = markup_s;
      }
   }
   configHandleEvent_p () {
      let el_o = document.getElementById("hist");
      if(this.el_s == "main"){
            el_o = document.querySelector(this.el_s);
      }
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
      }
   }
}
class SideBarList_cl {
      constructor (el_spl, template_spl) {
      this.el_s = el_spl;
      this.template_s = template_spl;
      this.configHandleEvent_p();
      
      
   }
   render_px (data_opl) {
      let markup_s = APPETT.tm_o.execute_px(this.template_s, data_opl);
      //div mit id und nicht querysel
      //let el_o = document.querySelector(this.el_s);
      let el_o = document.getElementById("allArt"); //div mit id allArt
      if (el_o != null) {
         el_o.innerHTML = markup_s;
      }
   }
   configHandleEvent_p () {
      let el_o = document.getElementById("allArt"); //div mit id allArt
      //let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.addEventListener("click", this.handleEvent_p);
      }
   }
   handleEvent_p (event_opl) {
      let cmd_s = event_opl.target.dataset.action;
      APPETT.es_o.publish_px("app.cmd", [cmd_s, null]);
   }

}

class SideBar_cl {

   constructor (el_spl) {
      this.listView_o = new monthauswahl_cl("div", "monthauswahl.tpl.html");
      this.sideView_o = new SideBarList_cl("div","sidebar.tpl.html")
      this.tags_o = new tags_cl("div","tags.tpl.html")
      this.el_s = el_spl;
      
      this.configHandleEvent_p();
      
   }
   render_px (data_opl) {
     
     this.sideView_o.render_px(data_opl);
     setTimeout(function(){this.tags_o.render_px()}.bind(this),8000);
     setTimeout(function(){this.listView_o.render_px()}.bind(this),12000);
      }
   
   configHandleEvent_p () {
      this.sideView_o.configHandleEvent_p();
      }
   handleEvent_p (event_opl) {
      this.sideView_o.handleEvent_p(event_opl);
   }
}

class Application_cl {

   constructor () {
      // Registrieren zum Empfang von Nachrichten
      APPETT.es_o.subscribe_px(this, "templates.loaded");
      APPETT.es_o.subscribe_px(this, "templates.failed");
      APPETT.es_o.subscribe_px(this, "app.cmd");
      this.sideBar_o = new SideBar_cl("aside");
      this.listView_o = new ListView_cl("main","list.tpl.html");
      this.detailView_o = new DetailView_cl("main", "detail.tpl.html");
      this.mainscreen_o = new mainscreen_cl("main","month.tpl.html")
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

         //footer wird nicht benötigt - siehe anforderung
         /*
         markup_s = APPETT.tm_o.execute_px("footer.tpl.html", null);
         el_o = document.querySelector("footer");
         if (el_o != null) {
            el_o.innerHTML = markup_s;
         }*/
         let nav_a = [
            ["home", "Startseite"],
            ["list", "Alle"]
            
         ];
         self.sideBar_o.render_px(nav_a);
         
         markup_s = APPETT.tm_o.execute_px("home.tpl.html", null);
         el_o = document.querySelector("main");
         if (el_o != null) {
            el_o.innerHTML = markup_s;
         }
         self.mainscreen_o.render_px();
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
         case "idBack":
            APPETT.es_o.publish_px("app.cmd", ["list", null]);
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