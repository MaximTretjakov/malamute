from django.urls import path
from projectapp.views import ProjectPageView

app_name = 'projectapp'

urlpatterns = [
    path('create/', ProjectPageView.as_view(), name='main')
]
