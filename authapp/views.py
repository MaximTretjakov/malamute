from django.views.generic import FormView, View
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm
from django.contrib import auth
from django.urls import reverse


class LoginPageView(FormView):
    def post(self, request, *args, **kwargs):
        login_form = ShopUserLoginForm(data=request.POST)
        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('projectapp:main'))
            else:
                return HttpResponse('Invalid login')
        else:
            return HttpResponseRedirect(reverse('authapp:login'))

    def get(self, request, *args, **kwargs):
        title = 'вход'
        next_url = request.GET.get('next', '')
        login_form = ShopUserLoginForm(data=request.POST or None)
        content = {'title': title, 'login_form': login_form, 'next': next_url}
        return render(request, 'authapp/login.html', content)


class LogoutPageView(View):
    def get(self, request):
        auth.logout(request)
        return HttpResponseRedirect(reverse('mainapp:home'))


class RegisterPageView(FormView):
    def post(self, request, *args, **kwargs):
        register_form = ShopUserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
        else:
            return render(request, 'authapp/register.html', {'register_form': register_form})

    def get(self, request, *args, **kwargs):
        title = 'регистрация'
        register_form = ShopUserRegisterForm()
        content = {'title': title, 'register_form': register_form}
        return render(request, 'authapp/register.html', content)
