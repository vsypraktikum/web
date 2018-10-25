# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1515085292.3837419
_enable_loop = True
_template_filename = '/mnt/607B-88B7/nextCloud/Frika/3. Semester/WEB/Praktikum/Praktikum3/mhb/templates/formCreateStudiengang.tpl'
_template_uri = 'formCreateStudiengang.tpl'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('<div id="createStudiengang">\r\n\t\t<h1>Create / Edit Studiengang</h1>\r\n\t\t<br>\r\n\t\t<form id="idWTForm" action="/saveStudiengang" method="POST">\r\n\t\t\t<input type="string" value="$id_s" id="id_s" name="id_s" />\r\n\t\t\t<div>\r\n\t\t\t\t<label for="bezeichnungStudiengang">Bezeichnung</label>\r\n\t\t\t\t<input type="string" value="$bezeichnungStudiengang" id="bezeichnungStudiengang" name="bezeichnungStudiengang" required />\r\n\t\t\t</div>\r\n\t\t\t<div>\r\n\t\t\t\t<label for="kurzbezeichnungStudiengang">Kurzbezeichnung</label>\r\n\t\t\t\t<input type="string" value="$kurzbezeichnungStudiengang" id="kurzbezeichnungStudiengang" name="kurzbezeichnungStudiengang" required />\r\n\t\t\t</div>\r\n\t\t\t<div>\r\n\t\t\t\t<label for="beschreibungStudiengang">Beschreibung</label>\r\n\t\t\t\t<input type="text" value="$beschreibungStudiengang" id="beschreibungStudiengang" name="beschreibungStudiengang" required />\r\n\t\t\t</div>\r\n\t\t\t<div>\r\n\t\t\t\t<label for="semesteranzahlStudiengang">Semesteranzahl</label>\r\n\t\t\t\t<input type="number" value="$semesteranzahlStudiengang" id="semesteranzahlStudiengang" name="semesteranzahlStudiengang" required />\r\n\t\t\t</div>\r\n\t\t\t<div>\r\n\t\t\t\t<input type="submit" value="Speichern"/>\r\n\t\t\t\t<input type="reset" value="Go Back" onclick="location.href = \'/lehr\'"/>\r\n\t\t\t</div>\r\n\t\t</form>\r\n</div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/mnt/607B-88B7/nextCloud/Frika/3. Semester/WEB/Praktikum/Praktikum3/mhb/templates/formCreateStudiengang.tpl", "uri": "formCreateStudiengang.tpl", "line_map": {"16": 0, "27": 21, "21": 2}, "source_encoding": "utf-8"}
__M_END_METADATA
"""
