# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1515084089.4438145
_enable_loop = True
_template_filename = '/mnt/607B-88B7/nextCloud/Frika/3. Semester/WEB/Praktikum/Praktikum3/mhb/templates/loginLehrende.tpl'
_template_uri = 'loginLehrende.tpl'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('<div id="loginL">\r\n\t<form id="loginL" action="" method="POST">\r\n\t\t<input type="text" id="username" name="username" value="" required />\r\n\t\t<input type="password" id="password" name="password" value="" required />\r\n\t\t<button onclick="loadDocLoginL()">Login</button>\r\n\t</form>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/mnt/607B-88B7/nextCloud/Frika/3. Semester/WEB/Praktikum/Praktikum3/mhb/templates/loginLehrende.tpl", "uri": "loginLehrende.tpl", "line_map": {"16": 0, "27": 21, "21": 1}, "source_encoding": "ascii"}
__M_END_METADATA
"""
