from django import template
register = template.Library()

def first_3_upper(value):
    result = value[:3].upper()
    return result + value[3:]

def last_3_upper(value):
    result = value[-3:].upper()
    return value[:-3]+result


register.filter('f3upper', first_3_upper)
register.filter('l3upper', last_3_upper)