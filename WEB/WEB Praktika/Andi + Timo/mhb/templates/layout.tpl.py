# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1515077945.9251614
_enable_loop = True
_template_filename = '/mnt/607B-88B7/nextCloud/Frika/3. Semester/WEB/Praktikum/Praktikum3/mhb/templates/layout.tpl'
_template_uri = 'layout.tpl'
_source_encoding = 'utf-8'
_exports = ['header']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def header():
            return render_header(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html>\r\n<head>\r\n  <link href="/mhb.css" rel="stylesheet">\r\n</head>\r\n<body>\r\n\t<div class="topnav">\r\n\t\tWebanwendung "Modulhandbuch (mhb)"\r\n\t\t<br>\r\n\t</div>\r\n\t<div class="content">\r\n\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\r\n\t</div>\r\n</body>\r\n<script src="ajax.js"></script>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 0, "34": 13, "28": 13, "45": 34, "23": 2}, "filename": "/mnt/607B-88B7/nextCloud/Frika/3. Semester/WEB/Praktikum/Praktikum3/mhb/templates/layout.tpl", "uri": "layout.tpl"}
__M_END_METADATA
"""
