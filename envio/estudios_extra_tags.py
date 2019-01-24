from django import template

register = template.Library()

# Custom tag for diagnostics
@register.simple_tag(name='debug_object_dump')
def debug_object_dump(var):
    return "hola"