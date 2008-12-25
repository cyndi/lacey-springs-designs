from django.conf.urls.defaults import *

from lsdesign.portfolio.models import Project

info_dict = {
    'queryset': Project.objects.all()
}

urlpatterns = patterns('',
    #url(r'^work/',
    #    view,
    #    name = "testURL"

    url('^$',
        'django.views.generic.list_detail.object_list',
        dict(info_dict), 
        name = "work_root"),

    url('^(?P<slug>[-\w]+)/$',
        'django.views.generic.date_based.object_detail',
        dict(info_dict, slug_field='slug'),
        name = "work_detail"),
)
