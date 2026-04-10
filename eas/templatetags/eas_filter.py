from django import template


register = template.Library()


@register.filter
def sub(value, arg):
    return value - arg

from django.utils.safestring import mark_safe
import re


@register.filter
def highlight(text, keyword):
    if text is None:
        return ""

    text = str(text)
    keyword = (keyword or "").strip()

    if not keyword:
        return text

    pattern = re.compile(re.escape(keyword), re.IGNORECASE)
    highlighted = pattern.sub(lambda m: f"<mark>{m.group(0)}</mark>", text)
    return mark_safe(highlighted)