from django.urls import path
from projectapp.views import ProjectPageView, ShowProjectPageView

app_name = 'projectapp'

urlpatterns = [
    path('create/', ProjectPageView.as_view(), name='main'),
    path('show/', ShowProjectPageView.as_view(), name='show')
]
