from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^lsdesign/', include('lsdesign.foo.urls')),
    url(r'^$',
        'django.views.generic.simple.direct_to_template',
        {'template': 'homepage.html'}),

    (r'^work/', include('lsdesign.portfolio.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
)

if getattr(settings, 'SERVE_STATIC_MEDIA', False):
    urlpatterns += patterns('django.views.static',
        (r'^%s(?P<path>.*)' % settings.MEDIA_URL, 'serve',
            {'document_root': settings.MEDIA_ROOT}),
    )

