
from django import template
register = template.Library()
from ..models import Event

@register.inclusion_tag('news/banner.html')
def show_banner():
    events = Event.objects.order_by('start')
    return {'events': events}
