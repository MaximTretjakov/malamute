from django.urls import path
from authapp.views import LogoutPageView, LoginPageView, RegisterPageView

app_name = 'authapp'

urlpatterns = [
    path('login/', LoginPageView.as_view(), name='login'),
    path('logout/', LogoutPageView.as_view(), name='logout'),
    path('register/', RegisterPageView.as_view(), name='register')
]
