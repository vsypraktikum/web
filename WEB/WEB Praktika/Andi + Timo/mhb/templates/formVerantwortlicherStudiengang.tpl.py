# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1515085284.3771296
_enable_loop = True
_template_filename = '/mnt/607B-88B7/nextCloud/Frika/3. Semester/WEB/Praktikum/Praktikum3/mhb/templates/formVerantwortlicherStudiengang.tpl'
_template_uri = 'formVerantwortlicherStudiengang.tpl'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        data_o = context.get('data_o', UNDEFINED)
        data_lehr = context.get('data_lehr', UNDEFINED)
        data_mod = context.get('data_mod', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<div id="formVerantwortlicherStudiengang">\r\n\t<table style="text-align:center;">\r\n\t<h1>Form Lehrender Studiengang</h1>\r\n\t<br>\r\n\t\t<select id="studiengang" name="studiengang">\r\n\t\t\t<option value="0">Wählen Sie Ihren Studiengang:</option>\r\n')
        for a in data_o.values():
            __M_writer('\t\t\t\t<option value="')
            __M_writer(str(a[1]))
            __M_writer('">')
            __M_writer(str(a[0]))
            __M_writer('</option>\r\n')
        __M_writer('\t\t</select>\r\n\t\t<button id="buttonstud">Studienganginfos und Modulhandbuch anzeigen</button>\r\n\t\t<p />\r\n\t\t<form id="createStudiengang" action="" method="POST">\r\n\t\t\t<button onclick="loadDoccreateStudiengang()">Studiengang Erfassen</button>\r\n\t\t</form> \r\n\t\t<form id="editStudiengang" action="" method="POST">\r\n\t\t\t<button onclick="loadDocstudiengangEdit()">Studiengang Bearbeiten</button>\r\n\t\t</form> \r\n\t\t<button id="buttonstuddelete">Studiengang Löschen</button><br>\r\n\t\t<p />\r\n\t\t<select id="lehr" name="lehr">\r\n\t\t\t<option value="0">Wählen Sie Ihre Lehrveranstaltung aus:</option>\r\n')
        for b in data_lehr.values():
            __M_writer('\t\t\t\t<option value="')
            __M_writer(str(b[0]))
            __M_writer('">')
            __M_writer(str(b[0]))
            __M_writer('</option>\r\n')
        __M_writer('\t\t</select>\r\n\t\t<p />\r\n\t\t<form action="/createLehrveranstaltung" method="POST">\r\n\t\t\t<button type="submit">Lehrveranstaltung Erfassen</button><br>\r\n\t\t</form> \r\n\t\t<button id="buttonlehredit">Lehrveranstaltung Bearbeiten</button><br>\r\n\t\t<button id="buttonlehrdelete">Lehrveranstaltung Löschen</button><br>\r\n\t\t<p />\r\n\t\t<select id="modul" name="modul">\r\n\t\t\t<option value="0">Wählen Sie Ihr Modul aus:</option>\r\n')
        for c in data_mod.values():
            __M_writer('\t\t\t\t<option value="')
            __M_writer(str(c[0]))
            __M_writer('">')
            __M_writer(str(c[0]))
            __M_writer('</option>\r\n')
        __M_writer('\t\t</select>\r\n\t\t<p />\r\n\t\t<form action="/createModul" method="POST">\r\n\t\t\t<button type="submit">Modul Erfassen</button><br>\r\n\t\t</form>\r\n\t\t<button id="buttonmoduledit">Modul Bearbeiten</button><br>\r\n\t\t<button id="buttonmoduldelete">Modul Löschen</button>\r\n\t\t<br>\r\n\t\t<p />\r\n\t\t<form action="/" method="POST">\r\n\t\t\t<button type="submit">Logout</button><br>\r\n\t\t</form> \r\n\t\t<script src="mhb_studiengang.js"></script>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/mnt/607B-88B7/nextCloud/Frika/3. Semester/WEB/Praktikum/Praktikum3/mhb/templates/formVerantwortlicherStudiengang.tpl", "uri": "formVerantwortlicherStudiengang.tpl", "line_map": {"16": 0, "24": 2, "25": 8, "26": 9, "27": 9, "28": 9, "29": 9, "30": 9, "31": 11, "32": 24, "33": 25, "34": 25, "35": 25, "36": 25, "37": 25, "38": 27, "39": 37, "40": 38, "41": 38, "42": 38, "43": 38, "44": 38, "45": 40, "51": 45}, "source_encoding": "utf-8"}
__M_END_METADATA
"""
