from django.contrib import admin

from projects.models import Technology,Project


class ProjectAdmin(admin.ModelAdmin):
    pass


class TechnologyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectAdmin)
admin.site.register(Technology, TechnologyAdmin)
