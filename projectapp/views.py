from django.views.generic import FormView
from django.shortcuts import render, HttpResponseRedirect
from projectapp.forms import ProjectUserForm
from django.urls import reverse


class ProjectPageView(FormView):
    def post(self, request, *args, **kwargs):
        """
        запилить создание проекта
        """
        project_form = ProjectUserForm(data=request.POST)
        if project_form.is_valid():
            project_form.save()
        return HttpResponseRedirect(reverse('projectapp:main'))

    def get(self, request, *args, **kwargs):
        """
        запилить отдачу проектов если существуют,
        если нет выводить запись что проектов нет и ссылку создать проект
        """
        project_form = ProjectUserForm(data=request.POST)
        content = {'title': 'Ваши проекты', 'project_form': project_form}
        return render(request, 'projectapp/projects.html', content)
