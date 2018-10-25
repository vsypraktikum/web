# coding: utf-8

# In dieser Variante die Markup-Erzeugung mit Hilfe einer Template-Engine durchführen

import os.path

from mako.template import Template
from mako.lookup import TemplateLookup

#----------------------------------------------------------
class View_cl(object):
#----------------------------------------------------------

   #-------------------------------------------------------
   def __init__(self, path_spl):
   #-------------------------------------------------------
      # Pfad hier zur Vereinfachung fest vorgeben
      self.path_s = os.path.join(path_spl, "tpl")
      self.lookup_o = TemplateLookup(directories=[self.path_s])

   #-------------------------------------------------------
   def create_p(self, template_spl, data_opl):
   #-------------------------------------------------------
      # Auswertung mit templates
      template_o = self.lookup_o.get_template(template_spl)
      return template_o.render(data_o = data_opl)

   #-------------------------------------------------------
   def createList_px(self, data_opl):
   #-------------------------------------------------------
      return self.create_p('liste.tpl', data_opl)

   #-------------------------------------------------------
   def createForm_px(self, id_spl, data_opl):
   #-------------------------------------------------------
      data_opl['id'] = id_spl
      return self.create_p('detail.tpl', data_opl)

# EOF