from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authapp.urls', namespace='authapp')),
    path('', include('projectapp.urls', namespace='projectapp')),
    path('', include('mainapp.urls', namespace='mainapp'))
]
