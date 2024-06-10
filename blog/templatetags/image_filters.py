from django import template
from django.utils.safestring import mark_safe

"""
Creamos una instancia del objeto Library que es un registro de etiquetas y filtros disponibles 
para su uso en plantillas
"""
register = template.Library()
"""
Aquí definimos un filtro personalizado llamado 'to_image'. 
Los filtros en Django son funciones que toman uno o dos argumentos:
 - El valor que se va a filtrar y un argumento opcional. 
 - Estos filtros se pueden usar en las plantillas de Django.
"""
@register.filter
def to_image(value):
    """
    Este filtro toma un valor, lo concatena con una cadena para formar una URL de imagen base64 y luego lo marca como seguro.
    mark_safe es una función de Django que se utiliza para marcar una cadena como segura para su uso en HTML.
    Esto significa que Django no escapará automáticamente caracteres HTML en esta cadena.
    """
    return mark_safe(f'data:image/png;base64,{value}')