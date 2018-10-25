# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1513178954.0201094
_enable_loop = True
_template_filename = '/mnt/607B-88B7/Projects/WEBPraktikum2/NEW/mhb/templates/formVerantwortlicherModul.tpl'
_template_uri = 'formVerantwortlicherModul.tpl'
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
        data_modul = context.get('data_modul', UNDEFINED)
        data_o = context.get('data_o', UNDEFINED)
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
        data_modul = context.get('data_modul', UNDEFINED)
        data_o = context.get('data_o', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<body>\r\n\t\t<table style="text-align:center;">\r\n\t\t<h1>Form Lehrender Modul</h1>\r\n\t\t<br>\r\n\t\t\t<select id="studiengang" name="studiengang">\r\n\t\t\t\t<option value="0">Wählen Sie Ihren Studiengang:</option>\r\n')
        for a in data_o.values():
            __M_writer('\t\t\t\t\t<option value="')
            __M_writer(str(a[1]))
            __M_writer('">')
            __M_writer(str(a[0]))
            __M_writer('</option>\r\n')
        __M_writer('\t\t\t</select>\r\n\t\t\t<button id = "buttonstud">Studienganginfos und Modulhandbuch anzeigen</button>\r\n\t\t\t<p />\r\n\t\t\t<select id="modul" name="modul">\r\n\t\t\t\t<option value="0">Wählen Sie Ihr Modul aus:</option>\r\n')
        for b in data_modul.values():
            __M_writer('\t\t\t\t\t<option value="')
            __M_writer(str(b[0]))
            __M_writer('">')
            __M_writer(str(b[0]))
            __M_writer('</option>\r\n')
        __M_writer('\t\t\t</select><br>\r\n\t\t\t<button id="buttonmoduledit">Modul Bearbeiten</button><br>\r\n\t\t\t<p />\r\n\t\t\t<form action="/" method="POST">\r\n\t\t\t\t<button type="submit">Logout</button><br>\r\n\t\t\t</form>\r\n\t\t\t<script src="mhb_modul.js"></script>\r\n\t</body>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 19, "65": 19, "66": 19, "27": 0, "36": 2, "69": 21, "68": 19, "41": 29, "75": 69, "47": 3, "67": 19, "55": 3, "56": 10, "57": 11, "58": 11, "59": 11, "60": 11, "61": 11, "62": 13, "63": 18}, "uri": "formVerantwortlicherModul.tpl", "filename": "/mnt/607B-88B7/Projects/WEBPraktikum2/NEW/mhb/templates/formVerantwortlicherModul.tpl", "source_encoding": "utf-8"}
__M_END_METADATA
"""
