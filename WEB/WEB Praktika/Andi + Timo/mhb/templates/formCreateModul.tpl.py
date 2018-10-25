# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1513179769.799057
_enable_loop = True
_template_filename = '/mnt/607B-88B7/Projects/WEBPraktikum2/NEW/mhb/templates/formCreateModul.tpl'
_template_uri = 'formCreateModul.tpl'
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
        __M_writer('\r\n    <body>\r\n\t\t<h1>Create / Edit Modul</h1>\r\n\t\t<br>\r\n\t\t<form id="idWTForm" action="/saveModul" method="POST">\r\n\t\t\t<input type="string" value="$studiengangID" id="studiengangID" name="studiengangID" />\r\n\t\t\t<div>\r\n\t\t\t\t<label for="bezeichnungModul">Modul Bezeichnung</label>\r\n\t\t\t\t<input type="string" value="$bezeichnungModul" id="bezeichnungModul" name="bezeichnungModul" required />\r\n\t\t\t</div>\r\n\t\t\t<div>\r\n\t\t\t\t<label for="beschreibungModul">Beschreibung</label>\r\n\t\t\t\t<input type="text" value="$beschreibungModul" id="beschreibungModul" name="beschreibungModul" required />\r\n\t\t\t</div>\r\n\t\t\t<div>\r\n\t\t\t\t<label for="anzahlCredits">Anzahl Kreditpunkte</label>\r\n\t\t\t\t<input type="number" value="$anzahlCredits" id="anzahlCredits" name="anzahlCredits" required />\r\n\t\t\t</div>\r\n\t\t\t<div>\r\n\t\t\t\t<label for="anzahlVorlesung">Anzahl SWS-Vorlesung</label>\r\n\t\t\t\t<input type="number" value="$anzahlVorlesung" id="anzahlVorlesung" name="anzahlVorlesung" required />\r\n\t\t\t</div>\r\n\t\t\t<div>\r\n\t\t\t\t<label for="anzahlUebung">Anzahl SWS-Übung</label>\r\n\t\t\t\t<input type="number" value="$anzahlUebung" id="anzahlUebung" name="anzahlUebung" required />\r\n\t\t\t</div>\r\n\t\t\t<div>\r\n\t\t\t\t<label for="anzahlPraktika">Anzahl SWS-Praktikum</label>\r\n\t\t\t\t<input type="number" value="$anzahlPraktika" id="anzahlPraktika" name="anzahlPraktika" required />\r\n\t\t\t</div>\r\n\t\t\t<div>\r\n\t\t\t\t<label for="voraussetzungen">Voraussetzungen</label>\r\n\t\t\t\t<input type="text" value="$voraussetzungen" id="voraussetzungen" name="voraussetzungen"/>\r\n\t\t\t</div>\r\n\t\t\t<div>\r\n\t\t\t\t<label for="modulVerantwortlicher">Modulverantwortlicher</label>\r\n\t\t\t\t<input type="string" value="$modulVerantwortlicher" id="modulVerantwortlicher" name="modulVerantwortlicher"/>\r\n\t\t\t</div>\r\n\t\t\t<div>\r\n\t\t\t\t<label for="studiengangKurzbezeichnung">Studiengang Kurzbezeichnung</label>\r\n\t\t\t\t<input type="string" value="$studiengangKurzbezeichnung" id="studiengangKurzbezeichnung" name="studiengangKurzbezeichnung"/>\r\n\t\t\t</div>\r\n\t\t\t<div>\r\n\t\t\t\t<input type="submit" value="Speichern"/>\r\n\t\t\t\t<input type="reset" value="Go Back" onclick="location.href = \'/lehr\'"/><!-- Abbrechen Button -->\r\n\t\t\t</div>\r\n\t\t</form>\r\n\t</body>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"34": 2, "51": 3, "39": 51, "57": 51, "27": 0, "45": 3}, "uri": "formCreateModul.tpl", "source_encoding": "utf-8", "filename": "/mnt/607B-88B7/Projects/WEBPraktikum2/NEW/mhb/templates/formCreateModul.tpl"}
__M_END_METADATA
"""
