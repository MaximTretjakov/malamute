from django import forms
from projectapp.models import Project


class ProjectUserForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = (
            'name',
            'git_url',
            'download_dir_path',
            'zip_project',
            'build_script_path',
            'unzip_project_dir',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
