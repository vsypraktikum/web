# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1513169886.1454463
_enable_loop = True
_template_filename = '/mnt/607B-88B7/Projects/WEBPraktikum2/NEW/mhb/templates/formStudiengang.tpl'
_template_uri = 'formStudiengang.tpl'
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
        id_s = context.get('id_s', UNDEFINED)
        data_lehr = context.get('data_lehr', UNDEFINED)
        data_o = context.get('data_o', UNDEFINED)
        data_mod = context.get('data_mod', UNDEFINED)
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
        id_s = context.get('id_s', UNDEFINED)
        data_lehr = context.get('data_lehr', UNDEFINED)
        data_o = context.get('data_o', UNDEFINED)
        data_mod = context.get('data_mod', UNDEFINED)
        def header():
            return render_header(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<body>\t\t\r\n\t\t<h1><u>Informationen zum Studiengang:</u> ')
        __M_writer(str(id_s))
        __M_writer('</h1>\r\n\t\t<table id="studInfos">\r\n\t\t\t<tr>\r\n\t\t\t\t<th>Bezeichnung des Studiengangs</th>\r\n\t\t\t\t<th>Kurzbezeichnung des Studiengangs</th>\r\n\t\t\t\t<th>Beschreibung des Studiengangs</th>\r\n\t\t\t\t<th>Anzahl der Semester des Studiengangs</th>\r\n\t\t\t\t<tr>\r\n')
        for a in data_o.values():
            if a[1] == id_s:
                __M_writer('\t\t\t\t\t\t\t\t<td>')
                __M_writer(str(a[0]))
                __M_writer('</td>\r\n\t\t\t\t\t\t\t\t<td>')
                __M_writer(str(a[1]))
                __M_writer('</td>\r\n\t\t\t\t\t\t\t\t<td>')
                __M_writer(str(a[2]))
                __M_writer('</td>\r\n\t\t\t\t\t\t\t\t<td>')
                __M_writer(str(a[3]))
                __M_writer('</td>\r\n\t\t\t\t\t\t\t\t</tr>\r\n')
        __M_writer('\t\t\t</tr>\r\n\t\t</table>\r\n\t\t<h1><u>Modulhandbuch:</u> ')
        __M_writer(str(id_s))
        __M_writer('</h1>\r\n\t\t<table id="modInfos">\r\n\t\t\t<tr>\r\n\t\t\t\t<th>Bezeichnung</th>\r\n\t\t\t\t<th>Beschreibung</th>\r\n\t\t\t\t<th>Kreditpunkte</th>\r\n\t\t\t\t<th>Anzahl Vorlesung</th>\r\n\t\t\t\t<th>Anzahl Übung</th>\r\n\t\t\t\t<th>Anzahl Praktikum</th>\r\n\t\t\t\t<th>Voraussetzungen</th>\r\n\t\t\t\t<th>Modulverantwortlicher</th>\r\n\t\t\t\t<tr>\r\n')
        for b in data_mod.values():
            if b[8] == id_s:
                __M_writer('\t\t\t\t\t\t\t<td>')
                __M_writer(str(b[0]))
                __M_writer('</td>\r\n\t\t\t\t\t\t\t<td>')
                __M_writer(str(b[1]))
                __M_writer('</td>\r\n\t\t\t\t\t\t\t<td>')
                __M_writer(str(b[2]))
                __M_writer('</td>\r\n\t\t\t\t\t\t\t<td>')
                __M_writer(str(b[3]))
                __M_writer('</td>\r\n\t\t\t\t\t\t\t<td>')
                __M_writer(str(b[4]))
                __M_writer('</td>\r\n\t\t\t\t\t\t\t<td>')
                __M_writer(str(b[5]))
                __M_writer('</td>\r\n\t\t\t\t\t\t\t<td>')
                __M_writer(str(b[6]))
                __M_writer('</td>\r\n\t\t\t\t\t\t\t<td>')
                __M_writer(str(b[7]))
                __M_writer('</td>\r\n\t\t\t\t\t\t\t</tr>\r\n')
        __M_writer('\t\t\t</tr>\r\n\t\t</table>\r\n\t\t<h1><u>Lehrveranstaltungen:</u> ')
        __M_writer(str(id_s))
        __M_writer('</h1>\r\n\t\t<table id="modInfos">\r\n\t\t\t<tr>\r\n\t\t\t\t<th>Bezeichnung</th>\r\n\t\t\t\t<th>Kurzbezeichnung</th>\r\n\t\t\t\t<th>Lage (Semester)</th>\r\n\t\t\t\t<th>Modul</th>\r\n\t\t\t\t<tr>\r\n')
        for c in data_lehr.values():
            if c[4] == id_s:
                __M_writer('\t\t\t\t\t\t\t<td>')
                __M_writer(str(c[0]))
                __M_writer('</td>\r\n\t\t\t\t\t\t\t<td>')
                __M_writer(str(c[1]))
                __M_writer('</td>\r\n\t\t\t\t\t\t\t<td>')
                __M_writer(str(c[2]))
                __M_writer('</td>\r\n\t\t\t\t\t\t\t<td>')
                __M_writer(str(c[3]))
                __M_writer('</td>\r\n\t\t\t\t\t\t\t</tr>\r\n')
        __M_writer('\t\t\t</tr>\r\n\t\t</table>\r\n\t\t<div>\r\n\t\t\t<p />\r\n\t\t\t<input type="reset" value="Logout" onclick="location.href = \'/\'"/><p />\r\n\t\t\t<button onclick="goBack()">Go Back</button>\r\n\t\t</div>\r\n\t\t<script>\r\n\t\tfunction goBack() {\r\n\t\t\twindow.history.back();\r\n\t\t}\r\n\t\t</script>\r\n\t</body>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "formStudiengang.tpl", "line_map": {"27": 0, "38": 2, "43": 81, "49": 3, "59": 3, "60": 5, "61": 5, "62": 13, "63": 14, "64": 15, "65": 15, "66": 15, "67": 16, "68": 16, "69": 17, "70": 17, "71": 18, "72": 18, "73": 22, "74": 24, "75": 24, "76": 36, "77": 37, "78": 38, "79": 38, "80": 38, "81": 39, "82": 39, "83": 40, "84": 40, "85": 41, "86": 41, "87": 42, "88": 42, "89": 43, "90": 43, "91": 44, "92": 44, "93": 45, "94": 45, "95": 49, "96": 51, "97": 51, "98": 59, "99": 60, "100": 61, "101": 61, "102": 61, "103": 62, "104": 62, "105": 63, "106": 63, "107": 64, "108": 64, "109": 68, "115": 109}, "filename": "/mnt/607B-88B7/Projects/WEBPraktikum2/NEW/mhb/templates/formStudiengang.tpl", "source_encoding": "utf-8"}
__M_END_METADATA
"""
