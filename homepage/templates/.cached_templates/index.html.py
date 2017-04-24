# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1493006081.1696875
_enable_loop = True
_template_filename = 'C:/Users/camer/practice/practice/homepage/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['content']


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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        csrf_input = context.get('csrf_input', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        quotes = context.get('quotes', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        csrf_input = context.get('csrf_input', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        quotes = context.get('quotes', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n\n<!--   <div class="input-group" style="text-align: center" >\n      <input type="text" class="form-control" id="search-input" placeholder="Search for...">\n      <span class="input-group-btn" style="width: 1px">\n        <button class="btn btn-default" id="search-button" style="width: 60px;" type="button">Search</button>\n      </span>\n    </div> -->\n<!-- <form style="text-align: center;" action="/homepage/index/">\n\t<div class="form-group">\n\t\t<input class="form-control" type="text" id="search" name="user_search" />\n\t</div>\n\t<button type="submit">Search</button>\n</form> -->\n\n<form action="" method="post">\n\t')
        __M_writer(str( csrf_input ))
        __M_writer('\n\t')
        __M_writer(str( form.as_table() ))
        __M_writer('\n\t<button type="submit"> Search </button>\n</form>\n\n\n<br>\n<br>\n')
        if quotes:
            __M_writer('\t<table>\n\t\t<tr>\n\t\t\t<th>ID</th>\n\t\t\t<th>Author</th>\n\t\t\t<th>Quote</th>\n\t\t\t<th>Tags</th>\n\t\t</tr>\n')
            for q in quotes:
                __M_writer('\t\t<tr>\n\n\t\t\t<td>')
                __M_writer(str(q.id))
                __M_writer('</td>\n\t\t\t<td>')
                __M_writer(str(q.author))
                __M_writer('</td>\n\t\t\t<td style="font-style: italic ">\'')
                __M_writer(str(q.quote))
                __M_writer("'</td>\n\t\t\t<td>")
                __M_writer(str(q.tags))
                __M_writer('</td>\n\t\t</tr>\n')
            __M_writer('\t</table>\n')
        else:
            __M_writer('<div style="text-align: center">\n\tSorry no results, try again.\n\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/camer/practice/practice/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"28": 0, "38": 1, "48": 3, "57": 3, "58": 20, "59": 20, "60": 21, "61": 21, "62": 28, "63": 29, "64": 36, "65": 37, "66": 39, "67": 39, "68": 40, "69": 40, "70": 41, "71": 41, "72": 42, "73": 42, "74": 45, "75": 46, "76": 47, "82": 76}}
__M_END_METADATA
"""
