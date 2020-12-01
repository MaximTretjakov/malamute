from django.views.generic import FormView
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse

from authapp.models import CiUser
from projectapp.forms import ProjectUserForm
from projectapp.models import Project


class ProjectPageView(FormView):
    def post(self, request, *args, **kwargs):
        project_form = ProjectUserForm(data=request.POST)
        if project_form.is_valid():
            form = project_form.save(commit=False)
            form.user = request.user
            form.save()
        return HttpResponseRedirect(reverse('projectapp:show'))

    def get(self, request, *args, **kwargs):
        project_form = ProjectUserForm()
        content = {
            'title': 'Ваши проекты',
            'project_form': project_form
        }
        return render(request, 'projectapp/projects.html', content)


class ShowProjectPageView(FormView):
    def get(self, request, *args, **kwargs):
        user = CiUser.objects.get(username=request.user)
        project_data = get_object_or_404(Project, user=user)
        project_form = ProjectUserForm(instance=project_data)
        content = {
            'title': 'Ваши созданные проекты',
            'project_form': project_form
        }
        return render(request, 'projectapp/created.html', content)
