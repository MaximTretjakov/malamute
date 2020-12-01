from django.db import models

from authapp.models import CiUser


class Project(models.Model):
    user = models.OneToOneField(CiUser, null=False, primary_key=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False, default='No data provided')
    git_url = models.CharField(max_length=255, blank=False, default='No data provided')
    download_dir_path = models.CharField(max_length=255, blank=False, default='No data provided')
    zip_project = models.CharField(max_length=255, blank=False, default='No data provided')
    build_script_path = models.CharField(max_length=255, blank=False, default='No data provided')
    unzip_project_dir = models.CharField(max_length=255, blank=False, default='No data provided')

