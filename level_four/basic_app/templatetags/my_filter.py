from django import template

register = template.Library()

@register.filter(name = 'cut')
def cut(value,arg):
    ## used to cut out the arg part from the string value ##

    return value.replace(arg,'')
