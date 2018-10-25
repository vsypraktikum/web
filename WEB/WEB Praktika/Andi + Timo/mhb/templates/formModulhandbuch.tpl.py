# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1513170036.3620503
_enable_loop = True
_template_filename = '/mnt/607B-88B7/Projects/WEBPraktikum2/NEW/mhb/templates/formModulhandbuch.tpl'
_template_uri = 'formModulhandbuch.tpl'
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
        def header():
            return render_header(context._locals(__M_locals))
        data_mod = context.get('data_mod', UNDEFINED)
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
        def header():
            return render_header(context)
        data_mod = context.get('data_mod', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<body>\r\n\t\t<h1><u>Modulhandbuch zum Studiengang:</u> ')
        __M_writer(str(id_s))
        __M_writer('</h1>\r\n\t\t<div>\r\n')
        for a in data_mod.values():
            if a[8] == id_s:
                __M_writer('\t\t\t\t\t<u>Bezeichnung des Moduls:</u> <p /> ')
                __M_writer(str(a[0]))
                __M_writer(' <p />\r\n\t\t\t\t\t<u>Beschreibung des Moduls:</u> <p /> ')
                __M_writer(str(a[1]))
                __M_writer(' <p />\r\n\t\t\t\t\t<u>Anzahl Kreditpunkte:</u> <p /> ')
                __M_writer(str(a[2]))
                __M_writer(' <p />\r\n\t\t\t\t\t<u>Anzahl Vorlesung:</u> <p /> ')
                __M_writer(str(a[3]))
                __M_writer(' <p />\r\n\t\t\t\t\t<u>Anzahl Übung:</u> <p /> ')
                __M_writer(str(a[4]))
                __M_writer(' <p />\r\n\t\t\t\t\t<u>Anzahl Praktikum:</u> <p /> ')
                __M_writer(str(a[5]))
                __M_writer(' <p />\r\n\t\t\t\t\t<u>Voraussetzungen:</u> <p /> ')
                __M_writer(str(a[6]))
                __M_writer(' <p />\r\n\t\t\t\t\t<u>Modulverantwortlicher</u> <p /> ')
                __M_writer(str(a[7]))
                __M_writer(' <p />\r\n')
        __M_writer('\t\t</div>\r\n\t</body>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "formModulhandbuch.tpl", "source_encoding": "utf-8", "line_map": {"64": 10, "65": 11, "66": 11, "67": 12, "68": 12, "69": 13, "70": 13, "71": 14, "72": 14, "73": 15, "74": 15, "75": 16, "76": 16, "77": 19, "83": 77, "27": 0, "36": 2, "41": 21, "47": 3, "55": 3, "56": 5, "57": 5, "58": 7, "59": 8, "60": 9, "61": 9, "62": 9, "63": 10}, "filename": "/mnt/607B-88B7/Projects/WEBPraktikum2/NEW/mhb/templates/formModulhandbuch.tpl"}
__M_END_METADATA
"""
