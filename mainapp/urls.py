from django.urls import path
from mainapp.views import HomePageView

app_name = 'mainapp'

urlpatterns = [
    path('', HomePageView.as_view(), name='home')
]
