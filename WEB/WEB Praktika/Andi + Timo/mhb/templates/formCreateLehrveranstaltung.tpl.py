# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1513179520.3279192
_enable_loop = True
_template_filename = '/mnt/607B-88B7/Projects/WEBPraktikum2/NEW/mhb/templates/formCreateLehrveranstaltung.tpl'
_template_uri = 'formCreateLehrveranstaltung.tpl'
_source_encoding = 'utf-8'
_exports = ['header']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'layout.tpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def header():
            return render_header(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<body>\r\n\t\t<h1>Create / Edit Studiengang</h1>\r\n\t\t<br>\r\n\t\t<form id="idWTForm" action="/saveLehrveranstaltung" method="POST">\r\n\t\t\t<input type="string" value="$id_s" id="id_s" name="id_s" />\r\n\t\t\t<div>\r\n\t\t\t\t<label for="bezeichnungLehrveranstaltung">Bezeichnung</label>\r\n\t\t\t\t<input type="string" value="$bezeichnungLehrveranstaltung" id="bezeichnungLehrveranstaltung" name="bezeichnungLehrveranstaltung" required />\r\n\t\t\t</div>\r\n\t\t\t<div>\r\n\t\t\t\t<label for="beschreibungLehrveranstaltung">Beschreibung</label>\r\n\t\t\t\t<input type="string" value="$beschreibungLehrveranstaltung" id="beschreibungLehrveranstaltung" name="beschreibungLehrveranstaltung" required />\r\n\t\t\t</div>\r\n\t\t\t<div>\r\n\t\t\t\t<label for="lageLehrveranstaltung">Lage (Semester)</label>\r\n\t\t\t\t<input type="number" value="$lageLehrveranstaltung" id="lageLehrveranstaltung" name="lageLehrveranstaltung" required />\r\n\t\t\t</div>\r\n\t\t\t<div>\r\n\t\t\t\t<label for="modulLehrveranstaltung">Modul</label>\r\n\t\t\t\t<input type="text" value="$modulLehrveranstaltung" id="modulLehrveranstaltung" name="modulLehrveranstaltung" required />\r\n\t\t\t</div>\r\n\t\t\t<div>\r\n\t\t\t\t<label for="studiengangKurzbezeichnung">Studiengang Kurzbezeichnung</label>\r\n\t\t\t\t<input type="text" value="$studiengangKurzbezeichnung" id="studiengangKurzbezeichnung" name="studiengangKurzbezeichnung" required />\r\n\t\t\t</div>\r\n\t\t\t<div>\r\n\t\t\t\t<input type="submit" value="Speichern"/>\r\n\t\t\t\t<input type="reset" value="Go Back" onclick="location.href = \'/lehr\'"/><!-- Abbrechen Button -->\r\n\t\t\t</div>\r\n\t\t</form>\r\n\t</body>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"34": 2, "51": 3, "39": 35, "57": 51, "27": 0, "45": 3}, "uri": "formCreateLehrveranstaltung.tpl", "source_encoding": "utf-8", "filename": "/mnt/607B-88B7/Projects/WEBPraktikum2/NEW/mhb/templates/formCreateLehrveranstaltung.tpl"}
__M_END_METADATA
"""
