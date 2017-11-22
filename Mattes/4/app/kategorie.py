import json

import cherrypy

from .database import katfehlerDatabase_cl, katursacheDatabase_cl

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
class KatUrsache_cl(object):
    # ----------------------------------------------------------

    # -------------------------------------------------------
    def __init__(self):
        # -------------------------------------------------------
        self.db_o = katursacheDatabase_cl()

    # -------------------------------------------------------
    def GET(self, id):
        # -------------------------------------------------------
        retVal_o = {
            'data': None,
        }
        if id == None:
            # Anforderung der Liste
            retVal_o['data'] = self.db_o.read_px()
        else:
            # Anforderung eines Dokuments
            data_o = self.db_o.read_px(id)
            if data_o != None:
                retVal_o['data'] = adjustId_p(id, data_o)

        return retVal_o

    # -------------------------------------------------------
    def POST(self, data_opl):
        # -------------------------------------------------------
        retVal_o = {
            'id': None
        }

        # data_opl: Dictionary mit den gelieferten key-value-Paaren

        # hier müsste man prüfen, ob die Daten korrekt vorliegen!
        id_s = data_opl["id_s"]
        data_o = {
            'title': data_opl["title_s"],
            'reference': data_opl["reference_s"]
        }
        # Create-Operation
        if self.db_o.update_px(id_s, data_o):
            retVal_o['id'] = id_s
        else:
            retVal_o['id'] = None

        return retVal_o

    # -------------------------------------------------------
    def PUT(self, data_opl):
        # -------------------------------------------------------
        # Sichern der Daten: jetzt wird keine vollständige Seite
        # zurückgeliefert, sondern nur noch die Information, ob das
        # Speichern erfolgreich war

        retVal_o = {
            'id': None
        }

        # data_opl: Dictionary mit den gelieferten key-value-Paaren
        # hier müsste man prüfen, ob die Daten korrekt vorliegen!



        data_o = {
            'title': data_opl["title_s"],
            'reference': data_opl["reference_s"]
        }
        # Update-Operation

        retVal_o['id'] = self.db_o.create_px(data_o)

        return retVal_o

    # -------------------------------------------------------
    def DELETE(self, id):
        # -------------------------------------------------------
        # Eintrag löschen, nur noch Rückmeldung liefern
        retVal_o = {
            'id': id
        }

        if self.db_o.delete_px(id):
            pass
        else:
            retVal_o['id'] = None

        return retVal_o

# ----------------------------------------------------------
class KatFehler_cl(object):
    # ----------------------------------------------------------

    # -------------------------------------------------------
    def __init__(self):
        # -------------------------------------------------------
        self.db_o = katfehlerDatabase_cl()

    # -------------------------------------------------------
    def GET(self, id):
        # -------------------------------------------------------
        retVal_o = {
            'data': None,
        }
        if id == None:
            # Anforderung der Liste
            retVal_o['data'] = self.db_o.read_px()
        else:
            # Anforderung eines Dokuments
            data_o = self.db_o.read_px(id)
            if data_o != None:
                retVal_o['data'] = adjustId_p(id, data_o)

        return retVal_o

    # -------------------------------------------------------
    def POST(self, data_opl):
        # -------------------------------------------------------
        retVal_o = {
            'id': None
        }

        # data_opl: Dictionary mit den gelieferten key-value-Paaren

        # hier müsste man prüfen, ob die Daten korrekt vorliegen!
        id_s = data_opl["id_s"]
        data_o = {
            'title': data_opl["title_s"],
            'reference': data_opl["reference_s"]
        }
        # Create-Operation
        if self.db_o.update_px(id_s, data_o):
            retVal_o['id'] = id_s
        else:
            retVal_o['id'] = None

        return retVal_o

    # -------------------------------------------------------
    def PUT(self, data_opl):
        # -------------------------------------------------------
        # Sichern der Daten: jetzt wird keine vollständige Seite
        # zurückgeliefert, sondern nur noch die Information, ob das
        # Speichern erfolgreich war

        retVal_o = {
            'id': None
        }

        # data_opl: Dictionary mit den gelieferten key-value-Paaren
        # hier müsste man prüfen, ob die Daten korrekt vorliegen!



        data_o = {
            'title': data_opl["title_s"],
            'reference': data_opl["reference_s"]
        }
        # Update-Operation

        retVal_o['id'] = self.db_o.create_px(data_o)

        return retVal_o

    # -------------------------------------------------------
    def DELETE(self, id):
        # -------------------------------------------------------
        # Eintrag löschen, nur noch Rückmeldung liefern
        retVal_o = {
            'id': id
        }

        if self.db_o.delete_px(id):
            pass
        else:
            retVal_o['id'] = None

        return retVal_o