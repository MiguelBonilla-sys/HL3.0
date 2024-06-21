from django import template

register = template.Library()

@register.filter
def translate_change_type(change_type):
    translations = {
        'ADD': 'Agregar',
        'DELETE': 'Eliminar',
        'UPDATE': 'Actualizado'
    }
    return translations.get(change_type, change_type)