from django import template
from django.template.defaultfilters import stringfilter
import markdown as md

register = template.Library()

@register.filter()
def multiply(value, arg):
    
    return "{:.2f}".format(value * arg)
    #usage {{ quantity | multiply:price }}

@register.filter()
def removeDollar(value):
    
    return float( value[1:])

@register.filter()
def procent(value, maxValue):
    
    return 50 * value / maxValue
    # max value is 50%, so the div will have a width of 50%

@register.filter()
@stringfilter
def markdown(value):
    return md.markdown(value, extensions=['markdown.extensions.fenced_code'])