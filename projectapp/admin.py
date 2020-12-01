from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'git_url', 'download_dir_path', 'zip_project', 'build_script_path', 'unzip_project_dir')
    ordering = ['name']


admin.site.register(Project, ProjectAdmin)
