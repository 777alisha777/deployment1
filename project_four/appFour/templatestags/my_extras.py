from django import template

register = template.Library()


def cut(value,arg):
    """

    This cuts out all values of "arg" from the string!

    """
    return value.replace(arg,'')#first argument what you are looking for and second what you wanna replace it with

register.filter('cut', cut)#second argument calls function
