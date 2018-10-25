# coding: utf-8

import cherrypy

from .database import Database_cl
from .view import View_cl


# GET     /tags/    alle Marken und die Anzahl der Artikel

#----------------------------------------------------------
class Tags_cl(object):
#----------------------------------------------------------

   exposed = True

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.db_o = Database_cl()
      self.view_o = View_cl()

   #-------------------------------------------------------
   def GET(self):
   #-------------------------------------------------------
      data_a = self.db_o.read_px()
      
      retVal_s = ''

      data_tag = []

      for value in data_a:
         for tagvalue in value['tag']:
            if tagvalue not in data_tag:
               data_tag.append(tagvalue)
      
      # return tags with occurring numbers
      data_return = {}
      i = 0
      for value in data_tag:
         data_single = {}
         
         data_single['tag'] = value
         
         #find data with tag
         count = 0
         for article in data_a:
            if value in article['tag']:
               count = count + 1
      
         data_single['count'] = count
      
         data_return[i] = data_single
         i = i + 1
      
      retVal_s = self.view_o.createList_px(data_return)

      return retVal_s

# EOF