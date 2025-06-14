# store/templatetags/filters.py
from django import template

register = template.Library()

@register.filter
def usd_to_vnd(value, rate=25000):
    try:
        vnd = float(value) * rate
        return "{:,.0f}₫".format(vnd).replace(",", ".")
    except:
        return ""
