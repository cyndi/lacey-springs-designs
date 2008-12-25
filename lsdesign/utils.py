from IPython.Shell import IPShellEmbed
from django.conf import settings
from django.template import RequestContext
from django.shortcuts import render_to_response

def nothing():
    pass

ipshell = nothing

if settings.DEBUG:
    try:
        ipshell = IPShellEmbed()
    except:
        pass

def render(template, context, request):
    return render_to_response(template, context, \
            context_instance = RequestContext(request))

