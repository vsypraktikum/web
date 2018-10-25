# coding:utf-8

# Demonstrator

import os.path
import cherrypy

from app import application, template

#----------------------------------------------------------
def main():
#----------------------------------------------------------
   
   # aktuelles Verzeichnis ermitteln, damit es in der Konfigurationsdatei als
   # Bezugspunkt verwendet werden kann   
   try:                                    # aktuelles Verzeichnis als absoluter Pfad
      currentDir_s = os.path.dirname(os.path.abspath(__file__))
   except:
      currentDir_s = os.path.dirname(os.path.abspath(sys.executable))
   cherrypy.Application.currentDir_s = currentDir_s

   configFileName_s = os.path.join(currentDir_s, 'server.conf') # im aktuellen Verzeichnis   
   if os.path.exists(configFileName_s) == False:
      # Datei gibt es nicht
      configFileName_s = None
   
   # autoreload und timeout_Monitor hier abschalten
   # für cherrypy-Versionen >= "3.1.0" !
   cherrypy.engine.autoreload.unsubscribe()
   cherrypy.engine.timeout_monitor.unsubscribe()

   # 1. Eintrag: Standardverhalten, Berücksichtigung der Konfigurationsangaben im configFile
   cherrypy.tree.mount(
      None, '/', configFileName_s
   )

   # 2. Eintrag: Method-Dispatcher für die "Applikation" "app" vereinbaren
   cherrypy.tree.mount(
      application.Application_cl(),
      '/app',
      {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
   )

   # 2. Eintrag: Method-Dispatcher für die "Applikation" "templates" vereinbaren
   cherrypy.tree.mount(
      template.Template_cl(),
      '/templates', 
      {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
   )

   cherrypy.engine.start()
   cherrypy.engine.block() 

#----------------------------------------------------------
if __name__ == '__main__':
#----------------------------------------------------------
   main()