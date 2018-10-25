# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1515082762.6377637
_enable_loop = True
_template_filename = '/mnt/607B-88B7/nextCloud/Frika/3. Semester/WEB/Praktikum/Praktikum3/mhb/templates/loginStudierende.tpl'
_template_uri = 'loginStudierende.tpl'
_source_encoding = 'ascii'
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
        __M_writer('\r\n\t<body>\r\n\t\t<div id="login">\r\n\t\t\t<form id="formlogin" action="" method="POST">\r\n\t\t\t\t<input type="text" id="username" name="username" value="" required />\r\n\t\t\t\t<button onclick="loadDocLogin()">Login</button>\r\n\t\t\t</form>\r\n\t\t</div>\r\n\t</body>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"34": 1, "51": 2, "39": 11, "57": 51, "27": 0, "45": 2}, "source_encoding": "ascii", "uri": "loginStudierende.tpl", "filename": "/mnt/607B-88B7/nextCloud/Frika/3. Semester/WEB/Praktikum/Praktikum3/mhb/templates/loginStudierende.tpl"}
__M_END_METADATA
"""
