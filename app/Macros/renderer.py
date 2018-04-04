from mako.template import Template
from .Macros import Macros


def render(jsondata):
    template = Template(jsondata)
    return template.render(macros=Macros())
