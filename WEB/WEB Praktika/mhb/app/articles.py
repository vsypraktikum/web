# coding: utf-8

import cherrypy
import datetime

from .database import Database_cl
from .view import View_cl


# GET        /articles/all/             alle Artikel
# GET        /articles/month/:month     die Artikel, die im angegebenen Monat erstellt oder geändert wurden
# GET        /articles/tag/:tag         die Artikel, die die angegebene Marke enthalten

#----------------------------------------------------------
class Articles_cl(object):
#----------------------------------------------------------

   exposed = True

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.db_o = Database_cl()
      self.view_o = View_cl()

   #-------------------------------------------------------
   def GET(self, mode, parameter=None):
   #-------------------------------------------------------
      retVal_s = ''

      if mode == 'all':
         retVal_s = self.getList_p()
      
      if mode == 'month':
         retVal_s = self.getArticlesByMonth_p(parameter)
         
      if mode == 'tag':
         retVal_s = self.getArticlesByTag_p(parameter)

      return retVal_s
  
   #-------------------------------------------------------
   def getList_p(self):
   #-------------------------------------------------------
      data_a = self.db_o.read_px()
      # default-Werte entfernen
      
      ndata_a = data_a[0:]
        
      return self.view_o.createList_px(ndata_a)
   
   #-------------------------------------------------------
   def getArticlesByMonth_p(self, month):
   #-------------------------------------------------------
      # Format muss sein: 01.2018, also das Jahr muss einbezogen werden
      year = month[3:7]
      month = month[0:2]
      
      data_a = self.db_o.read_px()
      
      data_unsort = []
      
      #--------------------------------
      i = 0

      for value in data_a:
         if (int(value['chdat'][3:5]) == int(month) and int(value['chdat'][6:10]) == int(year)): # python slicing substring 4th element up to 5th element = month
            data_unsort.append(value)

      data_sort = []
      
      data_unsort.sort(key=lambda x: x['chdat'])
      data_sort = data_unsort[::-1]

      return self.view_o.createList_px(data_sort)
      
   #-------------------------------------------------------
   def getArticlesByTag_p(self, tag):
   #-------------------------------------------------------
      data_a = self.db_o.read_px()
      
      data_unsort = []
      
      for value in data_a:
         for valuetag in value['tag']:
            if valuetag == tag:
               data_unsort.append(value)
      
      data_sort = []
      
      data_unsort.sort(key=lambda x: x['chdat'])
      data_sort = data_unsort[::-1]


      return self.view_o.createList_px(data_sort)
# EOF