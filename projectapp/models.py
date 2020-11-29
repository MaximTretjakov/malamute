from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100, blank=False, default='No data provided')
    git_url = models.CharField(max_length=255, blank=False, default='No data provided')
    download_dir_path = models.CharField(max_length=255, blank=False, default='No data provided')
    zip_project = models.CharField(max_length=255, blank=False, default='No data provided')
    build_script_path = models.CharField(max_length=255, blank=False, default='No data provided')
    unzip_project_dir = models.CharField(max_length=255, blank=False, default='No data provided')

