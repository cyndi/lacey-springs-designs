from django.contrib import admin

from lsdesign.portfolio.models import *

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Client)
admin.site.register(Medium)
admin.site.register(Project, ProjectAdmin)
