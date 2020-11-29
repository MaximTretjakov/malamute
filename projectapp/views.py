from django.views.generic import FormView
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from projectapp.forms import ProjectUserForm
from projectapp.models import Project


class ProjectPageView(FormView):
    def post(self, request, *args, **kwargs):
        project_form = ProjectUserForm(data=request.POST)
        if project_form.is_valid():
            project_form.save()
        return HttpResponseRedirect(reverse('projectapp:main'))

    def get(self, request, *args, **kwargs):
        """
        запилить отдачу проектов если существуют,
        если нет выводить запись что проектов нет и ссылку создать проект
        связать юзера с этой моделью, чтобы выводить данные о проектах для этого юзера
        """
        project_data = get_object_or_404(Project, pk=2)
        project_form = ProjectUserForm(instance=project_data)
        content = {'title': 'Ваши проекты', 'project_form': project_form}
        return render(request, 'projectapp/projects.html', content)
