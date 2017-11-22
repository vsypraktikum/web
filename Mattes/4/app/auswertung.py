import json

import cherrypy

from .database import fehlerDatabase_cl, katursacheDatabase_cl, katfehlerDatabase_cl, projektDatabase_cl, komponenteDatabase_cl

# -------------------------------------------------------
def adjustId_p(id_spl, data_opl):
    # -------------------------------------------------------

    if id_spl == None:
        data_opl['id'] = ''
    elif id_spl == '':
        data_opl['id'] = ''
    elif id_spl == '0':
        data_opl['id'] = ''
    else:
        data_opl['id'] = id_spl
    return data_opl

# ----------------------------------------------------------
class ProList_cl(object):
    # ----------------------------------------------------------

    # -------------------------------------------------------
    def __init__(self):
        # -------------------------------------------------------
        self.db_o = fehlerDatabase_cl()

    # -------------------------------------------------------
    def GET(self, id):
        # -------------------------------------------------------
        retVal_o = {
            'data': None,
            'projekte': None,
            'komponente': None
        }
        self.db_o.readData_p()
        retVal_o['data'] = self.db_o.read_px()


        db_opl = komponenteDatabase_cl()
        db_opl.readData_p()
        retVal_o['komponente'] = db_opl.read_px()

        db_opl = projektDatabase_cl()
        db_opl.readData_p()
        retVal_o['projekte'] = db_opl.read_px()

        return retVal_o

    # -------------------------------------------------------
    def POST(self, data_opl):
        # -------------------------------------------------------
        retVal_o = {
            'id': None
        }

        return retVal_o

    # -------------------------------------------------------
    def PUT(self, data_opl):

        retVal_o = {
            'id': None
        }

        return retVal_o

    # -------------------------------------------------------
    def DELETE(self, id):
        retVal_o = {
            'id': None
        }

        return retVal_o

class KatList_cl(object):
    # ----------------------------------------------------------

    # -------------------------------------------------------
    def __init__(self):
        # -------------------------------------------------------
        self.db_o = fehlerDatabase_cl()

    # -------------------------------------------------------
    def GET(self, id):
        # -------------------------------------------------------
        retVal_o = {
            'data': None,
            'katfehler': None,
            'katursache': None
        }

        self.db_o.readData_p()
        retVal_o['data'] = self.db_o.read_px()


        db_opl = katfehlerDatabase_cl()
        db_opl.readData_p()
        retVal_o['katfehler'] = db_opl.read_px()

        db_opl = katursacheDatabase_cl()
        db_opl.readData_p()
        retVal_o['katursache'] = db_opl.read_px()

        return retVal_o

    # -------------------------------------------------------
    def POST(self, data_opl):
        # -------------------------------------------------------
        retVal_o = {
            'id': None
        }

        return retVal_o

    # -------------------------------------------------------
    def PUT(self, data_opl):

        retVal_o = {
            'id': None
        }

        return retVal_o

    # -------------------------------------------------------
    def DELETE(self, id):
        retVal_o = {
            'id': None
        }

        return retVal_o