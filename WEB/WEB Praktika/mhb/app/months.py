# coding: utf-8

import cherrypy

from .database import Database_cl
from .view import View_cl


# GET /months/ 0 - 6 Monate, in denen Artikel gemäß Änderungs-/Erstellungszeitpunkt auftreten

#----------------------------------------------------------
class Months_cl(object):
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

      data_months = [] # format 01.2018 for januar 2018

      month = 9999
      year = 9999
      articleCount = 0
      recentMonthYear = '00.0000'
      lastAddedEntry = '00.0000'
      
      i = 0
      while i < 6:
         recentMonthYear = self.findRecentMonthYear_p(data_a, lastAddedEntry[0:2], lastAddedEntry[3:7])
         if recentMonthYear != '00.0000':
            data_months.append(recentMonthYear)
            lastAddedEntry = recentMonthYear
            
         i = i + 1
      #-------------------------------------------------------------------
      
      retVal_s = self.view_o.createList_px(data_months)

      return retVal_s

   #-------------------------------------------------------
   def findRecentMonthYear_p(self, data, month, year):
   #-------------------------------------------------------
      recentMonthYear = ''
     
      if month == '00':
         month = 9999
         year = 9999
     
      # find most recent year month combination
      currentYear = 0
      currentMonth = 0
      for value in data:
         if int(value['crdat'][6:10]) >= int(currentYear) and int(value['crdat'][6:10]) <= int(year):
            if int(value['crdat'][6:10]) == int(year) and int(value['crdat'][3:5]) >= int(month):
               pass
            else:
               currentYear = value['crdat'][6:10]
               currentMonth = value['crdat'][3:5]

         if int(value['chdat'][6:10]) >= int(currentYear) and int(value['chdat'][6:10]) <= int(year):
            if int(value['chdat'][6:10]) == int(year) and int(value['chdat'][3:5]) >= int(month):
               pass
            else:
               currentYear = value['chdat'][6:10]
               currentMonth = value['chdat'][3:5]
      #------------------------------------------------------------------------------------------
      if currentMonth == 0:
         currentMonth = '00'
         currentYear = '0000'

      recentMonthYear = str(currentMonth) + '.' + str(currentYear)

      return recentMonthYear
            
# EOF