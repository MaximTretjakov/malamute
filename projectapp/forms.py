from django import forms
from projectapp.models import Project


class ProjectUserForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
