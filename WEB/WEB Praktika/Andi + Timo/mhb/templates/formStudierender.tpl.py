# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1513170365.0522199
_enable_loop = True
_template_filename = '/mnt/607B-88B7/Projects/WEBPraktikum2/NEW/mhb/templates/formStudierender.tpl'
_template_uri = 'formStudierender.tpl'
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
        data_o = context.get('data_o', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<body>\r\n\t\t<h1>Form Studierender</h1>\r\n\t\t<br>\t\t\r\n\t\t\t<select id="studiengang" name="studiengang">\r\n\t\t\t\t<option value="0">Wählen Sie Ihren Studiengang:</option>\r\n')
        for a in data_o.values():
            __M_writer('\t\t\t\t\t<option value="')
            __M_writer(str(a[1]))
            __M_writer('">')
            __M_writer(str(a[0]))
            __M_writer('</option>\r\n')
        __M_writer('\t\t\t</select>\r\n\t\t\t<button id = "buttonstud">Studienganginfos und Modulhandbuch anzeigen</button>\r\n\t\t\t<form action="/" method="POST">\r\n\t\t\t\t<button type="submit">Logout</button><br>\r\n\t\t\t</form>\r\n\t\t\t<script src="mhb_student.js"></script>\r\n\t</body>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "formStudierender.tpl", "line_map": {"66": 60, "35": 2, "40": 19, "46": 3, "59": 10, "53": 3, "54": 9, "55": 10, "56": 10, "57": 10, "58": 10, "27": 0, "60": 12}, "filename": "/mnt/607B-88B7/Projects/WEBPraktikum2/NEW/mhb/templates/formStudierender.tpl", "source_encoding": "utf-8"}
__M_END_METADATA
"""
