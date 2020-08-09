from django import template
from django.template.defaultfilters import stringfilter

import markdown as md

register = template.Library()


@register.filter()
@stringfilter
def markdown(value):
    return md.markdown(value, extensions=['markdown.extensions.fenced_code'])

@register.filter()
@stringfilter
def markdown_preview(value : str):
    if(len(value) < 400):
        return markdown(value)
    else:
        end_index = value[400:].find('\n') + 400
        return markdown(value[0:end_index] + "\n\n...")