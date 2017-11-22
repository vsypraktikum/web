import json

import cherrypy

from .database import fehlerDatabase_cl, katursacheDatabase_cl, katfehlerDatabase_cl, komponenteDatabase_cl, qsmitarbeiterDatabase_cl, swentwicklerDatabase_cl

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
class Fehler_cl(object):
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
            'komp': None,
            'katfehler': None,
            'katursache': None,
            'qsmitarbeiter': None,
            'swentwickler': None
        }
        if id == None:
            # Anforderung der Liste
            retVal_o['data'] = self.db_o.read_px()

        elif id == 'behoben':
            retVal_o['data'] = {}
            data_opl = self.db_o.read_px()
            #Füllen mit den Datensätzen die mit 'behoben' markiert sind
            for key in data_opl:
                if data_opl[key]['status'] == 'behoben':
                    retVal_o['data'].update({key: ''})
                    retVal_o['data'][key] = data_opl[key]

        elif id == 'erkannt':
            retVal_o['data'] = {}
            data_opl = self.db_o.read_px()
            # Füllen mit den Datensätzen die mit 'erfasst' markiert sind
            for key in data_opl:
                if data_opl[key]['status'] == 'erkannt':
                    retVal_o['data'].update({key: ''})
                    retVal_o['data'][key] = data_opl[key]

        else:
            # Anforderung eines Dokuments
            data_o = self.db_o.read_px(id)
            if data_o != None:
                retVal_o['data'] = adjustId_p(id, data_o)

            db_opl = komponenteDatabase_cl()
            retVal_o['komp'] = db_opl.read_px()

            db_opl = katfehlerDatabase_cl()
            retVal_o['katfehler'] = db_opl.read_px()

            db_opl = katursacheDatabase_cl()
            retVal_o['katursache'] = db_opl.read_px()

            db_opl = qsmitarbeiterDatabase_cl()
            retVal_o['qsmitarbeiter'] = db_opl.read_px()

            db_opl = swentwicklerDatabase_cl()
            retVal_o['swentwickler'] = db_opl.read_px()

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
            'kompid': data_opl['kompid_s'],
            'status': data_opl['status_s'],
            'zustand': data_opl['zustand_s'],
            'bug': {
                'beschreibung': data_opl['bugbeschreibung_s'],
                'katid': data_opl['bugkatid_s'],
                'datum': data_opl['bugdatum_s'],
                'empid': data_opl['bugempid_s']
            },
            'fix': {
                'beschreibung': data_opl['fixbeschreibung_s'],
                'katid': data_opl['fixkatid_s'],
                'datum': data_opl['fixdatum_s'],
                'empid': data_opl['fixempid_s']
            }
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
            'kompid': data_opl['kompid_s'],
            'status': data_opl['status_s'],
            'zustand': data_opl['zustand_s'],
            'bug': {
                'beschreibung': data_opl['bugbeschreibung_s'],
                'katid': data_opl['bugkatid_s'],
                'datum': data_opl['bugdatum_s'],
                'empid': data_opl['bugempid_s']
            },
            'fix': {
                'beschreibung': data_opl['fixbeschreibung_s'],
                'katid': data_opl['fixkatid_s'],
                'datum': data_opl['fixdatum_s'],
                'empid': data_opl['fixempid_s']
            }
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