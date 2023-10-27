from django import template
from datetime import datetime

register = template.Library()

@register.filter
def mostra_duracao(value1, value2):

    if all ((isinstance(value1, datetime), (isinstance(value2, datetime)))):
        dias = (value1 - value2).days
        texto = 'dias'
        if dias == 1:
            texto = 'dia'
        return f"{dias} {texto}"
    return('Aguardando Devolução')